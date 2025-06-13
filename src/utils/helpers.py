import os
from datetime import datetime

def get_output_paths(base_folder: str = None) -> dict:
    """
    Returns a dict with absolute paths for raw, processed and report outputs,
    and creates those folders if they don’t exist.
    """
    # 1) Where do we store? Defaults to PROJECT_ROOT/outputs
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    outputs_root = base_folder or os.path.join(project_root, "outputs")

    # 2) Create subfolders
    raw_dir       = os.path.join(outputs_root, "raw")
    processed_dir = os.path.join(outputs_root, "processed")
    reports_dir   = os.path.join(outputs_root, "reports")

    for d in (raw_dir, processed_dir, reports_dir):
        os.makedirs(d, exist_ok=True)

    # 3) Build filepaths
    today = datetime.today().strftime("%Y-%m-%d")
    return {
        "raw":       os.path.join(raw_dir,        f"books_{today}.csv"),
        "processed": os.path.join(processed_dir,  f"processed_{today}.csv"),
        "report":    os.path.join(reports_dir,    f"report_{today}.html"),
    }
