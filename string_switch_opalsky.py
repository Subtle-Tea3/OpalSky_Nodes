import json
import os

class StringSwitchOpalSky:
    def __init__(self):
        # Load the JSON file with predefined styles (bank of styles)
        self.json_data = self.load_bank_of_styles()
        # Define preset mappings
        self.presets = {
            "Cinematic Noir": {
                "Lighting_and_Atmosphere": "Cinematic: Neo-noir",
                "Artistic_Medium_and_Texture": "Digital Painting: Hyperrealistic",
                "Cultural_and_Genre_Influences": "Gothic Horror",
                "Composition_and_Style_Structure": "Cinematic: Dramatic",
                "Photography_and_Realism": "Analog Film: Black & White"
            },
            "Fantasy Illustration": {
                "Lighting_and_Atmosphere": "Natural Light: Golden Hour",
                "Artistic_Medium_and_Texture": "Digital Painting: Concept Art",
                "Cultural_and_Genre_Influences": "Fantasy: High Fantasy",
                "Composition_and_Style_Structure": "Centered Composition",
                "Photography_and_Realism": "DSLR: Portrait"
            },
            "Retro Sci-Fi": {
                "Lighting_and_Atmosphere": "Artificial Light: Neon",
                "Artistic_Medium_and_Texture": "Pixel Art",
                "Cultural_and_Genre_Influences": "Sci-Fi: Alien Worlds",
                "Composition_and_Style_Structure": "Isometric",
                "Photography_and_Realism": "HDR"
            }
        }

    # Load bank of styles from a JSON file
    def load_bank_of_styles(self):
        current_directory = os.path.dirname(os.path.realpath(__file__))
        json_file_path = os.path.join(current_directory, "Styles.json")  # Ensure this matches the actual file name
        if os.path.exists(json_file_path):
            with open(json_file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    @classmethod
    def INPUT_TYPES(cls):
        # Initialize to access the predefined styles
        instance = cls()
        categories = instance.json_data

        # Extract categories for each predefined style
        lighting_options = categories.get("Lighting and Atmosphere", {}).get("categories", [])
        medium_options = categories.get("Artistic Medium and Texture", {}).get("categories", [])
        genre_options = categories.get("Cultural and Genre Influences", {}).get("categories", [])
        composition_options = categories.get("Composition and Style Structure", {}).get("categories", [])
        photography_options = categories.get("Photography and Realism", {}).get("categories", [])

        # Define preset options
        presets = ["Custom", "Cinematic Noir", "Fantasy Illustration", "Retro Sci-Fi"]

        return {
            "required": {
                # Custom strings section with styling
                "use_custom_strings": ("BOOLEAN", {"default": True}),
                "use_styles": ("BOOLEAN", {"default": False}),

                "string_1": ("STRING", {"default": "", "multiline": True}),
                "switch_string_1": ("BOOLEAN", {"default": True, "label": ""}),
                "string_2": ("STRING", {"default": "", "multiline": True}),
                "switch_string_2": ("BOOLEAN", {"default": True, "label": ""}),
                "string_3": ("STRING", {"default": "", "multiline": True}),
                "switch_string_3": ("BOOLEAN", {"default": True, "label": ""}),
                "string_4": ("STRING", {"default": "", "multiline": True}),
                "switch_string_4": ("BOOLEAN", {"default": True, "label": ""}),
                "string_5": ("STRING", {"default": "", "multiline": True}),
                "switch_string_5": ("BOOLEAN", {"default": True, "label": ""}),

                # Preset dropdown
                "preset": (presets, {"default": "Custom"}),

                # Predefined styles section
                "Lighting_and_Atmosphere": (lighting_options, {"default": "none"}),
                "Artistic_Medium_and_Texture": (medium_options, {"default": "none"}),
                "Cultural_and_Genre_Influences": (genre_options, {"default": "none"}),
                "Composition_and_Style_Structure": (composition_options, {"default": "none"}),
                "Photography_and_Realism": (photography_options, {"default": "none"}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("concatenated_string",)
    FUNCTION = "concatenate_strings"

    def concatenate_strings(self, use_styles, use_custom_strings,
                            Lighting_and_Atmosphere,
                            Artistic_Medium_and_Texture,
                            Cultural_and_Genre_Influences,
                            Composition_and_Style_Structure,
                            Photography_and_Realism,
                            string_1, switch_string_1, string_2, switch_string_2, string_3, switch_string_3,
                            string_4, switch_string_4, string_5, switch_string_5, preset):
        
        # Apply preset if not "Custom"
        if preset != "Custom" and preset in self.presets:
            preset_values = self.presets[preset]
            Lighting_and_Atmosphere = preset_values.get("Lighting_and_Atmosphere", "none")
            Artistic_Medium_and_Texture = preset_values.get("Artistic_Medium_and_Texture", "none")
            Cultural_and_Genre_Influences = preset_values.get("Cultural_and_Genre_Influences", "none")
            Composition_and_Style_Structure = preset_values.get("Composition_and_Style_Structure", "none")
            Photography_and_Realism = preset_values.get("Photography_and_Realism", "none")

        # Handle custom strings
        custom_strings = []
        if use_custom_strings:
            custom_strings = [string_1, string_2, string_3, string_4, string_5]
            custom_strings = [s for s, switch in zip(custom_strings, [switch_string_1, switch_string_2, switch_string_3, switch_string_4, switch_string_5]) if switch and s]
        
        # Handle predefined styles
        all_styles = []
        if use_styles:
            styles_map = self.json_data
            if Lighting_and_Atmosphere != "none":
                all_styles.append(styles_map["Lighting and Atmosphere"]["tags"][Lighting_and_Atmosphere])
            if Artistic_Medium_and_Texture != "none":
                all_styles.append(styles_map["Artistic Medium and Texture"]["tags"][Artistic_Medium_and_Texture])
            if Cultural_and_Genre_Influences != "none":
                all_styles.append(styles_map["Cultural and Genre Influences"]["tags"][Cultural_and_Genre_Influences])
            if Composition_and_Style_Structure != "none":
                all_styles.append(styles_map["Composition and Style Structure"]["tags"][Composition_and_Style_Structure])
            if Photography_and_Realism != "none":
                all_styles.append(styles_map["Photography and Realism"]["tags"][Photography_and_Realism])

        # If both `use_styles` and `use_custom_strings` are off, return an empty string
        if not use_styles and not use_custom_strings:
            return ("",)

        # Concatenate custom strings first, followed by styles
        all_strings = custom_strings + all_styles
        result = ", ".join(all_strings)

        return (result,)

# Print message on load
print("StringSwitchOpalSky loaded successfully")

# Node class mapping
NODE_CLASS_MAPPINGS = {
    "string_switch_opalsky": StringSwitchOpalSky
}

# Display Name Mapping
NODE_DISPLAY_NAME_MAPPINGS = {
    "string_switch_opalsky": "String Switch OpalSky"
}
