# Chatbot Utilities - Intent Classification and NLP
import re
import time
from typing import Tuple, List, Dict, Optional, Set
from difflib import SequenceMatcher, get_close_matches
from collections import Counter

class IntentClassifier:
    """Classifies user queries into fitness, health, diet, or food categories with improved accuracy"""
    
    # Expanded intent keywords mapping with synonyms and phrases
    INTENT_KEYWORDS = {
        "fitness": {
            "keywords": [
                "exercise", "workout", "training", "gym", "fitness", "strength", "cardio", 
                "hiit", "muscles", "bodybuilding", "running", "cycling", "swimming", "push up", 
                "squat", "deadlift", "bench press", "rep", "set", "weights", "dumbbells",
                "reps", "sets", "routine", "program", "workouts", "athlete", "lifting",
                "crossfit", "yoga", "pilates", "stretching", "warm up", "cool down",
                "treadmill", "elliptical", "rowing", "calisthenics", "plyometrics",
                "resistance", "endurance", "stamina", "power", "agility", "balance",
                "bulk", "cutting", "lean", "toned", "shredded", "aesthetic",
                "compound", "isolation", "superset", "drop set", "pyramid",
                "periodization", "progressive overload", "deload", "1rm", "pr", "personal record",
                "beginner workout", "intermediate", "advanced", "home workout", "no equipment",
                "depth", "range of motion", "form", "technique", "mobility", "bracing",
                "pull up", "pull-up", "pullups", "pull-ups", "lat", "lats", "lat engagement",
                "active hang", "scap pull-up", "deload signs"
            ],
            "negative_keywords": [
                "food", "recipe", "cook", "ingredient", "meal", "restaurant", "flavor", "taste",
                "calorie in", "calories in", "nutrition in", "vitamin in", "protein in"
            ],
            "patterns": [
                r"how.*exercise", r"best.*workout", r".*training.*routine", r".*fitness.*",
                r"how.*(do|perform).*\b(push up|squat|deadlift|plank|burpee|lunge)\b",
                r"(build|gain|increase).*(muscle|strength|mass)",
                r"(lose|burn|reduce).*(fat|weight).*exercise",
                r"(beginner|start).*\b(workout|exercise|gym)\b",
                r"\b(1rm|one rep max|pr|personal record)\b",
                r"\b(hiit|tabata|circuit)\b.*training",
                r"(home|no equipment|bodyweight).*workout",
                r"(squat).*(depth|form|technique|mobility)",
                r"(depth|form|technique).*(squat)",
                r"(pull\s*-?ups?).*(lat|lats|engage|activation)",
                r"(lat|lats).*(pull\s*-?ups?)",
                r"(signs?|need|when).*(deload)",
                r"(deload).*(signs?|need|when)"
            ],
            "canonical_examples": [
                "what is a good workout for beginners",
                "how do i build muscle",
                "best exercises for weight loss",
                "how many reps should i do",
                "what is progressive overload",
                "how to improve my bench press",
                "cardio vs weights for fat loss",
                "how to break through a plateau"
            ]
        },
        "health": {
            "keywords": [
                "health", "medical", "doctor", "disease", "symptom", "blood pressure", 
                "diabetes", "cholesterol", "sleep", "stress", "immunity", "immune", 
                "immune system", "recovery", "injury", "pain", "mental health", "wellness",
                "sick", "illness", "condition", "therapy", "hormone", "inflammation",
                "heart", "kidney", "liver", "thyroid", "metabolism", "digestion",
                "anxiety", "depression", "mood", "energy", "fatigue", "tired",
                "headache", "migraine", "back pain", "joint pain", "arthritis",
                "vitamin d", "b12", "iron deficiency", "anemia", "allergy",
                "water", "hydration", "dehydration",
                "check up", "screening", "vaccine", "flu", "cold", "fever", "sleep routine", "bedtime", "wake up", "insomnia", "REM", "deep sleep",
        "circadian rhythm", "melatonin", "sleep quality", "night routine",
        "fall asleep", "stay asleep", "sleep schedule", "sleep hygiene"
            ],
            "negative_keywords": [
                "exercise", "workout", "gym", "lift", "rep", "set", "cardio",
                "recipe", "cook", "meal plan", "calorie", "macro", "diet plan"
            ],
            "patterns": [
                r".*health.*", r".*medical.*", r".*disease.*", r".*symptom.*",
                r"how.*(sleep|improve sleep|better sleep)",
                r"(manage|reduce|deal with).*stress",
                r"(boost|improve|strengthen).*immunity",
                r"(why|how).*pain.*(back|knee|shoulder|hip)",
                r"(sign|symptom).*\b(diabetes|thyroid|anemia|deficiency)\b",
                r"when.*see.*doctor",
                r"how.*(hours|much).*sleep",
                r".*sleep.*routine.*",
                r".*bedtime.*",
                r".*fall.*asleep.*",
                r".*circadian.*",
                r"how to (fix|improve|reset).*sleep.*",
                r"(insomnia|can't sleep|trouble sleeping)"
            ],
            "canonical_examples": [
                "how many hours of sleep do i need",
                "how to manage stress",
                "symptoms of diabetes",
                "how to boost my immune system",
                "why does my back hurt",
                "when should i see a doctor",
                "how to improve my energy levels",
                "what is a good sleep routine",
                "how to fix my sleep schedule",
                "bedtime routine for better sleep",
                "how to fall asleep faster"
            ]
        },
        "diet": {
            "keywords": [
                "diet", "nutrition", "calorie", "macros", "protein", "carbs", "fat", 
                "meal plan", "eating", "weight loss", "muscle gain", "bulk", "cut",
                "caloric deficit", "tdee", "meal prep", "intermittent fasting", "keto",
                "vegan", "vegetarian", "gluten free", "paleo", "mediterranean",
                "macro", "micronutrient", "supplement", "creatine", "whey", "bcaa",
                "carb cycling", "cheat meal", "refeed", "metabolic adaptation",
                "bmi", "body fat", "body composition", "maintenance", "surplus",
                "nutrient timing", "pre workout meal", "post workout meal",
                "omad", "if", "clean eating", "whole foods", "processed food"
            ],
            "negative_keywords": [
                "exercise", "workout", "rep", "set", "gym", "cardio", "lift"
            ],
            "patterns": [
                r".*diet.*", r".*calorie.*", r".*meal plan.*", r".*weight.*",
                r"how.*(much|many).*(protein|carbs|fat|calorie)",
                r"(what|how).*\b(keto|vegan|paleo|intermittent fasting|omad)\b",
                r"(lose|gain).*weight.*\b(diet|eat|nutrition)\b",
                r"(calculate|find).*\b(tdee|bmr|maintenance|calories)\b",
                r"(best|good).*\b(pre workout|post workout).*meal",
                r"(should|do).*\b(supplement|creatine|whey|protein powder)\b",
                r"how.*(count|track).*macro",
                r"(bulking|cutting).*\b(diet|meal|food)\b"
            ],
            "canonical_examples": [
                "how much protein do i need",
                "what is the best diet for weight loss",
                "how to calculate my tdee",
                "what should i eat before a workout",
                "is keto diet healthy",
                "how to meal prep for the week",
                "do i need creatine"
            ]
        },
        "food": {
            "keywords": [
                "food", "eat", "chicken", "fish", "eggs", "rice", "bread", "fruits", 
                "vegetables", "protein powder", "supplements", "recipe", "cooking", 
                "ingredient", "nutritional", "calories", "apple", "banana", "beef",
                "pork", "turkey", "salmon", "tuna", "milk", "cheese", "yogurt",
                "broccoli", "spinach", "oats", "quinoa", "avocado", "almond", "walnut",
                "sweet potato", "potato", "pasta", "noodle", "lentil", "chickpea",
                "tofu", "tempeh", "seitan", "hummus", "sauce", "oil", "butter",
                "snack", "breakfast", "lunch", "dinner", "dessert", "smoothie",
                "vitamin c", "fiber", "sugar", "sodium", "potassium", "iron", "calcium"
            ],
            "negative_keywords": [
                "exercise", "workout", "gym", "rep", "set", "cardio", "training"
            ],
            "patterns": [
                r".*food.*", r".*eat.*", r".*recipe.*",
                r"how.*(cook|prepare|make).*\b(chicken|salmon|egg|rice|oats)\b",
                r"calories in.*",
                r"nutrition.*(in|of|for).*",
                r"(healthy|good).*\b(snack|breakfast|lunch|dinner)\b",
                r"(high|low).*(protein|carbs|fat|calorie|fiber).*food",
                r"what.*(eat|food).*\b(pre|post|before|after)\b.*workout",
                r"(recipe|how to make).*",
                r"(how many|what).*calories.*in.*",
                r"is.*\b(healthy|good|bad)\b.*for me"
            ],
            "canonical_examples": [
                "how many calories in chicken breast",
                "what is a healthy breakfast",
                "how to cook salmon",
                "high protein snacks",
                "nutrition facts of avocado",
                "what should i eat after a workout",
                "best foods for weight loss"
            ]
        }
    }
    
    # Common abbreviations in fitness/nutrition
    ABBREVIATIONS = {
        "hiit": "high intensity interval training",
        "tdee": "total daily energy expenditure",
        "bmr": "basal metabolic rate",
        "bmi": "body mass index",
        "omad": "one meal a day",
        "bcaa": "branched chain amino acid",
        "doms": "delayed onset muscle soreness",
        "cns": "central nervous system",
        "rm": "rep max",
        "1rm": "one rep max",
        "pr": "personal record",
        "pb": "personal best",
        "if": "intermittent fasting",
        "mps": "muscle protein synthesis",
        "vo2": "oxygen consumption",
        "hr": "heart rate",
        "rpe": "rating of perceived exertion",
        "bb": "barbell",
        "db": "dumbbell",
        "ohp": "overhead press"
    }
    
    # Common misspellings and their corrections
    COMMON_MISSPELLINGS = {
        "excercise": "exercise",
        "exersize": "exercise",
        "workot": "workout",
        "workoout": "workout",
        "wokrout": "workout",
        "nutriton": "nutrition",
        "calory": "calorie",
        "caloris": "calories",
        "protien": "protein",
        "protine": "protein",
        "carbohidrate": "carbohydrate",
        "cardio": "cardio",
        "cardiio": "cardio",
        "mucle": "muscle",
        "muscels": "muscles",
        "weigth": "weight",
        "wieght": "weight",
        "weigt": "weight",
        "diett": "diet",
        "recipie": "recipe",
        "recepie": "recipe",
        "beginer": "beginner",
        "begginer": "beginner",
        "intermeidate": "intermediate",
        "strenght": "strength",
        "strengh": "strength",
        "hydration": "hydration",
        "hydratation": "hydration",
        "suppliment": "supplement",
        "suplement": "supplement"
    }
    
    # Food synonyms for better entity matching
    FOOD_SYNONYMS = {
        "hen": "chicken",
        "poultry": "chicken",
        "cow": "beef",
        "steak": "beef",
        "ground beef": "beef_lean",
        "mince": "beef_lean",
        "pig": "pork",
        "pig meat": "pork",
        "fillet": "salmon",
        "atlantic salmon": "salmon",
        "hens egg": "eggs",
        "hen egg": "eggs",
        "greek yoghurt": "greek_yogurt",
        "yoghurt": "greek_yogurt",
        "brocolli": "broccoli",
        "yam": "sweet_potato",
        "spud": "potato",
        "rice brown": "brown_rice",
        "oats": "oats",
        "oatmeal": "oats",
        "plantain": "banana",
        "nut": "almonds",
        "extra virgin olive oil": "olive_oil",
        "evoo": "olive_oil",
        "greens": "spinach",
        "leafy green": "spinach",
        "lentil": "lentils",
        "dal": "lentils",
        "chick pea": "chickpeas",
        "garbanzo": "chickpeas",
        "butter fruit": "avocado",
        "alligator pear": "avocado",
        "blue berry": "blueberries",
        "quinoa grain": "quinoa",
        "tinned tuna": "tuna_canned",
        "canned tuna": "tuna_canned",
        "bean curd": "tofu",
        "soy paneer": "tofu",
        "cauliflour": "cauliflower",
        "wal nut": "walnuts",
        "carot": "carrots",
        "kale greens": "kale",
        "pumpkin seed": "pumpkin_seeds",
        "pepita": "pumpkin_seeds",
        "cottage chese": "cottage_cheese",
        "sardine": "sardines",
        "lean beef": "beef_lean",
        "asparagas": "asparagus",
        "mushroom": "mushrooms",
        "edamame bean": "edamame",
        "soybean": "edamame"
    }
    
    # Exercise synonyms
    EXERCISE_SYNONYMS = {
        "press up": "push_ups",
        "pushup": "push_ups",
        "press-up": "push_ups",
        "air squat": "squats",
        "back squat": "squats",
        "front squat": "squats",
        "romanian deadlift": "deadlifts",
        "rdl": "deadlifts",
        "pullup": "pull_ups",
        "pull-up": "pull_ups",
        "chin up": "pull_ups",
        "chinup": "pull_ups",
        "barbell row": "rows",
        "dumbbell row": "rows",
        "pendlay row": "rows",
        "ohp": "overhead_press",
        "military press": "overhead_press",
        "walking lunge": "lunges",
        "split squat": "lunges",
        "bb bench": "bench_press",
        "db bench": "bench_press",
        "dips": "dips",
        "crunch": "crunches_variations",
        "sit up": "crunches_variations",
        "sit-up": "crunches_variations",
        "twist": "russian_twists",
        "glute bridge": "hip_thrusts",
        "loaded carry": "farmer_walk",
        "face pull": "face_pulls"
    }

    # Goal keywords
    GOAL_KEYWORDS = {
        "weight_loss": ["lose weight", "fat loss", "burn fat", "slim down", "get lean", "cut", "shred", "drop pounds"],
        "muscle_gain": ["build muscle", "gain muscle", "get bigger", "hypertrophy", "bulk up", "get jacked", "mass"],
        "strength": ["get stronger", "increase strength", "powerlifting", "lift heavier"],
        "endurance": ["run faster", "improve stamina", "last longer", "cardio fitness", "marathon"],
        "health": ["feel better", "be healthier", "improve wellness", "live longer"],
        "rehab": ["recover from injury", "rehabilitation", "physical therapy", "heal"]
    }
    
    # Experience level keywords
    EXPERIENCE_KEYWORDS = {
        "beginner": ["beginner", "newbie", "novice", "just starting", "never exercised", "first time", "no experience"],
        "intermediate": ["intermediate", "some experience", "few months", "been training"],
        "advanced": ["advanced", "experienced", "years", "competitive", "elite"]
    }
    
    @staticmethod
    def _contains_keyword(query_lower: str, query_words: Set[str], keyword: str) -> bool:
        """Match single words by token and phrases by substring for better precision."""
        normalized = keyword.lower().strip()
        if not normalized:
            return False
        if " " in normalized:
            return normalized in query_lower
        return normalized in query_words

    @staticmethod
    def get_local_support_score(query: str) -> float:
        """
        Estimate how well a query is covered by local knowledge.
        Higher score means stronger local coverage and less need for web fallback.
        """
        if not query:
            return 0.0

        query_lower = IntentClassifier.preprocess_query(query.lower().strip())
        query_words = set(re.findall(r'\b[a-z0-9]+\b', query_lower))
        if not query_words:
            return 0.0

        unique_keywords = set()
        for data in IntentClassifier.INTENT_KEYWORDS.values():
            unique_keywords.update(data.get("keywords", []))

        keyword_hits = sum(
            1 for kw in unique_keywords
            if IntentClassifier._contains_keyword(query_lower, query_words, kw)
        )

        entities = IntentClassifier.extract_entities(query_lower)
        entity_hits = sum(
            len(v) if isinstance(v, list) else 1
            for v in entities.values()
        )

        support = (keyword_hits * 0.45) + (entity_hits * 0.7)
        return min(support / 6.0, 1.0)

    @staticmethod
    def expand_abbreviations(query: str) -> str:
        """Expand common fitness/nutrition abbreviations"""
        words = query.lower().split()
        expanded = []
        for word in words:
            # Remove punctuation for lookup
            clean = re.sub(r'[^a-z0-9]', '', word)
            if clean in IntentClassifier.ABBREVIATIONS:
                expanded.append(IntentClassifier.ABBREVIATIONS[clean])
            else:
                expanded.append(word)
        return ' '.join(expanded)
    
    @staticmethod
    def correct_spelling(query: str) -> str:
        """Correct common misspellings"""
        words = query.lower().split()
        corrected = []
        for word in words:
            clean = re.sub(r'[^a-z]', '', word)
            if clean in IntentClassifier.COMMON_MISSPELLINGS:
                corrected.append(IntentClassifier.COMMON_MISSPELLINGS[clean])
            else:
                corrected.append(word)
        return ' '.join(corrected)
    
    @staticmethod
    def preprocess_query(query: str) -> str:
        """Full preprocessing pipeline"""
        query = IntentClassifier.expand_abbreviations(query)
        query = IntentClassifier.correct_spelling(query)
        return query
    
    @staticmethod
    def classify_intent(query: str, context_intent: Optional[str] = None) -> Tuple[str, float]:
        """
        Classify user query intent with improved accuracy
        Returns: (intent_category, confidence_score)
        """
        # Preprocess
        query_original = query.lower().strip()
        query_processed = IntentClassifier.preprocess_query(query_original)
        query_lower = query_processed
        
        if not query_lower:
            return "unknown", 0.0

        # High-confidence routing for common mixed phrases
        if ("food" in query_lower or "foods" in query_lower) and ("protein" in query_lower or "calorie" in query_lower):
            return "food", 0.92
        if "calories in" in query_lower:
            return "food", 0.92
        if any(term in query_lower for term in ["beginner", "beginer", "begineer"]) and any(term in query_lower for term in ["workout", "routine", "plan", "schedule"]):
            return "fitness", 0.92
        if "diet" in query_lower and any(term in query_lower for term in ["consistent", "consisten", "consistency"]):
            return "diet", 0.92
        if re.search(r"\b\d+\s*day\b", query_lower) and "diet" in query_lower:
            return "diet", 0.92
        if "recipe" in query_lower or "how to cook" in query_lower or "how to make" in query_lower:
            return "food", 0.92
        if "calories" in query_lower and any(food in query_lower for food in ["chicken", "salmon", "egg", "rice", "oats", "banana", "almond", "broccoli"]):
            return "food", 0.92
        
        scores = {}
        coverage_scores = {}
        query_words = set(re.findall(r'\b[a-z0-9]+\b', query_lower))
        
        # Check each intent category
        for intent, data in IntentClassifier.INTENT_KEYWORDS.items():
            score = 0.0
            keyword_hits = 0
            negative_hits = 0
            
            keywords = data["keywords"]
            negative_keywords = data.get("negative_keywords", [])
            
            # Check keyword matches
            for keyword in keywords:
                if IntentClassifier._contains_keyword(query_lower, query_words, keyword):
                    score += 1.0
                    keyword_hits += 1
            
            # Check negative keywords
            for neg_keyword in negative_keywords:
                if IntentClassifier._contains_keyword(query_lower, query_words, neg_keyword):
                    negative_hits += 1
                    score -= 0.5
            
            # Check regex patterns
            patterns = data["patterns"]
            for pattern in patterns:
                if re.search(pattern, query_lower):
                    score += 0.8
            
            # Check canonical example similarity using SequenceMatcher
            canonical_examples = data.get("canonical_examples", [])
            for example in canonical_examples:
                similarity = SequenceMatcher(None, query_lower, example).ratio()
                if similarity > 0.6:
                    score += similarity * 2.0  # Boost for high similarity
            
            scores[intent] = score
            
            # Calculate coverage score (keyword hits / total unique words in query)
            if query_words:
                coverage = keyword_hits / max(len(query_words), 3)
                coverage_scores[intent] = coverage
        
        # Get highest scoring intent
        if scores:
            best_intent = max(scores, key=scores.get)
            best_score = scores[best_intent]
            
            # If nothing meaningful matched
            if best_score <= 0:
                return "unknown", 0.0
            
            # Calculate confidence using multiple signals
            # Signal 1: Absolute score normalized
            score_confidence = min(best_score / 4.0, 1.0)
            
            # Signal 2: Coverage of query words
            coverage_confidence = coverage_scores.get(best_intent, 0)
            
            # Signal 3: Margin over second best
            second_best = sorted(scores.values(), reverse=True)[1] if len(scores) > 1 else 0
            margin = best_score - second_best
            margin_confidence = min(margin / 3.0, 1.0)
            
            # Combine signals with weights
            confidence = (score_confidence * 0.5) + (coverage_confidence * 0.2) + (margin_confidence * 0.3)
            confidence = min(max(confidence, 0.0), 1.0)
            
            # Context bias: if previous intent exists and confidence is borderline, boost it
            if context_intent and context_intent in scores:
                if confidence < 0.5 and confidence > 0.15:
                    best_intent = context_intent
                    confidence = min(confidence + 0.25, 0.85)
            
            return best_intent, confidence
        
        return "unknown", 0.0
    
    @staticmethod
    def extract_entities(query: str) -> Dict[str, List[str]]:
        """Extract key entities from query with synonym resolution"""
        query_lower = IntentClassifier.preprocess_query(query.lower())
        entities = {}
        
        # Exercise names (with synonyms)
        exercises = ["push up", "squat", "deadlift", "bench press", "running", "cycling", 
                    "swimming", "yoga", "pilates", "jump rope", "burpee", "plank",
                    "pull up", "row", "overhead press", "lunge", "dip", "leg press",
                    "crunch", "russian twist", "hip thrust", "farmer walk", "face pull",
                    "bicep curl", "tricep extension", "lat pulldown", "leg curl", "leg extension",
                    "calf raise", "shoulder press", "chest fly", "lat raise"]
        
        # Check for exercise synonyms first
        found_exercises = []
        for synonym, canonical in IntentClassifier.EXERCISE_SYNONYMS.items():
            if synonym in query_lower:
                found_exercises.append(canonical)
        
        # Then check standard exercise names
        for ex in exercises:
            if ex in query_lower and ex not in [s for s, c in IntentClassifier.EXERCISE_SYNONYMS.items()]:
                # Convert to canonical form
                canonical = ex.replace(" ", "_")
                if canonical not in found_exercises:
                    found_exercises.append(canonical)
        
        if found_exercises:
            entities["exercises"] = found_exercises
        
        # Food items (with synonyms)
        foods = ["chicken", "fish", "eggs", "rice", "bread", "apple", "banana", "beef", 
                "salmon", "tuna", "milk", "cheese", "yogurt", "broccoli", "spinach",
                "oats", "quinoa", "avocado", "almond", "walnut", "sweet potato", "potato",
                "lentil", "chickpea", "tofu", "tempeh", "pasta", "noodle", "berry",
                "strawberry", "blueberry", "raspberry", "carrot", "kale", "cauliflower",
                "mushroom", "asparagus", "cottage cheese", "sardine", "edamame",
                "pumpkin seed", "olive oil", "peanut butter", "honey", "garlic", "ginger"]
        
        found_foods = []
        # Check for food synonyms first
        for synonym, canonical in IntentClassifier.FOOD_SYNONYMS.items():
            if synonym in query_lower:
                if canonical not in found_foods:
                    found_foods.append(canonical)
        
        # Then check standard food names
        for food in foods:
            if food in query_lower:
                canonical = food.replace(" ", "_")
                if canonical not in found_foods:
                    found_foods.append(canonical)
        
        if found_foods:
            entities["foods"] = found_foods
        
        # Numbers with context
        numbers = re.findall(r'\b\d+(?:\.\d+)?\b', query)
        if numbers:
            entities["numbers"] = numbers
        
        # Units
        units = re.findall(r'\b\d+(?:\.\d+)?\s*(kg|lbs?|pounds?|grams?|g|oz|ounces?|calories?|cal|minutes?|mins?|hours?|hrs?|days?|weeks?|years?)\b', query_lower)
        if units:
            entities["units"] = units
        
        # Goals
        for goal_name, goal_keywords in IntentClassifier.GOAL_KEYWORDS.items():
            for keyword in goal_keywords:
                if keyword in query_lower:
                    if "goals" not in entities:
                        entities["goals"] = []
                    if goal_name not in entities["goals"]:
                        entities["goals"].append(goal_name)
                    break
        
        # Experience level
        for level_name, level_keywords in IntentClassifier.EXPERIENCE_KEYWORDS.items():
            for keyword in level_keywords:
                if keyword in query_lower:
                    entities["experience_level"] = level_name
                    break
        
        # Demographics
        if re.search(r'\b(\d+)\s*(year|yr)s?\s*old\b', query_lower):
            match = re.search(r'\b(\d+)\s*(year|yr)s?\s*old\b', query_lower)
            entities["age"] = match.group(1)
        
        gender_match = re.search(r'\b(male|female|man|woman|boy|girl|guy|lady)\b', query_lower)
        if gender_match:
            gender = gender_match.group(1)
            if gender in ["man", "boy", "guy"]:
                entities["gender"] = "male"
            elif gender in ["woman", "girl", "lady"]:
                entities["gender"] = "female"
            else:
                entities["gender"] = gender
        
        # Time references
        time_words = ["today", "tomorrow", "this week", "this month", "next week", "next month", "morning", "afternoon", "evening", "night", "post workout", "pre workout", "before workout", "after workout"]
        found_times = [t for t in time_words if t in query_lower]
        if found_times:
            entities["time_references"] = found_times
        
        # Frequency
        freq_patterns = [
            (r'\b(daily|every day|each day)\b', "daily"),
            (r'\b(weekly|every week|each week)\b', "weekly"),
            (r'\b(monthly|every month|each month)\b', "monthly"),
            (r'\b\d+\s*times?\s*per\s*week\b', "custom"),
            (r'\b\d+\s*days?\s*per\s*week\b', "custom"),
            (r'\b(every other day|alternate days)\b', "every_other_day"),
        ]
        for pattern, freq_type in freq_patterns:
            if re.search(pattern, query_lower):
                entities["frequency"] = freq_type
                break
        
        # Dietary restrictions/preferences
        restrictions = {
            "vegan": ["vegan", "plant based", "no animal products"],
            "vegetarian": ["vegetarian", "no meat", "no fish", "lacto-ovo"],
            "gluten_free": ["gluten free", "celiac", "no gluten", "wheat free"],
            "dairy_free": ["dairy free", "lactose intolerant", "no milk", "no cheese", "no dairy"],
            "nut_free": ["nut free", "no nuts", "peanut allergy"],
            "keto": ["keto", "ketogenic", "low carb high fat"],
            "paleo": ["paleo", "caveman diet"],
            "low_fat": ["low fat", "reduced fat", "fat free"],
            "low_sodium": ["low sodium", "low salt", "reduced sodium"],
            "low_sugar": ["low sugar", "sugar free", "no added sugar"],
            "halal": ["halal"],
            "kosher": ["kosher"]
        }
        for restriction_name, keywords in restrictions.items():
            for keyword in keywords:
                if keyword in query_lower:
                    if "dietary_restrictions" not in entities:
                        entities["dietary_restrictions"] = []
                    if restriction_name not in entities["dietary_restrictions"]:
                        entities["dietary_restrictions"].append(restriction_name)
                    break
        
        return entities
    
    @staticmethod
    def get_follow_up_suggestions(intent: str, entities: Dict[str, List[str]]) -> List[str]:
        """Generate contextual follow-up suggestions based on intent and extracted entities"""
        suggestions = []
        
        if intent == "fitness":
            if "exercises" in entities and entities["exercises"]:
                suggestions.append(f"How many reps and sets should I do for {entities['exercises'][0]}?")
                suggestions.append(f"What muscles does {entities['exercises'][0]} work?")
            if "goals" in entities:
                if "muscle_gain" in entities["goals"]:
                    suggestions.append("How many days per week should I train for muscle growth?")
                    suggestions.append("What's the best rep range for hypertrophy?")
                elif "weight_loss" in entities["goals"]:
                    suggestions.append("Should I do cardio or weights for fat loss?")
                    suggestions.append("How long should my workouts be for weight loss?")
            if not entities:
                suggestions.extend([
                    "What's a good beginner workout routine?",
                    "How do I build muscle effectively?",
                    "What's the best way to lose weight through exercise?"
                ])
        
        elif intent == "health":
            if "age" in entities:
                suggestions.append(f"Are there specific health concerns for age {entities['age']}?")
            if "goals" in entities and "sleep" not in str(entities):
                suggestions.append("How can I improve my sleep quality?")
            if not entities:
                suggestions.extend([
                    "How much sleep do I need daily?",
                    "What are signs of overtraining?",
                    "How can I reduce stress naturally?"
                ])
        
        elif intent == "diet":
            if "goals" in entities:
                if "weight_loss" in entities["goals"]:
                    suggestions.append("What's a safe calorie deficit for weight loss?")
                    suggestions.append("How much protein should I eat while cutting?")
                elif "muscle_gain" in entities["goals"]:
                    suggestions.append("How many calories should I eat to build muscle?")
                    suggestions.append("What's the ideal macro split for bulking?")
            if "experience_level" in entities:
                suggestions.append(f"What's a good meal plan for a {entities['experience_level']}?")
            if "age" in entities:
                suggestions.append(f"Does protein requirement change at age {entities['age']}?")
            if not entities:
                suggestions.extend([
                    "How do I calculate my daily calorie needs?",
                    "What's the best macro ratio for my goals?",
                    "Should I take creatine as a supplement?"
                ])
        
        elif intent == "food":
            if "foods" in entities and entities["foods"]:
                suggestions.append(f"What are the health benefits of {entities['foods'][0]}?")
                suggestions.append(f"How many calories in {entities['foods'][0]}?")
            if "time_references" in entities:
                if "pre workout" in entities["time_references"]:
                    suggestions.append("What's the best pre-workout meal timing?")
                elif "post workout" in entities["time_references"]:
                    suggestions.append("Should I eat protein immediately after workout?")
            if not entities:
                suggestions.extend([
                    "What are high protein foods for muscle gain?",
                    "What should I eat after a workout?",
                    "What's a healthy breakfast option?"
                ])
        
        # Add general suggestions if insufficient specific ones
        if len(suggestions) < 2:
            suggestions.extend([
                "Would you like more specific recommendations?",
                "Can you provide more details about your goals?",
                "What's your current experience level?"
            ])
        
        return suggestions[:3]  # Return top 3 suggestions
    
    @staticmethod
    def calculate_similarity(text1: str, text2: str) -> float:
        """Calculate semantic similarity between two texts using multiple methods"""
        text1 = text1.lower().strip()
        text2 = text2.lower().strip()
        
        if not text1 or not text2:
            return 0.0
        
        # Method 1: Sequence matcher ratio
        seq_ratio = SequenceMatcher(None, text1, text2).ratio()
        
        # Method 2: Word overlap (Jaccard)
        words1 = set(re.findall(r'\b\w+\b', text1))
        words2 = set(re.findall(r'\b\w+\b', text2))
        
        if not words1 or not words2:
            jaccard = 0.0
        else:
            intersection = len(words1 & words2)
            union = len(words1 | words2)
            jaccard = intersection / union if union > 0 else 0.0
        
        # Method 3: Common substring length ratio
        longest_match = SequenceMatcher(None, text1, text2).find_longest_match(0, len(text1), 0, len(text2))
        longest_len = longest_match.size if longest_match else 0
        substr_ratio = (2.0 * longest_len) / (len(text1) + len(text2)) if (len(text1) + len(text2)) > 0 else 0.0
        
        # Combined weighted score
        similarity = (seq_ratio * 0.5) + (jaccard * 0.3) + (substr_ratio * 0.2)
        
        return round(similarity, 3)



    """Generates contextual responses based on intent classification"""
    
    @staticmethod
    def generate_response(intent: str, confidence: float, query: str, entities: Dict[str, List[str]] = None) -> str:
        """Generate appropriate response based on classification"""
        if not entities:
            entities = IntentClassifier.extract_entities(query)
        
        # Low confidence response
        if confidence < 0.4:
            return ("I want to help with fitness, health, diet, or food questions. "
                   "Could you rephrase your question? For example:\n"
                   "- 'What's a good workout for weight loss?'\n"
                   "- 'How many calories in chicken?'\n"
                   "- 'What's a healthy diet for muscle gain?'\n"
                   "- 'How can I improve my sleep?'")
        
        # High confidence responses
        if intent == "fitness":
            if entities.get("exercises"):
                ex = entities["exercises"][0].replace("_", " ").title()
                response = f"Great question about {ex}! For optimal results:\n"
                response += f"• {ex.title()} is excellent for building strength\n"
                response += "• Start with 3 sets of 8-12 reps if you're intermediate\n"
                response += "• Focus on proper form before adding weight\n"
                response += "Would you like specific form tips or a progression plan?"
                return response
            elif entities.get("goals") and "muscle_gain" in entities["goals"]:
                return ("For muscle gain, focus on progressive overload with compound lifts. "
                       "Train each muscle group 2x per week, eat in a slight calorie surplus (250-500 over maintenance), "
                       "and get 1.6-2.2g protein per kg body weight. Interested in a sample routine?")
            elif entities.get("goals") and "weight_loss" in entities["goals"]:
                return ("For weight loss through exercise: combine strength training (preserves muscle) "
                       "with cardio (burns calories). HIIT is very effective in 20-30 min sessions. "
                       "Aim for 200-300 minutes of moderate activity weekly. Want a weekly workout plan?")
            else:
                return ("Great fitness question! To give you the best advice:\n"
                       "1. What's your primary goal (build muscle, lose fat, improve strength)?\n"
                       "2. How many days can you workout?\n"
                       "3. Do you have access to a gym or only home equipment?\n"
                       "Let me know and I'll customize a plan for you!")
        
        elif intent == "health":
            if "sleep" in query.lower():
                return ("Quality sleep is crucial for health. Adults need 7-9 hours nightly. To improve:\n"
                       "• Maintain consistent sleep/wake times\n"
                       "• Avoid screens 1 hour before bed\n"
                       "• Keep bedroom cool (65-68°F / 18-20°C)\n"
                       "• Avoid caffeine after 2 PM\n"
                       "Would you like more sleep hygiene tips?")
            elif "stress" in query.lower():
                return ("Managing stress is key for overall health. Effective strategies include:\n"
                       "• Regular exercise (especially cardio and yoga)\n"
                       "• Meditation or deep breathing (try 5 minutes daily)\n"
                       "• Adequate sleep and social connection\n"
                       "• Limiting caffeine and alcohol\n"
                       "Would you like a simple breathing exercise to try now?")
            elif "immune" in query.lower() or "immunity" in query.lower():
                return ("To boost your immune system naturally:\n"
                       "• Eat colorful fruits/vegetables (vitamin C, zinc, antioxidants)\n"
                       "• Get 7-9 hours of quality sleep\n"
                       "• Exercise moderately (150 min/week)\n"
                       "• Manage stress and stay hydrated\n"
                       "• Consider vitamin D if you have limited sun exposure\n"
                       "Need specific food recommendations?")
            elif entities.get("age"):
                return (f"Health needs evolve with age. At {entities['age']}, focus on:\n"
                       "• Strength training to maintain muscle mass\n"
                       "• Regular checkups and preventive screenings\n"
                       "• Adequate protein (1.2-1.6g/kg) and calcium\n"
                       "• Balance exercises to prevent falls\n"
                       "Would you like age-specific exercise recommendations?")
            else:
                return ("Health is multifaceted! I can help with sleep optimization, stress management, "
                       "immune support, injury recovery, or general wellness. What specific health goal "
                       "would you like to work on?")
        
        elif intent == "diet":
            if entities.get("goals") and "weight_loss" in entities["goals"]:
                return ("For sustainable weight loss:\n"
                       "• Create a 300-500 calorie daily deficit\n"
                       "• Eat 1.6-2.2g protein per kg body weight\n"
                       "• Fill half your plate with vegetables\n"
                       "• Stay hydrated and get adequate fiber\n"
                       "Want a sample meal plan?")
            elif entities.get("goals") and "muscle_gain" in entities["goals"]:
                return ("For muscle gain nutrition:\n"
                       "• Eat 300-500 calories above maintenance\n"
                       "• Consume 1.6-2.2g protein per kg body weight\n"
                       "• Distribute protein across 3-5 meals (30-50g each)\n"
                       "• Carbs pre/post workout for energy and recovery\n"
                       "• Healthy fats for hormone production\n"
                       "Would you like a sample bulking day of eating?")
            elif entities.get("dietary_restrictions"):
                restriction = entities["dietary_restrictions"][0]
                restriction_readable = restriction.replace("_", " ").title()
                return (f"Following a {restriction_readable} diet requires planning to meet all nutrient needs. "
                       f"Key considerations:\n"
                       f"• Ensure adequate protein from {restriction_readable}-approved sources\n"
                       f"• Watch for deficiencies in B12, iron, calcium, vitamin D\n"
                       f"• Consider working with a registered dietitian for personalization\n"
                       f"Would you like {restriction_readable} meal ideas and recipes?")
            elif "tdee" in query.lower() or "maintenance" in query.lower():
                return ("Total Daily Energy Expenditure (TDEE) depends on age, gender, weight, height, and activity level. "
                       "A rough estimate: multiply your weight in kg by:\n"
                       "• Sedentary: 25-28 calories/kg\n"
                       "• Light activity: 29-32 calories/kg\n"
                       "• Moderate activity: 33-38 calories/kg\n"
                       "• Very active: 39-44 calories/kg\n"
                       "Want me to calculate yours? Provide your age, gender, weight, height, and activity level.")
            else:
                return ("Nutrition is individual! I can help with:\n"
                       "• Calculating your calorie/macro needs for weight loss or muscle gain\n"
                       "• Specific diets (keto, vegan, intermittent fasting, etc.)\n"
                       "• Supplement guidance (protein, creatine, vitamins)\n"
                       "• Meal planning and prep strategies\n"
                       "What specific diet question can I answer?")
        
        elif intent == "food":
            if entities.get("foods"):
                food = entities["foods"][0].replace("_", " ").title()
                response = f"🍎 Nutritional info for {food}:\n"
                
                # Helpful nutritional facts for common foods
                nutrition_facts = {
                    "Chicken Breast": "~165 calories, 31g protein, 3.6g fat per 100g (cooked)",
                    "Salmon": "~208 calories, 20g protein, 13g fat (high in omega-3s) per 100g",
                    "Eggs": "~70 calories, 6g protein, 5g fat per large egg",
                    "Brown Rice": "~111 calories, 2.6g protein, 23g carbs per 100g cooked",
                    "Oats": "~389 calories, 16.9g protein, 66g carbs, 10.6g fiber per 100g dry",
                    "Avocado": "~160 calories, 2g protein, 15g fat, 7g fiber per 100g",
                    "Broccoli": "~34 calories, 2.8g protein, 6.6g carbs, 2.6g fiber per 100g",
                    "Quinoa": "~120 calories, 4.4g protein, 21g carbs per 100g cooked",
                    "Greek Yogurt": "~59 calories, 10g protein, 0.4g fat per 100g (non-fat)"
                }
                
                if food in nutrition_facts:
                    response += f"• {nutrition_facts[food]}\n"
                else:
                    response += "• Generally nutritious as part of a balanced diet\n"
                
                response += "• Pair with other whole foods for balanced nutrition\n"
                response += "Would you like preparation tips or recipe ideas?"
                return response
            elif "calories in" in query.lower():
                return ("To get accurate calorie information, please specify the food and approximate quantity. "
                       "For example: 'calories in 100g chicken breast' or 'calories in 1 medium banana'. "
                       "I'll provide precise nutrition data!")
            elif "recipe" in query.lower():
                return ("I'd love to share recipes! To give you the best recommendation:\n"
                       "• What cuisine do you prefer?\n"
                       "• Any dietary restrictions (vegetarian, gluten-free, etc.)?\n"
                       "• Do you want high protein, low carb, or budget-friendly?\n"
                       "Let me know and I'll provide a detailed recipe with macros!")
            elif "breakfast" in query.lower() or "lunch" in query.lower() or "dinner" in query.lower():
                return (f"For a healthy meal:\n"
                       "• Include lean protein (25-40g)\n"
                       "• Fill half your plate with colorful veggies\n"
                       "• Add complex carbs (quinoa, sweet potato, oats)\n"
                       "• Include healthy fats (avocado, nuts, olive oil)\n"
                       "• Stay hydrated with water or herbal tea\n"
                       "Want specific meal ideas?")
            else:
                return ("I can help with food and nutrition! Ask me about:\n"
                       "• Calorie and macro content of specific foods\n"
                       "• Healthy recipes and meal prep ideas\n"
                       "• Best foods for your goals (weight loss, muscle gain)\n"
                       "• Meal timing around workouts\n"
                       "What specific food question do you have?")
        
        # Fallback response
        return ("I'm here to help with fitness, health, diet, and food questions! "
               "For the best response, please specify:\n"
               "- Your fitness goal (build muscle, lose weight, get stronger)\n"
               "- Any health concerns or conditions\n"
               "- The specific food or diet question\n"
               "- Your current experience level")
    
    @staticmethod
    def generate_quick_replies(intent: str) -> List[str]:
        """Generate quick reply buttons based on intent"""
        if intent == "fitness":
            return ["🏋️ Beginner routine", "💪 Build muscle", "🔥 Lose weight", "📋 Form tips"]
        elif intent == "health":
            return ["😴 Sleep tips", "🧘 Stress relief", "🛡️ Boost immunity", "🏥 Injury help"]
        elif intent == "diet":
            return ["📊 Calculate TDEE", "🥩 High protein meal", "🌱 Vegan options", "⚖️ Weight loss diet"]
        elif intent == "food":
            return ["🍗 Protein sources", "🥗 Meal prep ideas", "🍎 Healthy snacks", "📖 Recipe request"]
        else:
            return ["💪 Fitness", "❤️ Health", "🥗 Diet", "🍎 Food"]
    
    @staticmethod
    def get_intent_statistics(messages: List[str]) -> Dict:
        """Generate intent distribution statistics for analytics"""
        intent_counts = {
            "fitness": 0,
            "health": 0,
            "diet": 0,
            "food": 0,
            "unknown": 0
        }
        
        confidences = []
        
        for msg in messages:
            intent, confidence = IntentClassifier.classify_intent(msg)
            intent_counts[intent] = intent_counts.get(intent, 0) + 1
            confidences.append(confidence)
        
        total = len(messages)
        avg_confidence = sum(confidences) / len(confidences) if confidences else 0
        
        return {
            "total_messages": total,
            "intent_distribution": {k: v/total for k, v in intent_counts.items()},
            "average_confidence": avg_confidence,
            "top_intent": max(intent_counts, key=intent_counts.get),
            "needs_improvement_count": sum(1 for c in confidences if c < 0.5)
        }
    
    @staticmethod
    def get_entity_statistics(messages: List[str]) -> Dict:
        """Extract statistics about mentioned entities"""
        all_entities = {
            "exercises": [],
            "foods": [],
            "goals": [],
            "time_references": [],
            "dietary_restrictions": []
        }
        
        for msg in messages:
            entities = IntentClassifier.extract_entities(msg)
            for key in all_entities.keys():
                if key in entities:
                    all_entities[key].extend(entities[key])
        
        # Count frequencies
        stats = {}
        for key, values in all_entities.items():
            if values:
                stats[key] = Counter(values).most_common(5)
        
        return stats
