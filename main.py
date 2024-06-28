import os
import json
from core.text_extractor import TextExtractor

def main():
    try:
        # Define the path to the JSON file
        json_file_path = os.path.join(os.path.dirname(__file__), 'input', 'test.json')

        # Load the JSON data
        with open(json_file_path, 'r', encoding="utf8") as file:
            json_data = json.load(file)

        # Create an instance of TextExtractor
        extractor = TextExtractor()

        # Extract text from the JSON data
        extracted_text = extractor.extract_text(json_data)
        
        # print("Extracted Text:", extracted_text)
        # for text_type, text in extracted_text:
        #     print(f"Type: {text_type}")
        #     print(f"Text: {text}")
        #     print()

        # Define the path to the output directory and file
        output_directory = os.path.join(os.path.dirname(__file__), 'output')
        output_file_path = os.path.join(output_directory, 'extracted_text.json')

        # Create the output directory if it doesn't exist
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # Write extracted text to the output JSON file
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            json.dump(extracted_text, output_file, ensure_ascii=False, indent=4)

        print(f"Extracted text saved to {output_file_path}")


    except FileNotFoundError as fnf_error:
        print(f"FileNotFoundError: {fnf_error}. Please check if the file exists or the path is correct.")
    except json.JSONDecodeError as json_error:
        print(f"JSONDecodeError: {json_error}. Check if the JSON file is valid.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}. Please review the code for issues.")

if __name__ == "__main__":
    main()
