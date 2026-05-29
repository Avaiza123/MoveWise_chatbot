# ============================================
# COMPLETE FITNESS KNOWLEDGE BASE
# ============================================

FITNESS_KNOWLEDGE = {
    "workout_types": {
        "cardio": {
            "description": "Cardiovascular exercises that increase heart rate and improve endurance",
            "examples": ["Running", "Cycling", "Swimming", "Jump Rope", "Rowing", "Elliptical"],
            "benefits": ["Burns calories", "Improves heart health", "Increases stamina", "Reduces stress"],
            "duration": "20-60 minutes",
            "frequency": "3-5 times per week",
            "beginner_tip": "Start with 20-30 minutes at moderate intensity"
        },
        "strength_training": {
            "description": "Exercises using weights or resistance to build muscle",
            "examples": ["Weightlifting", "Bodyweight exercises", "Resistance bands", "Dumbbells"],
            "benefits": ["Builds muscle", "Increases metabolism", "Stronger bones", "Improves posture"],
            "duration": "30-60 minutes",
            "frequency": "3-4 times per week",
            "rest_days": "48 hours between same muscle group training"
        },
        "flexibility": {
            "description": "Exercises to improve range of motion and flexibility",
            "examples": ["Yoga", "Pilates", "Stretching", "Tai Chi"],
            "benefits": ["Reduces injury risk", "Improves posture", "Reduces muscle tension", "Increases mobility"],
            "duration": "15-30 minutes",
            "frequency": "3-7 times per week",
            "best_time": "After workouts or dedicated flexibility sessions"
        },
        "hiit": {
            "description": "High-Intensity Interval Training - alternating intense and recovery periods",
            "examples": ["Burpees", "Mountain climbers", "Jump squats", "Sprint intervals"],
            "benefits": ["Burns maximum calories", "Improves cardiovascular health", "Saves time", "Increases metabolism"],
            "duration": "15-30 minutes",
            "frequency": "2-3 times per week",
            "important": "Not suitable for absolute beginners; requires good fitness base"
        },
        "calisthenics": {
            "description": "Bodyweight exercises using gravity as resistance",
            "examples": ["Pull-ups", "Dips", "Pistol squats", "L-sits", "Muscle-ups", "Handstands"],
            "benefits": ["No equipment needed", "Improves relative strength", "Good for mobility", "Develops body control"],
            "duration": "30-60 minutes",
            "frequency": "3-5 times per week",
            "progression": "Increase reps → harder variations → add weight vest"
        },
        "functional_training": {
            "description": "Exercises mimicking real-life movements",
            "examples": ["Kettlebell swings", "Medicine ball throws", "Battle ropes", "Farmer's walk", "Tire flips"],
            "benefits": ["Improves daily movement", "Core stability", "Balance and coordination", "Injury prevention"],
            "duration": "20-40 minutes",
            "frequency": "2-3 times per week"
        },
        "plyometrics": {
            "description": "Explosive jump training for power",
            "examples": ["Box jumps", "Broad jumps", "Clapping push-ups", "Depth jumps", "Lateral bounds"],
            "benefits": ["Improves explosive power", "Sports performance", "Bone density", "Reactive strength"],
            "duration": "15-25 minutes",
            "frequency": "1-2 times per week",
            "warning": "High impact; require good joint health and warm-up"
        },
        "cross_training": {
            "description": "Combining multiple workout types in a session or week",
            "benefits": ["Balanced fitness", "Prevents overuse injuries", "Avoids boredom"],
            "example_week": ["Mon: Cardio", "Tue: Strength", "Wed: Yoga", "Thu: HIIT", "Fri: Rest", "Sat: Calisthenics", "Sun: Active recovery"]
        }
    },
    
    "exercises": {
        "push_ups": {
            "muscles_targeted": ["Chest", "Triceps", "Shoulders", "Core"],
            "difficulty": "Beginner to Advanced",
            "how_to": "Keep body straight, lower until chest nearly touches floor, push back up",
            "sets_reps": "3 sets of 10-15 reps",
            "variations": ["Wide grip", "Diamond grip", "Decline push-ups", "One-arm push-ups"]
        },
        "squats": {
            "muscles_targeted": ["Quadriceps", "Hamstrings", "Glutes", "Core"],
            "difficulty": "Beginner to Advanced",
            "how_to": "Feet shoulder-width apart, lower hips back and down, keep chest up, return to standing",
            "sets_reps": "3 sets of 12-15 reps",
            "variations": ["Goblet squats", "Jump squats", "Bulgarian split squats", "Pistol squats"]
        },
        "deadlifts": {
            "muscles_targeted": ["Hamstrings", "Glutes", "Back", "Core"],
            "difficulty": "Intermediate to Advanced",
            "how_to": "Feet hip-width apart, bend knees and hips, keep bar close to body, stand up",
            "sets_reps": "3-5 sets of 3-6 reps",
            "caution": "Proper form is critical; consider professional guidance"
        },
        "plank": {
            "muscles_targeted": ["Core", "Shoulders", "Back"],
            "difficulty": "Beginner to Advanced",
            "how_to": "Forearms on ground, body in straight line, engage core",
            "duration": "Start with 20-30 seconds, progress to 60+ seconds",
            "variations": ["Side plank", "Dynamic plank", "Plank with leg lifts"]
        },
        "pull_ups": {
            "muscles_targeted": ["Latissimus dorsi", "Biceps", "Rhomboids", "Rear delts", "Core"],
            "difficulty": "Intermediate to Advanced",
            "how_to": "Hang from bar, shoulders back, pull chest to bar, lower controlled",
            "sets_reps": "3 sets of 5-12 reps",
            "progression": ["Negatives", "Band-assisted", "Weighted pull-ups", "Typewriter pull-ups"],
            "common_mistakes": ["Kipping/swinging", "Partial range of motion", "Shoulders shrugged up"]
        },
        "rows": {
            "muscles_targeted": ["Upper back", "Rear delts", "Biceps", "Lats"],
            "difficulty": "Beginner to Intermediate",
            "variations": ["Barbell row", "Dumbbell row", "Seated cable row", "Inverted row (bodyweight)"],
            "how_to": "Hinge at hips, back flat, pull elbows past body",
            "sets_reps": "3-4 sets of 8-12 reps"
        },
        "overhead_press": {
            "muscles_targeted": ["Deltoids", "Triceps", "Upper chest", "Core"],
            "difficulty": "Intermediate",
            "how_to": "Barbell or dumbbells at shoulders, press overhead, avoid leaning back",
            "sets_reps": "3-4 sets of 5-10 reps",
            "alternative": "Arnold press, seated dumbbell press"
        },
        "lunges": {
            "muscles_targeted": ["Quadriceps", "Hamstrings", "Glutes", "Calves", "Core"],
            "difficulty": "Beginner to Advanced",
            "how_to": "Step forward, lower back knee toward ground, front knee at 90°",
            "variations": ["Walking lunges", "Reverse lunges", "Side lunges", "Curtsy lunges", "Jump lunges"],
            "sets_reps": "3 sets of 10-15 steps per leg"
        },
        "bench_press": {
            "muscles_targeted": ["Pectoralis major", "Triceps", "Anterior deltoids"],
            "difficulty": "Intermediate",
            "how_to": "Feet planted, arch slight, bar to lower chest, press straight up",
            "sets_reps": "3-5 sets of 5-12 reps",
            "variations": ["Incline bench", "Decline bench", "Dumbbell bench", "Close-grip (triceps focused)"]
        },
        "dips": {
            "muscles_targeted": ["Triceps", "Lower chest", "Shoulders"],
            "difficulty": "Intermediate to Advanced",
            "how_to": "Straight arms on parallel bars, lower until shoulders below elbows, push up",
            "sets_reps": "3 sets of 8-15 reps",
            "beginner_alternative": "Bench dips or assisted dip machine"
        },
        "leg_press": {
            "muscles_targeted": ["Quads", "Hamstrings", "Glutes"],
            "difficulty": "Beginner to Intermediate",
            "how_to": "Feet shoulder-width on platform, lower until knees at 90°, press",
            "foot_positions": {
                "high_foot": "More glutes/hamstrings",
                "low_foot": "More quads",
                "wide_stance": "Inner thighs",
                "narrow_stance": "Outer quads"
            }
        },
        "crunches_variations": {
            "standard_crunch": {"reps": "3x15-20", "target": "Upper rectus abdominis"},
            "reverse_crunch": {"reps": "3x12-15", "target": "Lower abs"},
            "bicycle_crunch": {"reps": "3x20 each side", "target": "Obliques + rectus"},
            "toe_touches": {"reps": "3x15-20", "target": "Upper abs"}
        },
        "russian_twists": {
            "muscles_targeted": ["Obliques", "Deep core"],
            "difficulty": "Beginner to Advanced",
            "how_to": "Lean back slightly, feet lifted (optional), rotate torso side to side",
            "weight_progression": "Bodyweight → light dumbbell → medicine ball",
            "sets_reps": "3 sets of 12-20 each side"
        },
        "hip_thrusts": {
            "muscles_targeted": ["Glutes maximus/medius/minimus", "Hamstrings", "Core"],
            "difficulty": "Beginner to Advanced",
            "how_to": "Shoulders on bench, barbell across hips, drive through heels to lift hips",
            "sets_reps": "3-4 sets of 8-15 reps",
            "note": "Best glute activation exercise per EMG studies"
        },
        "farmer_walk": {
            "muscles_targeted": ["Forearms", "Traps", "Core", "Erectors", "Glutes"],
            "difficulty": "Beginner to Advanced",
            "how_to": "Heavy weight in each hand (or one hand for anti-lateral flexion), walk 20-50m",
            "sets_distance": "3-5 sets of 50m",
            "benefits": ["Grip strength", "Posture", "Carrying capacity", "Core stability"]
        },
        "face_pulls": {
            "muscles_targeted": ["Rear delts", "Traps", "Rotator cuff", "Rhomboids"],
            "difficulty": "Beginner",
            "how_to": "Cable at face height, pull rope toward temples, externally rotate shoulders",
            "sets_reps": "3-4 sets of 15-20 reps",
            "importance": "Critical for shoulder health and posture correction"
        }
    },
    
    "training_principles": {
        "progressive_overload": "Gradually increase weight, reps, or intensity to continue seeing results",
        "recovery": "Rest is when muscles grow and repair; ensure 7-9 hours sleep",
        "consistency": "Regular training (3-5 days/week) is more important than intense sporadic workouts",
        "form_over_ego": "Perfect form with lighter weight beats poor form with heavy weight",
        "periodization": "Vary training every 4-12 weeks to prevent plateaus"
    },
    
    "advanced_principles": {
        "periodization_cycles": {
            "macrocycle": "6-12 months (overall goal)",
            "mesocycle": "3-6 weeks (specific focus)",
            "microcycle": "1 week (daily/weekly plan)",
            "types": [
                "Linear periodization: increase intensity, decrease volume each week",
                "Undulating periodization: alternate heavy/light days within week",
                "Block periodization: focus on one quality (strength, hypertrophy, endurance) per block"
            ]
        },
        "deload_weeks": {
            "when": "Every 4-8 weeks of intense training",
            "how": "Reduce volume by 40-60% OR intensity by 10-20%",
            "duration": "5-7 days",
            "signs_you_need_one": "Persistent fatigue, plateau in lifts, poor sleep, irritability, joint pain"
        },
        "training_to_failure": {
            "definition": "Cannot perform another rep with good form",
            "when_to_use": "Last set of an exercise, not every set",
            "frequency": "1-2 times per muscle group per week",
            "warning": "Excessive failure training increases CNS fatigue and injury risk"
        },
        "conjugate_method": {
            "description": "Train multiple qualities (strength, speed, hypertrophy) in same week",
            "example": "Day 1: Max effort lower body | Day 2: Dynamic effort upper | Day 3: Hypertrophy lower | Day 4: Repetition upper",
            "best_for": "Advanced lifters, powerlifters, athletes"
        },
        "grease_the_groove": {
            "description": "Submaximal sets spread throughout day",
            "application": "Multiple sets of 40-60% of max reps, 50-80% of max weight",
            "rest": "15+ minutes between sets",
            "best_for": "Pull-ups, push-ups, pistol squats, skill work"
        }
    },
    
    "nutrition": {
        "macros": {
            "protein": {
                "function": "Muscle repair, enzyme production, hormone synthesis",
                "recommended_intake": {
                    "sedentary": "0.8g/kg bodyweight",
                    "recreational_fitness": "1.2-1.5g/kg",
                    "strength_training": "1.6-2.2g/kg",
                    "cutting/weight_loss": "2.0-2.4g/kg"
                },
                "sources": ["Chicken", "Fish", "Eggs", "Greek yogurt", "Tofu", "Lentils", "Whey/casein"],
                "timing": "Spread across 3-6 meals; 20-40g per serving"
            },
            "carbohydrates": {
                "function": "Primary energy source, glycogen replenishment",
                "types": ["Simple (fast energy)", "Complex (sustained energy)", "Fiber (digestion)"],
                "sources_complex": ["Oats", "Brown rice", "Quinoa", "Sweet potatoes", "Beans"],
                "sources_simple": ["Fruit", "Honey", "White rice (post-workout)"],
                "intake_by_activity": {
                    "light": "3-5g/kg",
                    "moderate": "5-7g/kg",
                    "high_volume": "7-10g/kg",
                    "endurance": "8-12g/kg"
                }
            },
            "fats": {
                "function": "Hormone production (testosterone, estrogen), vitamin absorption, cell membranes",
                "recommended": "20-35% of total calories",
                "sources_healthy": ["Avocado", "Nuts", "Olive oil", "Fatty fish", "Egg yolks", "Coconut oil"],
                "avoid": "Trans fats, excessive saturated fats, hydrogenated oils"
            }
        },
        "meal_timing": {
            "pre_workout": {
                "when": "1-3 hours before exercise",
                "what": "Carbs + moderate protein, low fat/low fiber",
                "examples": ["Banana + peanut butter", "Oatmeal + whey", "Rice cakes + turkey", "Apple + Greek yogurt"]
            },
            "post_workout": {
                "when": "Within 2 hours (optimal 30-60 min)",
                "what": "Protein + carbs for muscle repair and glycogen replenishment",
                "examples": ["Protein shake + banana", "Chicken + rice", "Chocolate milk", "Tuna sandwich"]
            },
            "pre_sleep": {
                "when": "30-60 min before bed",
                "what": "Slow-digesting protein (casein) benefits muscle repair overnight",
                "examples": ["Cottage cheese", "Greek yogurt", "Casein shake", "Milk + whey"]
            }
        },
        "hydration": {
            "daily_needs": "Male: ~3.7L, Female: ~2.7L total water (including food sources)",
            "during_exercise": "150-300mL every 15-20 minutes",
            "post_exercise_replacement": "1.25-1.5L per kg lost during exercise",
            "urine_color_gauge": "Pale yellow = hydrated; dark yellow/amber = dehydrated",
            "electrolyte_replacement": "For sessions >60 min or heavy sweating; sodium, potassium, magnesium"
        },
        "supplements_evidence_based": {
            "creatine_monohydrate": {
                "benefits": ["Strength +5-15%", "Muscle mass", "High-intensity performance", "Cognitive benefits"],
                "dosing": "3-5g daily (maintenance); 20g/day for 5-7 days (loading optional)",
                "safety": "Most studied supplement; safe for long-term use",
                "who_benefits": "Strength athletes, vegetarians, older adults"
            },
            "whey_protein": {
                "benefits": ["Convenient protein source", "Fast absorption", "Leucine-rich (MPS trigger)"],
                "dosing": "20-40g post-workout or as needed to meet daily intake",
                "types": ["Concentrate (cheaper, some lactose)", "Isolate (purer, faster)", "Hydrolysate (pre-digested)"]
            },
            "caffeine": {
                "benefits": ["Reduced perceived effort", "Increased focus", "Fat oxidation"],
                "dosing": "3-6mg/kg bodyweight 45-60 min pre-workout",
                "caution": "Tolerance builds; avoid afternoon doses for sleep"
            },
            "beta_alanine": {
                "benefits": ["Buffers lactic acid", "Improves 60-240 sec performance (400m run, rowing, high-rep sets)"],
                "dosing": "2-5g daily (consistent for 4-8 weeks for saturation)",
                "side_effect": "Harmless tingling (paresthesia) for 15-20 min"
            },
            "omega_3_fish_oil": {
                "benefits": ["Reduces inflammation", "Joint health", "Cardiovascular", "Mood"],
                "dosing": "1-3g combined EPA/DHA daily",
                "note": "Especially useful for high-volume training"
            },
            "vitamin_d": {
                "dosing": "1000-4000 IU daily if deficient",
                "importance": "Bone health, immune function, muscle function",
                "who_needs": "Indoor workers, high latitudes, dark skin"
            }
        }
    },
    
    "recovery": {
        "sleep_optimization": {
            "athlete_needs": "8-10 hours nightly (more than general population)",
            "stages_importance": {
                "deep_sleep": "Growth hormone release, physical repair",
                "REM_sleep": "Motor skill consolidation, learning"
            },
            "sleep_hygiene": [
                "Consistent sleep/wake times (±30 min)",
                "Dark, cool room (18-20°C)",
                "No screens 60-90 min before bed",
                "No caffeine within 8-10 hours of bed",
                "No alcohol before bed (disrupts REM)",
                "Wind-down routine (reading, stretching, breathing)"
            ],
            "napping": {
                "power_nap": "10-20 minutes (alertness)",
                "full_cycle": "90 minutes (includes deep sleep)",
                "best_time": "Between 1-4 PM"
            }
        },
        "active_recovery": {
            "definition": "Low-intensity movement on rest days",
            "examples": [
                "Walking 20-40 min",
                "Light cycling (zone 1-2 heart rate)",
                "Swimming at conversational pace",
                "Yoga/stretching (60-70% effort)",
                "Mobility drills"
            ],
            "benefits": ["Flushes metabolic waste", "Reduces muscle soreness", "Maintains movement patterns"]
        },
        "passive_recovery": {
            "definition": "Complete rest",
            "when_needed": ["After extremely intense sessions", "When sick/injured", "During deload weeks"],
            "benefits": ["CNS restoration", "Full tissue repair"]
        },
        "modalities": {
            "foam_rolling": {
                "best_for": "General tightness, muscle knots (trigger points)",
                "how_to": "Slow rolling (1-2cm/second), pause at tender spots 20-30 seconds",
                "cautions": "Avoid direct joint rolling, bony areas, acute injuries"
            },
            "stretching_types": {
                "static": "Hold 15-60 seconds; best post-workout",
                "dynamic": "Active movement through range; best pre-workout",
                "pnf": "Contract-relax method; best for flexibility gains"
            },
            "cold_therapy": {
                "ice_bath": "10-15 minutes at 10-15°C; reduces inflammation",
                "cold_shower": "2-5 minutes; less intense alternative",
                "timing": "Immediately post intense session for inflammatory reduction",
                "note": "May blunt hypertrophy if used immediately after strength training"
            },
            "heat_therapy": {
                "sauna": "15-20 minutes post-workout; improves circulation, relaxation",
                "warm_bath": "Epsom salts (magnesium absorption) for muscle relaxation",
                "benefits": "Reduces stiffness, increases blood flow, mental relaxation"
            },
            "massage": {
                "sports_massage": "Once weekly for high-volume athletes",
                "self_massage": "Using lacrosse ball, stick, or massage gun",
                "frequency": "Maintenance: 2-4 weeks; Deep tissue: as needed"
            }
        }
    },
    
    "injury_prevention": {
        "common_aches": {
            "lower_back_pain": {
                "causes": ["Weak glutes/core", "Poor deadlift/squat form", "Sitting posture"],
                "prevention": ["Hip thrusts", "Bird-dogs", "Dead bugs", "Glute bridges", "Cat-cow stretches"],
                "red_flags": "Radiating leg pain, numbness, loss of bladder control → see doctor"
            },
            "knee_pain": {
                "causes": ["Weak quads/glutes", "Tight hamstrings/IT band", "Running form issues"],
                "prevention": ["Quad sets", "Clamshells", "Straight leg raises", "Walking lunges (light weight)"],
                "exercise_avoid_during_pain": ["Deep squats", "Leg extensions", "Plyometrics"]
            },
            "shoulder_pain": {
                "causes": ["Overhead pressing form", "Weak rotator cuff", "Poor scapular control"],
                "prevention": ["Face pulls", "External rotations", "Wall slides", "YTW raises"],
                "avoid_if_painful": "Upright rows, behind-neck presses, excessive dips"
            },
            "shin_splints": {
                "causes": ["Sudden running increase", "Poor footwear", "Overstriding", "Weak tibialis anterior"],
                "prevention": ["Toe raises", "Calf stretches", "Proper shoe fitting", "Gradual mileage increase 10%/week"],
                "treatment": "Rest, ice, compression, heel walking, arch support"
            },
            "elbow_pain_tennis_golfers": {
                "lateral_epicondylitis": "Pain outside elbow; from wrist extension (pull-ups, carrying)",
                "medial_epicondylitis": "Pain inside elbow; from wrist flexion (curls)",
                "prevention": ["Wrist curls (light eccentric)", "Grip strength training", "Form check"]
            }
        },
        "injury_risk_factors": [
            "Sudden volume increase >10-20% per week",
            "Skipping warm-up or cool-down",
            "Poor sleep (increases injury risk 1.5-2x)",
            "Previous injury (reinjury risk higher)",
            "Muscle imbalances (e.g., strong quads, weak hamstrings)"
        ],
        "warm_up_protocol": {
            "general": "5-10 minutes low-intensity (jump rope, elliptical)",
            "dynamic_stretches": ["Leg swings", "Arm circles", "Torso twists", "Walking lunges", "High knees"],
            "activation": ["Glute bridges", "Band pull-aparts", "Dead bugs", "Bird-dogs", "Scapular push-ups"],
            "sport_specific": "Light versions of main exercises (e.g., squat with empty bar)"
        },
        "cool_down_protocol": {
            "light_cardio": "3-5 minutes to gradually lower heart rate",
            "static_stretches": "Hold each 15-30 seconds, no bouncing (hamstring, quad, chest, back)",
            "myofascial_release": "Optional foam rolling session 5-10 min",
            "hydrate": "Replenish fluids"
        }
    },
    
    "tracking": {
        "objective_metrics": {
            "strength_tracking": [
                "One-rep max (1RM) for key lifts every 4-8 weeks",
                "Reps at given weight (e.g., squat 100kg × 8 → 100kg × 12 = progress)",
                "Volume load = weight × sets × reps"
            ],
            "body_composition": [
                "Scale weight (weigh same time daily, weekly average)",
                "Waist circumference (better health marker than BMI)",
                "Body fat % (calipers, DEXA, bioimpedance scales - trend matters more than absolute)",
                "Progress photos (front, side, back; same lighting, pose, time)",
                "How clothes fit"
            ],
            "cardiovascular": [
                "Resting heart rate (lower = fitter; normal 60-100 → athlete 40-60)",
                "Heart rate recovery (drop in 1 min post-exercise; >20 bpm = good)",
                "Timed distance (e.g., 5 km run time, 500m row)",
                "VO2 max estimate (from treadmill or field tests)"
            ],
            "mobility_flexibility": [
                "Sit-and-reach test (hamstring/lower back)",
                "Overhead squat depth",
                "Shoulder rotation range",
                "Ankle dorsiflexion measurement"
            ]
        },
        "subjective_metrics": {
            "rate_of_perceived_exertion_RPE": {
                "1-10 scale": "1 = very easy (sitting), 5 = moderate (conversational), 10 = maximal effort",
                "usage": "For cardio (RPE 3-6 for easy, RPE 7-9 for hard), Strength (RPE 7-9 for working sets)"
            },
            "session_RPE_sRPE": "Rate whole session effort (1-10) × minutes = training load score (TRIMP estimate)",
            "sleep_quality": "1-5 daily rating",
            "energy_levels": "Morning energy and workout energy (1-10)",
            "muscle_soreness": "1-10 (DOMS score), map location",
            "mood_motivation": "1-10 before/during workout"
        },
        "periodic_tests": {
            "every_2_weeks": "Body weight, waist circumference",
            "every_4_weeks": "1 rep max test (or RM estimation), timed mile, max push-ups in 1 min",
            "every_8_weeks": "Body fat %, progress photos, resting heart rate",
            "every_12_weeks": "Re-assess goals, reset routine (periodization shift)"
        },
        "common_apps_tools": {
            "free": ["Google Sheets (custom tracker)", "Strong (workout log)", "Strava (running/cycling)", "MyFitnessPal (nutrition)"],
            "paid": ["Whoop (recovery)", "Training Peaks (advanced programming)", "MacroFactor (nutrition/diet adherence)"]
        }
    },
    
    "psychology": {
        "behavioral_strategies": {
            "implementation_intention": "If/when [situation], then I will [action]. Example: 'If it's Monday 7 AM, then I will put on gym clothes'",
            "habit_stacking": "Attach new exercise habit to existing one: 'After I brush my teeth, I will do 10 push-ups'",
            "temptation_bundling": "Pair workout with something enjoyable: listen to favorite podcast only at gym",
            "environment_design": [
                "Lay out workout clothes night before",
                "Sleep in workout clothes if morning exerciser",
                "Pack gym bag and put by door"
            ]
        },
        "motivation_types": {
            "intrinsic": "Enjoy the process, feel good during/after, sense of accomplishment → most sustainable",
            "extrinsic": "External rewards (weight loss, competition, praise) → useful for starting",
            "build_intrinsic": [
                "Focus on how exercise makes you feel (more energy, less stress)",
                "Set process goals (consistency, form) not just outcome goals",
                "Find activities you genuinely enjoy"
            ]
        },
        "overcoming_common_mental_blocks": {
            "no_time": "20-minute HIIT beats nothing; 10-min workout is legitimate; morning workouts are rarely interrupted",
            "no_motivation": "The 5-minute rule: commit to 5 minutes only; often you'll continue after starting",
            "intimidation": "Go during off-hours, start with cardio you know, use beginner classes, everyone started somewhere",
            "perfectionism": "'Something' beats 'nothing'; imperfect workout still counts; missed day? just resume tomorrow",
            "boredom": "Switch modalities every 4 weeks, workout with friend, try new class, set monthly challenges"
        },
        "habit_formation_timeline": {
            "days_1_21": "Need consistent cues and rewards; hardest phase",
            "days_22_66": "Automaticity building; less mental effort needed",
            "beyond_66": "Habit ingrained; missing a day feels uncomfortable",
            "accelerating_habit": "Same time, same place, same preparation routine every time"
        },
        "goal_setting_SMART_examples": {
            "specific": "I will squat 100kg for 5 reps",
            "measurable": "Track via video or gym logs",
            "achievable": "From 80kg current → 100kg in 12 weeks (5% increase every 2-3 weeks)",
            "relevant": "Matches goal of strength gain",
            "time_bound": "By March 31st",
            "example_bad": "I want to get fitter",
            "example_good_SMART": "I will run 5 km in under 28 minutes by doing Couch to 5K program (3 runs/week) in 9 weeks"
        }
    },
    
    "faqs": {
        "q_morning_vs_evening_workout": {
            "answer": "The best time is when you can be consistent. Morning: fewer distractions, may improve sleep, but might have lower body temp. Evening: might have more strength/power (peak 4-8 PM), can relieve daily stress, but can interfere with sleep if too close to bedtime. Test both."
        },
        "q_how_long_to_see_results": {
            "answer": {
                "mood/sleep/energy": "Immediately to 1-2 weeks",
                "strength_beginner": "2-4 weeks (neural adaptations)",
                "visible_muscle_growth": "8-12 weeks (with proper nutrition)",
                "weight_loss": "4-6 weeks of consistent deficit",
                "cardio_fitness_metrics": "6-10 weeks (resting HR, VO2 max)"
            }
        },
        "q_cardio_before_or_after_weights": {
            "answer": {
                "goal_strength_muscle": "Weights first (cardio fatigues before lifting)",
                "goal_endurance": "Cardio first",
                "separate_sessions": "Optimal for both qualities (e.g., AM cardio, PM weights)",
                "same_session_recommendation": "Weights first, then cardio (20 min max) to avoid interference"
            }
        },
        "q_should_i_exercise_every_day": {
            "answer": "No. Rest days are essential. Structured 5-6 days training + 1-2 rest/active recovery days is optimal for most. Overtraining signs: persistent fatigue, performance drop, insomnia, irritability, elevated resting HR."
        },
        "q_home_gym_minimal_equipment": {
            "essentials_under_100usd": "Resistance bands (various tensions) + jump rope + yoga mat",
            "essentials_under_300usd": "Adjustable dumbbells (10-50 lbs) + pull-up bar or doorway suspension trainer (TRX style)",
            "essentials_under_500usd": "Add a foldable bench + kettlebell (16-24kg)",
            "full_routine_possible": "Squats, lunges, rows, presses, deadlifts, pull-ups, planks with above"
        },
        "q_female_training_different_male": {
            "answer": "Fundamental principles (progressive overload, consistency, nutrition) are identical. Differences: women may have greater fatigue resistance, recover faster between sets, need same protein per kg, but may benefit from cycle phase tracking (follicular = strength potential, luteal = endurance focus). No need for different exercises."
        },
        "q_how_break_plateau": {
            "strategies": [
                "Deload for 1 week (reduce volume/intensity 40-60%)",
                "Change rep ranges (strength 1-5 → hypertrophy 8-12 → endurance 15+)",
                "Add 2-5% more weight",
                "Increase weekly volume by 10-20%",
                "Add 1-2 more sets per exercise",
                "Reduce rest periods (e.g., 90 sec → 45 sec)",
                "Try new variation (barbell squat → front squat)",
                "Check diet (adequate protein + calories)",
                "Check sleep (7+ hours)"
            ]
        },
        "q_muscle_soreness_good_or_bad": {
            "answer": "Mild to moderate DOMS (delayed onset muscle soreness) 24-72 hours after new/intense exercise is normal and indicates muscle adaptation. Severe soreness that limits movement, sharp pain, or pain lasting >5-7 days may indicate injury. Extreme muscle swelling + dark urine = rhabdomyolysis (medical emergency)."
        },
        "q_can_i_spot_reduce_fat": {
            "answer": "No. Fat loss occurs systemically, not from exercising a specific area. You cannot target belly fat with crunches or arm fat with triceps extensions. Genetics determine where you lose fat first. Create a calorie deficit + full-body strength training + patience."
        },
        "q_walking_enough_exercise": {
            "answer": "Walking is excellent exercise and often underrated. It improves health, steps, recovery, and calorie burn. For many people, 7,000-10,000 steps/day is a strong baseline, but walking alone may not build much muscle or maximal fitness. Combine it with strength training for best results."
        },
        "q_rest_days_needed": {
            "answer": "Yes. Rest days are productive days because recovery drives adaptation. Most people do well with 3-5 training days plus 1-2 rest or active recovery days each week. If performance, sleep, or motivation drops, you likely need more recovery."
        },
        "q_muscle_soreness": {
            "answer": "Mild soreness after new or hard training is normal. It usually peaks 24-72 hours and fades within a few days. Sharp pain, joint pain, swelling, or soreness that keeps getting worse is a red flag. Active recovery, walking, sleep, hydration, and light movement help."
        },
        "q_hiit_vs_liss": {
            "answer": "HIIT is time-efficient and great for conditioning, but it is more fatiguing. LISS or steady-state cardio is easier to recover from and better for building a base. Most people do best with a mix: a few low-intensity sessions plus 1-3 HIIT sessions depending on goals and recovery."
        }
    }
}

