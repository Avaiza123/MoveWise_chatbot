import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from app.chatbot_engine import FitnessChatbot
from app.models.response_model import ChatbotResponse, ResponseType
from app.utils.intent_classifier import IntentClassifier
from app.knowledge_base.knowledge_store import KnowledgeStore


class IntentConfidenceTests(unittest.TestCase):
    def test_known_food_query_high_confidence(self):
        intent, confidence = IntentClassifier.classify_intent("How many calories in chicken breast?")
        self.assertEqual(intent, "food")
        self.assertGreaterEqual(confidence, 0.75)

    def test_unknown_query_low_confidence(self):
        intent, confidence = IntentClassifier.classify_intent("zxqv blorf qwerty")
        self.assertEqual(intent, "unknown")
        self.assertLessEqual(confidence, 0.1)

    def test_squat_depth_query_confidence_is_strong(self):
        intent, confidence = IntentClassifier.classify_intent("Squat depth requirements")
        self.assertEqual(intent, "fitness")
        self.assertGreaterEqual(confidence, 0.5)

    def test_pullup_lats_query_is_fitness(self):
        intent, confidence = IntentClassifier.classify_intent("How to engage lats in pull-ups")
        self.assertEqual(intent, "fitness")
        self.assertGreater(confidence, 0.2)


class FallbackRoutingTests(unittest.TestCase):
    def test_unknown_query_routes_to_web_fallback_when_result_available(self):
        bot = FitnessChatbot()

        fake_web = {
            "title": "GLP-1 receptor agonist",
            "summary": "GLP-1 receptor agonists are medications used for diabetes and obesity.",
            "source_url": "https://example.com/glp1",
        }

        with patch.object(bot, "_search_web", return_value=fake_web):
            response = bot.process_query("What are latest GLP-1 medications for obesity?")

        self.assertTrue(response.success)
        self.assertEqual(response.response_type, ResponseType.INFO)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(response.data.get("source"), "web_fallback")

    def test_high_confidence_query_skips_web_fallback(self):
        bot = FitnessChatbot()

        with patch.object(bot, "_handle_web_fallback") as mocked_fallback:
            response = bot.process_query("How many calories in chicken breast?")

        mocked_fallback.assert_not_called()
        self.assertTrue(response.success)
        self.assertIn(response.response_type, (ResponseType.SUCCESS, ResponseType.INFO))

    def test_bench_press_form_query_is_answered_locally(self):
        bot = FitnessChatbot()

        with patch.object(bot, "_handle_web_fallback") as mocked_fallback:
            response = bot.process_query("Elbow position in bench press")

        mocked_fallback.assert_not_called()
        self.assertTrue(response.success)
        self.assertIn(response.response_type, (ResponseType.SUCCESS, ResponseType.INFO))
        self.assertIn("elbow", response.message.lower())
        self.assertIsInstance(response.data, dict)
        self.assertIn(response.data.get("source"), {"local", "knowledge_memory"})

    def test_squat_depth_query_is_answered_locally(self):
        bot = FitnessChatbot()

        with patch.object(bot, "_handle_web_fallback") as mocked_fallback:
            response = bot.process_query("Squat depth requirements")

        mocked_fallback.assert_not_called()
        self.assertTrue(response.success)
        self.assertIn(response.response_type, (ResponseType.SUCCESS, ResponseType.INFO))
        self.assertIn("squat", response.message.lower())
        self.assertIn("depth", response.message.lower())
        self.assertIsInstance(response.data, dict)
        self.assertIn(response.data.get("source"), {"local", "knowledge_memory"})

    def test_pullup_lats_query_is_answered_locally(self):
        bot = FitnessChatbot()

        with patch.object(bot, "_handle_web_fallback") as mocked_fallback:
            response = bot.process_query("How to engage lats in pull-ups")

        mocked_fallback.assert_not_called()
        self.assertTrue(response.success)
        self.assertIn("lat", response.message.lower())

    def test_deload_signs_query_is_answered_locally(self):
        bot = FitnessChatbot()

        with patch.object(bot, "_handle_web_fallback") as mocked_fallback:
            response = bot.process_query("Signs you need a deload")

        mocked_fallback.assert_not_called()
        self.assertTrue(response.success)
        self.assertIn("deload", response.message.lower())

    def test_post_diet_query_does_not_crash(self):
        bot = FitnessChatbot()
        response = bot.process_query("Coming out of a diet without gaining fat")
        self.assertTrue(response.success)
        self.assertNotIn("unexpected error", response.message.lower())

    def test_metabolic_adaptation_query_is_answered_locally(self):
        bot = FitnessChatbot()

        with patch.object(bot, "_handle_web_fallback") as mocked_fallback:
            response = bot.process_query("Metabolic adaptation to dieting")

        mocked_fallback.assert_not_called()
        self.assertTrue(response.success)
        self.assertIn("metabolic adaptation", response.message.lower())


class EndpointAnswerSourceFlagTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app_py = Path(__file__).resolve().parents[1] / "app.py"
        spec = importlib.util.spec_from_file_location("api_module", app_py)
        cls.api_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.api_module)

    def test_chat_endpoint_returns_web_fallback_flag(self):
        mocked = ChatbotResponse(
            success=True,
            message="Web result",
            data={"source": "web_fallback", "source_url": "https://example.com"},
            response_type=ResponseType.INFO,
        )

        with patch.object(self.api_module.chatbot, "process_query", return_value=mocked):
            with self.api_module.app.test_request_context(
                "/api/chat", method="POST", json={"message": "latest glp-1 meds"}
            ):
                resp, status_code = self.api_module.chat()

        body = resp.get_json()
        self.assertEqual(status_code, 200)
        self.assertEqual(body.get("answer_source"), "web_fallback")

    def test_chat_endpoint_returns_local_flag_by_default(self):
        mocked = ChatbotResponse(
            success=True,
            message="Local result",
            data={"calories": 165},
            response_type=ResponseType.SUCCESS,
        )

        with patch.object(self.api_module.chatbot, "process_query", return_value=mocked):
            with self.api_module.app.test_request_context(
                "/api/chat", method="POST", json={"message": "calories in chicken"}
            ):
                resp, status_code = self.api_module.chat()

        body = resp.get_json()
        self.assertEqual(status_code, 200)
        self.assertEqual(body.get("answer_source"), "local")

    def test_knowledge_stats_endpoint_returns_data(self):
        with patch.object(self.api_module.chatbot.knowledge_store, "stats", return_value={"total_entries": 3}):
            with self.api_module.app.test_request_context(
                "/api/knowledge/stats", method="GET"
            ):
                resp, status_code = self.api_module.knowledge_stats()

        body = resp.get_json()
        self.assertEqual(status_code, 200)
        self.assertTrue(body.get("success"))
        self.assertEqual(body.get("data", {}).get("total_entries"), 3)


class KnowledgeLearningTests(unittest.TestCase):
    def test_response_is_learned_and_retrieved_from_memory(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            bot = FitnessChatbot()
            bot.knowledge_store = KnowledgeStore(file_path=Path(temp_dir) / "knowledge_memory.json")

            first = bot.process_query("Elbow position in bench press")
            self.assertTrue(first.success)

            second = bot.process_query("Elbow position in bench press")
            self.assertTrue(second.success)
            self.assertEqual(second.response_type, ResponseType.INFO)
            self.assertIsInstance(second.data, dict)
            self.assertEqual(second.data.get("source"), "knowledge_memory")


if __name__ == "__main__":
    unittest.main()
