# Expanded Diet and Nutrition Knowledge Base
DIET_KNOWLEDGE = {
    # ------------------------------------------------------------------
    # 1. NUTRITION BASICS (Deep dive)
    # ------------------------------------------------------------------
    "nutrition_basics": {
        "macronutrients": {
            "protein": {
                "function": "Builds and repairs muscle, creates enzymes and hormones, supports immune function, maintains skin/hair/nails.",
                "daily_intake": {
                    "sedentary_adult": "0.36g per pound (0.8g per kg) of body weight",
                    "active_adult": "0.8-1.0g per pound (1.6-2.2g per kg)",
                    "bodybuilder/athlete": "1.0-1.2g per pound (2.2-2.6g per kg)",
                    "weight_loss": "1.0-1.2g per pound to preserve muscle",
                    "older_adults": "1.0-1.2g per pound to prevent sarcopenia"
                },
                "sources": ["Chicken", "Fish", "Eggs", "Beans", "Greek yogurt", "Cottage cheese", "Nuts", "Tofu", "Tempeh", "Seitan", "Lean beef", "Turkey", "Lentils", "Edamame", "Quinoa"],
                "best_time": "Distribute throughout day, 20-40g per meal for optimal muscle protein synthesis (MPS). Post-workout window is valuable but total daily intake matters most.",
                "amino_acids": {
                    "essential": ["Leucine (key for MPS)", "Isoleucine", "Valine", "Lysine", "Methionine", "Phenylalanine", "Threonine", "Tryptophan", "Histidine"],
                    "complete_proteins": ["Animal products", "Soy", "Quinoa", "Buckwheat", "Hemp seeds"],
                    "incomplete_proteins": ["Most plants - combine legumes with grains for completeness"]
                }
            },
            "carbohydrates": {
                "function": "Provides energy for daily activities and workouts, fuels brain (which uses ~120g glucose daily), spares protein from being used as fuel.",
                "daily_intake": {
                    "sedentary": "2-3g per pound",
                    "moderately_active": "3-4g per pound",
                    "very_active": "4-6g per pound",
                    "ketogenic": "Less than 0.25g per pound (less than 50g total)"
                },
                "types": {
                    "complex": ["Oats", "Brown rice", "Sweet potatoes", "Whole wheat bread", "Quinoa", "Barley", "Buckwheat", "Legumes", "Starchy vegetables (corn, peas)"],
                    "simple": ["Fruits", "Honey", "White rice", "White bread", "Pasta", "Sugary drinks", "Candy", "Maple syrup"],
                    "fiber": ["Vegetables", "Fruit skins", "Whole grains", "Nuts", "Seeds", "Legumes", "Psyllium husk"]
                },
                "glycemic_index": {
                    "low_GI_under_55": ["Most vegetables", "Legumes", "Whole oats", "Barley", "Sweet potato (boiled)"],
                    "medium_GI_56-69": ["Brown rice", "Whole wheat bread", "Quinoa"],
                    "high_GI_over_70": ["White bread", "White rice", "Potato (baked)", "Cornflakes", "Watermelon"]
                },
                "tip": "Prioritize complex carbs and fiber. Simple carbs are best post-workout for glycogen replenishment or if you need quick energy during endurance exercise."
            },
            "fats": {
                "function": "Supports hormone production (testosterone, estrogen), nutrient absorption (A,D,E,K), brain function (60% of brain is fat), cell membrane integrity, insulation.",
                "daily_intake": "20-35% of total calories (minimum 0.3-0.4g per pound for hormone health)",
                "types": {
                    "unsaturated": {
                        "monounsaturated": ["Avocado", "Olive oil", "Nuts (almonds, cashews, pecans)", "Peanut butter"],
                        "polyunsaturated": ["Fatty fish (salmon, mackerel, sardines)", "Walnuts", "Flax seeds", "Chia seeds", "Sunflower seeds", "Soybean oil"],
                        "omega_3": ["Fatty fish", "Flaxseed", "Walnuts", "Chia seeds", "Algae oil (vegan)"],
                        "omega_6": ["Vegetable oils", "Nuts", "Seeds", "Poultry fat"]
                    },
                    "saturated": {
                        "sources": ["Coconut oil", "Butter", "Red meat", "Cheese", "Palm oil", "Dark chocolate"],
                        "daily_limit": "Less than 10% of total calories (per AHA)"
                    },
                    "trans_fats": {
                        "sources": ["Partially hydrogenated oils", "Fried fast foods", "Packaged cookies/cakes", "Margarine"],
                        "recommendation": "Avoid entirely (except naturally occurring in small amounts in meat/dairy)"
                    }
                },
                "healthy_sources": ["Avocado", "Olive oil", "Nuts", "Fatty fish", "Seeds", "Nut butters", "Dark chocolate (70%+ cocoa)"]
            }
        },
        "micronutrients": {
            "vitamins": {
                "fat_soluble": {
                    "vitamin_a": {"function": "Vision, immune function, skin health", "sources": ["Sweet potatoes", "Carrots", "Spinach", "Kale", "Eggs", "Liver"], "rda": "700-900 mcg RAE"},
                    "vitamin_d": {"function": "Calcium absorption, bone health, immunity, mood regulation", "sources": ["Sunlight (10-30 min/day)", "Fatty fish", "Fortified milk/juice", "Supplements"], "rda": "600-800 IU (many need 1000-2000 IU)"},
                    "vitamin_e": {"function": "Antioxidant, protects cell membranes", "sources": ["Nuts", "Seeds", "Spinach", "Sunflower oil", "Avocado"], "rda": "15 mg"},
                    "vitamin_k": {"function": "Blood clotting, bone metabolism", "sources": ["Leafy greens (kale, spinach, broccoli)", "Brussels sprouts", "Fermented foods"], "rda": "90-120 mcg"}
                },
                "water_soluble": {
                    "vitamin_c": {"function": "Collagen synthesis, immunity, antioxidant, iron absorption", "sources": ["Citrus fruits", "Bell peppers", "Strawberries", "Kiwi", "Broccoli", "Brussels sprouts"], "rda": "75-90 mg (smokers need +35mg)"},
                    "b1_thiamin": {"function": "Energy metabolism", "sources": ["Whole grains", "Pork", "Legumes", "Sunflower seeds"]},
                    "b2_riboflavin": {"function": "Energy production", "sources": ["Eggs", "Organ meats", "Mushrooms", "Spinach"]},
                    "b3_niacin": {"function": "DNA repair, energy", "sources": ["Chicken", "Turkey", "Tuna", "Brown rice"]},
                    "b5_pantothenic": {"function": "Fatty acid synthesis", "sources": ["Avocado", "Yogurt", "Eggs", "Broccoli"]},
                    "b6_pyridoxine": {"function": "Amino acid metabolism, neurotransmitter production", "sources": ["Chickpeas", "Poultry", "Fish", "Potatoes", "Bananas"]},
                    "b7_biotin": {"function": "Hair, skin, nails", "sources": ["Egg yolks", "Nuts", "Sweet potatoes", "Oats"]},
                    "b9_folate": {"function": "DNA synthesis, cell division (critical in pregnancy)", "sources": ["Leafy greens", "Legumes", "Asparagus", "Fortified grains"], "rda": "400 mcg (600 mcg pregnant)"},
                    "b12_cobalamin": {"function": "Nerve function, red blood cell formation", "sources": ["Animal products only", "Nutritional yeast (fortified)", "Supplements"], "rda": "2.4 mcg (vegans need supplement)"}
                }
            },
            "minerals": {
                "major_minerals": {
                    "calcium": {"function": "Bone health, muscle contraction, nerve signaling", "sources": ["Dairy", "Leafy greens (collards, kale)", "Fortified plant milks", "Sardines (with bones)", "Tofu (calcium-set)"], "rda": "1000-1200 mg"},
                    "magnesium": {"function": "Muscle function, sleep, blood sugar regulation, over 300 enzymes", "sources": ["Nuts (almonds, cashews)", "Seeds (pumpkin, chia)", "Spinach", "Black beans", "Dark chocolate", "Avocado"], "rda": "310-420 mg"},
                    "potassium": {"function": "Heart health, blood pressure regulation, fluid balance, nerve transmission", "sources": ["Bananas", "Sweet potatoes", "Potatoes (with skin)", "Spinach", "Avocado", "Beans", "Coconut water"], "rda": "2600-3400 mg (most need more)"},
                    "sodium": {"function": "Fluid balance, nerve function", "sources": ["Table salt", "Processed foods (excess)", "Pickled foods"], "upper_limit": "2300 mg (1500 mg for hypertension)"},
                    "chloride": {"function": "Digestion (stomach acid)", "sources": ["Table salt"]},
                    "phosphorus": {"function": "Bones, teeth, energy storage", "sources": ["Dairy", "Meat", "Fish", "Nuts", "Whole grains"]},
                    "sulfur": {"function": "Protein structure, detoxification", "sources": ["Protein-rich foods", "Garlic", "Onions", "Cruciferous vegetables"]}
                },
                "trace_minerals": {
                    "iron": {"function": "Oxygen transport (hemoglobin), energy production", "sources": {"heme_animal": ["Red meat", "Liver", "Dark poultry meat"], "non_heme_plant": ["Spinach", "Lentils", "Beans", "Fortified cereals", "Pumpkin seeds"]}, "rda": "8 mg (men), 18 mg (women pre-menopause)", "absorption_tip": "Pair plant iron with vitamin C (citrus, peppers) to boost absorption 5-6x"},
                    "zinc": {"function": "Immune function, wound healing, taste/smell", "sources": ["Oysters (extremely high)", "Red meat", "Poultry", "Beans", "Nuts", "Whole grains"], "rda": "8-11 mg"},
                    "iodine": {"function": "Thyroid hormone production", "sources": ["Iodized salt", "Seafood", "Seaweed", "Dairy"], "rda": "150 mcg"},
                    "selenium": {"function": "Antioxidant, thyroid function", "sources": ["Brazil nuts (1 nut = 100% RDA)", "Tuna", "Sardines", "Eggs"], "rda": "55 mcg"},
                    "copper": {"function": "Iron metabolism, nerve function", "sources": ["Shellfish", "Liver", "Nuts", "Seeds", "Dark chocolate"]},
                    "manganese": {"function": "Bone health, blood sugar regulation", "sources": ["Whole grains", "Nuts", "Leafy greens", "Tea"]},
                    "chromium": {"function": "Insulin sensitivity", "sources": ["Broccoli", "Grapes", "Meat", "Whole grains"]},
                    "molybdenum": {"function": "Enzyme function", "sources": ["Legumes", "Grains", "Leafy greens"]},
                    "fluoride": {"function": "Tooth decay prevention", "sources": ["Fluoridated water", "Tea", "Fish"]}
                }
            },
            "phytonutrients": {
                "carotenoids": {"function": "Antioxidants, vitamin A precursors", "sources": ["Carrots, sweet potatoes, spinach, kale, tomatoes (lycopene)"], "examples": ["Beta-carotene", "Lycopene", "Lutein", "Zeaxanthin"]},
                "polyphenols": {"function": "Antioxidant, anti-inflammatory", "sources": ["Berries, dark chocolate, tea, coffee, red wine (moderate), herbs"], "examples": ["Flavonoids (quercetin, catechins)", "Resveratrol", "Curcumin"]},
                "glucosinolates": {"function": "Detoxification, cancer protective", "sources": ["Broccoli, Brussels sprouts, cabbage, kale, cauliflower"]},
                "phytoestrogens": {"function": "Hormone modulation", "sources": ["Soy products, flax seeds, sesame seeds", "Legumes"]}
            }
        },
        "hydration": {
            "daily_needs": {
                "general": "0.5-1 oz per pound of body weight (e.g., 150 lb person: 75-150 oz)",
                "athletes": "Add 12-24 oz per hour of intense exercise",
                "thirst_cue": "Drink before thirsty; thirst indicates mild dehydration"
            },
            "urine_color": {
                "well_hydrated": "Pale yellow (lemonade color)",
                "dehydrated": "Dark yellow or amber",
                "overhydrated": "Clear (back off slightly)"
            },
            "electrolytes": {
                "when_needed": "During prolonged exercise (>1 hour sweating), hot weather, illness (vomiting/diarrhea)",
                "sources": ["Coconut water", "Electrolyte tablets", "Homemade: water + pinch salt + squeeze lemon + honey"]
            }
        }
    },
    
    # ------------------------------------------------------------------
    # 2. DIET PLANS (Expanded with specific protocols)
    # ------------------------------------------------------------------
    "diet_plans": {
        "balanced_diet": {
            "description": "General healthy eating for average person based on USDA MyPlate and Mediterranean principles",
            "composition": ["50% vegetables and fruits", "25% whole grains", "25% lean protein"],
            "daily_pattern": {
                "breakfast": "Oatmeal with berries and nuts OR Greek yogurt parfait OR eggs with whole grain toast + avocado",
                "snack": "Apple with almond butter OR cottage cheese with cucumber slices",
                "lunch": "Grilled chicken salad with olive oil dressing OR quinoa bowl with beans and vegetables",
                "snack": "Handful of almonds + orange OR hummus with carrots",
                "dinner": "Baked salmon with roasted sweet potato and asparagus OR lentil soup with side salad"
            },
            "plate_method": "Half plate produce, quarter protein, quarter complex carbs + thumb-sized healthy fat"
        },
        "mediterranean_diet": {
            "description": "Based on eating patterns of Greece, Italy, Spain; consistently ranked #1 for heart health",
            "key_foods": ["Olive oil (primary fat)", "Fish (at least 2x/week)", "Legumes", "Nuts and seeds", "Fruits and vegetables (especially leafy greens)", "Whole grains", "Herbs and spices", "Moderate red wine (optional)"],
            "limit": ["Red meat (few times/month)", "Processed meats", "Added sugar", "Refined grains"],
            "benefits": ["Reduced cardiovascular disease risk", "Lower inflammation", "Cognitive protection", "Longevity"]
        },
        "dash_diet": {
            "description": "Dietary Approaches to Stop Hypertension - designed to lower blood pressure",
            "emphasis": ["Low sodium (<2300mg or <1500mg)", "High potassium", "High magnesium", "High calcium"],
            "food_groups": {
                "grains": "6-8 servings/day (prefer whole)",
                "vegetables": "4-5 servings/day",
                "fruits": "4-5 servings/day",
                "dairy": "2-3 servings/day (low-fat)",
                "lean_protein": "≤6 servings/day",
                "nuts/seeds/legumes": "4-5 servings/week",
                "fats/oils": "2-3 servings/day",
                "sweets": "≤5 servings/week"
            }
        },
        "weight_loss": {
            "strategy": "Calorie deficit of 300-500 calories below maintenance (lose 0.5-1 lb per week)",
            "approach": [
                "Track calories or use portion control (apps: MyFitnessPal, Cronometer)",
                "Increase protein intake to 1.0-1.2g per pound (keeps you full, preserves muscle)",
                "Prioritize whole foods (higher volume, lower calorie density)",
                "Reduce processed foods and sugar",
                "Stay hydrated (water before meals reduces intake)",
                "Include regular exercise (NEAT matters: walk more)",
                "Get adequate sleep (poor sleep increases hunger hormones)",
                "Eat slowly and mindfully (takes 20 min for fullness signal)"
            ],
            "foods_to_limit": ["Sugary drinks (soda, juice, sweetened coffee)", "Processed snacks (chips, cookies)", "High-calorie oils (heavy dressings)", "Alcohol (7 cal/g, impairs judgment)", "Refined carbs (white bread, pastries)"],
            "foods_to_emphasize": ["Lean proteins (chicken, fish, tofu, legumes)", "Non-starchy vegetables (broccoli, spinach, peppers, cauliflower)", "Whole grains (oats, quinoa, brown rice)", "Fruits (berries, apples, citrus - whole fruit, not juice)", "Legumes (beans, lentils - high satiety)"],
            "volume_eating": "Fill up on low-calorie high-volume foods: leafy greens, zucchini, cucumbers, celery, cauliflower rice, broth-based soups",
            "sample_1500_calorie_day": {
                "breakfast": "2 eggs + 1 cup spinach + 1 slice whole grain toast (≈300 cal)",
                "lunch": "4 oz chicken breast + 2 cups mixed greens + 1 tbsp vinaigrette + 1/2 cup berries (≈350 cal)",
                "snack": "1 apple + 1 tbsp peanut butter (≈150 cal)",
                "dinner": "5 oz salmon + 1 cup roasted broccoli + 1/2 cup quinoa (≈500 cal)",
                "evening": "1 cup nonfat Greek yogurt (≈200 cal)"
            }
        },
        "muscle_gain": {
            "strategy": "Calorie surplus of 300-500 calories with progressive resistance training",
            "approach": [
                "Eat 1g protein per pound of body weight (minimum)",
                "Consume adequate carbs for energy and glycogen (3-4g per pound)",
                "Include healthy fats (0.4-0.5g per pound) for hormone production",
                "Time carbs and protein around workouts (pre and post)",
                "Progressively overload in gym",
                "Get 7-9 hours sleep for recovery",
                "Consider creatine supplementation (5g daily)"
            ],
            "sample_daily_2800_calories": {
                "meal1_breakfast": "4 eggs + 1 cup oats + 1 cup berries + 2 tbsp peanut butter (≈700 cal, 40g protein)",
                "meal2_lunch": "6 oz chicken breast + 1.5 cups brown rice + 2 cups broccoli (≈650 cal, 50g protein)",
                "meal3_post_workout": "2 scoops protein powder + 1 banana + 1 cup milk (≈400 cal, 50g protein)",
                "meal4_dinner": "6 oz lean beef + 1 sweet potato + 1 cup green beans (≈600 cal, 45g protein)",
                "meal5_before_bed": "1 cup cottage cheese + 1 tbsp almond butter (≈250 cal, 25g protein)"
            },
            "protein_timing": "20-40g every 3-4 hours"
        },
        "low_carb_ketogenic": {
            "description": "Very low carb (<50g/day), high fat (70-80% calories), moderate protein",
            "macros": {"carbs": "5-10%", "protein": "15-25%", "fat": "70-80%"},
            "allowed_foods": ["Meat (any)", "Fatty fish", "Eggs", "Non-starchy vegetables (leafy greens, broccoli, cauliflower, zucchini)", "High-fat dairy (cheese, butter, cream)", "Nuts and seeds (limit cashews)", "Avocado", "Berries (small amounts)", "Oils (olive, coconut, avocado)"],
            "avoid": ["Grains (wheat, rice, oats, corn)", "Sugar (honey, maple syrup, soda)", "Starchy vegetables (potatoes, sweet potatoes, peas)", "Most fruits (except berries)", "Legumes (beans, lentils)", "Processed foods"],
            "benefits": ["May aid fat loss (especially visceral fat)", "Appetite suppression", "Blood sugar control (type 2 diabetes)", "Epilepsy (medical use)"],
            "side_effects": ["Keto flu (fatigue, headache, brain fog - lasts 1-2 weeks)", "Bad breath (acetone)", "Constipation (need electrolytes)", "May raise LDL cholesterol in some"],
            "not_for": ["Type 1 diabetes (without medical supervision)", "Pancreatic conditions", "Gallbladder removed", "Pregnancy", "Eating disorder history"]
        },
        "intermittent_fasting": {
            "description": "Eating pattern with alternating fasting and eating windows",
            "protocols": {
                "16_8": "Fast 16 hours, eat in 8-hour window (most common, e.g., 12pm-8pm)",
                "18_6": "Fast 18, eat in 6-hour window",
                "20_4_warrior": "Fast 20, eat in 4-hour window",
                "5_2": "Eat normally 5 days, restrict to 500-600 calories 2 non-consecutive days",
                "alternate_day": "Alternate normal eating with fasting/very low calorie days",
                "omad": "One Meal A Day (eat once per day)"
            },
            "benefits": ["May aid fat loss (natural calorie reduction)", "Simplifies meal planning", "May improve insulin sensitivity", "Potential cellular autophagy (after 16-24 hours)"],
            "caution": "Not suitable for: pregnant/breastfeeding, underweight, diabetes (medication adjustment), adolescents, eating disorder history",
            "what_to_consume_during_fast": "Water, black coffee, unsweetened tea (zero calories). Avoid: cream, sugar, artificial sweeteners (may spike insulin in some).",
            "breaking_the_fast": "Start with easily digestible protein + fat + fiber, avoid massive carb load"
        },
        "plant_based_vegan": {
            "description": "Excludes some or all animal products",
            "variations": {
                "vegan": "No animal products (meat, dairy, eggs, honey)",
                "vegetarian": "No meat/fish, may include dairy and eggs",
                "pescatarian": "Vegetarian + fish/seafood",
                "flexitarian": "Mostly plant-based, occasional meat"
            },
            "nutrient_risks_to_watch": ["Vitamin B12 (must supplement or eat fortified foods)", "Iron (plant sources less absorbable - pair with vitamin C)", "Calcium (need leafy greens, fortified plant milks, tofu)", "Omega-3 (consider algae oil supplement)", "Zinc", "Iodine"],
            "protein_combinations": "Combine legumes (beans, lentils) with grains (rice, wheat) for complete amino acid profile",
            "benefits": ["Higher fiber intake", "Lower saturated fat", "Lower risk of heart disease, hypertension, type 2 diabetes", "Environmental benefits"],
            "sample_day": {
                "breakfast": "Tofu scramble with spinach + whole grain toast + berries",
                "lunch": "Chickpea salad sandwich + side of carrot sticks + hummus",
                "snack": "Smoothie with plant milk, banana, peanut butter, chia seeds",
                "dinner": "Lentil curry with brown rice + roasted cauliflower"
            }
        },
        "maintenance": {
            "strategy": "Consume calories equal to TDEE (Total Daily Energy Expenditure)",
            "approach": [
                "Track intake for 2-3 weeks to find maintenance level (scale stable)",
                "Include variety of whole foods for micronutrient coverage",
                "Maintain consistent macros: 30-35% protein, 40-50% carbs, 20-30% fats",
                "Support with regular exercise",
                "Allow flexibility (80/20 rule) for sustainability"
            ],
            "adjusting": "If weight changes over 2 weeks, adjust calories by 100-200"
        }
    },
    
    # ------------------------------------------------------------------
    # 3. FOOD CATEGORIES (Detailed with nutritional data)
    # ------------------------------------------------------------------
    "food_categories": {
        "proteins": {
            "animal_based": {
                "chicken_breast": {"protein": "31g per 100g", "calories": "165", "fat": "3.6g", "benefits": "Leanest protein, affordable, versatile"},
                "chicken_thigh": {"protein": "26g per 100g", "calories": "209", "fat": "10g", "benefits": "More flavor, juicier than breast"},
                "turkey_breast": {"protein": "29g per 100g", "calories": "135", "fat": "1.5g", "benefits": "Very lean, rich in B vitamins"},
                "beef_lean_90_10": {"protein": "26g per 100g", "calories": "176", "fat": "10g", "benefits": "Iron, zinc, creatine, B12"},
                "beef_grass_fed": {"protein": "~same", "benefits": "More omega-3s, CLA, antioxidants than grain-fed"},
                "pork_loin": {"protein": "27g per 100g", "calories": "143", "fat": "3.5g", "benefits": "Lean white meat, thiamine rich"},
                "salmon": {"protein": "22g per 100g", "calories": "208", "fat": "13g (omega-3s)", "benefits": "EPA/DHA for brain/heart health, vitamin D"},
                "tuna_canned": {"protein": "24g per 100g", "calories": "116", "benefits": "Cheap, convenient, high protein - limit to 2-3x/week due to mercury"},
                "sardines": {"protein": "25g per 100g", "calories": "208", "benefits": "Low mercury, high omega-3s, calcium (bones), vitamin D"},
                "eggs": {"protein": "6g per egg", "calories": "70", "fat": "5g", "benefits": "Complete protein, choline (brain health), lutein/zeaxanthin (eyes)"},
                "egg_whites": {"protein": "3.6g per white", "calories": "17", "benefits": "Pure protein, zero fat, low calorie"},
                "greek_yogurt": {"protein": "10-15g per cup", "calories": "130-200", "benefits": "Probiotics, calcium, casein (slow-digesting)"},
                "cottage_cheese": {"protein": "28g per cup", "calories": "180-220", "benefits": "Casein-rich (great before bed), calcium"},
                "whey_protein": {"protein": "20-25g per scoop", "calories": "100-120", "benefits": "Fast absorption, high leucine, post-workout ideal"},
                "casein_protein": {"protein": "20-25g per scoop", "calories": "100-120", "benefits": "Slow absorption (6-8 hrs), good before bed"}
            },
            "plant_based": {
                "lentils": {"protein": "9g per cooked cup", "calories": "230", "carbs": "40g", "fiber": "16g", "benefits": "Fiber, iron, folate, cheap"},
                "chickpeas": {"protein": "15g per cooked cup", "calories": "269", "fiber": "12g", "benefits": "Versatile (hummus, curries), manganese, folate"},
                "black_beans": {"protein": "15g per cup", "calories": "227", "fiber": "15g", "benefits": "Heart health, magnesium, antioxidants"},
                "tofu": {"protein": "15-20g per 100g", "calories": "76-150", "benefits": "Complete amino acids, calcium (if calcium-set), iron"},
                "tempeh": {"protein": "19g per 100g", "calories": "193", "benefits": "Fermented (probiotic), more fiber and protein than tofu"},
                "edamame": {"protein": "17g per cup", "calories": "188", "benefits": "Young soybeans, complete protein, folate, vitamin K"},
                "seitan": {"protein": "25g per 100g", "calories": "120", "benefits": "Wheat gluten - very high protein, but not gluten-free"},
                "hemp_seeds": {"protein": "10g per 3 tbsp", "calories": "170", "benefits": "Complete protein, omega-3s, magnesium"},
                "quinoa": {"protein": "8g per cup cooked", "calories": "222", "benefits": "Complete protein, fiber, iron, magnesium (technically a seed)"},
                "pea_protein": {"protein": "20-24g per scoop", "benefits": "Hypoallergenic plant protein, iron-rich"},
                "nutritional_yeast": {"protein": "8g per 2 tbsp", "calories": "60", "benefits": "Cheesy flavor, B12 fortified, complete protein"}
            }
        },
        "carbohydrates": {
            "whole_grains": {
                "oats": {"calories_per_cup_cooked": "166", "fiber": "4g", "benefits": "Beta-glucan lowers cholesterol, satiating"},
                "brown_rice": {"calories_per_cup": "216", "fiber": "3.5g", "benefits": "Manganese, selenium, whole grain"},
                "quinoa": {"calories_per_cup": "222", "protein": "8g", "fiber": "5g", "benefits": "Complete protein, iron"},
                "barley": {"calories_per_cup": "193", "fiber": "6g", "benefits": "High fiber, beta-glucan"},
                "buckwheat": {"calories_per_cup": "155", "benefits": "Gluten-free, rutin antioxidant, good for blood flow"},
                "wild_rice": {"calories_per_cup": "166", "benefits": "Higher protein and fiber than brown rice"},
                "whole_wheat_bread": {"per_slice": "70-90 cal", "fiber": "2-3g", "tip": "Look for '100% whole wheat' not 'wheat flour'"},
                "corn_tortillas": {"per_tortilla": "50-60 cal", "benefits": "Gluten-free, lower calorie than flour"}
            },
            "fruits": {
                "banana": {"calories": "105", "carbs": "27g", "benefits": "Potassium (good for cramps), pre-workout fuel"},
                "apple": {"calories": "95", "fiber": "4.4g", "benefits": "Pectin fiber, quercetin antioxidant, satiating"},
                "berries_mixed": {"calories_per_cup": "60-85", "fiber": "5-8g", "benefits": "Highest antioxidant content, low sugar among fruits"},
                "orange": {"calories": "62", "vitamin_c": "70mg (≈78% RDA)", "benefits": "Immune support, hydration"},
                "strawberries": {"calories_per_cup": "49", "vitamin_c": "89mg", "benefits": "Low sugar, high vitamin C, polyphenols"},
                "blueberries": {"calories_per_cup": "84", "antioxidants": "Very high (anthocyanins)", "benefits": "Brain health, recovery"},
                "grapes": {"calories_per_cup": "62", "benefits": "Resveratrol (heart health), but higher sugar"},
                "kiwi": {"calories": "42", "vitamin_c": "64mg", "benefits": "Vitamin K, E, serotonin (may improve sleep)"},
                "avocado": {"calories": "240", "fat": "22g", "fiber": "10g", "benefits": "Technically fruit - healthy fats, potassium, fiber"}
            },
            "vegetables": {
                "broccoli": {"calories_per_cup": "31", "fiber": "2.4g", "benefits": "Sulforaphane (cancer protective), vitamins C/K"},
                "spinach": {"calories_per_cup": "7", "iron": "0.8mg", "benefits": "Vitamin K, iron, magnesium, lutein for eyes"},
                "kale": {"calories_per_cup": "8", "vitamin_k": "684% RDA", "benefits": "Very nutrient-dense, antioxidants"},
                "sweet_potato": {"calories_medium": "103", "vitamin_a": "438% RDA", "benefits": "Beta-carotene, complex carbs for energy"},
                "cauliflower": {"calories_per_cup": "25", "benefits": "Versatile (rice/mash/pizza crust), glucosinolates"},
                "bell_peppers": {"calories_per_cup": "30", "vitamin_c": "190mg (red pepper)", "benefits": "Vitamin C, antioxidants"},
                "asparagus": {"calories_per_cup": "27", "benefits": "Folate, vitamin K, prebiotic fiber"},
                "zucchini": {"calories_per_cup": "19", "benefits": "High water content, low calorie, good for volume"},
                "mushrooms": {"calories_per_cup": "21", "benefits": "Ergothioneine (antioxidant), vitamin D if UV-exposed"},
                "brussels_sprouts": {"calories_per_cup": "38", "fiber": "3.3g", "benefits": "Sulforaphane, vitamin C, K"},
                "carrots": {"calories_per_cup": "52", "vitamin_a": "428% RDA", "benefits": "Beta-carotene, good raw or cooked (cooking increases bioaccessibility)"},
                "tomatoes": {"calories_medium": "22", "benefits": "Lycopene (cooking increases absorption), vitamin C"},
                "cucumber": {"calories_per_cup": "16", "benefits": "Hydration, low calorie, silica for skin"},
                "onions": {"calories_medium": "44", "benefits": "Quercetin (antioxidant), prebiotic fiber"}
            },
            "legumes": {
                "lentils_red": {"calories_per_cup": "230", "protein": "18g", "fiber": "16g", "iron": "37% RDA"},
                "black_beans": {"calories_per_cup": "227", "protein": "15g", "fiber": "15g", "magnesium": "30% RDA"},
                "kidney_beans": {"calories_per_cup": "225", "protein": "15g", "fiber": "13g", "benefits": "Phytonutrients, iron"},
                "pinto_beans": {"calories_per_cup": "245", "benefits": "Common in Mexican cuisine, high fiber"},
                "chickpeas": {"calories_per_cup": "269", "protein": "15g", "fiber": "12g", "manganese": "84% RDA"},
                "peas": {"calories_per_cup": "117", "protein": "8g", "fiber": "8g", "benefits": "Starchier than other legumes"},
                "soybeans": {"calories_per_cup": "298", "protein": "29g", "benefits": "Complete protein, high in all essential amino acids"}
            }
        },
        "healthy_fats": {
            "sources": {
                "avocado": {"fat": "22g per fruit", "type": "Monounsaturated", "calories": "240", "portion": "1/4-1/2 fruit"},
                "olive_oil_extra_virgin": {"fat": "14g per tbsp", "calories": "119", "benefits": "Polyphenols (EVOO only), heart health - don't overheat past smoke point (375°F)"},
                "almonds": {"fat": "14g per oz (23 nuts)", "calories": "164", "benefits": "Vitamin E, magnesium, protein", "portion": "1 oz (handful)"},
                "walnuts": {"fat": "18g per oz (14 halves)", "calories": "185", "benefits": "Alpha-linolenic acid (plant omega-3)", "portion": "1 oz"},
                "chia_seeds": {"fat": "9g per oz", "calories": "138", "benefits": "Omega-3, fiber (10g), thickens liquids"},
                "flax_seeds_ground": {"fat": "4g per tbsp", "calories": "37", "benefits": "Lignans (phytoestrogens), fiber - must grind to absorb nutrients"},
                "fatty_fish_salmon_sardines": {"fat": "13g per 3oz", "calories": "175-200", "benefits": "EPA/DHA omega-3s, vitamin D"},
                "coconut_oil": {"fat": "14g per tbsp", "calories": "117", "type": "Saturated (MCT)", "caution": "High in saturated fat - use sparingly"},
                "nut_butters": {"fat": "16g per 2 tbsp", "calories": "190", "portion": "2 tbsp", "tip": "Choose no added sugar/oil varieties"},
                "sesame_seeds": {"fat": "13g per oz", "benefits": "Copper, calcium, tahini is paste form"},
                "pumpkin_seeds": {"fat": "14g per oz", "benefits": "Magnesium, zinc, iron"}
            },
            "portion_guide": "Fist-sized for fatty fruit (avocado), thumb-tip for oils (1 tbsp), handful for nuts/seeds (1 oz)",
            "benefits": "Satiety, hormone production, nutrient absorption (especially fat-soluble vitamins A,D,E,K)"
        }
    },
    
    # ------------------------------------------------------------------
    # 4. MEAL TIMING (Expanded)
    # ------------------------------------------------------------------
    "meal_timing": {
        "pre_workout": {
            "timing": "1-3 hours before exercise (earlier for larger meals, later for smaller)",
            "what": "Carbs + moderate protein, low fat and fiber (digest slower)",
            "examples": [
                "Banana + 1 tbsp peanut butter (light, 45 min prior)",
                "Oatmeal with berries + scoop protein (2 hours prior)",
                "Toast with honey + 2 eggs (90 min prior)",
                "Apple + string cheese (30 min prior)",
                "Rice cakes with jam (super simple 15 min prior)"
            ],
            "avoid": "Heavy fatty/greasy meals (burgers, fried food), high-fiber large salads (causes GI distress)"
        },
        "post_workout": {
            "timing": "Within 30-120 minutes after exercise (anabolic window less critical than once thought, but still beneficial)",
            "what": "Carbs (to replenish glycogen) + protein (to repair muscle), ideally 3:1 or 4:1 carb:protein ratio for endurance; closer to 1:1 or 2:1 for strength",
            "examples": [
                "Chicken with rice + veggies",
                "Protein shake with banana + oat milk",
                "Tuna on whole grain crackers",
                "Greek yogurt with berries + honey",
                "Chocolate milk (effective, cheap, has 3:1 ratio)",
                "Eggs + sweet potato",
                "Salmon + quinoa"
            ],
            "leucine_threshold": "2-3g leucine (about 25-35g quality protein) to maximally stimulate MPS"
        },
        "peri_workout": {
            "intra_workout": "For workouts >90 min or endurance events: 30-60g carbs per hour (sports drink, gels, or diluted juice)",
            "BCAAs": "Generally unnecessary if eating enough protein (leucine alone is the key; BCAAs lack other aminos)"
        },
        "before_bed": {
            "nutrition": "Casein protein (slow-digesting) provides steady amino acid release overnight, may improve muscle protein synthesis.",
            "examples": ["Cottage cheese (1 cup)", "Greek yogurt (1 cup)", "Casein protein shake", "Milk + peanut butter"],
            "timing": "30-60 min before bed",
            "for_weight_loss": "If trying to lose weight, skip or keep very small - total calories matter more than timing."
        },
        "intermittent_fasting": {
            "concept": "Eating within a specific time window (e.g., 8 hours)",
            "benefits": ["May aid fat loss (natural calorie reduction)", "Simplifies meal planning (fewer meals)", "May improve insulin sensitivity", "Some evidence for cellular autophagy"],
            "popular_schedules": ["16:8 (most common)", "18:6", "20:4", "5:2"],
            "caution": "Not suitable for everyone; consult healthcare provider if you have diabetes, low blood pressure, history of eating disorders, or are pregnant/breastfeeding.",
            "while_fasting": "Water, black coffee, unsweetened tea, electrolytes (no calories)"
        },
        "meal_frequency": {
            "research": "Total daily intake matters more than frequency. Both 3 meals/day and 5-6 small meals work for different people.",
            "advantages_more_meals": ["May control hunger for some", "Smaller portions easier to digest", "Steadier energy"],
            "advantages_fewer_meals": ["Simpler", "Easier intermittent fasting", "More satiating per meal"],
            "recommendation": "Do what fits your lifestyle and hunger patterns"
        }
    },
    
    # ------------------------------------------------------------------
    # 5. SPECIAL POPULATIONS
    # ------------------------------------------------------------------
    "special_populations": {
        "pregnancy": {
            "calories": "First trimester: no increase; Second: +340 cal; Third: +450 cal",
            "key_nutrients": {
                "folic_acid": "600 mcg (prevents neural tube defects) - prenatal vitamin essential",
                "iron": "27 mg (supports increased blood volume)",
                "calcium": "1000 mg (fetal bone development)",
                "dha_omega3": "200-300 mg for baby's brain/eye development",
                "iodine": "220 mcg",
                "choline": "450 mg (brain development)"
            },
            "foods_to_avoid": ["Raw fish/sushi", "Unpasteurized dairy", "Deli meats (unless heated)", "High-mercury fish (shark, swordfish, king mackerel, tuna (limit))", "Raw eggs", "Alcohol (no safe amount)", "Excess caffeine (<200mg/day)"],
            "weight_gain": "Normal BMI: 25-35 lbs"
        },
        "older_adults_65_plus": {
            "protein_needs": "Higher: 1.0-1.2g per pound (to combat sarcopenia - age-related muscle loss)",
            "calcium_vitamin_d": "Calcium 1200 mg, Vitamin D 800-1000 IU (bone health, fall prevention)",
            "b12": "Absorption decreases with age - consider supplement or fortified foods",
            "hydration": "Thirst sensation diminishes - drink on schedule",
            "challenges": ["Chewing difficulties (soft foods)", "Reduced appetite (nutrient-dense foods)", "Medication interactions"],
            "fiber": "Maintain regular bowel movements (20-30g/day)"
        },
        "athletes_endurance": {
            "carb_needs": "5-7g per pound (very high)",
            "protein_needs": "0.9-1.0g per pound",
            "hydration": "Weigh before/after - lose <2% body weight; replace 16-24 oz per lb lost",
            "during_exercise": "30-60g carbs per hour after 60-90 min",
            "iron": "Monitor (foot strike hemolysis, sweat losses) - women at higher risk"
        },
        "diabetes_type2": {
            "carb_strategies": ["Consistent carbohydrate timing (don't skip meals)", "Choose low-GI carbs", "Pair carbs with protein and fiber", "Monitor blood sugar responses"],
            "plate_method": "1/2 non-starchy veg, 1/4 lean protein, 1/4 carbs (or less)",
            "limit": "Sugary drinks, refined carbs, sweets",
            "beneficial_patterns": ["Mediterranean", "DASH", "Low-carb (if not contraindicated)"],
            "monitoring": "Check blood glucose before and 2 hrs after meals to learn personal response"
        }
    },
    
    # ------------------------------------------------------------------
    # 6. SUPPLEMENTS (Evidence-based)
    # ------------------------------------------------------------------
    "supplements_evidence": {
        "strong_evidence": {
            "whey_protein": "Convenient protein source, high leucine, good post-workout - not essential if getting enough from food",
            "creatine_monohydrate": {"dose": "5g daily (no loading needed)", "benefits": "Strength, muscle mass, cognitive benefits, safety well-established", "timing": "Any time"},
            "vitamin_d": {"dose": "600-2000 IU (test blood levels if possible)", "who": "Northern latitudes, dark skin, minimal sun exposure, older adults"},
            "b12": {"dose": "25-100 mcg daily or 2500 mcg weekly", "who": "Vegans (essential), vegetarians, older adults (50+), pernicious anemia"},
            "folic_acid": {"dose": "400-600 mcg", "who": "Pregnant or trying to conceive (critical)"},
            "omega3_fish_oil": {"dose": "1-2g EPA+DHA combined", "benefits": "Triglycerides, inflammation, brain health if not eating fatty fish 2x/week", "note": "Algae oil for vegans"}
        },
        "moderate_evidence": {
            "caffeine": {"dose": "3-6 mg per kg body weight (200-400mg) 30-60 min pre-workout", "benefits": "Endurance, focus, fat oxidation"},
            "beta_alanine": {"dose": "2-5g daily (may cause tingling/paresthesia)", "benefits": "High-intensity exercise >60 seconds (buffer H+ ions)", "duration": "Needs ~4 weeks to load"},
            "citrulline_malate": {"dose": "6-8g pre-workout", "benefits": "Blood flow, reduces fatigue, reduces soreness"},
            "probiotics": {"benefits": "Digestive health, may support immunity, but strain-specific; food sources (yogurt, kefir, sauerkraut) are fine"},
            "magnesium": {"dose": "200-400 mg (elemental)", "who": "If deficient (common), for sleep/cramps/muscle function", "forms": "Glycinate (good for sleep), citrate (gentle laxative), oxide (poor absorption)"}
        },
        "weak_or_no_evidence": {
            "bcaas": "Whey has BCAAs already - BCAAs alone lack other aminos for MPS. Waste of money if eating enough protein.",
            "glutamine": "Body produces enough except severe illness. Not helpful for healthy active people.",
            "fat_burners": "Most are ineffective or dangerous (ephedrine banned, others barely work over caffeine alone).",
            "collagen": "Degraded to amino acids like any protein. Body rebuilds collagen - no proven need for supplement specifically.",
            "testosterone_boosters": "Ingredients (tribulus, fenugreek, etc.) largely fail in studies. Save money."
        },
        "caution_high_risk": {
            "stimulants_high_dose": "Heart palpitations, insomnia, anxiety",
            "mass_gainers": "Mostly sugar and maltodextrin - cheaper to blend oats + whey + peanut butter",
            "detox_teas_cleanses": "No evidence of 'detox' beyond liver/kidneys; some diuretics/laxatives dangerous long-term"
        }
    },
    
    # ------------------------------------------------------------------
    # 7. PRACTICAL TOOLS & CALCULATIONS
    # ------------------------------------------------------------------
    "calculations": {
        "bmr_mifflin_st_jeor": {
            "male": "BMR = (10 × weight in kg) + (6.25 × height in cm) - (5 × age) + 5",
            "female": "BMR = (10 × weight in kg) + (6.25 × height in cm) - (5 × age) - 161"
        },
        "tdee_multipliers": {
            "sedentary": "BMR × 1.2 (little or no exercise)",
            "lightly_active": "BMR × 1.375 (light exercise 1-3 days/week)",
            "moderately_active": "BMR × 1.55 (moderate exercise 3-5 days/week)",
            "very_active": "BMR × 1.725 (hard exercise 6-7 days/week)",
            "extra_active": "BMR × 1.9 (physical job + intense daily training)"
        },
        "macros_calculations": {
            "protein_grams": "bodyweight(lbs) × 0.8-1.0",
            "fat_grams": "bodyweight(lbs) × 0.3-0.4 (or 20-35% of calories ÷ 9 cal/g)",
            "carbs_grams": "remainder of calories after protein + fat ÷ 4 cal/g"
        },
        "body_comp": {
            "healthy_bf_percentage": {"men": "10-20%", "women": "18-28%"},
            "athletic_bf": {"men": "6-13%", "women": "14-20%"},
            "essential_bf": {"men": "2-5%", "women": "10-13%"}
        }
    },
    
    # ------------------------------------------------------------------
    # 8. RECIPES & MEAL PREP
    # ------------------------------------------------------------------
    "recipes": {
        "quick_high_protein_breakfast": [
            "Greek yogurt bowl: 1 cup yogurt + 1/2 cup berries + 1 tbsp nuts + drizzle honey (~300 cal, 25g protein)",
            "Protein oats: 1/2 cup oats + 1 scoop protein powder + 1 cup water/milk + 1/2 banana (~400 cal, 30g protein)",
            "Egg scramble: 3 eggs + handful spinach + 1 slice whole grain toast (~350 cal, 20g protein)",
            "Smoothie: 1 cup milk + 1 scoop protein + 1 tbsp peanut butter + 1/2 banana + ice (~400 cal, 35g protein)"
        ],
        "meal_prep_lunches": [
            "Chicken + roasted veggies + quinoa (makes 4-5 meals)",
            "Turkey chili: ground turkey, beans, tomatoes, peppers (batch cook)",
            "Lentil soup + side of Greek yogurt (freezes well)",
            "Tuna salad (Greek yogurt instead of mayo) + crackers + veggies"
        ],
        "low_calorie_high_volume": [
            "Zucchini noodles + turkey meatballs + marinara (under 400 cal)",
            "Cauliflower rice stir-fry with shrimp + vegetables (under 350 cal)",
            "Big salad: 4 cups greens + 4 oz chicken + cucumber + tomato + 2 tbsp light vinaigrette (under 350 cal)",
            "Egg white scramble with peppers, onions, spinach (~200 cal)"
        ],
        "post_workout_smoothie": "1 cup milk, 1 scoop whey, 1/2 cup frozen berries, 1/2 banana, handful spinach"
    }
}