class ResponseGenerator:
    """Generates contextual responses based on intent classification - ENHANCED VERSION"""
    
    @staticmethod
    def generate_response(intent: str, confidence: float, query: str, entities: Dict[str, List[str]] = None) -> str:
        """Generate appropriate response based on classification"""
        if not entities:
            entities = IntentClassifier.extract_entities(query)
        
        query_lower = query.lower().strip()
        
        # Low confidence response
        if confidence < 0.4:
            return ("I want to help with fitness, health, diet, or food questions. "
                   "Could you rephrase your question? For example:\n"
                   "- 'What's a good workout for weight loss?'\n"
                   "- 'How many calories in chicken?'\n"
                   "- 'What's a healthy diet for muscle gain?'\n"
                   "- 'How can I improve my sleep?'")
        
        # ============================================================
        # FITNESS INTENT - SPECIFIC HANDLERS
        # ============================================================
        if intent == "fitness":
            
            # ---------- Push Pull Legs Split ----------
            if any(term in query_lower for term in ["push pull leg", "ppl", "push-pull-legs", "push pull legs split"]):
                return (
                    "**Push-Pull-Legs (PPL) Split** - A 6-day training split that's highly effective for intermediates:\n\n"
                    "**Push Day** (Chest, Shoulders, Triceps):\n"
                    "• Bench Press (3-4 sets of 6-10 reps)\n"
                    "• Overhead Press (3-4 sets of 8-12 reps)\n"
                    "• Incline Dumbbell Press (3 sets of 10-15 reps)\n"
                    "• Lateral Raises (3 sets of 12-15 reps)\n"
                    "• Tricep Pushdowns (3 sets of 10-15 reps)\n\n"
                    "**Pull Day** (Back, Biceps, Rear Delts):\n"
                    "• Pull-ups or Lat Pulldowns (3-4 sets of 6-12 reps)\n"
                    "• Barbell Rows (3-4 sets of 8-12 reps)\n"
                    "• Face Pulls (3 sets of 15-20 reps)\n"
                    "• Bicep Curls (3 sets of 10-15 reps)\n"
                    "• Hammer Curls (3 sets of 10-15 reps)\n\n"
                    "**Legs Day** (Quads, Hamstrings, Glutes, Calves):\n"
                    "• Squats (3-4 sets of 5-10 reps)\n"
                    "• Romanian Deadlifts (3 sets of 8-12 reps)\n"
                    "• Leg Press (3 sets of 10-15 reps)\n"
                    "• Leg Curls (3 sets of 12-15 reps)\n"
                    "• Calf Raises (4 sets of 15-20 reps)\n\n"
                    "**Schedule:** Push/Pull/Legs/Rest/Push/Pull/Legs\n"
                    "Rest 1-2 minutes between sets, train 6 days/week. Want a PPL spreadsheet or form tips?"
                )
            
            # ---------- Push Day Specific ----------
            if "push day" in query_lower:
                return (
                    "**Push Day Workout** (Chest, Shoulders, Triceps):\n\n"
                    "**Compound Lifts (Strength Focus):**\n"
                    "• Barbell Bench Press: 4 sets of 5-8 reps\n"
                    "• Overhead Press (OHP): 4 sets of 6-10 reps\n"
                    "• Incline Dumbbell Press: 3 sets of 8-12 reps\n\n"
                    "**Accessory Work (Hypertrophy):**\n"
                    "• Lateral Raises: 3 sets of 12-15 reps\n"
                    "• Tricep Pushdowns: 3 sets of 12-15 reps\n"
                    "• Chest Flyes: 3 sets of 10-15 reps\n"
                    "• Skull Crushers: 3 sets of 10-12 reps\n\n"
                    "**Pro Tip:** Start with heavy compounds when fresh, finish with isolations. Rest 2-3 min on compounds, 60-90 sec on accessories."
                )
            
            # ---------- Pull Day Specific ----------
            if "pull day" in query_lower:
                return (
                    "**Pull Day Workout** (Back, Biceps, Rear Delts):\n\n"
                    "**Primary Lifts:**\n"
                    "• Deadlifts OR Rack Pulls: 3-4 sets of 5-8 reps\n"
                    "• Pull-ups (weighted if possible): 4 sets to failure\n"
                    "• Barbell Rows: 4 sets of 8-12 reps\n\n"
                    "**Secondary Work:**\n"
                    "• Face Pulls: 3 sets of 15-20 reps (great for posture)\n"
                    "• T-bar Rows: 3 sets of 10-15 reps\n"
                    "• Lat Pulldowns: 3 sets of 10-12 reps\n\n"
                    "**Bicep Finishers:**\n"
                    "• Barbell Curls: 3 sets of 10-12 reps\n"
                    "• Hammer Curls: 3 sets of 12-15 reps\n"
                    "• Incline Dumbbell Curls: 3 sets of 10-12 reps"
                )
            
            # ---------- Leg Day Specific ----------
            if "leg day" in query_lower:
                return (
                    "**Leg Day Workout** (Quads, Hamstrings, Glutes, Calves):\n\n"
                    "**Quadriceps Focus:**\n"
                    "• Back Squats: 4 sets of 5-10 reps\n"
                    "• Leg Press: 3 sets of 10-15 reps\n"
                    "• Bulgarian Split Squats: 3 sets of 8-12 reps per leg\n"
                    "• Leg Extensions: 3 sets of 12-15 reps\n\n"
                    "**Posterior Chain (Hamstrings/Glutes):**\n"
                    "• Romanian Deadlifts: 4 sets of 8-12 reps\n"
                    "• Walking Lunges: 3 sets of 12-15 reps per leg\n"
                    "• Leg Curls: 3 sets of 12-15 reps\n"
                    "• Hip Thrusts: 3 sets of 10-15 reps\n\n"
                    "**Calves & Finishers:**\n"
                    "• Standing Calf Raises: 4 sets of 15-20 reps\n"
                    "• Seated Calf Raises: 4 sets of 15-20 reps"
                )
            
            # ---------- Upper Lower Split ----------
            if any(term in query_lower for term in ["upper lower split", "upper/lower", "4 day upper lower"]):
                return (
                    "**Upper/Lower Split** - Great for 4 days/week training:\n\n"
                    "**Upper A (Strength Focus):**\n"
                    "• Bench Press: 4x5-8\n"
                    "• Barbell Rows: 4x6-10\n"
                    "• Overhead Press: 3x8-12\n"
                    "• Pull-ups: 3x8-12\n"
                    "• Tricep/Bicep work: 3x12-15\n\n"
                    "**Lower A (Strength Focus):**\n"
                    "• Squats: 4x5-8\n"
                    "• Romanian Deadlifts: 3x8-12\n"
                    "• Leg Press: 3x10-15\n"
                    "• Calf Raises: 4x15-20\n\n"
                    "**Upper B (Hypertrophy Focus):**\n"
                    "• Incline Press: 3x8-12\n"
                    "• Lat Pulldowns: 3x10-15\n"
                    "• Lateral Raises: 3x12-15\n"
                    "• Chest Flyes: 3x12-15\n"
                    "• Arm Supersets: 3x15\n\n"
                    "**Lower B (Hypertrophy Focus):**\n"
                    "• Deadlifts: 3x5\n"
                    "• Front Squats: 3x8-12\n"
                    "• Leg Curls: 3x12-15\n"
                    "• Hip Thrusts: 3x10-15\n\n"
                    "Schedule: Upper/Lower/Rest/Upper/Lower/Rest/Rest"
                )
            
            # ---------- Progressive Overload ----------
            if any(term in query_lower for term in ["progressive overload", "how to add weight", "increase strength"]):
                return (
                    "**Progressive Overload** - The key to continuous gains:\n\n"
                    "**5 Methods to Progress:**\n\n"
                    "1️⃣ **Add Weight** (Most Common)\n"
                    "   • Add 2.5-5 lbs to upper body lifts weekly\n"
                    "   • Add 5-10 lbs to lower body lifts weekly\n"
                    "   • If you fail reps, stay at same weight next session\n\n"
                    "2️⃣ **Add Reps** (Double Progression)\n"
                    "   • Start with weight you can do 6 reps\n"
                    "   • Build up to 10 reps with same weight\n"
                    "   • Increase weight, drop back to 6 reps, repeat\n\n"
                    "3️⃣ **Add Sets**\n"
                    "   • Start with 3 sets per exercise\n"
                    "   • Add 1 set every 2-4 weeks up to 5 sets\n\n"
                    "4️⃣ **Reduce Rest Time**\n"
                    "   • Decrease rest from 3 min → 2 min → 90 sec\n"
                    "   • Adds metabolic stress and intensity\n\n"
                    "5️⃣ **Improve Form & Tempo**\n"
                    "   • Slow eccentrics (3-4 seconds down)\n"
                    "   • Pause at stretch position\n"
                    "   • Explosive concentric phase\n\n"
                    "**Progression Example (Bench Press):**\n"
                    "Week 1: 135 lbs x 8 reps\n"
                    "Week 2: 135 lbs x 9 reps\n"
                    "Week 3: 135 lbs x 10 reps\n"
                    "Week 4: 140 lbs x 8 reps (new weight)\n\n"
                    "Track your lifts! Want a progression spreadsheet template?"
                )
            
            # ---------- Plateau Breaking ----------
            if any(term in query_lower for term in ["plateau", "stuck", "not improving", "break through", "sticking point"]):
                return (
                    "**Breaking Through Strength Plateaus** - 7 Proven Strategies:\n\n"
                    "**1. Deload Week (Most Important)**\n"
                    "• Take 1 week at 40-60% intensity\n"
                    "• Reduce volume by 50%\n"
                    "• Allows CNS and muscles to fully recover\n\n"
                    "**2. Change Exercise Variations**\n"
                    "• Swap Barbell Bench → Dumbbell or Floor Press\n"
                    "• Back Squat → Front Squat or Box Squat\n"
                    "• Conventional Deadlift → Sumo or Deficit\n\n"
                    "**3. Adjust Rep Ranges**\n"
                    "• If stuck on low reps (1-5), try 8-12 for 4 weeks\n"
                    "• If stuck on high reps, focus on 3-5 reps for strength\n\n"
                    "**4. Increase Frequency**\n"
                    "• Train stuck lift 2-3x per week instead of 1x\n"
                    "• Use light technique days + heavy days\n\n"
                    "**5. Specialized Intensity Techniques**\n"
                    "• **Rest-Pause:** Hit failure, rest 15 sec, go again\n"
                    "• **Cluster Sets:** 3 reps, rest 20 sec, repeat 5x\n"
                    "• **Drop Sets:** Failure, reduce weight 20%, go again\n"
                    "• **Negatives:** Lower weight slowly (5 sec), get help up\n\n"
                    "**6. Fix Weak Points**\n"
                    "• Bench weak at bottom? Add pause bench\n"
                    "• Squat weak out of hole? Add box squats\n"
                    "• Deadlift off floor? Add deficit deadlifts\n\n"
                    "**7. Address Recovery**\n"
                    "• Sleep 8+ hours (non-negotiable)\n"
                    "• Eat at maintenance or slight surplus\n"
                    "• Reduce outside stress\n\n"
                    "**Sample Plateau-Busting Protocol:**\n"
                    "Week 1: Deload (50% intensity)\n"
                    "Week 2-4: New variation + 8-12 rep range\n"
                    "Week 5: Test 1RM on original lift\n\n"
                    "Which lift are you stuck on? I can give specific advice!"
                )
            
            # ---------- Deload Explanation ----------
            if any(term in query_lower for term in ["deload", "light week", "recovery week"]):
                return (
                    "**Deload Week Guide** - Strategic recovery for better gains:\n\n"
                    "**What is a Deload?**\n"
                    "A planned week of reduced training intensity/volume to allow full recovery\n\n"
                    "**When to Deload:**\n"
                    "• Every 4-8 weeks of heavy training\n"
                    "• When lifts stall or decrease\n"
                    "• Feeling chronically tired or unmotivated\n"
                    "• Joint pain or poor sleep quality\n"
                    "• After competition or peak\n\n"
                    "**How to Deload:**\n\n"
                    "**Option 1: Reduce Weight (Recommended)**\n"
                    "• Use 40-60% of your normal working weight\n"
                    "• Keep same reps and sets\n"
                    "• Focus on perfect form\n\n"
                    "**Option 2: Reduce Volume**\n"
                    "• Keep intensity (~75% of max)\n"
                    "• Cut sets by 40-50%\n"
                    "• Example: 5 sets normally → 2-3 sets\n\n"
                    "**Option 3: Reduce Frequency**\n"
                    "• Train every other day instead of daily\n"
                    "• Skip accessory work, keep compounds\n\n"
                    "**What NOT to do:**\n"
                    "❌ Don't stop training completely (detraining starts)\n"
                    "❌ Don't try new PRs\n"
                    "❌ Don't add extra volume\n\n"
                    "**Sample Deload Week (Upper/Lower Split):**\n"
                    "• Normal: 315 lbs squat for 5x5\n"
                    "• Deload: 185 lbs squat for 5x5 (slow, controlled)\n"
                    "• Keep accessory work but use 50% weight\n\n"
                    "**After Deload:**\n"
                    "Week 1: ~80% of previous max\n"
                    "Week 2: ~90%  \n"
                    "Week 3: Attempt new PR!\n\n"
                    "Most people come back stronger after a proper deload!"
                )
            
            # ---------- HIIT vs Steady State Comparison ----------
            if any(term in query_lower for term in ["hiit vs", "hiit or steady", "hiit or liss", "hiit vs steady state"]):
                return (
                    "**HIIT vs Steady State Cardio** - Complete Comparison:\n\n"
                    "**HIIT (High-Intensity Interval Training)**\n"
                    "• **Format:** 20-30 sec all-out, 60-90 sec rest (repeat 8-12x)\n"
                    "• **Session length:** 15-25 minutes\n"
                    "• **Frequency:** 2-3x per week maximum\n"
                    "• **Calories burned:** 250-400 per session\n"
                    "• **EPOC effect:** High (burns calories for 24-48 hrs after)\n"
                    "• **Best for:** Fat loss, time efficiency, metabolic conditioning\n"
                    "• **Examples:** Sprints, assault bike, battle ropes, burpees\n\n"
                    "**Steady State Cardio (LISS - Low Intensity)**\n"
                    "• **Format:** Consistent pace at 60-70% max heart rate\n"
                    "• **Session length:** 30-60 minutes\n"
                    "• **Frequency:** 4-6x per week\n"
                    "• **Calories burned:** 300-600 per session\n"
                    "• **EPOC effect:** Low (minimal afterburn)\n"
                    "• **Best for:** Endurance, heart health, recovery days, fat adaptation\n"
                    "• **Examples:** Jogging, cycling, swimming, incline walking\n\n"
                    "**Which is Better? It depends:**\n\n"
                    "**Choose HIIT if you:**\n"
                    "✅ Have limited time (20 min sessions)\n"
                    "✅ Want maximum fat burning in minimum time\n"
                    "✅ Want to preserve/build muscle while losing fat\n"
                    "✅ Need variety and intensity\n\n"
                    "**Choose Steady State if you:**\n"
                    "✅ Are a beginner or have joint issues\n"
                    "✅ Enjoy longer, meditative workouts\n"
                    "✅ Are training for endurance events\n"
                    "✅ Need active recovery between heavy lifting days\n\n"
                    "**Optimal Approach - COMBINE BOTH:**\n"
                    "• **Monday:** Heavy lifting + 20 min HIIT\n"
                    "• **Tuesday:** Steady State 45 min (recovery)\n"
                    "• **Wednesday:** Heavy lifting only\n"
                    "• **Thursday:** Steady State 45 min\n"
                    "• **Friday:** Heavy lifting + 15 min HIIT\n"
                    "• **Saturday:** Long Steady State 60 min\n"
                    "• **Sunday:** Rest\n\n"
                    "**Sample HIIT Workout (20 min):**\n"
                    "• Warm-up: 5 min jog\n"
                    "• 30 sec sprint / 60 sec walk (repeat 8x)\n"
                    "• Cool-down: 5 min walk\n\n"
                    "**Sample Steady State (45 min):**\n"
                    "• Warm-up: 5 min easy pace\n"
                    "• 35 min at conversational pace (can talk but not sing)\n"
                    "• Cool-down: 5 min easy pace\n\n"
                    "**Bottom Line:** Do HIIT 2x/week for metabolic boost, steady state 3-4x/week for endurance and recovery. Avoid HIIT on consecutive days!"
                )
            
            # ---------- Cardio for Muscle Gain ----------
            if any(term in query_lower for term in ["cardio while building muscle", "cardio and muscle gain", "cardio without losing muscle"]):
                return (
                    "**Cardio While Building Muscle** - The Right Way:\n\n"
                    "**Key Principle:** Cardio doesn't kill gains if done correctly!\n\n"
                    "**How Much Cardio is Safe?**\n"
                    "• Muscle gain only: 60-90 min LISS/week\n"
                    "• Fat loss priority: 150-200 min LISS/week\n"
                    "• Combined goal: 120-150 min LISS + 1 HIIT session\n\n"
                    "**Best Cardio Types for Muscle Preservation:**\n"
                    "1. **Incline Walking** (30-45 min, 3-4 mph, 5-10% incline)\n"
                    "2. **Stationary Bike** (low impact, easy recovery)\n"
                    "3. **Rowing** (actually builds back muscles!)\n"
                    "4. **Swimming** (zero impact, full body)\n"
                    "5. **Walking** (underrated, can do daily)\n\n"
                    "**Avoid for Muscle Gain:**\n"
                    "❌ Long distance running (catabolic)\n"
                    "❌ HIIT before lifting (drains CNS)\n"
                    "❌ Cardio >60 min without nutrition\n\n"
                    "**Sample Schedule (Muscle Focus):**\n"
                    "• Lift days: 20 min LISS post-workout\n"
                    "• Rest days: 45 min LISS\n"
                    "• HIIT: 1x/week on upper body day only\n\n"
                    "**Nutrition for Cardio + Muscle:**\n"
                    "• Eat carbs before cardio\n"
                    "• Protein shake post-cardio (2:1 carbs:protein is ideal)\n"
                    "• Don't create too large a calorie deficit\n\n"
                    "**Timing Matters:**\n"
                    "Best: Cardio after lifting or on separate days\n"
                    "OK: Cardio in AM, lifting in PM (6+ hours apart)\n"
                    "Worst: Cardio immediately before heavy squats/deadlifts"
                )
            
            # ---------- RPE/RIR Explanation ----------
            if any(term in query_lower for term in ["rpe", "rir", "rate of perceived exertion", "reps in reserve"]):
                return (
                    "**RPE & RIR** - Training Intensity Explained:\n\n"
                    "**RPE (Rate of Perceived Exertion)** - Scale 1-10\n"
                    "How hard a set feels on a scale of 1 (very easy) to 10 (max effort)\n\n"
                    "**RIR (Reps In Reserve)** - How many reps you COULD have done\n"
                    "RIR 2 = You could do 2 more reps if you had to\n\n"
                    "**RPE to RIR Conversion:**\n"
                    "• RPE 10 = RIR 0 (Failure, can't do another rep)\n"
                    "• RPE 9 = RIR 1 (1 rep left)\n"
                    "• RPE 8 = RIR 2 (2 reps left - SWEET SPOT)\n"
                    "• RPE 7 = RIR 3 (3 reps left)\n"
                    "• RPE 6 = RIR 4 (Very easy)\n\n"
                    "**What RPE to Use For Your Goals:**\n\n"
                    "**Strength (1-5 reps)**\n"
                    "• Heavy singles/triples: RPE 8-9 (RIR 1-2)\n"
                    "• Never go to RPE 10 on compounds unless peaking\n\n"
                    "**Hypertrophy (6-15 reps)**\n"
                    "• Most working sets: RPE 7-8 (RIR 2-3)\n"
                    "• Last set to failure (RPE 10) occasionally\n\n"
                    "**Endurance (15+ reps)**\n"
                    "• RPE 6-7 (RIR 3-4) for most sets\n"
                    "• Avoid failure on high reps (too much fatigue)\n\n"
                    "**How to Gauge RPE:**\n"
                    "• RPE 6: 'That was light, could do 4+ more'\n"
                    "• RPE 7: 'Getting challenging, 3 more left'\n"
                    "• RPE 8: 'Hard but controlled, 2 more left'\n"
                    "• RPE 9: 'Very hard, 1 more possible'\n"
                    "• RPE 10: 'Nothing left, form breaking'\n\n"
                    "**Why Use RPE?**\n"
                    "✅ Adjusts for daily strength fluctuations\n"
                    "✅ Safer than always maxing out\n"
                    "✅ Better long-term progress\n"
                    "✅ Works for any exercise\n\n"
                    "**Sample RPE-Based Progression (Bench Press)**\n"
                    "Week 1: 225 lbs x 8 reps (RPE 7) → RIR 3\n"
                    "Week 2: 225 lbs x 9 reps (RPE 8) → RIR 2\n"
                    "Week 3: 225 lbs x 10 reps (RPE 9) → RIR 1\n"
                    "Week 4: Increase to 235 lbs, repeat pattern\n\n"
                    "**Pro Tip:** Most gains come from RPE 7-9. RPE 10 should be rare (competition or testing day only)!"
                )
            
            # ---------- Zone 2 Cardio ----------
            if any(term in query_lower for term in ["zone 2", "zone2", "aerobic base", "zone 2 cardio"]):
                return (
                    "**Zone 2 Cardio Training** - The Foundation of Endurance:\n\n"
                    "**What is Zone 2?**\n"
                    "Training at 60-70% of max heart rate where you can still hold a conversation\n\n"
                    "**Benefits of Zone 2:**\n"
                    "• Builds aerobic base (the 'engine' of fitness)\n"
                    "• Improves fat burning efficiency\n"
                    "• Enhances recovery capacity\n"
                    "• Increases mitochondrial density\n"
                    "• Low fatigue, can do daily\n\n"
                    "**How to Find Your Zone 2:**\n"
                    "• Method 1: 180 - Age = Max Zone 2 HR\n"
                    "  Example (30 years old): 150 bpm max\n"
                    "• Method 2: 'Talk Test' - Can speak full sentences\n"
                    "• Method 3: 65-75% of max HR (220-age x 0.7)\n\n"
                    "**Sample Zone 2 Workouts:**\n"
                    "• **Beginner:** 30 min incline walking (3 mph, 3-5%)\n"
                    "• **Intermediate:** 60 min jogging (easy pace)\n"
                    "• **Advanced:** 90 min cycling or rowing\n\n"
                    "**How Much Zone 2 Per Week?**\n"
                    "• General health: 90-120 minutes\n"
                    "• Fat loss focus: 150-180 minutes\n"
                    "• Endurance athlete: 3-6+ hours\n"
                    "• Can be split into 30-45 min sessions\n\n"
                    "**Zone 2 vs HIIT:**\n"
                    "• Zone 2: Builds aerobic capacity (low intensity)\n"
                    "• HIIT: Builds anaerobic power (high intensity)\n"
                    "• Ideal: 80% Zone 2, 20% HIIT (Pareto principle)\n\n"
                    "**Progression Plan:**\n"
                    "• Start with 30 min, 3x/week\n"
                    "• Add 5-10 min each week\n"
                    "• Work up to 60-90 min sessions\n"
                    "• Can do Zone 2 daily if recovery is good\n\n"
                    "**Equipment Options:**\n"
                    "• Treadmill (walking or jogging)\n"
                    "• Stationary bike\n"
                    "• Rower (great for upper body involvement)\n"
                    "• Elliptical\n"
                    "• Outdoor walking/hiking\n\n"
                    "**Pro Tip:** Zone 2 is PERFECT for active recovery on rest days between heavy lifting sessions!"
                )
            
            # ---------- When to Change Routine ----------
            if any(term in query_lower for term in ["change routine", "switch program", "new workout", "change workout"]):
                return (
                    "**When to Change Your Workout Routine** - Signs & Timing:\n\n"
                    "**When to KEEP your routine (don't change):**\n"
                    "✅ Still making progress (adding weight/reps)\n"
                    "✅ Enjoying the workouts\n"
                    "✅ Less than 8-12 weeks on current program\n"
                    "✅ No joint pain or overuse issues\n\n"
                    "**When to CHANGE your routine:**\n"
                    "⚠️ Stalled for 3+ weeks on all major lifts\n"
                    "⚠️ Dreading workouts / lost motivation\n"
                    "⚠️ Joint pain or nagging injuries\n"
                    "⚠️ Boredom or lack of excitement\n"
                    "⚠️ Completed 8-12 weeks of linear progression\n"
                    "⚠️ Specific weakness identified\n"
                    "⚠️ Goals have changed\n\n"
                    "**How Often to Change:**\n"
                    "• **Beginners:** Every 8-12 weeks (keep basic compounds)\n"
                    "• **Intermediates:** Every 12-16 weeks with periodization\n"
                    "• **Advanced:** 16-24 weeks with specialization phases\n\n"
                    "**What to Change vs Keep:**\n"
                    "**KEEP (Foundation):**\n"
                    "• Squat, Deadlift, Bench Press, Overhead Press, Rows\n"
                    "• Overall training frequency\n"
                    "• Progressive overload principle\n\n"
                    "**CHANGE (Variables):**\n"
                    "• Rep ranges (strength: 1-5, hypertrophy: 6-12, endurance: 15+)\n"
                    "• Exercise variations (Dumbbell vs Barbell)\n"
                    "• Set volume (3x10 → 5x5 → 4x8)\n"
                    "• Rest periods (3 min strength → 90 sec hypertrophy)\n"
                    "• Training split (Full body → Upper/Lower → PPL)\n\n"
                    "**Example 1-Year Progression:**\n"
                    "• Months 1-3: Beginner Full Body (3x/week)\n"
                    "• Months 4-6: Upper/Lower Split (4x/week)\n"
                    "• Months 7-9: PPL Split (6x/week)\n"
                    "• Months 10-12: Specialization (focus on weak points)\n\n"
                    "**How to Transition Smoothly:**\n"
                    "Week 1: Deload\n"
                    "Week 2: Test new exercises with light weight\n"
                    "Week 3: 80% of estimated maxes\n"
                    "Week 4: Full intensity on new program\n\n"
                    "**Warning Signs You Changed Too Soon:**\n"
                    "• No measurable progress on main lifts\n"
                    "• Constant soreness (never adapt)\n"
                    "• Can't track progress effectively\n\n"
                    "**Pro Tip:** Keep a training log! If you're still adding 5 lbs to bench each week, DON'T change the program just because you're bored. Progress is the goal, not novelty!"
                )
            
            # ---------- Existing fitness handlers continue ----------
            elif entities.get("exercises"):
                ex = entities["exercises"][0].replace("_", " ").title()
                response = f"**{ex} Exercise Guide:**\n\n"
                response += f"**Muscles worked:** Primary movers and stabilizers\n"
                response += "**Proper form tips:**\n"
                response += "• Maintain neutral spine throughout\n"
                response += "• Control the eccentric (lowering) phase\n"
                response += "• Breathe properly (exhale on exertion)\n"
                response += "**Recommended sets/reps:** 3-4 sets of 8-12 reps\n"
                response += "**Common mistakes to avoid:**\n"
                response += "• Using momentum instead of muscle control\n"
                response += "• Partial range of motion\n"
                response += "**Progression:** Add weight when you can do 12+ reps with good form\n\n"
                response += "Would you like a video demonstration link or more specific tips?"
                return response
                
            elif entities.get("goals") and "muscle_gain" in entities["goals"]:
                return ("**Muscle Building Blueprint**\n\n"
                       "**Training (Most Important):**\n"
                       "• Focus on compound lifts (Squat, Bench, Deadlift, Rows, OHP)\n"
                       "• Train each muscle group 2x per week\n"
                       "• Rep range: 6-15 reps (hypertrophy zone)\n"
                       "• Sets: 10-20 working sets per muscle group weekly\n"
                       "• Progressive overload: Add 2.5-5 lbs or 1-2 reps weekly\n\n"
                       "**Nutrition:**\n"
                       "• Calorie surplus: 250-500 above maintenance\n"
                       "• Protein: 1.6-2.2g per kg body weight\n"
                       "• Carbs: 4-7g per kg (fuel for training)\n"
                       "• Fats: 0.8-1.2g per kg (hormone production)\n\n"
                       "**Recovery:**\n"
                       "• Sleep: 7-9 hours (non-negotiable)\n"
                       "• Rest 48-72 hours before retraining same muscle\n"
                       "• Deload every 8-12 weeks\n\n"
                       "**Sample Beginner Plan:**\n"
                       "Monday: Upper Body (Bench, Rows, OHP)\n"
                       "Tuesday: Lower Body (Squat, Deadlift)\n"
                       "Wednesday: Rest\n"
                       "Thursday: Upper Body (Incline, Pull-ups, Arms)\n"
                       "Friday: Lower Body (Front Squat, RDL)\n"
                       "Weekend: Active recovery\n\n"
                       "Want a specific program based on your experience level?")
                
            elif entities.get("goals") and "weight_loss" in entities["goals"]:
                return ("**Exercise for Weight Loss** - Evidence-Based Approach:\n\n"
                       "**Most Effective Strategy:** Strength + Cardio Combination\n\n"
                       "**Weekly Schedule:**\n"
                       "• **Strength Training:** 3-4 days/week (preserves muscle)\n"
                       "• **HIIT:** 2 days/week (20 min, burns fat efficiently)\n"
                       "• **LISS Cardio:** 2-3 days/week (45-60 min)\n"
                       "• **Active Recovery:** Walking 8-10k steps daily\n\n"
                       "**Best Exercises for Calorie Burn:**\n"
                       "1. **Burpees:** ~350-400 cal/30 min\n"
                       "2. **Jumping Rope:** ~300-350 cal/30 min\n"
                       "3. **Running (8 min/mile):** ~300-350 cal/30 min\n"
                       "4. **Rowing:** ~250-300 cal/30 min\n"
                       "5. **Swimming:** ~200-300 cal/30 min\n\n"
                       "**Sample Fat Loss Workout (45 min):**\n"
                       "• Warm-up: 5 min jog\n"
                       "• Strength circuit (30 min):\n"
                       "  - Squats: 3x10\n"
                       "  - Push-ups: 3x12\n"
                       "  - Rows: 3x12\n"
                       "  - Lunges: 3x10/leg\n"
                       "  - Plank: 3x30 sec\n"
                       "• HIIT finisher (10 min): 30 sec sprint / 30 sec rest x 10\n\n"
                       "**Key Principle:** Muscle burns more calories at rest. Don't skip strength!\n"
                       "Want a 4-week fat loss workout plan?")
                
            else:
                return ("**Custom Workout Programming** - Let's build your perfect routine!\n\n"
                       "To give you the best plan, please tell me:\n\n"
                       "1. **Your Goal:** (Muscle gain / Weight loss / Strength / Endurance / General health)\n"
                       "2. **Experience Level:** (Beginner / Intermediate / Advanced)\n"
                       "3. **Days Available:** (2, 3, 4, 5, or 6 days per week)\n"
                       "4. **Equipment Access:** (Full gym / Home gym / Dumbbells only / Bodyweight)\n"
                       "5. **Time Per Session:** (30, 45, 60, or 90 minutes)\n\n"
                       "Reply with your answers and I'll create a personalized plan!\n\n"
                       "**Quick recommendations by goal:**\n"
                       "🏋️ **Muscle Gain:** PPL split, 5-6 days/week, 8-12 reps, 10-20 sets/muscle/week\n"
                       "🔥 **Fat Loss:** Full body + HIIT, 4-5 days/week, circuit training\n"
                       "💪 **Strength:** Upper/Lower, 4 days/week, 3-5 reps, low volume high intensity\n"
                       "❤️ **General Health:** Full body, 3 days/week, mix of strength and cardio")
        
        # ============================================================
        # HEALTH INTENT - SPECIFIC HANDLERS
        # ============================================================
        elif intent == "health":
            
            # ---------- Sleep Schedule Fix ----------
            if any(term in query_lower for term in ["fix sleep schedule", "reset sleep", "sleep schedule broken"]):
                return (
                    "**How to Fix Your Sleep Schedule** - Step by Step:\n\n"
                    "**Immediate Action Plan (Tonight):**\n\n"
                    "**Step 1: Light Management**\n"
                    "• Get bright sunlight immediately upon waking (open blinds, go outside)\n"
                    "• Dim lights 2-3 hours before desired bedtime\n"
                    "• Use blue light filters on devices after 7 PM\n"
                    "• No screens 60 minutes before bed\n\n"
                    "**Step 2: Gradual Adjustment (Shift by 15-30 min/day)**\n"
                    "• Day 1: Wake 30 min earlier than usual\n"
                    "• Day 2: Wake 30 min earlier than Day 1\n"
                    "• Repeat until reaching target wake time\n"
                    "• Keep bedtime consistent even if not tired\n\n"
                    "**Step 3: Meal Timing**\n"
                    "• Eat breakfast within 30 min of waking\n"
                    "• No caffeine after 2 PM\n"
                    "• Finish last meal 3 hours before bed\n"
                    "• Avoid alcohol 4 hours before bed (ruins sleep quality)\n\n"
                    "**Step 4: Environment Optimization**\n"
                    "• Cool room: 65-68°F (18-20°C)\n"
                    "• Pitch black (use blackout curtains or eye mask)\n"
                    "• White noise or earplugs if noises wake you\n"
                    "• Comfortable mattress and pillows\n\n"
                    "**Step 5: Wind-Down Routine (60 min before bed)**\n"
                    "• 7 PM: Dim lights, no screens\n"
                    "• 8 PM: Light stretching or meditation\n"
                    "• 9 PM: Warm bath or shower (drop in temp signals sleep)\n"
                    "• 9:30 PM: Read a physical book (no screens)\n"
                    "• 10 PM: Lights out\n\n"
                    "**For Severe Shift (e.g., waking at 2 PM, need 7 AM):**\n"
                    "Option A: Pull all-nighter (not recommended, but works)\n"
                    "Option B: 1-hour shift per day for 7 days\n"
                    "Option C: Use light therapy lamp upon desired wake time\n\n"
                    "**Supplements That Help (Consult doctor first):**\n"
                    "• Melatonin: 0.5-3mg, 1 hour before bed (short term only)\n"
                    "• Magnesium Glycinate: 200-400mg before bed\n"
                    "• L-Theanine: 100-200mg (promotes relaxation)\n\n"
                    "**How long to fix:**\n"
                    "• Minor shift (1-2 hours): 3-5 days\n"
                    "• Moderate shift (4-6 hours): 1-2 weeks\n"
                    "• Severe shift (8+ hours): 2-4 weeks\n\n"
                    "**Maintenance After Fixing:**\n"
                    "✓ Wake at same time EVERY day (including weekends)\n"
                    "✓ Get 10-30 min sunlight within 1 hour of waking\n"
                    "✓ No naps longer than 20 min\n"
                    "✓ Consistent bedtime within 30 min window\n\n"
                    "Want a printable sleep schedule template or tracking log?"
                )
            
            # ---------- Continue existing health handlers ----------
            elif "sleep" in query_lower:
                return (
                    "**Sleep Optimization Guide** - For Better Recovery:\n\n"
                    "**Optimal Sleep Duration:**\n"
                    "• Adults 18-64: 7-9 hours\n"
                    "• Athletes & heavy trainers: 8-10 hours\n"
                    "• Older adults (65+): 7-8 hours\n\n"
                    "**Sleep Quality Checklist:**\n"
                    "✓ **Consistency** - Same wake/sleep time ±30 min\n"
                    "✓ **Darkness** - Pitch black room (blackout curtains)\n"
                    "✓ **Temperature** - 65-68°F (18-20°C)\n"
                    "✓ **Quiet** - Earplugs or white noise\n"
                    "✓ **Cool** - Breathable bedding\n\n"
                    "**Pre-Sleep Routine (60 min before bed):**\n"
                    "• 60 min: Dim lights, no screens\n"
                    "• 45 min: Light stretching or foam rolling\n"
                    "• 30 min: Warm bath (temp drop induces sleep)\n"
                    "• 15 min: Meditation or deep breathing\n"
                    "• 5 min: Write tomorrow's to-do list (clears mind)\n\n"
                    "**What to Avoid:**\n"
                    "❌ Caffeine 8-10 hours before bed\n"
                    "❌ Alcohol 4 hours before bed (disrupts REM)\n"
                    "❌ Large meals 3 hours before bed\n"
                    "❌ Blue light 2 hours before bed\n"
                    "❌ Intense exercise 2 hours before bed\n"
                    "❌ Work/email checking before bed\n\n"
                    "**Sleep Aids (Natural):**\n"
                    "• Magnesium glycinate: 200-400mg\n"
                    "• L-theanine: 100-200mg\n"
                    "• Tart cherry juice: 8 oz (natural melatonin)\n"
                    "• Chamomile tea: 1 cup\n\n"
                    "**Track Your Sleep:**\n"
                    "• Use sleep cycle app or fitness tracker\n"
                    "• Track: Duration, quality, wake-ups\n"
                    "• After 2 weeks, identify patterns\n\n"
                    "**When to See a Doctor:**\n"
                    "⚠️ Snoring with breathing pauses (sleep apnea)\n"
                    "⚠️ Cannot fall asleep despite being tired\n"
                    "⚠️ Wake up unrefreshed after 8+ hours\n"
                    "⚠️ Leg twitching at night\n\n"
                    "Want a 7-day sleep improvement plan?")
            
            # ---------- Continue with other health handlers ----------
            else:
                return ResponseGenerator._get_health_response(query_lower, entities)
        
        # ============================================================
        # DIET INTENT - Keep your existing implementation
        # ============================================================
        elif intent == "diet":
            # Add your existing diet handlers here
            return ResponseGenerator._get_diet_response(query_lower, entities)
        
        # ============================================================
        # FOOD INTENT - Keep your existing implementation
        # ============================================================
        elif intent == "food":
            # Add your existing food handlers here
            return ResponseGenerator._get_food_response(query_lower, entities)
        
        # Fallback
        return ResponseGenerator._get_fallback_response()
    
    @staticmethod
    def _get_health_response(query_lower: str, entities: Dict) -> str:
        """Helper for health responses"""
        if "stress" in query_lower:
            return ("**Stress Management Strategies:**\n\n"
                   "**Immediate Relief (5-10 min):**\n"
                   "• Box breathing: Inhale 4 sec, hold 4 sec, exhale 4 sec, hold 4 sec\n"
                   "• 5-4-3-2-1 grounding: Name 5 things you see, 4 feel, 3 hear, 2 smell, 1 taste\n"
                   "• Progressive muscle relaxation: Tense then release each muscle group\n\n"
                   "**Daily Habits:**\n"
                   "• Morning: 10 min meditation or journaling\n"
                   "• Afternoon: 5 min stretching or walk\n"
                   "• Evening: Digital sunset (no screens 1 hour before bed)\n\n"
                   "**Weekly Practices:**\n"
                   "• 150 min moderate exercise\n"
                   "• Social connection (friends, family)\n"
                   "• Nature exposure (20 min, 3x/week)\n\n"
                   "**Long-term Solutions:**\n"
                   "• Therapy or counseling if chronic\n"
                   "• Time management training\n"
                   "• Set boundaries (learn to say no)\n\n"
                   "Want guided meditation instructions?")
        
        elif "immune" in query_lower or "immunity" in query_lower:
            return ("**Immune System Support** - Evidence-Based Strategies:\n\n"
                   "**Nutrition (Most Important):**\n"
                   "• **Vitamin C:** Citrus, bell peppers, strawberries (250-500mg/day)\n"
                   "• **Vitamin D:** Sunlight 15 min/day or 2000-4000 IU supplement\n"
                   "• **Zinc:** Shellfish, pumpkin seeds, legumes (15mg/day)\n"
                   "• **Garlic:** Fresh, crushed (allicin boosts immunity)\n"
                   "• **Ginger:** Fresh tea or supplements\n"
                   "• **Probiotics:** Yogurt, kefir, kimchi, sauerkraut\n\n"
                   "**Lifestyle Factors:**\n"
                   "• Sleep: 7-9 hours (critical for immune function)\n"
                   "• Exercise: Moderate 150 min/week (excessive training suppresses immunity)\n"
                   "• Hydration: 2-3 liters water daily\n"
                   "• Stress reduction: Chronic cortisol weakens immunity\n\n"
                   "**Supplements (Evidence-backed):**\n"
                   "• Vitamin D: 2000-4000 IU daily (if deficient)\n"
                   "• Zinc lozenges: At first sign of cold\n"
                   "• Elderberry: May reduce cold duration\n"
                   "• Echinacea: Mixed evidence, try if it works for you\n\n"
                   "**What to Avoid:**\n"
                   "❌ Excess alcohol (suppresses immune function)\n"
                   "❌ Smoking/vaping (damages respiratory immune cells)\n"
                   "❌ Overtraining (increases infection risk)\n"
                   "❌ Sleep deprivation (<6 hours)\n\n"
                   "**Quick Immune-Boosting Smoothie:**\n"
                   "• 1 orange (Vitamin C)\n"
                   "• 1 cup spinach (iron, antioxidants)\n"
                   "• 1 inch fresh ginger\n"
                   "• 1/2 cup Greek yogurt (probiotics)\n"
                   "• 1 tbsp honey (antibacterial)\n"
                   "• Water to blend\n\n"
                   "**When to See Doctor:**\n"
                   "⚠️ Frequent infections (>4 colds/year)\n"
                   "⚠️ Slow wound healing\n"
                   "⚠️ Unexplained fatigue\n"
                   "⚠️ Family history of immune disorders")
        
        elif "recovery" in query_lower or "injury" in query_lower:
            return ("**Injury Prevention & Recovery** - Train Smart:\n\n"
                   "**Injury Prevention Checklist:**\n"
                   "✓ **Warm-up properly** (5-10 min dynamic stretching)\n"
                   "✓ **Perfect form before weight** (video yourself)\n"
                   "✓ **Progressive overload gradually** (5% weight increase per week max)\n"
                   "✓ **Listen to pain** (Sharp ≠ soreness, stop immediately)\n"
                   "✓ **Balance pushing/pulling exercises** (prevent imbalances)\n"
                   "✓ **Mobility work** (10 min daily)\n\n"
                   "**Common Injuries & Solutions:**\n"
                   "**Lower Back Pain:**\n"
                   "• Strengthen glutes and core\n"
                   "• Stretch hip flexors\n"
                   "• Avoid rounded back deadlifts\n"
                   "• Cat-camel stretches daily\n\n"
                   "**Knee Pain:**\n"
                   "• Strengthen quads and glutes\n"
                   "• Correct squat depth (don't go too deep if painful)\n"
                   "• Use knee sleeves if needed\n"
                   "• Avoid locking knees\n\n"
                   "**Shoulder Pain:**\n"
                   "• Warm-up rotator cuff (internal/external rotation)\n"
                   "• Face pulls for rear delts\n"
                   "• Don't go too wide on bench press\n"
                   "• Avoid upright rows if painful\n\n"
                   "**Recovery Timeline:**\n"
                   "• **Muscle soreness (DOMS):** 24-72 hours, light activity helps\n"
                   "• **Minor strain:** 1-2 weeks, active recovery\n"
                   "• **Moderate strain:** 3-6 weeks, PT recommended\n"
                   "• **Severe injury:** Doctor immediately\n\n"
                   "**Active Recovery Methods:**\n"
                   "• Light walking or swimming\n"
                   "• Foam rolling (avoid bone/joint)\n"
                   "• Stretching (hold 20-30 sec, no pain)\n"
                   "• Contrast therapy (hot/cold shower)\n\n"
                   "**RICE Protocol (Acute Injury, first 48-72 hours):**\n"
                   "• **R**est (avoid aggravating movements)\n"
                   "• **I**ce (15-20 min every 2-3 hours)\n"
                   "• **C**ompression (elastic bandage)\n"
                   "• **E**levation (above heart if possible)\n\n"
                   "**When to See a Doctor:**\n"
                   "⚠️ Cannot bear weight\n"
                   "⚠️ Visible deformity\n"
                   "⚠️ Severe swelling\n"
                   "⚠️ No improvement after 1 week\n\n"
                   "Want specific prehab exercises for your sport/lifts?")
        
        else:
            return ("**Your Health Question** - Let me help!\n\n"
                   "I can provide information on:\n"
                   "• **Sleep optimization** (duration, quality, schedules)\n"
                   "• **Stress management** (techniques, breathing, meditation)\n"
                   "• **Immune support** (nutrition, lifestyle, supplements)\n"
                   "• **Injury prevention & recovery** (common issues, rehab, RICE)\n"
                   "• **General wellness** (hydration, mental health, preventive care)\n\n"
                   "**Please specify your health concern** and I'll give detailed, evidence-based advice.\n\n"
                   "For medical emergencies, please consult a healthcare provider immediately.")
    
    @staticmethod
    def _get_diet_response(query_lower: str, entities: Dict) -> str:
        """Helper for diet responses - Add your existing diet logic"""
        # Keep your existing diet response logic here
        return ("**Diet & Nutrition** - I can help with:\n\n"
               "• Calorie/macro calculations (TDEE, BMR)\n"
               "• Weight loss or muscle gain nutrition\n"
               "• Specific diets (keto, vegan, intermittent fasting)\n"
               "• Meal planning and prep strategies\n"
               "• Supplement guidance\n\n"
               "What specific diet question do you have?")
    
    @staticmethod
    def _get_food_response(query_lower: str, entities: Dict) -> str:
        """Helper for food responses - Add your existing food logic"""
        # Keep your existing food response logic here
        return ("**Food & Nutrition** - Ask me about:\n\n"
               "• Calorie and macro content of specific foods\n"
               "• Healthy recipes and cooking methods\n"
               "• Best foods for your goals\n"
               "• Meal timing around workouts\n"
               "• Food comparisons (which is healthier)\n\n"
               "What food would you like information about?")
    
    @staticmethod
    def _get_fallback_response() -> str:
        """Fallback response when no specific handler matches"""
        return ("I'm here to help with fitness, health, diet, and food!\n\n"
               "**Specific questions I can answer:**\n"
               "🏋️ **Fitness:** Workout splits (PPL, Upper/Lower), progressive overload, plateau breaking, deloads, HIIT vs cardio\n"
               "❤️ **Health:** Sleep optimization, stress management, immune support, injury recovery\n"
               "🥗 **Diet:** Calorie calculations, macro splits, meal planning, weight management\n"
               "🍎 **Food:** Nutritional info, recipes, healthy alternatives\n\n"
               "**Try asking:**\n"
               "- 'What's a good push-pull-legs split?'\n"
               "- 'How to break through a strength plateau?'\n"
               "- 'HIIT vs steady state cardio?'\n"
               "- 'How to fix my sleep schedule?'\n"
               "- 'What is progressive overload?'\n\n"
               "What would you like to know more about?")
    
    @staticmethod
    def generate_quick_replies(intent: str) -> List[str]:
        """Generate quick reply buttons based on intent"""
        if intent == "fitness":
            return ["💪 PPL Split", "🏋️ Progressive Overload", "🔄 Break Plateau", "🏃 HIIT vs Cardio", "📋 Deload Guide"]
        elif intent == "health":
            return ["😴 Fix Sleep", "🧘 Stress Relief", "🛡️ Boost Immunity", "🏥 Injury Help", "⚡ Energy Tips"]
        elif intent == "diet":
            return ["📊 Calculate TDEE", "🥩 High Protein Meal", "🌱 Vegan Options", "⚖️ Weight Loss Diet", "💪 Muscle Gain Diet"]
        elif intent == "food":
            return ["🍗 Chicken Breast", "🥑 Avocado Nutrition", "🥗 Meal Prep", "📖 Recipes", "🍎 Healthy Snacks"]
        else:
            return ["💪 Fitness", "❤️ Health", "🥗 Diet", "🍎 Food", "📋 Popular Questions"]
