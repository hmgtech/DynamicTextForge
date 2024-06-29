# LeadPages Text Manager
##### AI/Python Take-home Test

LeadPages Text Manager is a tool to extract and replace text in JSON files for LeadPages. It provides functionalities to extract text from textboxes and buttons, keeping track of the text types, and replace the content of the extracted text with new context using AI prompts.

## Features

- Extract text from JSON data while keeping track of text types (e.g., headlines, paragraphs, buttons).
- Replace text content with new context. 

## Project Structure

```sh
LeadPages Text Manager
│
├── core/
│   ├── generative_ai.py
│   ├── text_extractor.py
│   └── text_replacer.py
├── input/
│   └── test.json
└── output/
│   └── extracted_text.json
│   └── replaced_text.json
├── .gitignore
├── config.py
├── main.py
├── README.md
├── requirements.txt
├── setup.py
├── utils.py
```

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/hmgtech/leadpages_text_manager.git
    cd leadpage_text_manager
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

4. Install the package:
    ```sh
    python setup.py install
    ```

## Usage

1. Place your JSON file in the `input` directory. The file should be named `test.json` or adjust the path in `main.py` accordingly.

2. Run the `main.py` script:
    ```sh
    python main.py
    ```

3. The script will print the extracted text and the replaced text to the console.

## Output
```bash

```

## License
```sh
This project is licensed under the MIT License.
```
## Author

- **Hiteshkumar Gupta** - [hiteshgupta2198@gmail.com](hiteshgupta2198@gmail.com)
- GitHub: [hmgtech](https://github.com/hmgtech)
