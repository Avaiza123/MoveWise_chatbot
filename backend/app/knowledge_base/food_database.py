# Food Database and Nutrition Facts - Complete Edition
# Last Updated: 2024

FOOD_DATABASE = {
    "foods": {
        "chicken_breast": {
            "category": "Protein",
            "serving_size": "100g (cooked)",
            "calories": 165,
            "protein": 31,
            "carbs": 0,
            "fat": 3.6,
            "saturated_fat": 1.0,
            "fiber": 0,
            "sugar": 0,
            "sodium": 74,
            "potassium": 256,
            "iron": 1.0,
            "calcium": 15,
            "vitamin_b6": 0.6,
            "benefits": ["Lean protein", "Low fat", "Versatile", "Muscle building", "High satiety"],
            "preparation": "Grill, bake, or boil",
            "shelf_life": "3-4 days refrigerated",
            "freezer_life": "4-6 months",
            "cost_level": "$$",
            "season": "Year-round"
        },
        "salmon": {
            "category": "Protein + Omega-3",
            "serving_size": "100g (cooked)",
            "calories": 206,
            "protein": 22,
            "carbs": 0,
            "fat": 12,
            "saturated_fat": 2.5,
            "omega_3": 2.5,
            "fiber": 0,
            "sugar": 0,
            "sodium": 61,
            "potassium": 363,
            "vitamin_d": 11.0,
            "vitamin_b12": 3.2,
            "benefits": ["Omega-3 fatty acids", "Heart health", "Brain health", "Anti-inflammatory", "Skin health"],
            "preparation": "Bake, grill, or pan-sear",
            "shelf_life": "1-2 days refrigerated",
            "freezer_life": "2-3 months",
            "cost_level": "$$$",
            "varieties": ["Atlantic", "Sockeye", "Coho", "Chinook"],
            "wild_vs_farmed": "Wild has more omega-3s"
        },
        "eggs": {
            "category": "Protein",
            "serving_size": "1 large egg (50g)",
            "calories": 70,
            "protein": 6,
            "carbs": 0.6,
            "fat": 5,
            "saturated_fat": 1.6,
            "fiber": 0,
            "sugar": 0.6,
            "sodium": 62,
            "potassium": 63,
            "iron": 0.9,
            "calcium": 28,
            "vitamin_d": 1.0,
            "vitamin_b12": 0.5,
            "choline": 147,
            "benefits": ["Complete amino acids", "Choline for brain", "Versatile", "Eye health (lutein)", "Budget protein"],
            "preparation": "Boil, fry, scramble, or bake",
            "shelf_life": "3-5 weeks refrigerated",
            "cost_level": "$",
            "cooking_times": {"soft_boil": "6 min", "hard_boil": "10 min", "poached": "3-4 min"},
            "grades": ["AA", "A", "B"]
        },
        "greek_yogurt": {
            "category": "Protein + Probiotics",
            "serving_size": "100g (plain, non-fat)",
            "calories": 59,
            "protein": 10,
            "carbs": 3,
            "fat": 0.4,
            "saturated_fat": 0.2,
            "fiber": 0,
            "sugar": 3,
            "sodium": 36,
            "calcium": 110,
            "probiotics": ["Lactobacillus", "Bifidobacterium"],
            "benefits": ["Gut health", "Calcium for bones", "Versatile", "High protein", "Low calorie"],
            "note": "Choose plain, unsweetened for health benefits",
            "shelf_life": "1-2 weeks refrigerated",
            "cost_level": "$$",
            "comparison": "Much higher protein than regular yogurt"
        },
        "broccoli": {
            "category": "Vegetable",
            "serving_size": "100g (raw)",
            "calories": 34,
            "protein": 2.8,
            "carbs": 7,
            "fat": 0.4,
            "saturated_fat": 0.1,
            "fiber": 2.4,
            "sugar": 1.7,
            "sodium": 33,
            "potassium": 316,
            "vitamin_c": 89,
            "vitamin_k": 102,
            "vitamin_a": 31,
            "folate": 63,
            "calcium": 47,
            "iron": 0.7,
            "benefits": ["Vitamin C (high)", "Sulforaphane (cancer fighter)", "Low calorie", "Bone health", "Immune support"],
            "preparation": "Steam, roast, or eat raw",
            "tip": "Steam for 3-4 minutes to maximize nutrients",
            "shelf_life": "1 week refrigerated",
            "freezer_life": "10-12 months",
            "cost_level": "$",
            "season": "Peak: October-April"
        },
        "sweet_potato": {
            "category": "Carbohydrate",
            "serving_size": "100g (baked with skin)",
            "calories": 86,
            "protein": 1.6,
            "carbs": 20,
            "fat": 0.1,
            "saturated_fat": 0,
            "fiber": 3,
            "sugar": 4.2,
            "sodium": 55,
            "potassium": 337,
            "vitamin_a": 709,
            "vitamin_c": 12,
            "manganese": 0.5,
            "benefits": ["Beta-carotene", "Potassium", "Sustained energy", "Vitamin B6", "Antioxidants"],
            "preparation": "Bake, roast, or steam",
            "best_for": "Pre or post-workout",
            "shelf_life": "1-2 weeks cool dark place",
            "cost_level": "$",
            "varieties": ["Orange", "White", "Purple"],
            "glycemic_index": 70
        },
        "brown_rice": {
            "category": "Carbohydrate",
            "serving_size": "100g (cooked)",
            "calories": 111,
            "protein": 2.6,
            "carbs": 23,
            "fat": 0.9,
            "saturated_fat": 0.2,
            "fiber": 1.8,
            "sugar": 0.4,
            "sodium": 2,
            "potassium": 77,
            "magnesium": 39,
            "manganese": 0.9,
            "benefits": ["B vitamins", "Sustained energy", "Gluten-free", "Fiber", "Magnesium"],
            "preparation": "Boil for 45 minutes",
            "note": "Better than white rice for nutrients",
            "shelf_life": "6 months pantry, 1 year sealed",
            "cost_level": "$",
            "ratio": "2:1 water to rice"
        },
        "oats": {
            "category": "Carbohydrate",
            "serving_size": "100g (dry rolled oats)",
            "calories": 389,
            "protein": 17,
            "carbs": 66,
            "fat": 7,
            "saturated_fat": 1.2,
            "fiber": 11,
            "sugar": 0.3,
            "sodium": 2,
            "potassium": 350,
            "magnesium": 138,
            "iron": 4.3,
            "beta_glucan": 4.0,
            "benefits": ["Fiber for digestion", "Beta-glucan for cholesterol", "Filling", "Heart health", "Blood sugar control"],
            "preparation": "Boil with water or milk (3:1 liquid to oats)",
            "best_for": "Breakfast",
            "shelf_life": "1-2 years pantry",
            "cost_level": "$",
            "varieties": ["Rolled", "Steel-cut", "Instant", "Quick"]
        },
        "banana": {
            "category": "Fruit",
            "serving_size": "100g (medium ~118g)",
            "calories": 89,
            "protein": 1.1,
            "carbs": 23,
            "fat": 0.3,
            "saturated_fat": 0.1,
            "fiber": 2.6,
            "sugar": 12,
            "sodium": 1,
            "potassium": 358,
            "magnesium": 27,
            "vitamin_b6": 0.4,
            "vitamin_c": 8.7,
            "benefits": ["Potassium (muscle function)", "Quick energy", "Portable", "Vitamin B6", "Magnesium"],
            "best_for": "Pre-workout snack",
            "ripeness": "Green=resistant starch, Yellow=ready, Spotted=sweetest",
            "shelf_life": "3-7 days room temp",
            "cost_level": "$",
            "glycemic_index": {"green": 30, "yellow": 51, "spotted": 65}
        },
        "almonds": {
            "category": "Fat + Protein",
            "serving_size": "23 almonds (28g)",
            "calories": 164,
            "protein": 6,
            "carbs": 6,
            "fat": 14,
            "saturated_fat": 1.1,
            "monounsaturated": 9.0,
            "polyunsaturated": 3.5,
            "fiber": 3.5,
            "sugar": 1.2,
            "sodium": 0,
            "magnesium": 76,
            "vitamin_e": 7.3,
            "calcium": 76,
            "benefits": ["Magnesium", "Vitamin E (antioxidant)", "Heart health", "Blood sugar control", "Healthy skin"],
            "note": "Calorie-dense, use portion control",
            "best_for": "Snack or with oatmeal",
            "shelf_life": "1-2 years sealed",
            "cost_level": "$$",
            "preparation": "Raw, roasted, or soaked"
        },
        "olive_oil": {
            "category": "Healthy Fat",
            "serving_size": "1 tablespoon (15ml)",
            "calories": 119,
            "protein": 0,
            "carbs": 0,
            "fat": 14,
            "saturated_fat": 2.0,
            "monounsaturated": 10.0,
            "polyunsaturated": 1.5,
            "fiber": 0,
            "sugar": 0,
            "vitamin_e": 1.9,
            "polyphenols": "High in EVOO",
            "benefits": ["Monounsaturated fats", "Anti-inflammatory", "Heart health", "Rich in antioxidants", "Brain health"],
            "tip": "Use for salads; avoid high heat cooking (smoke point ~375°F)",
            "storage": "Cool, dark place",
            "shelf_life": "18-24 months",
            "cost_level": "$$$",
            "varieties": ["Extra Virgin", "Virgin", "Pure", "Light"]
        },
        "spinach": {
            "category": "Vegetable",
            "serving_size": "100g (raw ~3 cups)",
            "calories": 23,
            "protein": 2.7,
            "carbs": 3.6,
            "fat": 0.4,
            "saturated_fat": 0.1,
            "fiber": 2.2,
            "sugar": 0.4,
            "sodium": 79,
            "potassium": 558,
            "vitamin_a": 469,
            "vitamin_c": 28,
            "vitamin_k": 483,
            "folate": 194,
            "iron": 2.7,
            "calcium": 99,
            "benefits": ["Iron (plant-based)", "Calcium", "Vitamins A, C, K", "Low calorie", "Eye health (lutein)"],
            "preparation": "Raw in salad or cooked",
            "note": "Cooking increases bioavailability of some nutrients",
            "shelf_life": "3-5 days refrigerated",
            "cost_level": "$",
            "season": "Year-round, peak spring/fall"
        },
        "lentils": {
            "category": "Legume/Protein",
            "serving_size": "100g (cooked)",
            "calories": 116,
            "protein": 9,
            "carbs": 20,
            "fat": 0.4,
            "saturated_fat": 0.1,
            "fiber": 8,
            "sugar": 1.8,
            "sodium": 2,
            "potassium": 369,
            "folate": 180,
            "iron": 3.3,
            "magnesium": 36,
            "benefits": ["Plant-based protein", "Fiber (lowers cholesterol)", "Iron", "Budget-friendly", "Blood sugar control"],
            "preparation": "Boil for 20-30 minutes (no soaking needed)",
            "best_for": "Vegetarians and vegans",
            "shelf_life": "1-2 years dry",
            "cost_level": "$",
            "varieties": ["Brown", "Green", "Red", "Black/Beluga"],
            "ratio": "3:1 water to lentils"
        },
        "chickpeas": {
            "category": "Legume/Protein",
            "serving_size": "100g (cooked)",
            "calories": 139,
            "protein": 8.9,
            "carbs": 22.5,
            "fat": 2.1,
            "saturated_fat": 0.2,
            "fiber": 6.5,
            "sugar": 3.8,
            "sodium": 7,
            "potassium": 291,
            "folate": 172,
            "iron": 2.9,
            "manganese": 1.0,
            "benefits": ["Complete protein with grains", "Fiber", "Budget-friendly", "Blood sugar control", "Heart health"],
            "preparation": "Boil 1-2 hours (after 8-hour soak) or canned",
            "uses": "Hummus, curry, salad, roasted snack",
            "shelf_life": "1-2 years dry, 1-2 years canned",
            "cost_level": "$",
            "other_names": "Garbanzo beans"
        },
        "avocado": {
            "category": "Healthy Fat + Fruit",
            "serving_size": "100g (half medium ~150g total)",
            "calories": 160,
            "protein": 2,
            "carbs": 9,
            "fat": 15,
            "saturated_fat": 2.1,
            "monounsaturated": 10.0,
            "polyunsaturated": 1.8,
            "fiber": 7,
            "sugar": 0.7,
            "sodium": 7,
            "potassium": 485,
            "vitamin_k": 21,
            "folate": 81,
            "vitamin_c": 10,
            "benefits": ["Potassium (more than banana)", "Healthy fats", "Creamy texture", "Fiber", "Heart health", "Skin health"],
            "note": "High calorie, use in moderation",
            "ripeness": "Soft to gentle pressure when ripe",
            "shelf_life": "2-5 days counter, 2-3 days after cut",
            "cost_level": "$$$",
            "prep_tip": "Brush with lemon to prevent browning"
        },
        "berries": {
            "category": "Fruit",
            "serving_size": "100g (mixed)",
            "calories": 57,
            "protein": 1.1,
            "carbs": 14,
            "fat": 0.3,
            "saturated_fat": 0,
            "fiber": 2,
            "sugar": 10,
            "vitamin_c": 40,
            "antioxidants": "Very high (anthocyanins)",
            "benefits": ["Antioxidants (high ORAC score)", "Low calorie", "Fiber", "Brain health", "Heart health", "Anti-aging"],
            "types": {
                "blueberries": {"calories": 57, "antioxidants": "High", "best_for": "Brain health"},
                "strawberries": {"calories": 32, "vitamin_c": 59, "best_for": "Immune health"},
                "raspberries": {"calories": 52, "fiber": 6.5, "best_for": "Digestion"},
                "blackberries": {"calories": 43, "fiber": 5.3, "best_for": "Vitamin C"}
            },
            "fresh_frozen": "Frozen are just as nutritious, often cheaper",
            "shelf_life": "3-7 days refrigerated",
            "freezer_life": "6-12 months",
            "cost_level": "$$$ (fresh), $ (frozen)"
        },
        "quinoa": {
            "category": "Carbohydrate + Complete Protein",
            "serving_size": "100g (cooked)",
            "calories": 120,
            "protein": 4.4,
            "carbs": 21,
            "fat": 1.9,
            "saturated_fat": 0.2,
            "fiber": 2.8,
            "sugar": 0.9,
            "iron": 1.5,
            "magnesium": 64,
            "manganese": 0.6,
            "benefits": ["Complete protein (all 9 amino acids)", "Gluten-free", "High in magnesium", "Fiber-rich", "Quick cooking"],
            "preparation": "Rinse first, boil 15 minutes (2:1 water)",
            "shelf_life": "2-3 years dry",
            "cost_level": "$$",
            "colors": ["White", "Red", "Black"]
        },
        "tuna_canned": {
            "category": "Protein",
            "serving_size": "100g (drained, in water)",
            "calories": 116,
            "protein": 25,
            "carbs": 0,
            "fat": 1,
            "saturated_fat": 0.3,
            "omega_3": 0.4,
            "sodium": 300,
            "selenium": 90,
            "benefits": ["High protein (25g/100g)", "Convenient", "Budget protein", "Selenium (antioxidant)"],
            "warning": "Limit to 2-3 servings/week due to mercury",
            "preparation": "Drain, mix with mayo or eat plain",
            "shelf_life": "3-5 years unopened",
            "cost_level": "$",
            "varieties": ["Skipjack (lowest mercury)", "Albacore", "Yellowfin"],
            "best_for": "Quick sandwiches, salads, pasta"
        },
        "tofu": {
            "category": "Plant Protein",
            "serving_size": "100g (firm)",
            "calories": 76,
            "protein": 8,
            "carbs": 2,
            "fat": 5,
            "saturated_fat": 0.8,
            "fiber": 0.3,
            "calcium": 350,
            "iron": 1.8,
            "benefits": ["Complete plant protein", "Calcium-fortified", "Versatile", "Soy isoflavones (heart health)", "Budget-friendly"],
            "preparation": "Press, then bake, stir-fry, or scramble",
            "shelf_life": "3-5 days refrigerated, 3-5 months frozen",
            "cost_level": "$",
            "firmness": ["Silken", "Soft", "Medium", "Firm", "Extra firm"]
        },
        "cauliflower": {
            "category": "Vegetable",
            "serving_size": "100g (raw)",
            "calories": 25,
            "protein": 2,
            "carbs": 5,
            "fat": 0.3,
            "fiber": 2,
            "sugar": 2,
            "vitamin_c": 48,
            "vitamin_k": 16,
            "folate": 57,
            "benefits": ["Low carb/Keto friendly", "Vitamin C", "Cruciferous cancer fighters", "Versatile (rice, pizza crust, mash)"],
            "preparation": "Roast, steam, or eat raw",
            "shelf_life": "1 week refrigerated",
            "cost_level": "$",
            "season": "Peak spring/fall"
        },
        "blueberries": {
            "category": "Fruit",
            "serving_size": "100g (about 1 cup)",
            "calories": 57,
            "protein": 0.7,
            "carbs": 14,
            "fat": 0.3,
            "fiber": 2.4,
            "sugar": 10,
            "vitamin_c": 9.7,
            "vitamin_k": 19.3,
            "manganese": 0.3,
            "anthocyanins": 164,
            "benefits": ["Highest antioxidants among fruits", "Brain health (improves memory)", "Heart health", "Anti-aging"],
            "shelf_life": "1 week refrigerated",
            "freezer_life": "6-12 months",
            "cost_level": "$$$",
            "best_for": "Oatmeal, smoothies, yogurt"
        },
        "walnuts": {
            "category": "Healthy Fat",
            "serving_size": "28g (7-9 halves, 1/4 cup)",
            "calories": 185,
            "protein": 4.3,
            "carbs": 3.9,
            "fat": 18.5,
            "saturated_fat": 1.7,
            "alpha_linolenic_acid": 2.5,
            "fiber": 1.9,
            "magnesium": 45,
            "benefits": ["Highest omega-3 ALA", "Brain-shaped for brain health", "Heart health", "Anti-inflammatory"],
            "best_for": "Snack, salads, oatmeal",
            "shelf_life": "6 months pantry, 1 year fridge",
            "cost_level": "$$",
            "note": "Store in fridge to prevent rancidity"
        },
        "carrots": {
            "category": "Vegetable",
            "serving_size": "100g (1 medium)",
            "calories": 41,
            "protein": 0.9,
            "carbs": 10,
            "fat": 0.2,
            "fiber": 2.8,
            "sugar": 4.7,
            "vitamin_a": 835,
            "vitamin_k": 13.2,
            "potassium": 320,
            "benefits": ["Beta-carotene (Vitamin A)", "Eye health", "Low calorie", "Crunchy snack", "Heart health"],
            "preparation": "Raw, roasted, steamed, or juiced",
            "shelf_life": "3-4 weeks refrigerated",
            "cost_level": "$",
            "color_varieties": ["Orange", "Purple", "Yellow", "Red"]
        },
        "chicken_thigh": {
            "category": "Protein",
            "serving_size": "100g (cooked, skinless)",
            "calories": 209,
            "protein": 26,
            "carbs": 0,
            "fat": 11,
            "saturated_fat": 3.0,
            "iron": 1.1,
            "benefits": ["More flavor than breast", "More iron than breast", "Juicy", "Budget-friendly"],
            "disadvantage": "Higher fat/calories than breast",
            "preparation": "Grill, bake, or pan-sear",
            "shelf_life": "3-4 days refrigerated",
            "cost_level": "$",
            "best_for": "Curries, stir-fries"
        },
        "kale": {
            "category": "Vegetable",
            "serving_size": "100g (raw)",
            "calories": 49,
            "protein": 4.3,
            "carbs": 9,
            "fat": 0.9,
            "fiber": 2,
            "sugar": 2,
            "vitamin_a": 500,
            "vitamin_c": 120,
            "vitamin_k": 704,
            "calcium": 150,
            "iron": 1.6,
            "benefits": ["Nutrient-dense superfood", "Very high vitamin K", "Antioxidants (quercetin)", "Anti-inflammatory"],
            "preparation": "Massage raw for salads, bake into chips, or sauté",
            "shelf_life": "5-7 days refrigerated",
            "cost_level": "$$",
            "varieties": ["Curly", "Lacinato/Dino", "Red Russian"]
        },
        "pumpkin_seeds": {
            "category": "Healthy Fat + Mineral",
            "serving_size": "28g (2 tablespoons)",
            "calories": 151,
            "protein": 7,
            "carbs": 5,
            "fat": 13,
            "fiber": 1.7,
            "magnesium": 156,
            "zinc": 2.2,
            "iron": 2.3,
            "benefits": ["Very high in magnesium (37% DV)", "Zinc for immunity", "Iron", "Sleep aid (tryptophan)", "Prostate health"],
            "preparation": "Raw, roasted, or add to salads/yogurt",
            "shelf_life": "6 months pantry, 1 year fridge",
            "cost_level": "$$",
            "other_names": "Pepitas"
        },
        "cottage_cheese": {
            "category": "Protein",
            "serving_size": "100g (low-fat 2%)",
            "calories": 84,
            "protein": 11,
            "carbs": 3,
            "fat": 2.3,
            "sodium": 364,
            "calcium": 83,
            "benefits": ["High protein (casein - slow digesting)", "Calcium", "Satiety (great before bed)", "Versatile"],
            "preparation": "Eat plain, with fruit, or in recipes",
            "shelf_life": "1-2 weeks refrigerated",
            "cost_level": "$$",
            "best_for": "Pre-sleep snack (slow protein)"
        },
        "sardines": {
            "category": "Protein + Omega-3",
            "serving_size": "100g (canned in water)",
            "calories": 208,
            "protein": 25,
            "carbs": 0,
            "fat": 11,
            "omega_3": 1.5,
            "calcium": 382,
            "vitamin_d": 4.8,
            "vitamin_b12": 8.9,
            "selenium": 52,
            "benefits": ["Low mercury (small fish)", "High calcium (with bones)", "Omega-3s", "Vitamin D", "Sustainable"],
            "preparation": "Eat on crackers, in salads, or pasta",
            "shelf_life": "3-5 years unopened",
            "cost_level": "$$",
            "best_for": "Tinned fish enthusiasts"
        },
        "beef_lean": {
            "category": "Protein",
            "serving_size": "100g (lean ground beef 90/10, cooked)",
            "calories": 176,
            "protein": 26,
            "carbs": 0,
            "fat": 7,
            "saturated_fat": 3.3,
            "iron": 2.6,
            "zinc": 6.0,
            "vitamin_b12": 2.5,
            "creatine": 0.5,
            "benefits": ["High iron (heme)", "Zinc for immunity", "Creatine for muscle", "Vitamin B12"],
            "preparation": "Pan-fry, grill, or bake",
            "shelf_life": "2-3 days refrigerated",
            "cost_level": "$$$",
            "best_for": "Post-workout (zinc+iron)"
        },
        "asparagus": {
            "category": "Vegetable",
            "serving_size": "100g (cooked)",
            "calories": 22,
            "protein": 2.4,
            "carbs": 4,
            "fat": 0.2,
            "fiber": 2,
            "vitamin_k": 50,
            "folate": 134,
            "vitamin_a": 38,
            "benefits": ["Natural diuretic", "Prebiotic fiber", "Folates (pregnancy)", "High vitamin K"],
            "preparation": "Roast, grill, or steam (3-5 minutes)",
            "shelf_life": "3-4 days refrigerated",
            "cost_level": "$$$",
            "season": "Peak spring"
        },
        "mushrooms": {
            "category": "Vegetable/Fungus",
            "serving_size": "100g (white, raw)",
            "calories": 22,
            "protein": 3.1,
            "carbs": 3.3,
            "fat": 0.3,
            "fiber": 1,
            "vitamin_d": 0.2,
            "selenium": 9.3,
            "benefits": ["Only plant source of vitamin D (if UV-exposed)", "Selenium", "B vitamins", "Low calorie", "Umami flavor"],
            "preparation": "Sauté, roast, or eat raw",
            "shelf_life": "5-7 days refrigerated",
            "cost_level": "$",
            "varieties": ["White", "Cremini", "Portobello", "Shiitake", "Oyster"]
        },
        "edamame": {
            "category": "Plant Protein",
            "serving_size": "100g (cooked, from frozen)",
            "calories": 122,
            "protein": 11,
            "carbs": 10,
            "fat": 5,
            "fiber": 5,
            "folate": 311,
            "vitamin_k": 26,
            "iron": 2.3,
            "benefits": ["Complete plant protein", "High folate", "Fiber-rich", "Kidney health", "Soy isoflavones"],
            "preparation": "Boil 5 minutes, salt and eat from pod",
            "shelf_life": "6-12 months frozen",
            "cost_level": "$$",
            "best_for": "Healthy snack or appetizer"
        }
    }
}