# ------------------------------------------------------------------
# 9. RESPONSES TO COMMON QUESTIONS (Expanded)
# ------------------------------------------------------------------
DIET_RESPONSES = {
    "common_questions": {
        "should_i_diet": "A balanced diet with regular exercise is more sustainable than strict dieting. Instead of 'going on a diet,' aim to build lasting healthy habits. The best approach is eating whole foods, getting adequate protein and fiber, staying hydrated, sleeping well, and moving daily.",
        "best_diet": "The best diet is one you can stick to! There is no single optimal diet for everyone. Focus on: 1) Whole foods (minimally processed), 2) Adequate protein for your goals, 3) Plenty of vegetables and fiber, 4) Healthy fats, 5) Consistency over perfection. Mediterranean, DASH, and balanced diets have the strongest evidence for long-term health.",
        "low_carb": "Low-carb can work for weight loss (often due to reduced appetite and water loss initially) but isn't necessary. A calorie deficit via any approach causes fat loss. Low-carb may benefit those with insulin resistance, PCOS, or type 2 diabetes. For most, moderate carb intake (3-5g per pound) from quality sources (vegetables, whole grains, legumes, fruit) is perfectly fine for health and performance.",
        "supplements": "Whole foods first; supplements fill specific gaps. Get blood work to check for deficiencies. The only supplements with strong evidence for most people are: 1) Vitamin D (if deficient), 2) B12 (vegans/vegetarians/older adults), 3) Creatine (for strength training), 4) Whey or plant protein (if struggling to meet protein needs), 5) Omega-3 (if not eating fatty fish 2x/week). Ask your doctor which you need. Don't waste money on fat burners, BCAAs, or 'detox' products.",
        "cheat_day": "Occasional treats are fine; the 80/20 rule works for most (80% healthy whole foods, 20% flexible/fun foods). A full 'cheat day' (unlimited calories) can undo a week's deficit for some people. Instead, consider a single 'cheat meal' or flexible daily treats (e.g., small dessert, favorite snack). Stress about perfect eating is worse than the treat itself. Consistency over perfection.",
        "how_much_protein": "Sedentary: 0.36g/lb (0.8g/kg). Active: 0.8-1.0g/lb (1.6-2.2g/kg). Weight loss: 1.0-1.2g/lb to preserve muscle. Older adults: 1.0-1.2g/lb. Bodybuilding: 1.0-1.2g/lb. More than 1.2-1.5g/lb provides no additional benefit and may displace carbs/fats.",
        "carbs_at_night": "Eating carbs at night does NOT automatically turn into fat. Total calorie balance matters. For muscle gain, carbs at night support recovery and sleep (through serotonin/melatonin). If you've already met your calorie target, adding carbs will cause surplus. Timing is secondary to total daily intake.",
        "diet_soda": "Diet soda is calorie-free and likely safe in moderation. Some studies show it may increase sweet cravings or appetite in some people, but it does NOT spike insulin (contrary to popular claims). If it helps you avoid sugary drinks, it's a net positive. However, water, sparkling water, unsweetened tea/coffee are better choices.",
        "breakfast": "Breakfast is not 'the most important meal of the day' for everyone. If you're hungry in the morning, eat breakfast. If not, intermittent fasting or skipping breakfast is fine - as long as you eat nutritious foods during your eating window and total calories work for your goals. The breakfast cereal industry popularized that slogan.",
        "vegetarian_protein": "Easily achievable: lentils (18g/cup), chickpeas (15g), tofu (20g/100g), tempeh (19g), seitan (25g), edamame (17g), quinoa (8g), Greek yogurt (15g/cup), cottage cheese (28g/cup), eggs (6g), nuts/seeds, and plant protein powders if needed. Combine legumes + grains for complete amino acid profile throughout the day.",
    },
    "myths_debunked": {
        "starvation_mode": "Starvation mode (significant metabolic slowdown) only occurs with extreme prolonged calorie restriction (<800 cal/day) and very low body fat. A reasonable deficit of 300-500 calories does NOT cause this.",
        "detox": "Your liver and kidneys do full-time detox. No juice cleanse, tea, or supplement improves this. Save your money.",
        "eating_fat_makes_you_fat": "Dietary fat does not directly become body fat. Excess total calories (regardless of source) causes fat storage. Healthy fats are essential for hormone function, brain health, and nutrient absorption.",
        "eating_after_6pm": "Meal timing matters very little. Late-night eating only causes weight gain if it pushes you into calorie surplus. Focus on total daily intake.",
        "spot_reduction": "You cannot lose fat from a specific body part by exercising that area (e.g., crunches for belly fat). Fat loss happens systemically via calorie deficit. Strength training builds muscle underneath, which changes shape.",
        "all_calories_equal": "For weight loss, calories matter most. For health, body composition, hunger, and energy, food quality matters hugely. 500 calories from chicken+broccoli differs from 500 calories from soda+cookies in terms of satiety, micronutrients, metabolic effect, and muscle preservation.",
        "more_protein_bad_for_kidneys": "High protein intake is safe for healthy kidneys. Only those with pre-existing kidney disease (e.g., CKD stage 3+) need restriction. For healthy individuals, 1-1.5g per pound is fine.",
        "fruit_has_too_much_sugar": "Fruit contains fiber, water, vitamins, and antioxidants that slow sugar absorption. Whole fruit is not the same as refined sugar. Eat whole fruit freely (2-4 servings/day). Fruit juice lacks fiber and should be limited."
    },
    "red_flags": {
        "see_doctor_before_diet": [
            "Unexplained weight loss",
            "History of eating disorder",
            "Diabetes (type 1 or 2 on medication)",
            "Kidney disease",
            "Pregnancy or breastfeeding",
            "Underlying medical condition (thyroid, heart disease, etc.)",
            "Taking blood thinners (e.g., Warfarin - vitamin K interactions)"
        ]
    }
}