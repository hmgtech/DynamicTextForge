import json
from pathlib import Path

def load_json_file(file_path: Path) -> dict:
    """Load JSON data from a file."""
    try:
        with file_path.open('r', encoding="utf8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return {}
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON file at {file_path}: {e}")
        return {}

def save_json_file(data: dict, file_path: Path) -> None:
    """Save data as JSON to a file."""
    try:
        with file_path.open('w', encoding='utf-8') as output_file:
            json.dump(data, output_file, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"Error writing to file {file_path}: {e}")

def ensure_directory_exists(directory: Path) -> None:
    """Ensure the directory exists, create if it doesn't."""
    try:
        if not directory.exists():
            directory.mkdir(parents=True, exist_ok=True)
    except IOError as e:
        print(f"Error creating directory {directory}: {e}")

def create_text_mapping(extracted_json, replaced_json):
    """Create a mapping of text from the extracted JSON to the replaced JSON."""
    try:
        text_mapping = {}
        for ext_section, rep_section in zip(extracted_json, replaced_json):
            for ext_content, rep_content in zip(ext_section['content'], rep_section['content']):
                text_mapping[ext_content['text']] = rep_content['text']
        return text_mapping
    except KeyError as e:
        print(f"KeyError occurred: {e}")
        return {}