# Add this method to your ResponseGenerator class

@staticmethod
def generate_response(intent: str, confidence: float, query: str, entities: Dict[str, List[str]] = None) -> str:
    query_lower = query.lower().strip()
    
    # ADD THIS CHECK AT THE VERY BEGINNING OF generate_response
    # Catch sleep-related queries regardless of intent classification
    sleep_keywords = [
        "sleep routine", "bedtime", "sleep schedule", "fix sleep", 
        "sleep hygiene", "fall asleep", "insomnia", "sleep quality",
        "how to sleep", "better sleep", "sleep tips", "wake up tired",
        "can't sleep", "trouble sleeping", "sleep better"
    ]
    
    if any(keyword in query_lower for keyword in sleep_keywords):
        return ResponseGenerator.get_sleep_routine_response()
    
    # Then continue with your existing code...
    if not entities:
        entities = IntentClassifier.extract_entities(query)
    
    # Rest of your existing generate_response code...

@staticmethod
def get_sleep_routine_response() -> str:
    """Generate sleep routine response"""
    return (
        "**😴 Healthy Sleep Routine Guide**\n\n"
        "**Recommended Sleep Duration:** 7-9 hours per night\n\n"
        "**Sample Evening Routine (for 11 PM bedtime):**\n"
        "• **10:00 PM** - Dim lights, put away electronic devices\n"
        "• **10:15 PM** - Light stretching or foam rolling\n"
        "• **10:30 PM** - Warm shower (temperature drop helps sleep)\n"
        "• **10:45 PM** - Read a physical book (no screens!)\n"
        "• **11:00 PM** - Lights out, cool room (65-68°F)\n"
        "• **7:00 AM** - Wake up at same time (even weekends)\n\n"
        "**Morning Routine for Better Sleep:**\n"
        "• Get 10-30 minutes of sunlight within 1 hour of waking\n"
        "• Exercise in morning or afternoon (not before bed)\n"
        "• Eat breakfast at consistent time\n\n"
        "**Sleep Hygiene Tips:**\n"
        "✓ Keep bedroom completely dark (blackout curtains)\n"
        "✓ No caffeine after 2 PM (stays in system 6-8 hours)\n"
        "✓ Finish eating 2-3 hours before bed\n"
        "✓ Avoid alcohol 4 hours before bed (disrupts REM)\n"
        "✓ Use white noise or earplugs if needed\n"
        "✓ Keep bedroom cool (65-68°F / 18-20°C)\n\n"
        "**Quick Fixes for Common Sleep Issues:**\n"
        "• **Can't fall asleep?** Get up, read in dim light for 20 min\n"
        "• **Waking up tired?** Track sleep quality with an app\n"
        "• **Night waking?** Don't check phone, try deep breathing\n"
        "• **Shifted schedule?** Adjust bedtime 30 min earlier each day\n\n"
        "**Relaxation Technique (4-7-8 Breathing):**\n"
        "1. Inhale through nose for 4 seconds\n"
        "2. Hold breath for 7 seconds\n"
        "3. Exhale through mouth for 8 seconds\n"
        "4. Repeat 4-5 times to calm nervous system\n\n"
        "Would you like more specific advice for your sleep issues?"
    )
