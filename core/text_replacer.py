import json

class TextReplacer:
    def __init__(self, json_data, generative_ai):
        """
        Initialize TextReplacer with JSON data and a GenerativeAI instance.
        :param json_data: JSON data containing sections to be rephrased.
        :param generative_ai: Instance of GenerativeAI class for text generation.
        """
        self.json_data = json_data
        self.generative_ai = generative_ai

    def rephrase_section(self):
        """
        Rephrase sections in the JSON data using Generative AI.
        :return: List of processed JSON objects with updated content.
        """
        processed_json_data = []

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
            print("Generating content for {0}.".format(section_name))
            generated_text = self.generative_ai.generate_text(prompt_text)
            # Append updated section to processed_json_data list
            processed_json_data.append(generated_text)
        return processed_json_data
