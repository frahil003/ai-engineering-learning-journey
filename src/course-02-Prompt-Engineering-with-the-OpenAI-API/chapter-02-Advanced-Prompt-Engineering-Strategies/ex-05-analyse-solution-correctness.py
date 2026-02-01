import responseHelper

code = '''
def calculate_rectangle_area(length, width):
    area = length * width
    return area
'''

# Create a prompt that analyzes correctness of the code
prompt = f"""Asses the function provided in the delimited code string: <delimited>{code}<delimited>. Follow these steps:
Step 1: check for correct syntax
Step 2: check for receiving two inputs
Step 3: check for returning one output"""

response = responseHelper.get_response(0, prompt)
responseHelper.print_response(response)