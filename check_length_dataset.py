import json
import tiktoken

enc = tiktoken.encoding_for_model("gpt-3.5-turbo")
file_path = "improved_synthetic_recipes.jsonl"

too_long_count = 0
total_count = 0

with open(file_path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f, 1):
        data = json.loads(line)
        completion_tokens = len(enc.encode(data['completion']))
        if completion_tokens > 1000:
            print(f"Line {i} completion too long: {completion_tokens} tokens")
            too_long_count += 1
        total_count += 1

print(f"\n✅ Done checking {total_count} completions.")
if too_long_count == 0:
    print("All completions are within the acceptable token limit. 🎉")
else:
    print(f"{too_long_count} completions exceeded the token limit.")
