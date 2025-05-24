import openai
import json
import random
import time

openai.api_key = "your-openai-api-key"  # Replace with your actual API key

# Example restrictions and meal types (add more for variety)
dietary_restrictions = [
    "vegan", "gluten-free", "keto", "nut-free",
    "dairy-free", "low-sugar", "vegetarian", "pescatarian"
]

meal_types = ["breakfast", "lunch", "dinner", "snack", "dessert"]

# Output file
output_file = "synthetic_recipes.jsonl"
samples_to_generate = 10000

# Temperature controls creativity (0.7 is balanced)
temperature = 0.7
max_tokens = 300

for i in range(samples_to_generate):
    restriction = random.choice(dietary_restrictions)
    meal = random.choice(meal_types)

    # Create a natural user-style prompt
    prompt = f"I follow a {restriction} diet. Can you recommend a {meal}?"

    try:
        # Generate response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens
        )

        completion = response.choices[0].message.content.strip()

        # Format for fine-tuning
        record = {
            "prompt": prompt,
            "completion": " " + completion  # space prefix for fine-tuning
        }

        # Append to file
        with open(output_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(record) + "\n")

        # Log progress
        if (i + 1) % 100 == 0:
            print(f"{i + 1} / {samples_to_generate} samples generated...")

        time.sleep(0.5)  # Avoid rate limit issues

    except Exception as e:
        print(f"Error at sample {i + 1}: {e}")
        time.sleep(2)  # Wait before retrying
