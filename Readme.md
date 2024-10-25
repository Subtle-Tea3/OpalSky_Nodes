Node Name: StringSwitch_OpalSky
Description:
The StringSwitch_OpalSky node concatenates up to five strings based on corresponding boolean switches. When a switch is turned on (set to True), the associated string is included in the output. The resulting strings are concatenated into a single string, separated by commas and spaces.

This node is useful for scenarios where you want to create dynamic text outputs based on selected conditions, such as generating prompt strings for image generation or combining text for other purposes.

Inputs:
string_1 to string_5 (STRING): These are text inputs where you can input any string. Each string is paired with a boolean switch that determines whether it will be included in the concatenated result.

switch_1 to switch_5 (BOOLEAN): Boolean switches that correspond to the strings above. When a switch is set to True, the respective string will be included in the output. If a switch is set to False, the associated string will be ignored.

Outputs:
concatenated_string (STRING): The concatenated result of all selected strings. Only strings whose corresponding switches are turned on (True) will appear in the result, separated by a comma and a space (, ).
Example Usage:
Input:

string_1 = "dark cinematic lighting"
string_2 = "photo realistic"
string_3 = "high resolution"
string_4 = ""
string_5 = "movie poster"
switch_1 = True
switch_2 = True
switch_3 = False
switch_4 = False
switch_5 = True
Output:

concatenated_string = "dark cinematic lighting, photo realistic, movie poster"
In this example, string_1, string_2, and string_5 are concatenated because their corresponding switches are turned on (True). string_3 and string_4 are not included because either the string is empty or the switch is set to False.

Edge Cases:
All Switches Off:

If all the switches are set to False, the output will be an empty string ("").
Empty Strings:

If a string input is empty but the switch is turned on, the empty string will not be included in the output. The concatenation only includes non-empty strings.
Mixed Empty Strings and Switches:

You can input a combination of filled and empty strings, with the corresponding switches determining what gets included in the final output.
How to Use in ComfyUI:
Add the StringSwitchOpalSky node from the node library (found under custom nodes).
Enter the desired text strings into the input fields.
Toggle the boolean switches to include or exclude the respective strings.
The concatenated string output will be available at the concatenated_string output, which can be connected to other nodes that require a string input.
Where to Save the Documentation:
The documentation should be stored in a location where it can be easily accessed by users, such as:

In the Node Directory:

You can save the documentation in a markdown file called README.md or DOCUMENTATION.md within the same folder where the node is stored (e.g., custom_nodes/OpalSky_Nodes/README.md).
In a Wiki or Documentation System:

If you’re distributing your node on platforms like GitHub, Civitai, or any other open-source node repository, you can include the documentation in the repository's main README.md file or in a separate docs/ folder.
As Part of ComfyUI's Node Documentation:

If ComfyUI has an integrated documentation system (like tooltips or an in-app help menu), you could submit the documentation to be included there.
For Personal Use:

If this node is only for your personal use, consider keeping the documentation in your own documentation folder alongside other custom nodes or projects.
This documentation provides clear instructions on how to use the node and covers most scenarios users might encounter. You can expand or modify it as needed based on additional features or user feedback.