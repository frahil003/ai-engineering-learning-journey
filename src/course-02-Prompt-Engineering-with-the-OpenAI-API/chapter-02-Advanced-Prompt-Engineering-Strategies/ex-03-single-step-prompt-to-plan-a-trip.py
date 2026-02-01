import responseHelper

# Create a single-step prompt to get help planning the vacation
prompt = "Help me to plan a beach vacation"

response = responseHelper.get_response(0, prompt)

responseHelper.print_response(response)