# Enhanced Categories
FOOD_CATEGORIES = {
    "high_protein": ["Chicken breast", "Salmon", "Eggs", "Greek yogurt", "Lentils", "Chickpeas", "Tuna canned", "Cottage cheese", "Sardines", "Beef lean", "Tofu", "Edamame"],
    "low_calorie": ["Broccoli", "Spinach", "Carrots", "Cucumber", "Berries", "Chicken breast", "Cauliflower", "Kale", "Asparagus", "Mushrooms"],
    "post_workout": ["Banana", "Brown rice", "Chicken breast", "Sweet potato", "Eggs", "Salmon", "Quinoa", "Cottage cheese"],
    "pre_workout": ["Banana", "Oats", "Apple", "Toast", "Greek yogurt", "Berries", "Sweet potato"],
    "healthy_fats": ["Almonds", "Olive oil", "Avocado", "Salmon", "Coconut oil", "Walnuts", "Pumpkin seeds", "Sardines"],
    "plant_based": ["Lentils", "Chickpeas", "Beans", "Tofu", "Tempeh", "Nuts", "Seeds", "Quinoa", "Edamame"],
    "quick_prep": ["Eggs", "Canned tuna", "Greek yogurt", "Cottage cheese", "Bananas", "Berries", "Carrots", "Edamame (frozen)"],
    "budget_friendly": ["Eggs", "Canned tuna", "Lentils", "Chickpeas", "Oats", "Brown rice", "Bananas", "Carrots", "Cabbage", "Frozen vegetables"],
    "keto_low_carb": ["Salmon", "Eggs", "Chicken breast", "Broccoli", "Cauliflower", "Olive oil", "Almonds", "Avocado", "Spinach", "Mushrooms"],
    "high_fiber": ["Lentils", "Chickpeas", "Oats", "Broccoli", "Berries", "Avocado", "Pumpkin seeds", "Edamame", "Kale", "Cauliflower"],
    "immune_boosting": ["Broccoli", "Spinach", "Berries", "Garlic", "Ginger", "Oranges", "Bell peppers", "Mushrooms", "Greek yogurt"],
    "iron_rich": ["Spinach", "Lentils", "Beef lean", "Pumpkin seeds", "Quinoa", "Tofu", "Chickpeas", "Kale", "Sardines"],
    "calcium_rich": ["Greek yogurt", "Sardines (with bones)", "Kale", "Tofu (calcium-set)", "Broccoli", "Almonds", "Edamame", "Cottage cheese"],
    "omega_3_rich": ["Salmon", "Sardines", "Walnuts", "Flaxseeds", "Chia seeds", "Pumpkin seeds"],
    "anti_inflammatory": ["Salmon", "Berries", "Broccoli", "Olive oil", "Walnuts", "Spinach", "Mushrooms", "Turmeric (spice)"]
}

