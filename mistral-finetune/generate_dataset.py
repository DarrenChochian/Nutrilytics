import json, pathlib

PROJECT_DIR = pathlib.Path(__file__).resolve().parent          # …\mistral-finetune
DATA_DIR    = PROJECT_DIR / "dataset"
DATA_DIR.mkdir(exist_ok=True)

out_file = DATA_DIR / "dataset.json"

data = [
    {
        "instruction": "Turn this into a question.",
        "input": f"This is synthetic sentence number {i}.",
        "output": f"What is synthetic sentence number {i}?"
    }
    for i in range(10_000)
]

with out_file.open("w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print(f"✅  Wrote {len(data)} samples to {out_file}")
