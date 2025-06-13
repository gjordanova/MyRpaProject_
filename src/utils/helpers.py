import os
from datetime import datetime

def get_output_paths():
    today = datetime.today().strftime("%Y-%m-%d")
    base = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    raw_dir = os.path.join(base, "outputs", "raw")
    proc_dir = os.path.join(base, "outputs", "processed")
    rep_dir = os.path.join(base, "outputs", "reports")
    os.makedirs(raw_dir, exist_ok=True)
    os.makedirs(proc_dir, exist_ok=True)
    os.makedirs(rep_dir, exist_ok=True)
    return {
        "raw": os.path.join(raw_dir, f"books_{today}.json"),
        "processed": os.path.join(proc_dir, f"processed_books_{today}.csv"),
        "report": os.path.join(rep_dir, f"report_{today}.html"),
    }

def save_raw(data, path):
    import json
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