# Enhanced Meal Suggestions
MEAL_SUGGESTIONS = {
    "breakfast": [
        "Scrambled eggs with toast and avocado",
        "Oatmeal with berries and almonds (or walnuts)",
        "Greek yogurt with granola, banana, and pumpkin seeds",
        "Protein pancakes with banana and cottage cheese",
        "Smoothie: spinach, banana, berries, Greek yogurt",
        "Avocado toast with poached egg",
        "Overnight oats with chia seeds and berries"
    ],
    "lunch": [
        "Grilled chicken with brown rice and broccoli",
        "Salmon with sweet potato and asparagus",
        "Tuna salad with mixed greens and avocado",
        "Chickpea curry with brown rice",
        "Lentil soup with quinoa and side salad",
        "Turkey and avocado wrap with spinach",
        "Quinoa bowl: roasted vegetables, tofu, tahini dressing",
        "Cottage cheese with berries and pumpkin seeds"
    ],
    "dinner": [
        "Lean ground turkey with roasted vegetables and sweet potato",
        "Baked white fish with roasted cauliflower and lemon",
        "Vegetable stir-fry with tofu and brown rice",
        "Lentil and vegetable stew with whole grain bread",
        "Salmon with quinoa and steamed asparagus",
        "Chicken thigh curry with chickpeas and cauliflower rice",
        "Zucchini noodles with marinara and lean beef",
        "Stuffed bell peppers with ground turkey and quinoa"
    ],
    "snacks": [
        "Apple with almond butter",
        "Greek yogurt with berries",
        "Mixed nuts (small handful - 1/4 cup)",
        "Protein shake with banana",
        "Carrot sticks with hummus",
        "Hard-boiled egg (salt and pepper)",
        "Cottage cheese with black pepper",
        "Handful of pumpkin seeds",
        "Celery with peanut butter",
        "Trail mix (no added sugar)",
        "Roasted chickpeas (crunchy snack)",
        "Banana with peanut butter"
    ],
    
    # Advanced Meal Plans
    "meal_plans": {
        "high_protein_day": {
            "breakfast": "Greek yogurt (200g) + Berries + Pumpkin seeds",
            "morning_snack": "Hard-boiled eggs (2)",
            "lunch": "Grilled chicken breast + Quinoa + Broccoli",
            "afternoon_snack": "Cottage cheese (100g)",
            "dinner": "Lean beef + Sweet potato + Spinach",
            "evening_snack": "Cottage cheese or Greek yogurt",
            "total_protein_approx": "150g"
        },
        "plant_based_day": {
            "breakfast": "Oatmeal (50g) + Berries + Walnuts + Plant milk",
            "morning_snack": "Apple with almond butter",
            "lunch": "Lentil soup + Quinoa + Mixed greens salad",
            "afternoon_snack": "Roasted chickpeas + Carrots",
            "dinner": "Tofu stir-fry with broccoli, mushrooms, brown rice",
            "evening_snack": "Edamame (100g)",
            "total_protein_approx": "70g"
        },
        "budget_day": {
            "breakfast": "Oatmeal (50g) + Banana",
            "morning_snack": "Hard-boiled egg (1)",
            "lunch": "Canned tuna + Brown rice + Frozen mixed vegetables",
            "afternoon_snack": "Carrot sticks + Hummus (homemade from canned chickpeas)",
            "dinner": "Lentil and chickpea curry + Brown rice",
            "evening_snack": "Popcorn (air-popped)",
            "total_cost_approx": "$8-10/day"
        },
        "low_carb_keto_day": {
            "breakfast": "Scrambled eggs (3) + Avocado (half) + Spinach",
            "morning_snack": "Pumpkin seeds (28g)",
            "lunch": "Salmon + Asparagus roasted in olive oil",
            "afternoon_snack": "Celery with cream cheese",
            "dinner": "Chicken thigh sautéed with cauliflower rice and mushrooms",
            "evening_snack": "Handful of walnuts",
            "total_carbs_approx": "<50g"
        },
        "post_workout_recovery_day": {
            "breakfast": "Protein shake (whey) + Banana + Oats",
            "morning_snack": "Greek yogurt (150g)",
            "lunch": "Salmon + Quinoa + Roasted sweet potato + Broccoli",
            "post_workout_snack": "Cottage cheese (150g) + Berries",
            "dinner": "Lean beef + Brown rice + Asparagus",
            "evening_snack": "Casein protein shake or Cottage cheese",
            "purpose": "Muscle repair and glycogen replenishment"
        }
    }
}