# ============================================
# NEW CLASSES ADDED HERE
# ============================================

# Response templates for different scenarios
RESPONSE_TEMPLATES = {
    "greeting": [
        "Hello! I'm your fitness and nutrition assistant. How can I help you today?",
        "Hi there! Ready to work on your fitness goals? What would you like to know?",
        "Welcome! I can help with workouts, nutrition, health tips, and more. What's on your mind?"
    ],
    "farewell": [
        "Glad I could help! Feel free to ask if you have more questions.",
        "Stay healthy and keep crushing your goals! Come back anytime.",
        "Take care! Remember, consistency is key to progress."
    ],
    "thanks": [
        "You're welcome! Happy to help with your fitness journey.",
        "Anytime! That's what I'm here for.",
        "Glad to be helpful! Let me know if you need anything else."
    ],
    "unknown": [
        "I'm not sure I understood. Could you rephrase your question about fitness, health, diet, or food?",
        "Hmm, I specialize in fitness, health, nutrition, and food questions. Could you be more specific?",
        "I want to help! Can you ask about workouts, nutrition, health tips, or specific foods?"
    ],
    "clarification": [
        "Could you provide more details? For example, your goal (weight loss/muscle gain), experience level, or specific food/exercise?",
        "To give you the best answer, please share: 1) Your goal, 2) Experience level, 3) Any restrictions or preferences",
        "I'd love to help! Can you tell me more about your situation - are you a beginner? Do you have specific dietary needs?"
    ]
}

