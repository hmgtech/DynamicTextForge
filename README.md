# Dynamic Text Forge

##### Dynamic Text Forge is a Python-based tool for extracting and transforming text content from JSON representations of landing pages. It integrates AI prompts to dynamically replace existing text, enabling easy customization of landing page content.

## Features

- Extract text from JSON data while keeping track of text types (e.g., headlines, paragraphs, buttons).
- Replace text content with new context with AI. 

## Project Structure

```sh
DynamicTextForge
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
└── test/
│   └── text_extractor_test.py
│   └── text_replacer_test.py
├── .env
├── .gitignore
├── config.py
├── main.py
├── README.md
├── requirements.txt
├── setup.py
├── utils.py
```
# My Approach

## Text Extraction Task

### Input
- `data` (dict or list)
- Optional `section_name`
- `results` list
- `current_text_type`

### Output
- `results` (list of dictionaries with section info and extracted text)

### Algorithm

1. **Recursively Traverse `data`**:
    - If `data` is a dictionary:
        1. **New Section Detection**:
            - Check for new section based on 'level' and 'name'.
        2. **Update `current_text_type`**:
            - If `'type'` matches `['LpButtonReact', 'LpTextReact', 'paragraph', 'headline']`, update `current_text_type`.
        3. **Extract Text**:
            - Extract 'text' and add to `results` with section information.
            - Ensure uniqueness using `extracted_set`.
        4. **Process 'content'**:
            - If 'content' is a list, recursively process each item.
    - If `data` is a list:
        1. Recursively process each item.

2. **Append Text to Section Method**:
    - **Input**: `results`, `section_name`, `text_type`, `text`
    - **Functionality**:
        - Add `text` with `text_type` to the appropriate `section_name` in `results`.
        - If `section_name` exists, add content.
        - If `section_name` does not exist, add to "Unsectioned".
### Time Complexity
The time complexity of the `extract_text` method is **O(n)**, where **n** is the total number of elements in the input data structure. This complexity arises because the method traverses through each element exactly once, whether it's a dictionary key-value pair or a list item.

### Space Complexity
The space complexity of the `extract_text` method is **O(n + k)**:
- **O(n)** space is used by the `results` list and the `extracted_set`, where **n** is the total number of elements in the input data structure.
- **O(k)** space is used on the call stack due to recursion, where **k** is the maximum depth of recursion in the nested data structure.

---

## Text Replacement Task

### Input
- `extracted_text`
- `original_json_data`

### Output
- Save new JSON file with original format and new context

### Algorithm

1. **Overview**:
    - Call `replace_text_with_generative_ai` with `extracted_text` and `json_data`.
    - Save the generated `replaced_text` to file (`REPLACED_WITH_ORIGINAL_JSON_PATH`).
    - Print a confirmation message indicating where the updated JSON has been saved.

2. **Replace Text with Generative AI**:
    1. **Setup**:
        - Ensure `GENAI_API_KEY` is set; raise an error if not.
        - Initialize `GenerativeAI` with Gemini API key and `GENAI_MODEL_NAME`.
        - Configure the AI model settings.
    2. **Text Replacement**:
        - Initialize `TextReplacer` with `extracted_text` and the configured AI model.
        - Use `text_replacer.rephrase_section()` to replace text based on AI-generated content.
        - Save the resulting `replaced_text` to file (`REPLACED_TEXT_PATH`).
    3. **Mapping and Replacement (as shown in Step 3 and 4)**:
        - Create a mapping between the original and replaced text using `create_text_mapping` with `extracted_text` and `replaced_text`.
        - Return the updated `original_json` after replacing text using `text_mapping`.

3. **Create Text Mapping**:
    1. **Initialization**:
        - Initialize an empty `text_mapping` dictionary.
    2. **Mapping**:
        - Iterate through `extracted_json` and `replaced_json` sections to map original text to its replacement.
    3. **Completion**:
        - Return the `text_mapping` dictionary once mapping is complete.

4. **Replace Text in Original JSON**:
    1. **Recursively Traverse**:
        - Traverse the `original` JSON structure.
    2. **Replacement**:
        - Replace text where a dictionary element contains a `'text'` key matching an entry in `text_mapping`.
    3. **Handling Nesting**:
        - Handle nested dictionaries and lists by recursively calling itself.
    4. **Return**:
        - Return the updated `original` JSON structure.

### Time Complexity
- **Rephrase Section (`rephrase_section` method)**: O(n), where n is the number of sections in `self.json_data`.
- **Replace Text in Original (`replace_text_in_original` method)**: O(m), where m is the total number of elements in the nested data structure `data`.

### Space Complexity
- **Rephrase Section (`rephrase_section` method)**: O(n), due to space for `processed_json_data`, where n is the number of sections in `self.json_data`.
- **Replace Text in Original (`replace_text_in_original` method)**: O(k + t), where k is the maximum recursion depth and t is the number of entries in `text_mapping`. This includes space for the recursive call stack and the `text_mapping` dictionary.


## Prerequisites

- Python 3.7 or higher
- Required Python libraries:
  - `requests`
  - `json`
  - `google.generativeai`
- A valid Generative AI API key (`GENAI_API_KEY`)
- Environment file (`.env`) for storing configuration

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/hmgtech/DynamicTextForge
    cd DynamicTextForge
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
5. [OPTIONAL] Install DynamicTextForge package in editable mode for development using `setup.py` file:
    ```sh
    pip install -e .
    ```
## Usage

1. Place input JSON file in the `input` directory. The file should be named `test.json` or adjust the path in `main.py` accordingly.

2. Run the `main.py` script:
    ```sh
    python main.py
    ```

3. The script will print the extracted text and the replaced text to the console.

## Unit Tests

1. Run all unit tests using `unittest`:
    ```sh
    python -m unittest discover -s tests
    ```

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

## Future Scope for Improvements

1. **Develop In-House Language Model (LLM)**:
   - Build our own language model instead of relying on third-party services. This gives us more control over content quality and customization.

2. **Enhance Content Generation with Images**:
   - Expand content generation capabilities to include creating images tailored to the generated text. This enhances visual appeal and engagement.

3. **Create User Interface (UI)**:
   - Once the system is reliable, we can develop a friendly UI for users to upload JSON files. They can easily view the newly generated content and visualize its representation as a website.

4. **Migration to Cloud Infrastructure (e.g., AWS)**:
   - Move our entire generation process to a cloud platform like AWS for scalability, reliability, and cost efficiency.