# New: Nutrition Reference Values (Daily Values)
NUTRITION_REFERENCE = {
    "daily_calories": 2000,  # Reference for adult
    "daily_values_percent": {
        "protein": 50,      # grams per day (10-35% calories)
        "carbs": 275,       # grams per day (45-65% calories)
        "fat": 65,          # grams per day (20-35% calories)
        "fiber": 30,        # grams per day
        "sugar": 50,        # grams per day (added sugars limit)
        "sodium": 2300,     # mg per day
        "potassium": 4700,  # mg per day
        "iron": 18,         # mg for adult women, 8mg for men
        "calcium": 1000,    # mg per day
        "vitamin_c": 90,    # mg per day
        "vitamin_d": 20,    # mcg per day
        "vitamin_b12": 2.4, # mcg per day
        "magnesium": 420,   # mg for adult men, 320 for women
        "zinc": 11,         # mg for men, 8 for women
        "omega_3": 1.6      # g per day (ALA), 250mg EPA/DHA
    }
}

# New: Cooking Methods and Their Effects
COOKING_GUIDES = {
    "best_methods_by_food": {
        "broccoli": {"best": "Steaming (3-4 min)", "nutrient_retention": 90, "why": "Preserves sulforaphane and vitamin C"},
        "salmon": {"best": "Baking at 375°F (12-15 min)", "nutrient_retention": 85, "why": "Preserves omega-3s"},
        "eggs": {"best": "Poaching or soft-boiling", "nutrient_retention": 95, "why": "Minimizes oxidation of cholesterol"},
        "spinach": {"best": "Light steaming (1-2 min)", "nutrient_retention": 90, "why": "Reduces oxalates, increases iron absorption"},
        "sweet_potato": {"best": "Baking with skin on", "nutrient_retention": 85, "why": "Preserves fiber and beta-carotene"},
        "chicken_breast": {"best": "Grilling or baking", "nutrient_retention": 90, "why": "Avoids added fats"},
        "mushrooms": {"best": "Sautéing or roasting", "nutrient_retention": 80, "why": "Enhances umami, retains vitamin D"}
    },
    "general_tips": {
        "steaming": "Best for preserving water-soluble vitamins (B, C)",
        "roasting": "Concentrates flavors, good for root vegetables",
        "microwaving": "Actually retains nutrients well due to short cooking time",
        "boiling": "Least healthy - nutrients leach into water (use water for soups)",
        "frying": "Adds calories, but can make some nutrients more bioavailable",
        "raw": "Maximum nutrients for some foods (bell peppers, berries)"
    }
}

