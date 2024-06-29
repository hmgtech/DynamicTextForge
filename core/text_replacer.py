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
                prompt_text = f"Examine the current {section_name} section:\n"
                prompt_text += json.dumps(section, indent=4) + "\n"
                prompt_text += "It is tailored for ScheduleMaster, a digital scheduler for task management.\n"
                prompt_text += "Now, transform this text to be suitable for LeadPages:\n"
                prompt_text += "'With Leadpages, you can build landing pages, deliver lead magnets, track your analytics, manage your leads, sell your products and services, and more.'\n"
                prompt_text += "Maintain the original format of the section but replace the text with equivalent content for LeadPages. Ensure the number of content items remains the same. Please create innovative and appealing statements. Provide the result as a JSON object.\n"


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
    
    def replace_text_in_original(self, data, text_mapping):
        """
        Replaces text in the nested data structure based on a given text mapping.

        Args:
        - data (dict or list): The nested data structure to replace text in.
        - text_mapping (dict): A dictionary mapping original text to replacement text.

        Returns:
        - data (dict or list): The data structure with replaced text.
        """

        try:
            if isinstance(data, dict):
                
                if 'text' in data:
                    text = data['text'].strip()
                    if text in text_mapping:
                        data['text'] = text_mapping[text]

                if 'content' in data and isinstance(data['content'], list):
                    for item in data['content']:
                        self.replace_text_in_original(item, text_mapping)
                
                for key, value in data.items():
                    if isinstance(value, (dict, list)):
                        self.replace_text_in_original(value, text_mapping)
            
            elif isinstance(data, list):
                for item in data:
                    self.replace_text_in_original(item, text_mapping)

            return data
        except Exception as e:
            print(f"An error occurred during text replacement: {e}")
            return data
