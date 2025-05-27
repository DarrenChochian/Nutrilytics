import json

file_path = 'improved_synthetic_recipes.jsonl'

with open(file_path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f, 1):
        try:
            data = json.loads(line)
            if not data['prompt'].strip() or not data['completion'].strip():
                print(f"⚠️ Empty field at line {i}: {data}")
        except json.JSONDecodeError:
            print(f"❌ JSON error at line {i}")