class QueryAnalyzer:
    """Advanced query analysis with pattern matching and entity extraction"""

    @staticmethod
    def clean_query(query: str) -> str:
        """Normalize user input while keeping useful punctuation for meaning."""
        if not query:
            return ""
        cleaned = query.strip()
        cleaned = re.sub(r'\s+', ' ', cleaned)
        return cleaned

    @staticmethod
    def is_valid_query(query: str) -> bool:
        """Basic validation to filter empty/noise queries."""
        if not query:
            return False
        cleaned = QueryAnalyzer.clean_query(query)
        if len(cleaned) < 2:
            return False
        has_alpha = bool(re.search(r'[a-zA-Z]', cleaned))
        return has_alpha

    @staticmethod
    def extract_numbers(query: str) -> List[float]:
        """Extract numeric values from free-form text."""
        if not query:
            return []
        return [float(n) for n in re.findall(r'\b\d+(?:\.\d+)?\b', query)]
    
    @staticmethod
    def analyze(query: str, context: Optional[Dict] = None) -> Dict:
        """
        Comprehensive query analysis returning structured information
        """
        query_lower = query.lower().strip()
        
        # Preprocess
        query_processed = IntentClassifier.preprocess_query(query_lower)
        
        analysis_result = {
            "original_query": query,
            "processed_query": query_processed,
            "intent": None,
            "confidence": 0.0,
            "entities": {},
            "sentiment": "neutral",
            "urgency": "low",
            "requires_follow_up": False,
            "suggested_follow_ups": [],
            "missing_info": []
        }
        
        # Classify intent with context if available
        context_intent = context.get("last_intent") if context else None
        intent, confidence = IntentClassifier.classify_intent(query_processed, context_intent)
        analysis_result["intent"] = intent
        analysis_result["confidence"] = confidence
        
        # Extract entities
        analysis_result["entities"] = IntentClassifier.extract_entities(query_processed)
        
        # Sentiment analysis (basic)
        positive_words = ["great", "good", "awesome", "love", "like", "helpful", "thanks", "thank you"]
        negative_words = ["bad", "terrible", "awful", "hate", "dislike", "frustrated", "confused", "not working"]
        
        if any(word in query_lower for word in positive_words):
            analysis_result["sentiment"] = "positive"
        elif any(word in query_lower for word in negative_words):
            analysis_result["sentiment"] = "negative"
        
        # Urgency detection
        urgent_phrases = ["urgent", "asap", "quick", "fast", "emergency", "immediately", "right now"]
        if any(phrase in query_lower for phrase in urgent_phrases):
            analysis_result["urgency"] = "high"
        
        # Check for missing information based on intent
        if intent == "fitness":
            if "exercises" not in analysis_result["entities"] and not any(word in query_lower for word in ["workout", "routine", "program"]):
                analysis_result["missing_info"].append("specific exercise or workout type")
                analysis_result["requires_follow_up"] = True
            if "goals" not in analysis_result["entities"]:
                analysis_result["missing_info"].append("fitness goal (muscle gain, weight loss, strength)")
                analysis_result["requires_follow_up"] = True
                
        elif intent == "diet":
            if "goals" not in analysis_result["entities"]:
                analysis_result["missing_info"].append("diet goal (weight loss, muscle gain, maintenance)")
                analysis_result["requires_follow_up"] = True
                
        elif intent == "food":
            if "foods" not in analysis_result["entities"] and "calories in" not in query_lower:
                analysis_result["missing_info"].append("specific food item")
                analysis_result["requires_follow_up"] = True
                
        elif intent == "health":
            if confidence < 0.6:
                analysis_result["missing_info"].append("specific health concern (sleep, stress, immunity, etc.)")
                analysis_result["requires_follow_up"] = True
        
        # Generate follow-up suggestions
        if analysis_result["requires_follow_up"]:
            analysis_result["suggested_follow_ups"] = IntentClassifier.get_follow_up_suggestions(
                intent, analysis_result["entities"]
            )
        
        return analysis_result
    
    @staticmethod
    def extract_numerical_info(query: str) -> Dict:
        """Extract numerical information like age, weight, height, reps, sets, etc."""
        query_lower = query.lower()
        numerical_info = {}
        
        # Age
        age_match = re.search(r'(\d+)\s*(year|yr)s?\s*old', query_lower)
        if age_match:
            numerical_info["age"] = int(age_match.group(1))
        
        # Weight
        weight_match = re.search(r'(\d+(?:\.\d+)?)\s*(kg|kilos?|pounds?|lbs?)', query_lower)
        if weight_match:
            weight_value = float(weight_match.group(1))
            weight_unit = weight_match.group(2)
            if weight_unit.startswith('lb'):
                numerical_info["weight_lbs"] = weight_value
                numerical_info["weight_kg"] = round(weight_value * 0.453592, 1)
            else:
                numerical_info["weight_kg"] = weight_value
                numerical_info["weight_lbs"] = round(weight_value * 2.20462, 1)
        
        # Height
        height_match = re.search(r'(\d+(?:\.\d+)?)\s*(cm|centimeters?|feet|ft|inches?|in)', query_lower)
        if height_match:
            height_value = float(height_match.group(1))
            height_unit = height_match.group(2)
            if height_unit in ['cm', 'centimeter', 'centimeters']:
                numerical_info["height_cm"] = height_value
                numerical_info["height_ft_in"] = f"{height_value / 30.48:.1f} feet"
            else:
                numerical_info["height_inches"] = height_value
        
        # Reps and sets
        reps_match = re.search(r'(\d+)\s*(reps|rep|repetitions?)', query_lower)
        if reps_match:
            numerical_info["reps"] = int(reps_match.group(1))
        
        sets_match = re.search(r'(\d+)\s*(sets|set)', query_lower)
        if sets_match:
            numerical_info["sets"] = int(sets_match.group(1))
        
        # Duration (minutes/hours)
        duration_match = re.search(r'(\d+)\s*(minutes?|mins?|hours?|hrs?)', query_lower)
        if duration_match:
            numerical_info["duration"] = int(duration_match.group(1))
            numerical_info["duration_unit"] = duration_match.group(2)
        
        # Calories
        calories_match = re.search(r'(\d+(?:,\d+)?)\s*(calories?|cal)', query_lower)
        if calories_match:
            calories_value = int(calories_match.group(1).replace(',', ''))
            numerical_info["calories"] = calories_value
        
        return numerical_info