# New: Portion Size Visual Guide
PORTION_VISUAL_GUIDE = {
    "protein": {
        "chicken/fish/meat": {"size": "Deck of cards", "grams": "100g"},
        "eggs": {"size": "2 golf balls", "grams": "100g"},
        "tofu": {"size": "1/2 checkbook", "grams": "100g"}
    },
    "carbohydrates": {
        "rice/pasta/quinoa": {"size": "Tennis ball", "grams": "100g"},
        "potato/sweet_potato": {"size": "Computer mouse", "grams": "150g"},
        "oats": {"size": "½ baseball", "grams": "40g dry"}
    },
    "vegetables": {
        "leafy_greens": {"size": "2 baseballs", "grams": "85g"},
        "broccoli/cauliflower": {"size": "Baseball", "grams": "100g"}
    },
    "fats": {
        "nuts": {"size": "Golf ball", "grams": "28g"},
        "avocado": {"size": "Golf ball", "grams": "50g (¼ avocado)"},
        "oil/butter": {"size": "Thumb tip", "grams": "14g (1 tbsp)"}
    },
    "fruits": {
        "apple/orange": {"size": "Baseball", "grams": "150g"},
        "berries": {"size": "Baseball", "grams": "100g"}
    }
}

# New: Seasonal Produce Guide (North America)
SEASONAL_GUIDE = {
    "spring": ["Asparagus", "Spinach", "Strawberries", "Peas", "Radishes", "Spring onions", "Lettuce", "Artichokes"],
    "summer": ["Berries", "Tomatoes", "Corn", "Zucchini", "Cucumber", "Bell peppers", "Peaches", "Plums", "Melons", "Eggplant", "Green beans"],
    "fall": ["Sweet potatoes", "Pumpkin", "Butternut squash", "Apples", "Pears", "Brussels sprouts", "Cauliflower", "Mushrooms", "Cranberries"],
    "winter": ["Kale", "Broccoli", "Carrots", "Cabbage", "Potatoes", "Onions", "Garlic", "Lemons", "Oranges", "Grapefruit", "Parsnips"]
}

