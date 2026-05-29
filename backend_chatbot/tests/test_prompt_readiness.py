import unittest

from app.chatbot_engine import FitnessChatbot


QUICK_TOP_20_PROMPTS = [
    "What's a good beginner workout routine?",
    "How many calories in a chicken breast?",
    "How much protein do I need daily?",
    "Best exercises for weight loss",
    "How to improve my sleep quality?",
    "Is keto diet safe?",
    "How to cook salmon?",
    "Symptoms of overtraining",
    "What supplements should I take?",
    "Home workouts without equipment",
    "How many reps for muscle growth?",
    "Healthy breakfast ideas",
    "Why does my back hurt after deadlifts?",
    "How to calculate my TDEE?",
    "What's intermittent fasting?",
    "Benefits of drinking more water",
    "How to stay motivated to exercise?",
    "Best high protein snacks",
    "Cardio before or after weights?",
    "How to lose belly fat?",
]

EXTENDED_READINESS_PROMPTS = [
    "How to do a proper squat?",
    "What muscles does push-ups work?",
    "How do I build muscle mass?",
    "What's progressive overload and how do I use it?",
    "How to break through a strength plateau?",
    "What's the difference between compound and isolation exercises?",
    "Proper form for deadlift?",
    "How to bench press safely?",
    "Tips for pull-ups when I can't do one yet",
    "Is it bad to lock my knees on leg press?",
    "How deep should I squat?",
    "How many days a week should I train?",
    "What's a good push-pull-legs split?",
    "How long should my workouts be?",
    "Should I do full body or split routines?",
    "What's deload week and do I need it?",
    "HIIT vs steady state cardio - which is better?",
    "Is walking enough exercise?",
    "How many calories does running burn?",
    "Best exercises with just dumbbells",
    "Resistance band full body workout",
    "Apartment-friendly cardio exercises",
    "How to workout in a small space",
    "Tips for better sleep quality",
    "Is it bad to workout on little sleep?",
    "How to fix my sleep schedule?",
    "How to reduce stress naturally?",
    "Signs of overtraining and burnout",
    "Does exercise help with depression?",
    "How to boost my immune system?",
    "Should I workout when sick?",
    "How long does muscle soreness last?",
    "How to lower cholesterol naturally",
    "How many calories should I eat to lose weight?",
    "What's a safe calorie deficit?",
    "How to lose fat but keep muscle?",
    "What's the ideal macro ratio for muscle gain?",
    "Good sources of healthy fats",
    "Is counting macros necessary?",
    "What can I eat on intermittent fasting?",
    "Vegan diet for muscle gain - is it possible?",
    "Mediterranean diet meal ideas",
    "How to meal prep for the week?",
    "Best post-workout meal for recovery",
    "Budget-friendly high protein meals",
    "Should I take creatine?",
    "Is whey protein necessary?",
    "Do fat burners work?",
    "Natural pre-workout alternatives to caffeine",
    "Nutrition facts of avocado",
    "Protein content in eggs",
    "Carbs in brown rice vs white rice",
    "Is salmon healthy? How much fat?",
    "Benefits of eating broccoli",
    "Is quinoa better than rice?",
    "Greek yogurt vs regular yogurt - which is healthier?",
    "How many calories in a banana?",
    "Is peanut butter good for weight loss?",
    "Healthy chicken breast recipes",
    "Quick vegetarian protein meals",
    "High protein snacks under 200 calories",
    "Which has more protein - chicken or tofu?",
    "Almond milk vs oat milk nutrition",
    "Fresh vs frozen vegetables - any difference?",
    "Is dark chocolate actually healthy?",
    "Best foods to eat before bed",
    "Post-workout meal timing - how soon?",
    "What to eat when craving junk food",
    "How to loose weight?",
    "What's a good workot routine?",
    "How much protien do I need?",
    "HIIT vs LISS for fat loss?",
    "How to get in shape?",
    "What should I eat?",
    "My diet isn't working",
    "I want to lose 20 pounds",
    "I want to build muscle",
    "I've never exercised before, where do I start?",
    "How to avoid injury as a beginner?",
    "Exercises for seniors",
    "Workouts for people with bad knees",
    "I want to lose weight but also build muscle - can I do both?",
    "Diet for type 2 diabetes management",
    "Low impact exercises for arthritis",
    "How to get visible abs in 3 months?",
    "Body recomposition - lose fat and gain muscle simultaneously",
    "Why am I gaining weight while exercising?",
    "Not seeing muscle growth after 6 months",
    "Always tired during workouts - what's wrong?",
    "How to stop late night snacking?",
]


class PromptReadinessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bot = FitnessChatbot()

    def test_quick_top_20_no_crash_no_fallback_attempted(self):
        for prompt in QUICK_TOP_20_PROMPTS:
            with self.subTest(prompt=prompt):
                response = self.bot.process_query(prompt)
                self.assertTrue(response.message)
                self.assertNotIn("unexpected error", response.message.lower())
                source = response.data.get("source") if isinstance(response.data, dict) else None
                self.assertNotEqual(source, "web_fallback_attempted")

    def test_extended_suite_no_internal_error(self):
        for prompt in EXTENDED_READINESS_PROMPTS:
            with self.subTest(prompt=prompt):
                response = self.bot.process_query(prompt)
                self.assertTrue(response.message)
                self.assertNotIn("unexpected error", response.message.lower())


if __name__ == "__main__":
    unittest.main()
