import json
from pathlib import Path

def load_json_file(file_path: Path) -> dict:
    """Load JSON data from a file."""
    with file_path.open('r', encoding="utf8") as file:
        return json.load(file)

def save_json_file(data: dict, file_path: Path) -> None:
    """Save data as JSON to a file."""
    with file_path.open('w', encoding='utf-8') as output_file:
        json.dump(data, output_file, ensure_ascii=False, indent=4)

def ensure_directory_exists(directory: Path) -> None:
    """Ensure the directory exists, create if it doesn't."""
    if not directory.exists():
        directory.mkdir(parents=True, exist_ok=True)