# New: Storage Guidelines
STORAGE_GUIDELINES = {
    "refrigerator_temps": "35-40°F (2-4°C)",
    "freezer_temps": "0°F (-18°C) or below",
    "produce": {
        "berries": "Refrigerate, don't wash until ready to eat; lasts 3-7 days",
        "leafy_greens": "Refrigerate in bag with paper towel; lasts 5-7 days",
        "avocado": "Counter until ripe, then refrigerate; lasts 2-3 days ripe",
        "bananas": "Counter, separate from other fruit; lasts 3-5 days",
        "potatoes/onions": "Cool, dark, dry place (not fridge); lasts 1-2 months"
    },
    "protein": {
        "fresh_fish": "Eat within 1-2 days or freeze",
        "fresh_chicken": "Eat within 2-3 days or freeze",
        "eggs": "Refrigerate, use within 3-5 weeks",
        "canned_fish": "Pantry unopened, fridge after opening (use within 2 days)"
    },
    "freezer_times": {
        "cooked_meals": "2-3 months",
        "raw_chicken/fish": "6-9 months",
        "raw_beef/pork": "6-12 months",
        "vegetables": "8-12 months (blanch first)",
        "berries": "6-12 months",
        "bread": "3-6 months"
    },
    "never_freeze": ["Eggs in shell", "Canned food", "Mayonnaise", "Cream-based sauces", "Leafy greens (raw)"]
}