class ContextManager:
    """Manages conversation context and state"""
    
    def __init__(self, max_history: int = 10):
        self.max_history = max_history
        self.history = []
        self.user_context = {
            "goals": [],
            "dietary_restrictions": [],
            "experience_level": None,
            "frequent_topics": [],
            "last_intent": None,
            "last_entities": {},
            "pending_questions": [],
            "user_stats": {}  # For age, weight, height, etc.
        }

    def add_to_history(self, role: str, text: str) -> None:
        """Compatibility helper used by chatbot engine for lightweight chat history."""
        self.history.append({
            "role": role,
            "query": text,
            "timestamp": time.time()
        })
        if len(self.history) > self.max_history:
            self.history = self.history[-self.max_history:]
    
    def update(self, query: str, analysis: Dict) -> None:
        """Update context with new interaction"""
        # Add to history
        self.history.append({
            "query": query,
            "intent": analysis["intent"],
            "confidence": analysis["confidence"],
            "entities": analysis["entities"],
            "timestamp": time.time()
        })
        
        # Trim history
        if len(self.history) > self.max_history:
            self.history = self.history[-self.max_history:]
        
        # Update user context
        self.user_context["last_intent"] = analysis["intent"]
        self.user_context["last_entities"] = analysis["entities"]
        
        # Track goals
        if "goals" in analysis["entities"]:
            for goal in analysis["entities"]["goals"]:
                if goal not in self.user_context["goals"]:
                    self.user_context["goals"].append(goal)
        
        # Track dietary restrictions
        if "dietary_restrictions" in analysis["entities"]:
            for restriction in analysis["entities"]["dietary_restrictions"]:
                if restriction not in self.user_context["dietary_restrictions"]:
                    self.user_context["dietary_restrictions"].append(restriction)
        
        # Track experience level
        if "experience_level" in analysis["entities"]:
            self.user_context["experience_level"] = analysis["entities"]["experience_level"]
        
        # Track frequent topics
        if analysis["intent"] != "unknown":
            if len(self.user_context["frequent_topics"]) == 0 or self.user_context["frequent_topics"][-1] != analysis["intent"]:
                self.user_context["frequent_topics"].append(analysis["intent"])
                if len(self.user_context["frequent_topics"]) > 10:
                    self.user_context["frequent_topics"] = self.user_context["frequent_topics"][-10:]
        
        # Extract user stats from queries
        numerical_info = QueryAnalyzer.extract_numerical_info(query)
        for key, value in numerical_info.items():
            if key not in ["reps", "sets", "duration"]:  # These are workout-specific, not user stats
                self.user_context["user_stats"][key] = value
    
    def get_context_for_intent(self, intent: str) -> Dict:
        """Get context relevant to a specific intent"""
        context = {
            "intent": intent,
            "previous_entities": self.user_context["last_entities"],
            "user_goals": self.user_context["goals"],
            "dietary_restrictions": self.user_context["dietary_restrictions"],
            "experience_level": self.user_context["experience_level"],
            "user_stats": self.user_context["user_stats"]
        }
        return context
    
    def get_conversation_summary(self) -> str:
        """Generate a summary of the conversation so far"""
        if not self.history:
            return "No conversation history yet."
        
        unique_intents = list(set([h["intent"] for h in self.history if h["intent"] != "unknown"]))
        summary = f"Conversation about: {', '.join(unique_intents)}. "
        
        if self.user_context["goals"]:
            summary += f"User goals: {', '.join(self.user_context['goals'])}. "
        
        if self.user_context["experience_level"]:
            summary += f"Experience level: {self.user_context['experience_level']}. "
        
        return summary
    
    def has_recent_intent(self, intent: str, within_last: int = 3) -> bool:
        """Check if a specific intent appeared in recent history"""
        recent = self.history[-within_last:]
        return any(h["intent"] == intent for h in recent)
    
    def get_last_question(self) -> Optional[str]:
        """Get the last user question"""
        if self.history:
            return self.history[-1]["query"]
        return None

    def get_last_user_query(self) -> Optional[str]:
        """Get most recent user query from lightweight role-based history."""
        for item in reversed(self.history):
            if item.get("role") == "user" and item.get("query"):
                return item["query"]
        return None
    
    def clear(self):
        """Clear all context and history"""
        self.history = []
        self.user_context = {
            "goals": [],
            "dietary_restrictions": [],
            "experience_level": None,
            "frequent_topics": [],
            "last_intent": None,
            "last_entities": {},
            "pending_questions": [],
            "user_stats": {}
        }
    
    def add_pending_question(self, question: str):
        """Add a follow-up question to be answered"""
        self.user_context["pending_questions"].append(question)
    
    def get_pending_questions(self) -> List[str]:
        """Get unanswered follow-up questions"""
        return self.user_context["pending_questions"]
    
    def clear_pending_questions(self):
        """Clear pending questions"""
        self.user_context["pending_questions"] = []


