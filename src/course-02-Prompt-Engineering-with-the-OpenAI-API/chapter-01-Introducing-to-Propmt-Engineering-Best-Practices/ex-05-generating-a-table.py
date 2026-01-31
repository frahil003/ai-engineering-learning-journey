import responseHelper

# Create a prompt that generates the table
prompt = "Generate a table of 5 books, with columns for Title, Author and Year that should read when you are a science fiction lover."

# Get the response
response = responseHelper.get_response(0, prompt)
responseHelper.print_response(response)