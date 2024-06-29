# LeadPages Text Manager
##### AI/Python Take-home Test

LeadPages Text Manager is a tool to extract and replace text in JSON files for LeadPages. It provides functionalities to extract text from textboxes and buttons, keeping track of the text types, and replace the content of the extracted text with new context using AI prompts.

## Features

- Extract text from JSON data while keeping track of text types (e.g., headlines, paragraphs, buttons).
- Replace text content with new context with AI. 

## Project Structure

```sh
LeadPages Text Manager
│
├── core/
│   └── __init__.py
│   ├── generative_ai.py
│   ├── text_extractor.py
│   └── text_replacer.py
├── input/
│   └── test.json
└── output/
│   └── extracted_text.json
│   └── replaced_text_checkpoint.json
│   └── replaced_text_with_original.json
├── .env
├── .gitignore
├── config.py
├── main.py
├── README.md
├── requirements.txt
├── setup.py
├── utils.py
```
## Approach
### Text Extraction Task
- Input: `data` (dict or list), optional `section_name`, `results` list, `current_text_type`.
- Output: `results` (list of dictionaries with section info and extracted text).
1. Recursively traverse `data`.
2. For each dictionary (`data`):
   - Checked for new section based on 'level' and 'name'.
   - Update `current_text_type` if `'type'` matches `['LpButtonReact', 'LpTextReact', 'paragraph', 'headline']`.
   - Extract 'text', add to `results` with section information, ensure uniqueness using `extracted_set`.
   - Recursively processed 'content' if list.
3. For each list (`data`):
   - Recursively processed each item.

#### Append Text to Section Method
- **Input**: `results`, `section_name`, `text_type`, `text`.
- **Functionality**: Add `text` with `text_type` to appropriate `section_name` in `results`.
  - If `section_name` exists, add content.
  - If `section_name` does not exist, add to "Unsectioned".

### Text Replacement Task
- Input: `extracted_text`, `original_json_data`.
- Output: Save new json file with original format with new context
#### Overview Steps
- Call `replace_text_with_generative_ai` with `extracted_text` and `json_data`.
- Save the generated `replaced_text` to file (`REPLACED_WITH_ORIGINAL_JSON_PATH`).
- Print a confirmation message indicating where the updated JSON has been saved.

#### Replaced Text with Generative AI
- Ensure `GENAI_API_KEY` is set; an error will be raised if it's not.
- Initialized `GenerativeAI` with Gemini API key and `GENAI_MODEL_NAME`.
- Configure the AI model settings.
- Initialized `TextReplacer` with `extracted_text` and the configured AI model.
- Used `text_replacer.rephrase_section()` to replace text based on AI-generated content.
- Saved the resulting `replaced_text` to file (`REPLACED_TEXT_PATH`).
- Created a mapping between original and replaced text using `create_text_mapping` with `extracted_text` and `replaced_text`.
- Returned the updated `original_json` after replacing text using `text_mapping`.

#### Create Text Mapping
- Initialized an empty `text_mapping` dictionary.
- Iterate through `extracted_json` and `replaced_json` sections to map original text to its replacement.
- Returned the `text_mapping` dictionary once mapping is complete.

#### Replace Text in Original JSON
- Recursively traverse the `original` JSON structure.
- Replaced text where a dictionary element contains a `'text'` key matching an entry in `text_mapping`.
- Handled nested dictionaries and lists by recursively calling itself.
- Returned the updated `original` JSON structure.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/hmgtech/leadpages_text_manager.git
    cd leadpages_text_manager
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```
    Note: During the installation, you might see the following warning:
    ```sh
    google-ai-generativelanguage 0.6.6 requires protobuf!=3.20.0,!=3.20.1,!=4.21.0,!=4.21.1,!=4.21.2,!=4.21.3,!=4.21.4,!=4.21.5,<5.0.0dev,>=3.19.5, but you'll have protobuf 5.27.2 which is incompatible.
    ```
    You can safely ignore this warning as it does not affect the functionality of the code.
4. Create a .env file in the root directory and add Gemini API key as shown in .env.example:
    ```sh
    GOOGLE_GEMINI_API_KEY=add_gemini_api_key_here
    ```

## Usage

1. Place input JSON file in the `input` directory. The file should be named `test.json` or adjust the path in `main.py` accordingly.

2. Run the `main.py` script:
    ```sh
    python main.py
    ```

3. The script will print the extracted text and the replaced text to the console.

## Output

In output, we will receive three files:
- extracted_text.json
- replaced_text_checkpoint.json
- replaced_text_with_original.json

File `replaced_text_with_original.json` is the final output which contains website contents with new context (i.e., Leadpages) generated by AI prompts.

## License
```sh
This project is licensed under the MIT License.
```
## Author

- **Hiteshkumar Gupta** - [hiteshgupta2198@gmail.com](hiteshgupta2198@gmail.com)
- GitHub: [hmgtech](https://github.com/hmgtech)
