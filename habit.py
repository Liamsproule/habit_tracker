import json
from pathlib import Path
from datetime import date

print("Welcome to Habit Tracker!")

HABITS = ["3 sets", "Learning", "Eat well"]

results = []
for h in HABITS:
    ans = input(f"Did you do '{h}' today? (y/n) ")
    results.append({"habit": h, "done": ans.lower() == "y"})


DATA_FILE = Path("data.json")

def save_result(today_results):
    if DATA_FILE.exists():
        with DATA_FILE.open() as f:
            data = json.load(f)
    else:
        data = []

    data.append({"date": str(date.today()), "results": today_results})

    with DATA_FILE.open("w") as f:
        json.dump(data, f, indent=2)

save_result(results)
total   = len(results)
success = sum(1 for r in results if r["done"])
print(f"You completed {success}/{total} habits today.")
