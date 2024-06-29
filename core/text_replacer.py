import json

class TextReplacer:
    def __init__(self, json_data, generative_ai):
        """
        Initialize TextReplacer with JSON data and a GenerativeAI instance.

        Args:
        - json_data (list): JSON data containing sections to be rephrased.
        - generative_ai (GenerativeAI): Instance of GenerativeAI class for text generation.
        """
        self.json_data = json_data
        self.generative_ai = generative_ai

    def rephrase_section(self):
        """
        Rephrase sections in the JSON data using Generative AI.

        Returns:
        - list: List of processed JSON objects with updated content.
        """
        processed_json_data = []

        try:
            # Iterate through JSON data and generate new text for each section
            for section in self.json_data:
                section_name = section["section_name"]
                section_content = section["content"]

                # Create prompt with existing section content and LeadPages context
                prompt_text = f"Look at the current {section_name} section:\n"
                prompt_text += json.dumps(section, indent=4) + "\n"
                prompt_text += f"It is designed for ScheduleMaster, a digital scheduler to help someone schedule tasks.\n"
                prompt_text += f"Now, replace the text with LeadPages content: LeadPages, a landing page builder to help you build landing pages for your business.\n"
                prompt_text += f"Keep format same section name, just replace the text. Please match same number of content items.\n"
                prompt_text += f"Please come up with innovative ideas and attractive statements. In response, just give me best json object."

                # Generate new text with Generative AI
                print(f"Generating content for {section_name} section.")
                generated_text = self.generative_ai.generate_text(prompt_text)

                # Append updated section to processed_json_data list
                processed_json_data.append(generated_text)

        except KeyError as e:
            print(f"Error: Missing key in section data: {e}")
        except Exception as e:
            print(f"Error: An unexpected error occurred during section rephrasing: {e}")

        return processed_json_data
    
    def replace_text_in_original(self, original, text_mapping):
        """
        Recursively replaces text in a nested dictionary or list structure.

        Args:
        - original (dict or list): The original data structure where text replacements will occur.
        - text_mapping (dict): A dictionary mapping original text to replacement text.

        Returns:
        - original (dict or list): The modified data structure with text replacements.
        """
        try:
            if isinstance(original, dict):
                if 'text' in original and original['text'] in text_mapping:
                    original['text'] = text_mapping[original['text']]
                for key, value in original.items():
                    if isinstance(value, (dict, list)):
                        self.replace_text_in_original(value, text_mapping)
            elif isinstance(original, list):
                for item in original:
                    self.replace_text_in_original(item, text_mapping)
        except Exception as e:
            print(f"Error: An error occurred during text replacement: {e}")

        return original