# ============================================
# FITNESS RESPONSES (for assistant use)
# ============================================

FITNESS_RESPONSES = {
    "beginner_routine": {
        "intro": "Great! Here's a beginner-friendly workout routine:",
        "routine": [
            "Monday: 20 min cardio (walking, cycling, or swimming)",
            "Tuesday: Full body strength (15 min with bodyweight exercises)",
            "Wednesday: Rest or 15 min yoga",
            "Thursday: 20 min cardio",
            "Friday: Full body strength (15 min)",
            "Saturday: Rest or light activity",
            "Sunday: Rest"
        ],
        "tips": [
            "Warm up for 5 minutes before each session",
            "Cool down and stretch for 5 minutes after",
            "Stay hydrated throughout the day",
            "Gradually increase intensity over 4-6 weeks"
        ]
    },
    "goal_specific": {
        "weight_loss": {
            "strategy": "Create calorie deficit with cardio + strength training",
            "weekly_routine": ["3-4 cardio sessions (30-45 min each)", "2-3 strength sessions (30 min each)"],
            "key_points": ["Combine exercise with proper diet", "Don't cut calories too drastically", "Include both steady-state and HIIT cardio"]
        },
        "muscle_gain": {
            "strategy": "Progressive strength training with adequate nutrition",
            "weekly_routine": ["4-5 strength training sessions", "1-2 light cardio sessions"],
            "key_points": ["Focus on compound exercises", "Progressive overload is crucial", "Eat in calorie surplus"]
        },
        "endurance": {
            "strategy": "Gradual increase in cardio capacity",
            "weekly_routine": ["3-4 cardio sessions with varying intensity", "1-2 strength sessions"],
            "key_points": ["Build base with steady-state cardio", "Add interval training gradually", "Recovery is important"]
        },
        "athletic_performance_overall": {
            "strategy": "Balance strength, speed, agility, mobility",
            "weekly_routine": {
                "Monday": "Power: Olympic lifts or plyometrics",
                "Tuesday": "Strength: Upper + core",
                "Wednesday": "Agility: Ladder drills, cone drills + cardio",
                "Thursday": "Strength: Lower + core", 
                "Friday": "Speed: Sprints, interval training",
                "Saturday": "Active recovery: Swimming, yoga",
                "Sunday": "Rest"
            }
        },
        "rehabilitation_after_break": {
            "strategy": "Very gradual progression, focus on form and mobility",
            "weeks_1_3": ["2-3x/week: 15-20 min low-impact cardio (walking, elliptical)", "Light stretching daily", "No heavy resistance"],
            "weeks_4_6": ["3x/week: Add bodyweight exercises (partial ROM)", "4x/week: Cardio 20-25 min"],
            "weeks_7_9": ["4x/week: Full body resistance (light-medium intensity)", "Interval training 1x/week"],
            "months_4_6": "Return to previous routine at 70-80% volume"
        },
        "body_recomposition_loss_fat_gain_muscle": {
            "strategy": "Calorie deficit moderate with high protein (2.0-2.4g/kg)",
            "weekly_split": {
                "strength": "4x/week heavy compound lifts",
                "cardio": "2x/week moderate; 1x/week HIIT",
                "active_recovery": "1 day walking/light yoga"
            },
            "key_points": [
                "Progress photos > scale weight",
                "Maintain or increase lifts (fat loss + muscle gain possible for beginners/intermediates)",
                "Sleep 7+ hours critical"
            ]
        },
        "marathon_ultra_endurance": {
            "strategy": "Periodized running plan with strength support",
            "weekly_components": [
                "Long run (25-35% of weekly mileage)",
                "Tempo run (comfortably hard)",
                "Interval/speed work",
                "Easy recovery runs",
                "Strength training 2x/week (focus: injury prevention)"
            ],
            "strength_focus": "Single-leg work, glutes, core, hips",
            "taper": "3 weeks before race: reduce volume 20-30% each week"
        },
        "senior_fitness_50_plus": {
            "strategy": "Maintain mobility, bone density, balance",
            "principles": [
                "Lower impact preferred (swimming, cycling, elliptical, walking)",
                "Focus on functional strength (chairs, groceries, stairs)",
                "Balance training 2-3x/week (prevents falls)",
                "Flexibility work including neck, hips, ankles"
            ],
            "weekly_example": {
                "Mon": "Walking 30 min + balance exercises",
                "Tue": "Strength (light weights or bodyweight)",
                "Wed": "Swimming or water aerobics 30 min",
                "Thu": "Rest or gentle yoga",
                "Fri": "Strength (different exercises)",
                "Sat": "Walking 40 min + stretching",
                "Sun": "Rest"
            },
            "special_note": "Consult doctor before starting; warm up longer (10-15 min)"
        },
        "busy_professional_limited_time": {
            "strategy": "High intensity, minimal equipment, time-efficient",
            "typical_session": "20-25 minutes, 3-5x/week",
            "sample_20_min_workout": [
                "2 min warm-up: jumping jacks, high knees",
                "Circuit (repeat 4x): 40 sec work, 20 sec rest",
                "- Squats or goblet squats",
                "- Push-ups or incline push-ups",
                "- Lunges or reverse lunges",
                "- Plank or mountain climbers",
                "- Rows (using resistance band or bottles)",
                "2 min cool-down: stretches"
            ],
            "key": "Compound exercises, supersets, minimal rest"
        }
    }
}