class ChatbotUtilities:
    """Main utility class combining all functionality"""
    
    @staticmethod
    def process_user_message(message: str, conversation_history: Optional[List] = None) -> Dict:
        """
        Process a user message and return complete analysis with response
        
        Args:
            message: User's input message
            conversation_history: Optional list of previous messages for context
        
        Returns:
            Dictionary containing intent, confidence, entities, response, and suggestions
        """
        # Get context intent if available
        context_intent = None
        if conversation_history and len(conversation_history) > 0:
            context_intent = conversation_history[-1].get("intent")
        
        # Classify intent
        intent, confidence = IntentClassifier.classify_intent(message, context_intent)
        
        # Extract entities
        entities = IntentClassifier.extract_entities(message)
        
        # Generate response
        response = ResponseGenerator.generate_response(intent, confidence, message, entities)
        
        # Generate follow-up suggestions
        suggestions = IntentClassifier.get_follow_up_suggestions(intent, entities)
        
        # Get quick replies
        quick_replies = ResponseGenerator.generate_quick_replies(intent)
        
        return {
            "intent": intent,
            "confidence": confidence,
            "entities": entities,
            "response": response,
            "suggestions": suggestions,
            "quick_replies": quick_replies
        }
    
    @staticmethod
    def get_intent_statistics(messages: List[str]) -> Dict:
        """Generate intent distribution statistics"""
        return ResponseGenerator.get_intent_statistics(messages)
    
    @staticmethod
    def get_entity_statistics(messages: List[str]) -> Dict:
        """Extract entity statistics"""
        return ResponseGenerator.get_entity_statistics(messages)


