import responseHelper

text = "Bonjour tout le monde. Ceci est un texte d'exemple."

# Create the instructions
instructions = "Determine the language of the given text delimited by triple backticks and generate a suitable title for this text. "

# Create the output format
output_format = """Use the following format for the output:
- Text: <the given text>
- Language: <the determined language>
- Title: <the generated title>"""

# Create the final prompt
prompt = instructions + output_format + f"```{text}```"
response = responseHelper.get_response(0, prompt)
responseHelper.print_response(response)