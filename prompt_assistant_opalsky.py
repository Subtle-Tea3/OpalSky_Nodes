import json
import os
from server import PromptServer

class PromptAssistantOpalSky:
    def __init__(self):
        self.json_data = self.load_bank_of_styles()

    def load_bank_of_styles(self):
        # Load the styles_OpalSky.json file
        current_directory = os.path.dirname(os.path.realpath(__file__))
        json_file_path = os.path.join(current_directory, "styles_OpalSky.json")
        if os.path.exists(json_file_path):
            with open(json_file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    @classmethod
    def INPUT_TYPES(s):
        instance = PromptAssistantOpalSky()
        categories = instance.json_data

        # Extract style options from each category and add "none" as the default option
        lighting_options = ["none"] + [style['name'] for style in categories.get("Lighting and Atmosphere", [])]
        medium_options = ["none"] + [style['name'] for style in categories.get("Artistic Medium and Texture", [])]
        genre_options = ["none"] + [style['name'] for style in categories.get("Cultural and Genre Influences", [])]
        composition_options = ["none"] + [style['name'] for style in categories.get("Composition and Style Structure", [])]
        photography_options = ["none"] + [style['name'] for style in categories.get("Photography and Realism", [])]

        return {
            "required": {
                "text_positive": ("STRING", {"default": "", "multiline": True}),
                "text_negative": ("STRING", {"default": "", "multiline": True}),
                "Lighting_and_Atmosphere": (lighting_options, {"default": "none"}),
                "Artistic_Medium_and_Texture": (medium_options, {"default": "none"}),
                "Cultural_and_Genre_Influences": (genre_options, {"default": "none"}),
                "Composition_and_Style_Structure": (composition_options, {"default": "none"}),
                "Photography_and_Realism": (photography_options, {"default": "none"}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("styled_positive", "styled_negative")
    FUNCTION = "style_prompts"

    def style_prompts(self, text_positive, text_negative,
                      Lighting_and_Atmosphere, Artistic_Medium_and_Texture,
                      Cultural_and_Genre_Influences, Composition_and_Style_Structure,
                      Photography_and_Realism):

        categories = self.json_data

        # Extract positive and negative styles based on selected categories
        positive_styles = [text_positive]  # Start with user-input positive prompt
        negative_styles = [text_negative]  # Start with user-input negative prompt

        def get_prompts(category_name, selected_style):
            category = categories.get(category_name, [])
            style = next((item for item in category if item['name'] == selected_style), None)
            if style:
                # Replace {prompt} with the user-provided positive or negative prompt as appropriate
                positive = style.get("prompt", "").replace("{prompt}", text_positive)
                negative = style.get("negative_prompt", "")
                return positive, negative
            return "", ""

        # Append style-specific prompts to positive and negative lists
        if Lighting_and_Atmosphere != "none":
            pos, neg = get_prompts("Lighting and Atmosphere", Lighting_and_Atmosphere)
            positive_styles.append(pos)
            negative_styles.append(neg)

        if Artistic_Medium_and_Texture != "none":
            pos, neg = get_prompts("Artistic Medium and Texture", Artistic_Medium_and_Texture)
            positive_styles.append(pos)
            negative_styles.append(neg)

        if Cultural_and_Genre_Influences != "none":
            pos, neg = get_prompts("Cultural and Genre Influences", Cultural_and_Genre_Influences)
            positive_styles.append(pos)
            negative_styles.append(neg)

        if Composition_and_Style_Structure != "none":
            pos, neg = get_prompts("Composition and Style Structure", Composition_and_Style_Structure)
            positive_styles.append(pos)
            negative_styles.append(neg)

        if Photography_and_Realism != "none":
            pos, neg = get_prompts("Photography and Realism", Photography_and_Realism)
            positive_styles.append(pos)
            negative_styles.append(neg)

        # Concatenate the final styled positive and negative prompts
        styled_positive = ", ".join(filter(None, positive_styles))
        styled_negative = ", ".join(filter(None, negative_styles))

        # Emit the update_preview event to notify the frontend
        PromptServer.instance.send_sync("opalsky.promptassistant.update_preview", {
            "styled_positive": styled_positive,
            "styled_negative": styled_negative
        })

        return styled_positive, styled_negative

# Node Class Mapping
NODE_CLASS_MAPPINGS = {
    "PromptAssistantOpalSky": PromptAssistantOpalSky
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PromptAssistantOpalSky": "Prompt Assistant OpalSky"
}
