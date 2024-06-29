import json
from pathlib import Path

from core.generative_ai import GenerativeAI
from core.text_extractor import TextExtractor
from core.text_replacer import TextReplacer

from config import INPUT_JSON_PATH, OUTPUT_DIR, EXTRACTED_TEXT_PATH, REPLACED_TEXT_PATH, GENAI_API_KEY, GENAI_MODEL_NAME
from utils import load_json_file, save_json_file, ensure_directory_exists

def extract_text_from_json(json_data: dict) -> dict:
    """Extract text from JSON data."""
    extractor = TextExtractor()
    return extractor.extract_text(json_data)

def replace_text_with_generative_ai(extracted_text: dict) -> dict:
    """Replace text using GenerativeAI."""
    if not GENAI_API_KEY:
        raise ValueError("API_KEY environment variable is not set.")
    
    generative_ai = GenerativeAI(api_key=GENAI_API_KEY, model_name=GENAI_MODEL_NAME)
    generative_ai.configure()
    
    text_replacer = TextReplacer(json_data=extracted_text, generative_ai=generative_ai)
    return text_replacer.rephrase_section()

def main():
    try:
        # Ensure the output directory exists
        ensure_directory_exists(OUTPUT_DIR)

        # Load the JSON data
        json_data = load_json_file(INPUT_JSON_PATH)
        if not json_data:
            raise ValueError(f"No data found in {INPUT_JSON_PATH}")

        # Extract text and save to file
        extracted_text = extract_text_from_json(json_data)
        save_json_file(extracted_text, EXTRACTED_TEXT_PATH)
        print(f"Extracted text saved to {EXTRACTED_TEXT_PATH}")

        # Replace text and save to file
        replaced_text = replace_text_with_generative_ai(extracted_text)
        save_json_file(replaced_text, REPLACED_TEXT_PATH)
        print(f"Replaced text saved to {REPLACED_TEXT_PATH}")

    except FileNotFoundError as fnf_error:
        print(f"FileNotFoundError: {fnf_error}. Please check if the file exists or the path is correct.")
    except json.JSONDecodeError as json_error:
        print(f"JSONDecodeError: {json_error}. Check if the JSON file is valid.")
    except ValueError as value_error:
        print(f"ValueError: {value_error}. Please ensure environment variables are set correctly.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}. Please review the code for issues.")

if __name__ == "__main__":
    main()