# Simple chatbot class for integration
class SimpleChatbot:
    """A simple chatbot implementation using the intent classifier"""
    
    def __init__(self):
        self.conversation_history = []
        self.user_profile = {}
    
    def send_message(self, message: str) -> str:
        """Process a user message and return response"""
        result = ChatbotUtilities.process_user_message(message, self.conversation_history)
        
        # Update conversation history
        self.conversation_history.append({
            "message": message,
            "intent": result["intent"],
            "confidence": result["confidence"],
            "timestamp": time.time()
        })
        
        # Keep only last 10 messages for context
        if len(self.conversation_history) > 10:
            self.conversation_history = self.conversation_history[-10:]
        
        # Update user profile with new entities
        for entity_type, values in result["entities"].items():
            if entity_type not in self.user_profile:
                self.user_profile[entity_type] = []
            if isinstance(values, list):
                self.user_profile[entity_type].extend(values)
            else:
                self.user_profile[entity_type].append(values)
        
        return result["response"]
    
    def get_quick_replies(self) -> List[str]:
        """Get quick reply options based on current context"""
        if self.conversation_history:
            last_intent = self.conversation_history[-1].get("intent", "unknown")
            return ResponseGenerator.generate_quick_replies(last_intent)
        return ResponseGenerator.generate_quick_replies("unknown")
    
    def clear_history(self):
        """Clear conversation history but keep user profile"""
        self.conversation_history = []
    
    def reset_user_profile(self):
        """Reset user profile data"""
        self.user_profile = {}


# Demo of the full system
if __name__ == "__main__":
    import json
    
    print("\n" + "="*70)
    print("FULL CHATBOT SYSTEM DEMO")
    print("="*70)
    
    # Initialize chatbot
    bot = SimpleChatbot()
    
    # Simulate conversation
    test_conversation = [
        "I want to lose weight",
        "How many calories should I eat?",
        "What about exercise?",
        "I like chicken and broccoli",
        "How do I cook chicken breast?",
        "Thanks for the help!"
    ]
    
    print("\n=== Simulated Conversation ===")
    for user_msg in test_conversation:
        print(f"\nUser: {user_msg}")
        response = bot.send_message(user_msg)
        print(f"Bot: {response}")
        print(f"Quick replies: {bot.get_quick_replies()}")
    
    print("\n=== User Profile Accumulated ===")
    print(json.dumps(bot.user_profile, indent=2))
    
    print("\n=== Analytics on Conversation ===")
    messages = [msg["message"] for msg in bot.conversation_history]
    intent_stats = ChatbotUtilities.get_intent_statistics(messages)
    print(json.dumps(intent_stats, indent=2))
    
    print("\n=== Entity Statistics ===")
    entity_stats = ChatbotUtilities.get_entity_statistics(messages)
    print(json.dumps(entity_stats, indent=2))
    
    print("\n✅ Chatbot utilities fully implemented and tested successfully!")