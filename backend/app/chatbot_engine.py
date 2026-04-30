# Main Chatbot Engine
import logging
import os
import json
import requests
from typing import Dict, Optional, Any, List
from datetime import datetime
from pathlib import Path

from app.models.response_model import ChatbotResponse, ResponseType, ERROR_CODES, SUCCESS_CODES
from app.utils.intent_classifier import IntentClassifier, QueryAnalyzer, ContextManager, RESPONSE_TEMPLATES
from app.knowledge_base.fitness_knowledge import FITNESS_KNOWLEDGE, FITNESS_RESPONSES
from app.knowledge_base.health_knowledge import HEALTH_KNOWLEDGE, HEALTH_RESPONSES
from app.knowledge_base.diet_knowledge import DIET_KNOWLEDGE, DIET_RESPONSES
from app.knowledge_base.food_database import FOOD_DATABASE, FOOD_CATEGORIES, MEAL_SUGGESTIONS
from app.knowledge_base.knowledge_store import KnowledgeStore

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FitnessChatbot:
    """Main Chatbot Engine for Fitness, Health, Diet, and Food"""
    
    def __init__(self):
        self.intent_classifier = IntentClassifier()
        self.query_analyzer = QueryAnalyzer()
        self.context_manager = ContextManager()
        self.name = "Fitness Chatbot"
        self.enable_web_fallback = os.environ.get("ENABLE_WEB_FALLBACK", "true").lower() in ("1", "true", "yes", "on")
        self.web_cache_path = Path(__file__).resolve().parent / "knowledge_base" / "web_cache.json"
        self.web_cache = self._load_web_cache()
        self.knowledge_store = KnowledgeStore()
        self.knowledge_store.prune_low_quality()
        self.knowledge_store.ingest_web_cache(self.web_cache)
        logger.info("Fitness Chatbot initialized successfully")
    
    def process_query(self, user_query: str, user_id: Optional[str] = None) -> ChatbotResponse:
        """
        Process user query and generate response
        """
        try:
            # Validate query
            if not self.query_analyzer.is_valid_query(user_query):
                return ChatbotResponse(
                    success=False,
                    message="Invalid query. Please ask a meaningful question.",
                    response_type=ResponseType.ERROR,
                    error_code=ERROR_CODES["INVALID_QUERY"]
                )
            
            # Clean query
            clean_query = self.query_analyzer.clean_query(user_query)
            clean_query = self._expand_contextual_query(clean_query)
            logger.info(f"Processing query: {clean_query}")
            
            # Classify intent
            intent, confidence = self.intent_classifier.classify_intent(clean_query)
            logger.info(f"Intent: {intent}, Confidence: {confidence}")

            # Retrieval path from persistent learned knowledge, constrained by predicted intent.
            learned = self.knowledge_store.retrieve(clean_query, intent=intent, min_score=0.52)
            if learned:
                return ChatbotResponse(
                    success=True,
                    message=learned["answer"],
                    data={
                        "source": "knowledge_memory",
                        "retrieval_score": learned["retrieval_score"],
                        "knowledge_key": learned["key"],
                        "tags": learned["tags"],
                        "intent": learned.get("intent", intent),
                    },
                    response_type=ResponseType.INFO,
                )
            
            # Handle low confidence only when there is effectively no signal.
            if confidence < 0.05 and intent != "unknown":
                intent = "unknown"
            
            # Extract entities
            entities = self.intent_classifier.extract_entities(clean_query)

            # Estimate whether local knowledge likely contains enough signal.
            local_support = self.intent_classifier.get_local_support_score(clean_query)

            if self._should_use_web_fallback(intent, confidence, local_support, entities):
                web_response = self._handle_web_fallback(clean_query, intent, confidence)
                if web_response:
                    return web_response
            
            # Get response based on intent
            if intent == "fitness":
                response = self._handle_fitness_query(clean_query, entities)
            elif intent == "health":
                response = self._handle_health_query(clean_query, entities)
            elif intent == "diet":
                response = self._handle_diet_query(clean_query, entities)
            elif intent == "food":
                response = self._handle_food_query(clean_query, entities)
            else:
                response = ChatbotResponse(
                    success=False,
                    message=RESPONSE_TEMPLATES["unknown"][0],
                    response_type=ResponseType.INFO,
                    error_code=ERROR_CODES["INTENT_NOT_FOUND"]
                )

            # If local handler produced a generic answer, try web lookup only for very low-confidence cases.
            if confidence < 0.25 and self._looks_generic_response(intent, response):
                web_response = self._handle_web_fallback(clean_query, intent, confidence)
                if web_response:
                    response = web_response
            
            # Add to conversation history
            self.context_manager.add_to_history("user", clean_query)
            self.context_manager.add_to_history("bot", response.message)

            self._maybe_learn_from_response(clean_query, intent, confidence, response)
            
            return response
            
        except Exception as e:
            logger.error(f"Error processing query: {str(e)}")
            return ChatbotResponse(
                success=False,
                message="An unexpected error occurred. Please try again.",
                response_type=ResponseType.ERROR,
                error_code=ERROR_CODES["INTERNAL_ERROR"]
            )

    def _maybe_learn_from_response(self, query: str, intent: str, confidence: float, response: ChatbotResponse) -> None:
        """Store useful answers so future similar prompts can be answered from memory."""
        if not response or not response.success:
            return

        if not response.message or len(response.message.strip()) < 40:
            return

        response_source = "local"
        if isinstance(response.data, dict):
            response_source = response.data.get("source", "local")

        if response_source in {"web_fallback_attempted"}:
            return

        if self._looks_generic_response(intent, response):
            return

        if confidence < 0.25 and response_source != "web_fallback":
            return

        key = self._cache_key(query, intent)
        tags = [intent]
        if isinstance(response.data, dict):
            exercise = response.data.get("exercise")
            focus = response.data.get("focus")
            if exercise:
                tags.append(str(exercise))
            if focus:
                tags.append(str(focus))

        self.knowledge_store.add_or_update(
            key=key,
            question=query,
            answer=response.message,
            source=response_source,
            confidence=confidence,
            intent=intent,
            tags=tags,
        )

    def _expand_contextual_query(self, query: str) -> str:
        """Expand short follow-up messages using the previous user query context."""
        query_lower = (query or "").strip().lower()
        if not query_lower:
            return query

        context_starters = (
            "and ",
            "and for",
            "what about",
            "how about",
            "is that",
            "tell me more",
            "and what",
        )

        needs_context = query_lower.startswith(context_starters) or query_lower in {
            "is that safe?",
            "how many sets?",
            "tell me more about that",
        }

        if not needs_context:
            return query

        last_user = self.context_manager.get_last_user_query()
        if not last_user or last_user.strip().lower() == query_lower:
            return query

        return f"{last_user}. Follow-up: {query}"

    def _should_use_web_fallback(self, intent: str, confidence: float, local_support: float, entities: Dict) -> bool:
        """Decide if query should go to web fallback because local data is likely insufficient."""
        if not self.enable_web_fallback:
            return False

        if intent != "unknown" and confidence >= 0.75:
            return False

        if intent == "unknown":
            return True

        # For known intents, let local handlers attempt first unless signal is extremely weak.
        if confidence < 0.2 and local_support < 0.1 and not entities:
            return True

        return False

    def _looks_generic_response(self, intent: str, response: ChatbotResponse) -> bool:
        """Detect broad/generic local responses that likely mean no specific data match."""
        text = (response.message or "").lower()
        generic_markers = [
            "simple fitness guide",
            "daily wellness tips",
            "simple diet guide",
            "food information available",
            "can provide detailed nutrition information",
        ]

        if any(marker in text for marker in generic_markers):
            return True

        if not response.data and intent in {"food", "diet", "health", "fitness"}:
            return True

        return False

    def _handle_web_fallback(self, query: str, intent: str, confidence: float) -> Optional[ChatbotResponse]:
        """Fetch concise web-backed answer when local KB does not have a strong match."""
        web_result = self._search_web(query, intent)
        if not web_result:
            return ChatbotResponse(
                success=False,
                message=(
                    "I could not find a strong exact match in my local data, and I was unable to fetch reliable web results right now. "
                    "Please try again in a moment or rephrase with more detail so I can help from local knowledge."
                ),
                data={
                    "source": "web_fallback_attempted",
                    "intent": intent,
                    "classifier_confidence": confidence,
                },
                response_type=ResponseType.INFO,
                error_code=ERROR_CODES["INTENT_NOT_FOUND"],
            )

        message_lines = [
            "I could not find a strong exact match in my local data, so I checked current web sources:",
            "",
            web_result["summary"],
            "",
            f"Source: {web_result['source_url']}",
            "",
            "If you want, I can also convert this into a practical workout/meal/sleep plan.",
        ]

        return ChatbotResponse(
            success=True,
            message="\n".join(message_lines),
            data={
                "source": "web_fallback",
                "intent": intent,
                "classifier_confidence": confidence,
                "source_url": web_result["source_url"],
                "source_title": web_result["title"],
            },
            response_type=ResponseType.INFO,
        )

    def _search_web(self, query: str, intent: str) -> Optional[Dict[str, str]]:
        """
        Search web using DuckDuckGo Instant Answer API.
        Returns best available summary snippet and source URL.
        """
        try:
            cache_key = self._cache_key(query, intent)
            cached = self.web_cache.get(cache_key)
            if isinstance(cached, dict) and cached.get("summary") and cached.get("source_url"):
                return cached

            search_query = f"{query} {intent}"
            resp = requests.get(
                "https://api.duckduckgo.com/",
                params={
                    "q": search_query,
                    "format": "json",
                    "no_html": 1,
                    "no_redirect": 1,
                    "skip_disambig": 1,
                },
                timeout=7,
            )
            resp.raise_for_status()
            payload = resp.json()

            abstract = (payload.get("AbstractText") or "").strip()
            if abstract:
                result = {
                    "title": (payload.get("Heading") or "DuckDuckGo").strip(),
                    "summary": abstract,
                    "source_url": (payload.get("AbstractURL") or "https://duckduckgo.com/").strip(),
                }
                self.web_cache[cache_key] = result
                self._save_web_cache()
                return result

            related = payload.get("RelatedTopics") or []
            for item in related:
                if isinstance(item, dict) and item.get("Text") and item.get("FirstURL"):
                    result = {
                        "title": (item.get("Text")[:60] + "...") if len(item.get("Text", "")) > 60 else item.get("Text"),
                        "summary": item.get("Text").strip(),
                        "source_url": item.get("FirstURL").strip(),
                    }
                    self.web_cache[cache_key] = result
                    self._save_web_cache()
                    return result

            wiki_result = self._search_wikipedia(query)
            if wiki_result:
                self.web_cache[cache_key] = wiki_result
                self._save_web_cache()
                return wiki_result

            return None
        except Exception as exc:
            logger.warning(f"Web fallback lookup failed: {exc}")
            return self._search_wikipedia(query)

    def _cache_key(self, query: str, intent: str) -> str:
        return f"{intent.lower().strip()}::{query.lower().strip()}"

    def _load_web_cache(self) -> Dict[str, Dict[str, str]]:
        try:
            if not self.web_cache_path.exists():
                return {}
            payload = json.loads(self.web_cache_path.read_text(encoding="utf-8"))
            if isinstance(payload, dict):
                return payload
            return {}
        except Exception:
            return {}

    def _save_web_cache(self) -> None:
        try:
            self.web_cache_path.parent.mkdir(parents=True, exist_ok=True)
            self.web_cache_path.write_text(
                json.dumps(self.web_cache, ensure_ascii=True, indent=2),
                encoding="utf-8",
            )
        except Exception as exc:
            logger.warning(f"Unable to save web cache: {exc}")

    def _search_wikipedia(self, query: str) -> Optional[Dict[str, str]]:
        """Secondary fallback using Wikipedia summary API."""
        try:
            search_resp = requests.get(
                "https://en.wikipedia.org/w/rest.php/v1/search/title",
                params={"q": query, "limit": 1},
                timeout=7,
            )
            search_resp.raise_for_status()
            pages = search_resp.json().get("pages", [])
            if not pages:
                return None

            title = pages[0].get("title", "")
            if not title:
                return None

            summary_resp = requests.get(
                f"https://en.wikipedia.org/api/rest_v1/page/summary/{title.replace(' ', '_')}",
                timeout=7,
            )
            summary_resp.raise_for_status()
            summary_payload = summary_resp.json()

            summary_text = (summary_payload.get("extract") or "").strip()
            if not summary_text:
                return None

            return {
                "title": (summary_payload.get("title") or title).strip(),
                "summary": summary_text,
                "source_url": summary_payload.get("content_urls", {}).get("desktop", {}).get("page", "https://wikipedia.org"),
            }
        except Exception:
            return None
    
    def _handle_fitness_query(self, query: str, entities: Dict) -> ChatbotResponse:
        """Handle fitness-related queries"""
        query_lower = query.lower()
        numbers = self.query_analyzer.extract_numbers(query_lower)
        is_beginner = any(term in query_lower for term in ["beginner", "beginer", "begineer"])
        asks_plan = any(term in query_lower for term in ["routine", "workout", "plan", "schedule"])

        if "squat" in query_lower and any(term in query_lower for term in ["depth", "range", "form", "technique", "mobility"]):
            return ChatbotResponse(
                success=True,
                message="For squat depth, use this practical standard:\n\n"
                       "• General goal: descend until hip crease is at or slightly below top of knee\n"
                       "• Keep full-foot pressure (big toe, little toe, heel) to avoid collapsing forward\n"
                       "• Knees track over toes; avoid cave-in\n"
                       "• Maintain neutral spine and brace before each rep\n"
                       "• Depth should be pain-free and controlled with stable bar path\n\n"
                       "If you cannot hit depth yet, improve these first:\n"
                       "• Ankle dorsiflexion mobility\n"
                       "• Hip external rotation control\n"
                       "• Core bracing and tempo (3-second eccentric)\n\n"
                       "Useful progression: goblet squat to box, then gradually lower box height.",
                data={
                    "exercise": "squat",
                    "focus": "depth_requirements",
                    "target_depth": "hip_crease_at_or_below_knee",
                    "source": "local",
                },
                response_type=ResponseType.SUCCESS
            )

        if "bench press" in query_lower and any(term in query_lower for term in ["elbow", "form", "position", "technique"]):
            return ChatbotResponse(
                success=True,
                message="For bench press elbow position, use this setup:\n\n"
                       "• Keep elbows about 45 to 75 degrees from your torso (not fully flared at 90)\n"
                       "• Wrists stacked over elbows at the bottom position\n"
                       "• Forearms mostly vertical when the bar touches lower chest/sternum area\n"
                       "• Tuck slightly on the way down, then press up and slightly back\n"
                       "• Keep shoulder blades retracted and down to protect shoulders\n\n"
                       "Common mistakes:\n"
                       "• Elbows too wide (shoulder stress)\n"
                       "• Elbows too tucked (triceps-dominant, unstable bar path)\n"
                       "• Bouncing bar off chest\n\n"
                       "Cue: 'Stack wrist-elbow, touch low chest, press back toward eyes.'",
                data={
                    "exercise": "bench_press",
                    "focus": "elbow_position",
                    "recommended_elbow_angle": "45-75_degrees",
                    "source": "local",
                },
                response_type=ResponseType.SUCCESS
            )

        if ("pull up" in query_lower or "pull-up" in query_lower or "pullups" in query_lower or "pull-ups" in query_lower) and any(term in query_lower for term in ["lat", "lats", "engage", "activation", "feel"]):
            return ChatbotResponse(
                success=True,
                message="To engage lats better in pull-ups, use these cues:\n\n"
                       "• Start from an active hang: depress shoulders (pull shoulder blades down) before bending elbows\n"
                       "• Think 'drive elbows to your back pockets' instead of pulling with hands\n"
                       "• Keep ribs down and slight hollow-body tension to avoid swinging\n"
                       "• Use a shoulder-width or just-wider grip; very wide grips often reduce quality ROM\n"
                       "• Pause 1 second at the top and lower with control for 2-3 seconds\n\n"
                       "Drills to improve lat activation:\n"
                       "• Scap pull-ups (2-3 sets of 8-12)\n"
                       "• Straight-arm pulldowns\n"
                       "• Chest-supported rows with elbow path close to torso",
                data={
                    "exercise": "pull_ups",
                    "focus": "lat_engagement",
                    "source": "local",
                },
                response_type=ResponseType.SUCCESS
            )

        if "deload" in query_lower and any(term in query_lower for term in ["sign", "need", "when", "should"]):
            return ChatbotResponse(
                success=True,
                message="Common signs you likely need a deload:\n\n"
                       "• Performance stalls or drops for 2+ weeks\n"
                       "• Usual weights feel unusually heavy (high RPE)\n"
                       "• Persistent joint/tendon soreness\n"
                       "• Poor sleep, low motivation, irritability\n"
                       "• Elevated resting heart rate and poor recovery between sessions\n\n"
                       "Deload approach (7 days):\n"
                       "• Reduce load to ~60-70% or cut volume by 40-50%\n"
                       "• Keep movement patterns but avoid failure\n"
                       "• Prioritize sleep, hydration, and steps",
                data={
                    "focus": "deload_signs",
                    "source": "local",
                },
                response_type=ResponseType.SUCCESS
            )

        if any(term in query_lower for term in ["effective", "efffective"]) and any(term in query_lower for term in ["workout", "exercise", "training"]):
            return ChatbotResponse(
                success=True,
                message="Here are highly effective workouts/exercises for most people:\n\n"
                       "• Compound strength moves: Squats, deadlifts, push-ups, rows, overhead press\n"
                       "• Cardio for fat loss and fitness: Brisk incline walk, cycling, running intervals\n"
                       "• HIIT (2-3x/week): 15-20 minutes of hard/easy intervals\n"
                       "• Core and stability: Planks, side planks, dead bug\n\n"
                       "Best weekly structure:\n"
                       "• 3 strength days\n"
                       "• 2 cardio days\n"
                       "• 1 mobility/recovery day\n"
                       "• 1 full rest day\n\n"
                       "If you tell me your goal (weight loss, muscle gain, stamina), I can generate a precise day-by-day plan.",
                data={
                    "top_exercises": ["squats", "deadlifts", "push-ups", "rows", "planks"],
                    "weekly_structure": ["3 strength", "2 cardio", "1 mobility", "1 rest"]
                },
                response_type=ResponseType.SUCCESS
            )

        if is_beginner and asks_plan and any(n >= 10 for n in numbers):
            return ChatbotResponse(
                success=True,
                message="Here is a practical 10-day beginner workout plan:\n\n"
                       "Day 1: 20 min brisk walk + light stretching\n"
                       "Day 2: Full-body bodyweight (squats, push-ups, plank)\n"
                       "Day 3: Rest or easy yoga/mobility\n"
                       "Day 4: 25 min cardio (walk/cycle)\n"
                       "Day 5: Full-body bodyweight\n"
                       "Day 6: Rest + 15 min mobility\n"
                       "Day 7: 30 min low-intensity cardio\n"
                       "Day 8: Full-body bodyweight (slightly more reps)\n"
                       "Day 9: Rest or light walk\n"
                       "Day 10: Cardio + core session\n\n"
                       "Start easy and focus on consistency and good form.",
                data={"days": 10, "level": "beginner", "focus": ["cardio", "strength", "recovery"]},
                response_type=ResponseType.SUCCESS
            )
        
        # Check for specific fitness topics
        if "beginner" in query_lower and ("routine" in query_lower or "workout" in query_lower or "plan" in query_lower):
            return ChatbotResponse(
                success=True,
                message="Here is a simple beginner workout plan you can follow for your first week:\n\n"
                       "Monday: 20 minute brisk walk\n"
                       "Tuesday: Full body bodyweight workout\n"
                       "Wednesday: Rest or gentle stretching\n"
                       "Thursday: 20 minute cardio session\n"
                       "Friday: Full body bodyweight workout\n"
                       "Saturday: Light activity like walking or yoga\n"
                       "Sunday: Rest\n\n"
                       "Helpful tips:\n"
                       "• Warm up for 5 minutes before training\n"
                       "• Start with easy sets and perfect form\n"
                       "• Drink water and sleep well\n"
                       "• Increase intensity gradually each week",
                data=FITNESS_RESPONSES["beginner_routine"],
                response_type=ResponseType.SUCCESS
            )
        
        elif "weight loss" in query_lower or "lose weight" in query_lower:
            return ChatbotResponse(
                success=True,
                message="Weight Loss Strategy:\n" +
                       f"• Strategy: {FITNESS_RESPONSES['goal_specific']['weight_loss']['strategy']}\n" +
                       "• Weekly Routine:\n" +
                       "\n".join(f"  - {item}" for item in FITNESS_RESPONSES["goal_specific"]["weight_loss"]["weekly_routine"]) +
                       "\n• Key Points:\n" +
                       "\n".join(f"  - {point}" for point in FITNESS_RESPONSES["goal_specific"]["weight_loss"]["key_points"]),
                data=FITNESS_RESPONSES["goal_specific"]["weight_loss"],
                response_type=ResponseType.SUCCESS
            )
        
        elif "muscle" in query_lower or "build muscle" in query_lower:
            return ChatbotResponse(
                success=True,
                message="Muscle Building Strategy:\n" +
                       f"• Strategy: {FITNESS_RESPONSES['goal_specific']['muscle_gain']['strategy']}\n" +
                       "• Weekly Routine:\n" +
                       "\n".join(f"  - {item}" for item in FITNESS_RESPONSES["goal_specific"]["muscle_gain"]["weekly_routine"]) +
                       "\n• Key Points:\n" +
                       "\n".join(f"  - {point}" for point in FITNESS_RESPONSES["goal_specific"]["muscle_gain"]["key_points"]),
                data=FITNESS_RESPONSES["goal_specific"]["muscle_gain"],
                response_type=ResponseType.SUCCESS
            )
        
        elif "cardio" in query_lower:
            workout = FITNESS_KNOWLEDGE["workout_types"]["cardio"]
            return ChatbotResponse(
                success=True,
                message=f"**Cardio Exercise Guide**\n\n" +
                       f"Description: {workout['description']}\n\n" +
                       f"**Examples:** {', '.join(workout['examples'])}\n\n" +
                       f"**Benefits:**\n" +
                       "\n".join(f"• {benefit}" for benefit in workout['benefits']) +
                       f"\n\n**Duration:** {workout['duration']}\n" +
                       f"**Frequency:** {workout['frequency']}\n\n" +
                       f"**Beginner Tip:** {workout['beginner_tip']}",
                data=workout,
                response_type=ResponseType.SUCCESS
            )
        
        elif "strength" in query_lower or "weights" in query_lower:
            workout = FITNESS_KNOWLEDGE["workout_types"]["strength_training"]
            return ChatbotResponse(
                success=True,
                message=f"**Strength Training Guide**\n\n" +
                       f"Description: {workout['description']}\n\n" +
                       f"**Examples:** {', '.join(workout['examples'])}\n\n" +
                       f"**Benefits:**\n" +
                       "\n".join(f"• {benefit}" for benefit in workout['benefits']) +
                       f"\n\n**Duration:** {workout['duration']}\n" +
                       f"**Frequency:** {workout['frequency']}\n" +
                       f"**Rest Days:** {workout['rest_days']}",
                data=workout,
                response_type=ResponseType.SUCCESS
            )
        
        elif any(exercise in query_lower for exercise in ["push up", "squat", "deadlift", "plank", "bench press"]):
            # Find the exercise
            for exercise_name, exercise_data in FITNESS_KNOWLEDGE["exercises"].items():
                if exercise_name.replace("_", " ") in query_lower:
                    return ChatbotResponse(
                        success=True,
                        message=f"**{exercise_name.replace('_', ' ').title()} Guide**\n\n" +
                               f"**Muscles Targeted:** {', '.join(exercise_data['muscles_targeted'])}\n" +
                               f"**Difficulty:** {exercise_data['difficulty']}\n\n" +
                               f"**How to Perform:**\n{exercise_data['how_to']}\n\n" +
                               f"**Sets & Reps:** {exercise_data['sets_reps']}\n\n" +
                               f"**Variations:**\n" +
                               "\n".join(f"• {var}" for var in exercise_data['variations']),
                        data=exercise_data,
                        response_type=ResponseType.SUCCESS
                    )
        
        if ("plan" in query_lower or "schedule" in query_lower or "routine" in query_lower) and "workout" in query_lower:
            return ChatbotResponse(
                success=True,
                message="To set a workout routine, keep it simple:\n\n"
                       "• 3 days strength (full body)\n"
                       "• 2 days cardio\n"
                       "• 1 to 2 recovery days\n"
                       "• Keep sessions 30 to 45 minutes\n\n"
                       "A sample week is: Mon strength, Tue cardio, Wed rest, Thu strength, Fri cardio, Sat strength, Sun rest.",
                data=FITNESS_KNOWLEDGE["training_principles"],
                response_type=ResponseType.SUCCESS
            )

        if "plan" in query_lower or "schedule" in query_lower:
            return ChatbotResponse(
                success=True,
                message="A good fitness plan starts simple:\n\n"
                       "• Train 3 to 5 days per week\n"
                       "• Mix cardio, strength, and mobility work\n"
                       "• Rest at least 1 to 2 days per week\n"
                       "• Progress slowly so your body adapts\n\n"
                       "If you want, I can build a beginner, fat loss, muscle gain, or home workout plan for you.",
                data=FITNESS_KNOWLEDGE["training_principles"],
                response_type=ResponseType.SUCCESS
            )

        # General fitness response
        return ChatbotResponse(
            success=True,
            message="Here is a simple fitness guide:\n\n"
                   "• Build up slowly and stay consistent\n"
                   "• Use good form before adding heavier weight\n"
                   "• Rest and recovery are part of progress\n"
                   "• Mix strength, cardio, and mobility work\n\n"
                   "If you want, I can give you a beginner workout, weight loss plan, muscle gain plan, or home routine.",
            data=FITNESS_KNOWLEDGE["training_principles"],
            response_type=ResponseType.SUCCESS
        )
    
    def _handle_health_query(self, query: str, entities: Dict) -> ChatbotResponse:
        """Handle health-related queries"""
        query_lower = query.lower()

        if "back" in query_lower and any(term in query_lower for term in ["deadlift", "deadlifts", "hurt", "pain"]):
            return ChatbotResponse(
                success=True,
                message="Back pain after deadlifts usually comes from setup or load management issues:\n\n"
                       "• Keep a neutral spine and brace hard before each rep\n"
                       "• Keep the bar close to your shins and thighs throughout\n"
                       "• Avoid jerking the bar off the floor\n"
                       "• Reduce load 10-20% and rebuild with strict technique\n"
                       "• Add core stability and hip hinge drills between sessions\n\n"
                       "Stop and seek professional evaluation if pain is sharp, radiates down the leg, or persists beyond a few days.",
                data={"focus": "deadlift_back_pain", "source": "local"},
                response_type=ResponseType.SUCCESS
            )
        
        if "sleep" in query_lower:
            sleep_info = HEALTH_KNOWLEDGE["general_health"]["sleep"]
            return ChatbotResponse(
                success=True,
                message=f"You usually need about {sleep_info['recommended_hours']}.\n\n"
                       f"Why it matters: {sleep_info['importance']}\n\n"
                       "Helpful sleep tips:\n"
                       + "\n".join(f"• {tip}" for tip in sleep_info['tips']) +
                       "\n\nSleep happens in light sleep, deep sleep, and REM sleep, and each stage helps recovery in a different way.",
                data=sleep_info,
                response_type=ResponseType.SUCCESS
            )
        
        elif "hydration" in query_lower or "water" in query_lower:
            hydration = HEALTH_KNOWLEDGE["general_health"]["hydration"]
            return ChatbotResponse(
                success=True,
                message=f"Water helps your body regulate temperature, digest food, and move nutrients around.\n\n"
                       f"A simple daily target is around {hydration['daily_intake']}.\n\n"
                       f"Signs you may need more water: {', '.join(hydration['signs_of_dehydration'])}.\n\n"
                       "Easy hydration tips:\n"
                       + "\n".join(f"• {tip}" for tip in hydration['tips']),
                data=hydration,
                response_type=ResponseType.SUCCESS
            )
        
        elif "stress" in query_lower:
            stress = HEALTH_KNOWLEDGE["general_health"]["stress_management"]
            return ChatbotResponse(
                success=True,
                message=f"Stress can affect your body, sleep, mood, and recovery.\n\n"
                       f"A simple way to start: {stress['quick_relief']}\n\n"
                       "Other things that help:\n"
                       + "\n".join(f"• {technique}" for technique in stress['management_techniques']),
                data=stress,
                response_type=ResponseType.SUCCESS
            )
        
        # General health wellness tips
        return ChatbotResponse(
            success=True,
            message="**Daily Wellness Tips:**\n" +
                   "\n".join(f"• {tip}" for tip in HEALTH_RESPONSES["wellness_tips"]) +
                   "\n\n⚠️ **Important:** This is general health information. For medical concerns, " +
                   "consult a healthcare professional.",
            data=HEALTH_RESPONSES["wellness_tips"],
            response_type=ResponseType.SUCCESS
        )
    
    def _handle_diet_query(self, query: str, entities: Dict) -> ChatbotResponse:
        """Handle diet and nutrition queries"""
        query_lower = query.lower()
        numbers = self.query_analyzer.extract_numbers(query_lower)

        if "tdee" in query_lower or ("calculate" in query_lower and "calorie" in query_lower):
            return ChatbotResponse(
                success=True,
                message="To estimate TDEE quickly:\n\n"
                       "1) Estimate BMR with Mifflin-St Jeor\n"
                       "2) Multiply by activity factor:\n"
                       "• Sedentary: 1.2\n"
                       "• Light: 1.375\n"
                       "• Moderate: 1.55\n"
                       "• Very active: 1.725\n"
                       "• Athlete-level: 1.9\n\n"
                       "Then adjust by weekly scale trend (+/-100 to 200 kcal) to find your true maintenance.",
                data={"focus": "tdee", "source": "local"},
                response_type=ResponseType.SUCCESS
            )

        if "supplement" in query_lower or "supplements" in query_lower:
            return ChatbotResponse(
                success=True,
                message="For most people, the core evidence-based supplements are:\n\n"
                       "• Creatine monohydrate: 3-5 g daily\n"
                       "• Protein powder: only if you miss protein targets\n"
                       "• Vitamin D3: if blood levels are low\n"
                       "• Omega-3: if fatty fish intake is low\n"
                       "• Caffeine (optional) for performance, if tolerated\n\n"
                       "Start with training, sleep, calories, and protein first; supplements are secondary.",
                data={"focus": "supplements_basics", "source": "local"},
                response_type=ResponseType.SUCCESS
            )

        if any(term in query_lower for term in ["coming out of a diet", "reverse diet", "after dieting", "without gaining fat", "post diet"]):
            return ChatbotResponse(
                success=True,
                message="To come out of a diet without rapid fat gain, use a reverse-diet transition:\n\n"
                       "• Increase calories gradually (about 80-150 kcal/week)\n"
                       "• Keep protein high (~1.6-2.2 g/kg body weight)\n"
                       "• Add carbs first to support training and recovery\n"
                       "• Hold body weight gain to ~0.1-0.25% per week\n"
                       "• Keep lifting performance trending up\n"
                       "• Keep daily steps/cardio stable for 2-3 weeks before reducing\n\n"
                       "Use waist + scale trend + gym performance to adjust each week.",
                data={
                    "focus": "reverse_diet",
                    "source": "local",
                },
                response_type=ResponseType.SUCCESS
            )

        if "metabolic adaptation" in query_lower or ("adaptation" in query_lower and "diet" in query_lower):
            return ChatbotResponse(
                success=True,
                message="Metabolic adaptation is your body's response to prolonged calorie deficit:\n\n"
                       "• Resting energy expenditure can drop\n"
                       "• Non-exercise activity often decreases subconsciously\n"
                       "• Hunger can increase while satiety drops\n"
                       "• Training output may decline over time\n\n"
                       "How to manage it:\n"
                       "• Use moderate deficits, not aggressive crashes\n"
                       "• Keep protein high and resistance training consistent\n"
                       "• Include diet breaks/refeed periods when needed\n"
                       "• Sleep 7-9 hours and manage stress\n"
                       "• Transition out with reverse dieting after long cuts",
                data={
                    "focus": "metabolic_adaptation",
                    "source": "local",
                },
                response_type=ResponseType.SUCCESS
            )

        if "food" in query_lower and "protein" in query_lower:
            return self._handle_food_query(query, entities)

        if "diet" in query_lower and any(term in query_lower for term in ["consistent", "consisten", "consistency"]):
            return ChatbotResponse(
                success=True,
                message="Great question. The best way to stay consistent on diet is to make it easy:\n\n"
                       "• Plan meals the night before\n"
                       "• Keep protein in every meal\n"
                       "• Use the 80/20 rule (not perfection)\n"
                       "• Keep healthy snacks ready\n"
                       "• Track progress weekly, not daily\n"
                       "• If you miss one meal, restart at the next meal\n\n"
                       "Consistency beats strict dieting every time.",
                data={"focus": ["planning", "protein", "habit building"]},
                response_type=ResponseType.SUCCESS
            )

        if any(n >= 10 for n in numbers) and ("diet" in query_lower or "weight loss" in query_lower):
            return ChatbotResponse(
                success=True,
                message="Here is a simple 10-day weight-loss diet plan template:\n\n"
                       "Days 1-3: High-protein, balanced meals + no sugary drinks\n"
                       "Days 4-6: Same structure + more vegetables + portion control\n"
                       "Days 7-8: Keep meals simple, repeat best-performing days\n"
                       "Days 9-10: Maintain consistency + hydration + early dinner\n\n"
                       "Daily structure:\n"
                       "Breakfast: Eggs/oats + fruit\n"
                       "Lunch: Lean protein + whole grain + vegetables\n"
                       "Snack: Yogurt/nuts/fruit\n"
                       "Dinner: Protein + vegetables + light carb\n\n"
                       "Target a moderate calorie deficit and steady routine.",
                data={"days": 10, "goal": "weight_loss"},
                response_type=ResponseType.SUCCESS
            )
        
        if "protein" in query_lower:
            protein = DIET_KNOWLEDGE["nutrition_basics"]["macronutrients"]["protein"]
            return ChatbotResponse(
                success=True,
                message=f"**Protein Guide**\n\n" +
                       f"**Function:** {protein['function']}\n\n" +
                       f"**Daily Intake:** {protein['daily_intake']}\n\n" +
                       f"**Best Sources:**\n" +
                       "\n".join(f"• {source}" for source in protein['sources']) +
                       f"\n\n**Timing Tip:** {protein['best_time']}",
                data=protein,
                response_type=ResponseType.SUCCESS
            )
        
        elif "carb" in query_lower:
            carbs = DIET_KNOWLEDGE["nutrition_basics"]["macronutrients"]["carbohydrates"]
            return ChatbotResponse(
                success=True,
                message=f"**Carbohydrate Guide**\n\n" +
                       f"**Function:** {carbs['function']}\n\n" +
                       f"**Daily Intake:** {carbs['daily_intake']}\n\n" +
                       f"**Complex Carbs:** {', '.join(carbs['types']['complex'])}\n" +
                       f"**Simple Carbs:** {', '.join(carbs['types']['simple'])}\n\n" +
                       f"**Tip:** {carbs['tip']}",
                data=carbs,
                response_type=ResponseType.SUCCESS
            )
        
        elif "fat" in query_lower:
            fats = DIET_KNOWLEDGE["nutrition_basics"]["macronutrients"]["fats"]
            trans_fat_info = fats.get("types", {}).get("trans_fats", {})
            avoid_text = trans_fat_info.get("recommendation", "Trans fats should be minimized as much as possible.")
            return ChatbotResponse(
                success=True,
                message=f"**Fat Guide**\n\n" +
                       f"**Function:** {fats['function']}\n\n" +
                       f"**Daily Intake:** {fats['daily_intake']}\n\n" +
                       f"**Healthy Fat Sources:**\n" +
                       "\n".join(f"• {source}" for source in fats['healthy_sources']) +
                       f"\n\n**Important:** {avoid_text}",
                data=fats,
                response_type=ResponseType.SUCCESS
            )
        
        elif "weight loss" in query_lower:
            weight_loss = DIET_KNOWLEDGE["diet_plans"]["weight_loss"]
            return ChatbotResponse(
                success=True,
                message=f"**Weight Loss Diet Strategy**\n\n" +
                       f"**Strategy:** {weight_loss['strategy']}\n\n" +
                       f"**Key Approaches:**\n" +
                       "\n".join(f"• {approach}" for approach in weight_loss['approach']) +
                       f"\n\n**Foods to Limit:**\n" +
                       "\n".join(f"• {food}" for food in weight_loss['foods_to_limit']) +
                       f"\n\n**Foods to Emphasize:**\n" +
                       "\n".join(f"• {food}" for food in weight_loss['foods_to_emphasize']),
                data=weight_loss,
                response_type=ResponseType.SUCCESS
            )
        
        elif "muscle" in query_lower or "bulk" in query_lower:
            muscle_gain = DIET_KNOWLEDGE["diet_plans"]["muscle_gain"]
            sample_daily = muscle_gain.get("sample_daily")
            if not sample_daily:
                sample_daily = muscle_gain.get("sample_daily_2800_calories", {})
            if isinstance(sample_daily, dict):
                sample_lines = [f"• {k.replace('_', ' ').title()}: {v}" for k, v in sample_daily.items()]
            elif isinstance(sample_daily, list):
                sample_lines = [f"• {item}" for item in sample_daily]
            else:
                sample_lines = ["• Keep protein high and include balanced meals across the day"]
            return ChatbotResponse(
                success=True,
                message=f"**Muscle Gain Diet Strategy**\n\n" +
                       f"**Strategy:** {muscle_gain['strategy']}\n\n" +
                       f"**Key Approaches:**\n" +
                       "\n".join(f"• {approach}" for approach in muscle_gain['approach']) +
                       f"\n\n**Sample Daily Macros:**\n" +
                       "\n".join(sample_lines),
                data=muscle_gain,
                response_type=ResponseType.SUCCESS
            )
        
        if "schedule" in query_lower or "plan" in query_lower:
            balanced = DIET_KNOWLEDGE["diet_plans"]["balanced_diet"]
            return ChatbotResponse(
                success=True,
                message="Here is a simple 1-day diet plan you can repeat and adjust for 10 days:\n\n"
                       "Breakfast: Oatmeal with berries and nuts or eggs with toast\n"
                       "Snack: Fruit with yogurt or nuts\n"
                       "Lunch: Chicken, rice, and vegetables or a bean and grain bowl\n"
                       "Snack: Apple, hummus, or cottage cheese\n"
                       "Dinner: Salmon or chicken with vegetables and a healthy carb\n\n"
                       "A healthy diet works best when it is balanced, repeatable, and realistic.",
                data=balanced,
                response_type=ResponseType.SUCCESS
            )

        # General diet advice
        return ChatbotResponse(
            success=True,
            message="Here is a simple diet guide:\n\n"
                   "• Choose mostly whole foods\n"
                   "• Include protein, vegetables, healthy fats, and quality carbs\n"
                   "• Stay hydrated and keep portions realistic\n"
                   "• Be consistent instead of chasing extreme diets\n\n"
                   "If you want, I can make a weight loss plan, muscle gain plan, or meal plan for you.",
            data=DIET_RESPONSES,
            response_type=ResponseType.SUCCESS
        )
    
    def _handle_food_query(self, query: str, entities: Dict) -> ChatbotResponse:
        """Handle food-related queries"""
        query_lower = query.lower()

        if "supplement" in query_lower or "supplements" in query_lower:
            return self._handle_diet_query(query, entities)

        if "high calorie" in query_lower or "high calories" in query_lower:
            foods = ["Oats", "Almonds", "Avocado", "Olive oil", "Salmon", "Peanut butter", "Whole eggs"]
            return ChatbotResponse(
                success=True,
                message="High-calorie healthy foods include:\n" + "\n".join(f"• {food}" for food in foods) +
                       "\n\nThese are useful for muscle gain or increasing daily calories in a healthy way.",
                data={"foods": foods, "use_case": "muscle_gain_or_high_energy"},
                response_type=ResponseType.SUCCESS
            )
        
        # Check if asking about specific food
        if entities.get("foods"):
            food_name = entities["foods"][0]
            for db_food_name, food_info in FOOD_DATABASE["foods"].items():
                if food_name in db_food_name or db_food_name in food_name:
                    return ChatbotResponse(
                        success=True,
                        message=f"**{db_food_name.replace('_', ' ').title()} Nutrition Info**\n\n" +
                               f"**Category:** {food_info['category']}\n" +
                               f"**Serving Size:** {food_info['serving_size']}\n\n" +
                               f"**Nutrition Per Serving:**\n" +
                               f"• Calories: {food_info['calories']}\n" +
                               f"• Protein: {food_info['protein']}g\n" +
                               f"• Carbs: {food_info['carbs']}g\n" +
                               f"• Fat: {food_info['fat']}g\n" +
                               f"• Fiber: {food_info['fiber']}g\n\n" +
                               f"**Benefits:**\n" +
                               "\n".join(f"• {benefit}" for benefit in food_info['benefits']) +
                               f"\n\n**Preparation:** {food_info.get('preparation', 'Use common safe preparation methods such as raw, boiled, baked, or mixed in meals as appropriate.')}",
                        data=food_info,
                        response_type=ResponseType.SUCCESS
                    )
        
        # Check if asking about meal suggestions
        if "meal" in query_lower:
            if "breakfast" in query_lower:
                meals = MEAL_SUGGESTIONS["breakfast"]
                return ChatbotResponse(
                    success=True,
                    message="**Breakfast Ideas:**\n" +
                           "\n".join(f"• {meal}" for meal in meals),
                    data={"meals": meals},
                    response_type=ResponseType.SUCCESS
                )
            elif "lunch" in query_lower:
                meals = MEAL_SUGGESTIONS["lunch"]
                return ChatbotResponse(
                    success=True,
                    message="**Lunch Ideas:**\n" +
                           "\n".join(f"• {meal}" for meal in meals),
                    data={"meals": meals},
                    response_type=ResponseType.SUCCESS
                )
            elif "dinner" in query_lower:
                meals = MEAL_SUGGESTIONS["dinner"]
                return ChatbotResponse(
                    success=True,
                    message="**Dinner Ideas:**\n" +
                           "\n".join(f"• {meal}" for meal in meals),
                    data={"meals": meals},
                    response_type=ResponseType.SUCCESS
                )
            elif "snack" in query_lower:
                meals = MEAL_SUGGESTIONS["snacks"]
                return ChatbotResponse(
                    success=True,
                    message="**Healthy Snack Ideas:**\n" +
                           "\n".join(f"• {meal}" for meal in meals),
                    data={"meals": meals},
                    response_type=ResponseType.SUCCESS
                )
        
        # Check for high protein, low calorie, etc.
        if "high protein" in query_lower or "protein food" in query_lower or "protein foods" in query_lower:
            foods = FOOD_CATEGORIES["high_protein"]
            return ChatbotResponse(
                success=True,
                message="**High Protein Foods:**\n" +
                       "\n".join(f"• {food}" for food in foods),
                data={"foods": foods},
                response_type=ResponseType.SUCCESS
            )
        
        if "low calorie" in query_lower:
            foods = FOOD_CATEGORIES["low_calorie"]
            return ChatbotResponse(
                success=True,
                message="**Low Calorie Foods:**\n" +
                       "\n".join(f"• {food}" for food in foods),
                data={"foods": foods},
                response_type=ResponseType.SUCCESS
            )
        
        # General food information
        return ChatbotResponse(
            success=True,
            message="**Food Information Available:**\n" +
                   "I can provide detailed nutrition information for foods like chicken, salmon, eggs, " +
                   "vegetables, fruits, and more.\n\n" +
                   "Ask me about:\n" +
                   "• Specific foods and their nutrition\n" +
                   "• Meal suggestions\n" +
                   "• High protein foods\n" +
                   "• Low calorie options\n" +
                   "• Pre/post-workout foods",
            response_type=ResponseType.SUCCESS
        )
    
    def get_greeting(self) -> str:
        """Get greeting message"""
        return RESPONSE_TEMPLATES["greeting"]
