import responseHelper

text = "The sun was setting behind the mountains, casting a warm golden glow across the landscape. Birds chirped their final songs of the day."

# Create the instructions
instructions = "Determine the language of the given text delimited by triple backticks. Also determine the number of sentences of the delimited text. If the text contains more than one sentence, generate s suitable title for it, otherwise, write 'N/A' for the title."

# Create the output format
output_format = """Use the following format for the output:
- Text: <the given text>
- Language: <the determined language>
- Title: <the generated title>
- Number of sentences: <>the determined number of sentences"""

prompt = instructions + output_format + f"```{text}```"
response = responseHelper.get_response(0, prompt)
responseHelper.print_response(response)