class TextExtractor:
    def __init__(self):
        self.extracted_set = set()

    def extract_text(self, data, section_name=None, results=None, current_text_type=None) -> list:
        """
        Extracts text from nested dictionaries or lists recursively, maintaining section structure.

        Args:
        - data (dict or list): The nested data structure to extract text from.
        - section_name (str, optional): The name of the current section.
        - results (list, optional): The list to store the extracted text.
        - current_text_type (str, optional): The current text type being processed.

        Returns:
        - results (list): A list of dictionaries containing section information and extracted text.
        """
        if results is None:
            results = []

        try:
            if isinstance(data, dict):
                # Check if this is a new section
                if 'level' in data and data['level'] == 'section' and 'name' in data:
                    section_name = data['name']
                    section_result = {"section_name": section_name, "content": []}
                    results.append(section_result)
                    # Reset the extracted set for the new section
                    self.extracted_set = set()

                # Update text type if 'type' key exists
                if 'type' in data:
                    if data['type'] in ['LpButtonReact', 'LpTextReact', 'paragraph', 'headline']:
                        current_text_type = data['type']
                
                if 'text' in data:
                    text = data['text'].strip()
                    if section_name and (current_text_type, text) not in self.extracted_set:
                        self.append_text_to_section(results, section_name, current_text_type, text)
                        self.extracted_set.add((current_text_type, text))
                
                if 'content' in data and isinstance(data['content'], list):
                    for item in data['content']:
                        self.extract_text(item, section_name, results, current_text_type)
                
                for value in data.values():
                    self.extract_text(value, section_name, results, current_text_type)
            
            elif isinstance(data, list):
                for item in data:
                    self.extract_text(item, section_name, results, current_text_type)
            
            return results
        except Exception as e:
            print(f"An error occurred: {e}")
            return results

    def append_text_to_section(self, results, section_name, text_type, text):
        """Helper method to add extracted text to the appropriate section."""
        content_item = {"type": text_type, "text": text}
        if section_name:
            for section in results:
                if section.get('section_name') == section_name:
                    section['content'].append(content_item)
                    return
            # If section not found, create a new one
            results.append({"section_name": section_name, "content": [content_item]})
        else:
            # If no section_name, add to a default "Unsectioned" group
            for section in results:
                if section.get('section_name') == "Unsectioned":
                    section['content'].append(content_item)
                    return
            results.append({"section_name": "Unsectioned", "content": [content_item]})