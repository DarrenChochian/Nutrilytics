import json
import random
import time
from openai import OpenAI
import os
from dotenv import load_dotenv


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


dietary_restrictions = [
    "vegan", "vegetarian", "pescatarian", "gluten-free", "dairy-free", "nut-free",
    "egg-free", "soy-free", "low-sugar", "low-sodium", "keto", "paleo", "halal", "kosher",
    "low-carb", "high-protein", "diabetic-friendly", "heart-healthy", "anti-inflammatory",
    "low-FODMAP", "raw", "whole30", "Mediterranean", "plant-based", "lactose-intolerant",
    "sugar-free", "wheat-free", "corn-free", "shellfish-free", "peanut-free", "tree-nut-free",
    "nightshade-free", "low-cholesterol", "renal-diet", "macrobiotic", "alkaline",
    "clean-eating", "organic", "locally-sourced", "non-GMO", "MSG-free", "preservative-free",
    "low-fat", "zero-fat", "high-fiber", "low-fiber", "fructose-free", "casein-free",
    "histamine-free", "glucose-free", "carnivore", "flexitarian", "dairy-limited", 
    "spice-sensitive", "fermentation-free", "grain-free", "oat-free", "barley-free", 
    "rye-free", "celiac-safe", "gastroparesis-friendly", "ulcer-friendly", "acid-reflux-safe", 
    "GERD-safe", "gallbladder-safe", "sulfite-free", "salicylate-free", "low-purine", 
    "low-oxalate", "low-tyramine", "low-histamine", "low-lectin", "lectin-free"
]

meal_types = ["breakfast", "lunch", "dinner", "snack", "dessert"]

output_file = "improved_synthetic_recipes.jsonl"
samples_to_generate = 10000  # updated to 10,000 samples

temperature = 0.7
max_tokens = 350

def format_restrictions(restrictions):
    if len(restrictions) == 1:
        return restrictions[0]
    elif len(restrictions) == 2:
        return f"{restrictions[0]} and {restrictions[1]}"
    else:
        return ", ".join(restrictions[:-1]) + f", and {restrictions[-1]}"

print("Script started...")
print(f"Generating {samples_to_generate} synthetic recipes...")

for i in range(samples_to_generate):
    try:
        restrictions = random.sample(dietary_restrictions, k=random.randint(1, len(dietary_restrictions)))
        restriction_text = format_restrictions(restrictions)
        meal = random.choice(meal_types)

        prompt = (
            f"I follow a diet that is {restriction_text}. "
            f"Can you recommend a {meal} recipe that meets all of these dietary restrictions? "
            "Please be specific and detailed."
        )

        print(f"[Sample {i+1}] Prompt: {prompt[:60]}...")

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens
        )

        completion = response.choices[0].message.content.strip()

        record = {
            "prompt": prompt,
            "completion": " " + completion
        }

        with open(output_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(record) + "\n")

        print(f"[Sample {i+1}] Completed and saved.")
        time.sleep(1)  # delay to avoid rate limits

    except Exception as e:
        print(f"[Sample {i+1}] Error: {e}")
        print("Retrying in 3 seconds...")
        time.sleep(3)
        continue

print("Script finished.")
