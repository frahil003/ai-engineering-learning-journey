import responseHelper

# Create a prompt detailing steps to plan the trip
prompt = """Make a plan for a beach vacation.
Step 1: Identify four potential locations
Step 2: Give some accommodation options
Step 3: Give some activities
Step 4: Evaluate the pros and cons"""

response = responseHelper.get_response(0, prompt)

responseHelper.print_response(response)