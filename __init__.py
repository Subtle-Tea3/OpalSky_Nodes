import os
from .string_switch_opalsky import StringSwitchOpalSky
from .prompt_assistant_opalsky import PromptAssistantOpalSky

WEB_DIRECTORY = os.path.join(os.path.dirname(__file__), "js")
__all__ = ["NODE_CLASS_MAPPINGS", "WEB_DIRECTORY"]

NODE_CLASS_MAPPINGS = {
    "StringSwitchOpalSky": StringSwitchOpalSky,
    "PromptAssistantOpalSky": PromptAssistantOpalSky,
}

# Optional: print to confirm nodes loaded
print("\033[34mOpalSky Nodes: \033[92mLoaded\033[0m")