# New: Allergen Information
ALLERGEN_INFO = {
    "common_allergens": {
        "eggs": {"allergen": "Egg", "notes": "Avoid if egg allergy, can substitute with flax eggs or commercial egg replacer"},
        "almonds": {"allergen": "Tree nuts", "notes": "May cause cross-reaction with other nuts, seeds often safe alternative"},
        "walnuts": {"allergen": "Tree nuts", "notes": "One of most common nut allergies"},
        "salmon": {"allergen": "Fish", "notes": "Distinct from shellfish allergy"},
        "tuna_canned": {"allergen": "Fish", "notes": "Avoid all fish if allergic"},
        "sardines": {"allergen": "Fish", "notes": "Small fish, same allergy risk"},
        "greek_yogurt": {"allergen": "Dairy (milk)", "notes": "Lactose intolerant may tolerate Greek yogurt due to lower lactose"},
        "cottage_cheese": {"allergen": "Dairy (milk)", "notes": "Higher lactose, may cause issues for lactose intolerant"},
        "tofu": {"allergen": "Soy", "notes": "Common allergen, avoid if soy allergy"},
        "edamame": {"allergen": "Soy", "notes": "Whole soybeans, same allergy risk"},
        "wheat": {"allergen": "Gluten/Wheat", "notes": "Found in breads, pasta, cereals"},
        "shellfish": {"allergen": "Crustacean", "notes": "Separate from fish allergy"}
    },
    "allergen_free_alternatives": {
        "dairy_free": ["Coconut yogurt", "Almond milk", "Oat milk", "Soy milk", "Cashew cheese"],
        "egg_free": ["Flax egg (1 tbsp flax + 3 tbsp water)", "Chia egg", "Applesauce (1/4 cup = 1 egg)", "Commercial egg replacer"],
        "nut_free": ["Sunflower seeds", "Pumpkin seeds", "Roasted chickpeas", "Coconut (if tolerated)"],
        "gluten_free": ["Brown rice", "Quinoa", "Oats (certified gluten-free)", "Buckwheat", "Corn tortillas"],
        "soy_free": ["Lentils", "Chickpeas", "Pea protein", "Hemp seeds", "Beans"]
    }
}

