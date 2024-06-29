import time
import google.generativeai as genai
import json

class GenerativeAI:
    def __init__(self, api_key, model_name):
        """
        Initialize the GenerativeAI class with API key and model name.
        
        Args:
        - api_key (str): API key for authentication with Generative AI service.
        - model_name (str): Name of the Generative AI model to use for text generation.
        """
        self.api_key = api_key
        self.model_name = model_name
        self.model = genai.GenerativeModel(model_name)

    def configure(self):
        """
        Configure the Generative AI library with the provided API key.
        """
        genai.configure(api_key=self.api_key)

    def generate_text(self, prompt_text):
        """
        Generate text based on the provided prompt using the configured model.
        
        Args:
        - prompt_text (str): Text prompt to generate content from.
        
        Returns:
        - dict: JSON response containing generated content.
        
        Raises:
        - ValueError: If there's an issue decoding the JSON response.
        """
        response = self.model.generate_content(prompt_text)
        
        # Extract JSON object from the embedded string format
        json_start_index = response.text.find("{")
        json_end_index = response.text.rfind("}") + 1
        json_content = response.text[json_start_index:json_end_index]

        try:
            json_response = json.loads(json_content)
            return json_response
        except json.JSONDecodeError:
            raise ValueError("Failed to decode JSON response from Generative AI")
