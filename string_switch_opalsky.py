import json
import os

class String_Switch_OpalSky:
    def __init__(self):
        # Load the JSON file with predefined styles (bank of styles)
        self.json_data = self.load_bank_of_styles()

    # Load bank of styles from a JSON file
    def load_bank_of_styles(self):
        current_directory = os.path.dirname(os.path.realpath(__file__))
        json_file_path = os.path.join(current_directory, "style_bank.json")  # Update the path as necessary
        if os.path.exists(json_file_path):
            with open(json_file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    @classmethod
    def INPUT_TYPES(s):
        # Initialize to access the predefined styles
        instance = String_Switch_OpalSky()
        categories = instance.json_data
        
        # Extract categories for each predefined style
        lighting_options = categories.get("Lighting and Atmosphere", {}).get("categories", [])
        medium_options = categories.get("Artistic Medium and Texture", {}).get("categories", [])
        genre_options = categories.get("Cultural and Genre Influences", {}).get("categories", [])
        composition_options = categories.get("Composition and Style Structure", {}).get("categories", [])
        photography_options = categories.get("Photography and Realism", {}).get("categories", [])

        # Define 5 predefined styles with custom options from the JSON
        return {
            "required": {
                # Toggle for using styles or custom strings
                "use_styles": ("BOOLEAN", {"default": False}),
                "use_custom_strings": ("BOOLEAN", {"default": True}),
                
                # Predefined styles
                "Lighting_and_Atmosphere": (lighting_options, {"default": "none"}),
                "switch_Lighting_and_Atmosphere": ("BOOLEAN", {"default": True}),
                "Artistic_Medium_and_Texture": (medium_options, {"default": "none"}),
                "switch_Artistic_Medium_and_Texture": ("BOOLEAN", {"default": True}),
                "Cultural_and_Genre_Influences": (genre_options, {"default": "none"}),
                "switch_Cultural_and_Genre_Influences": ("BOOLEAN", {"default": True}),
                "Composition_and_Style_Structure": (composition_options, {"default": "none"}),
                "switch_Composition_and_Style_Structure": ("BOOLEAN", {"default": True}),
                "Photography_and_Realism": (photography_options, {"default": "none"}),
                "switch_Photography_and_Realism": ("BOOLEAN", {"default": True}),
                
                # Custom strings
                "string_1": ("STRING", {"default": "", "multiline": False}),
                "switch_string_1": ("BOOLEAN", {"default": True}),
                "string_2": ("STRING", {"default": "", "multiline": False}),
                "switch_string_2": ("BOOLEAN", {"default": True}),
                "string_3": ("STRING", {"default": "", "multiline": False}),
                "switch_string_3": ("BOOLEAN", {"default": True}),
                "string_4": ("STRING", {"default": "", "multiline": False}),
                "switch_string_4": ("BOOLEAN", {"default": True}),
                "string_5": ("STRING", {"default": "", "multiline": False}),
                "switch_string_5": ("BOOLEAN", {"default": True}),
            }
        }

    # Method to process the input and return concatenated string
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("concatenated_string",)
    FUNCTION = "concatenate_strings"
    
    def concatenate_strings(self, use_styles, use_custom_strings,
                            Lighting_and_Atmosphere, switch_Lighting_and_Atmosphere,
                            Artistic_Medium_and_Texture, switch_Artistic_Medium_and_Texture,
                            Cultural_and_Genre_Influences, switch_Cultural_and_Genre_Influences,
                            Composition_and_Style_Structure, switch_Composition_and_Style_Structure,
                            Photography_and_Realism, switch_Photography_and_Realism,
                            string_1, switch_string_1, string_2, switch_string_2, string_3, switch_string_3,
                            string_4, switch_string_4, string_5, switch_string_5):
        
        # Handling predefined styles and corresponding tags from JSON
        all_styles = []
        if use_styles:
            styles_map = self.json_data
            if switch_Lighting_and_Atmosphere and Lighting_and_Atmosphere != "none":
                all_styles.append(styles_map["Lighting and Atmosphere"]["tags"][Lighting_and_Atmosphere])
            if switch_Artistic_Medium_and_Texture and Artistic_Medium_and_Texture != "none":
                all_styles.append(styles_map["Artistic Medium and Texture"]["tags"][Artistic_Medium_and_Texture])
            if switch_Cultural_and_Genre_Influences and Cultural_and_Genre_Influences != "none":
                all_styles.append(styles_map["Cultural and Genre Influences"]["tags"][Cultural_and_Genre_Influences])
            if switch_Composition_and_Style_Structure and Composition_and_Style_Structure != "none":
                all_styles.append(styles_map["Composition and Style Structure"]["tags"][Composition_and_Style_Structure])
            if switch_Photography_and_Realism and Photography_and_Realism != "none":
                all_styles.append(styles_map["Photography and Realism"]["tags"][Photography_and_Realism])

        # Handling custom strings
        custom_strings = []
        if use_custom_strings:
            custom_strings = [string_1, string_2, string_3, string_4, string_5]
            custom_strings = [s for s, switch in zip(custom_strings, [switch_string_1, switch_string_2, switch_string_3, switch_string_4, switch_string_5]) if switch and s]

        # If both use_styles and use_custom_strings are off, return an empty string
        if not use_styles and not use_custom_strings:
            return ("",)

        # Concatenate styles and custom strings separately
        all_strings = all_styles + custom_strings
        
        result = ", ".join(all_strings)

        return (result,)

# Node class mapping
NODE_CLASS_MAPPINGS = {
    "String_Switch_OpalSky": String_Switch_OpalSky
}
