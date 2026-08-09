from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

MODEL_PATH = PROJECT_ROOT / "models"
CONFIG_PATH = PROJECT_ROOT / "config"
DATASET_PATH = PROJECT_ROOT / "Dataset"
DATA_PATH = PROJECT_ROOT / "data"

def get_project_root() -> Path:
    """Dynamically finds the project root directory regardless of execution context."""
    try:
        curr = Path(__file__).resolve().parent
    except NameError:
        curr = Path().resolve()
    
    for p in [curr] + list(curr.parents):
        if (p / "config").exists() and (p / "models").exists():
            return p
    return PROJECT_ROOT