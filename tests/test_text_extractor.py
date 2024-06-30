import unittest
import json
import os
import sys
import logging
from pathlib import Path


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core import text_extractor
from utils import (
    load_json_file
)

class TestTextExtractor(unittest.TestCase):
    """
    Unit tests for validating the functionality of TextExtractor class.

    This test case verifies the extraction of structured content from JSON data,
    specifically testing scenarios where sections and their content are extracted
    correctly according to expected formats.
    """
    
    def setUp(self):
        """
        Set up test environment by initializing the TextExtractor instance and loading test data.
        
        Raises:
            FileNotFoundError: If the test input JSON file is not found.
            json.JSONDecodeError: If the test input JSON file cannot be decoded.
        """
        self.extractor = text_extractor.TextExtractor()
        # Define base directory
        BASE_DIR = Path(__file__).resolve().parent
        try:
            self.json_data = load_json_file(BASE_DIR / 'test_input.json')
        except FileNotFoundError as e:
            logging.error(f"Failed to load test input file: {BASE_DIR / 'test_input.json'}")
            raise e
        except json.JSONDecodeError as e:
            logging.error(f"Failed to decode JSON in file: {BASE_DIR / 'test_input.json'}")
            raise e
    
    def test_extract_text(self):
        """
        Test case to verify the extract_text method of TextExtractor class.
        
        Validates that the method correctly extracts structured content from the input JSON
        and matches it against the expected output structure.
        """
        results = self.extractor.extract_text(self.json_data)
        
        expected_output = [
            {
                "section_name": "Hero",
                "content": [
                    {
                        "type": "headline",
                        "text": "Optimize your team's holiday schedules for just $10."
                    },
                    {
                        "type": "paragraph",
                        "text": "Exclusive holiday discount for new clients: You pay only $10 now through January 1 for unlimited employees, calendars, and dashboards."
                    },
                    {
                        "type": "LpButtonReact",
                        "text": "Start Scheduling"
                    }
                ]
            }
        ]
        
        self.assertEqual(results, expected_output)

if __name__ == '__main__':
    unittest.main()