# Meal Timing and Nutrient Synergy
MEAL_TIMING_GUIDE = {
    "pre_workout": {
        "when": "1-2 hours before exercise",
        "macros": "Carbs + moderate protein, low fat (slows digestion)",
        "examples": ["Banana", "Oatmeal with berries", "Toast with honey", "Apple"]
    },
    "post_workout": {
        "when": "Within 30-60 minutes after exercise",
        "macros": "Protein + Carbs (4:1 carb:protein ideal for endurance)",
        "examples": ["Protein shake + banana", "Chicken + sweet potato", "Greek yogurt + berries", "Chocolate milk"]
    },
    "before_bed": {
        "when": "30-60 minutes before sleep",
        "macros": "Slow-digesting protein (casein)",
        "examples": ["Cottage cheese", "Greek yogurt", "Casein protein shake"],
        "benefit": "Muscle protein synthesis during sleep"
    },
    "nutrient_combos": {
        "iron_+_vitamin_c": "Increases iron absorption 6x (spinach + lemon)",
        "fats_+_fat_soluble_vitamins": "Eat avocado/salmon with vegetables for ADEK vitamins",
        "protein_+_carbs_post_workout": "Enhances glycogen replenishment",
        "turmeric_+_black_pepper": "Increases curcumin absorption by 2000%"
    }
}

# Health Condition Specific Recommendations
CONDITION_GUIDELINES = {
    "high_blood_pressure": {
        "focus": "Reduce sodium, increase potassium",
        "best_foods": ["Bananas", "Spinach", "Sweet potatoes", "Salmon", "Greek yogurt", "Beans", "Lentils"],
        "avoid": ["Canned soups", "Processed meats", "Frozen meals", "Pickled foods"]
    },
    "diabetes_insulin_resistance": {
        "focus": "Low glycemic index, high fiber",
        "best_foods": ["Broccoli", "Lentils", "Chickpeas", "Berries", "Nuts", "Quinoa", "Avocado"],
        "limit": ["White rice", "White bread", "Sugary fruits", "Juice", "Sweetened yogurt"]
    },
    "high_cholesterol": {
        "focus": "Increase fiber and omega-3s, reduce saturated fat",
        "best_foods": ["Oats (beta-glucan)", "Salmon", "Walnuts", "Avocado", "Olive oil", "Legumes", "Berries"],
        "limit": ["Red meat", "Butter", "Coconut oil", "Fried foods", "Pastries"]
    },
    "gout": {
        "focus": "Low purine foods",
        "best_foods": ["Fruits", "Vegetables", "Eggs", "Nuts", "Whole grains", "Low-fat dairy"],
        "avoid": ["Organ meats", "Sardines", "Anchovies", "Shellfish", "Beer", "Red meat"]
    },
    "anemia": {
        "focus": "Iron-rich with vitamin C for absorption",
        "best_foods": ["Spinach (with lemon)", "Lean beef", "Lentils", "Pumpkin seeds", "Fortified cereals"],
        "combo_meals": ["Lentil soup + tomato", "Steak + broccoli", "Spinach salad + strawberries"]
    },
    "athletic_performance": {
        "focus": "Protein timing, carb loading, hydration",
        "recommended": ["Lean proteins", "Complex carbs", "Beets (nitrates)", "Tart cherry juice (recovery)"],
        "timing_essential": "Post-workout protein within 60 min"
    }
}