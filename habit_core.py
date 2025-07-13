# habit_core.py
import json
from datetime import date
from pathlib import Path

DATA_FILE = Path(__file__).with_name("data.json")

HABITS = ["3 sets", "Learning", "Eat well"]

def ask_yes_no(question):
    ans = input(f"{question} (y/n) ")
    return ans.strip().lower() == "y"

def run_cli():
    print("Welcome to Habit Tracker!")
    results = []
    for h in HABITS:
        results.append({"habit": h, "done": ask_yes_no(f"Did you do '{h}' today?")})

    save_result(results)

    total   = len(results)
    success = sum(1 for r in results if r["done"])
    print(f"You completed {success}/{total} habits today.")

def save_result(today_results):
    if DATA_FILE.exists():
        with DATA_FILE.open(encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = []

    data.append({"date": str(date.today()), "results": today_results})
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

# lets you keep the old behaviour for now:
if __name__ == "__main__":
    run_cli()
