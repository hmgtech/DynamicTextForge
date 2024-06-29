from pathlib import Path
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Constants for paths
BASE_DIR = Path(__file__).resolve().parent
INPUT_JSON_PATH = BASE_DIR / 'input' / 'test.json'
OUTPUT_DIR = BASE_DIR / 'output'
EXTRACTED_TEXT_PATH = OUTPUT_DIR / 'extracted_text.json'
REPLACED_TEXT_PATH = OUTPUT_DIR / 'replaced_text_checkpoint.json'
REPLACED_WITH_ORIGINAL_JSON_PATH = BASE_DIR / 'output' / 'replaced_text_with_original.json'

# Constants for Generative AI
GENAI_API_KEY = os.getenv("GOOGLE_GEMINI_API_KEY")
GENAI_MODEL_NAME = 'gemini-1.5-flash'
