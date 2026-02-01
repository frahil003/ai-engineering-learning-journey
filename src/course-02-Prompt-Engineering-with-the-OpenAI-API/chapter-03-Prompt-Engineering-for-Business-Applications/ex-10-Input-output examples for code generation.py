import responseHelper as rs

examples="""input = [10, 5, 8] -> output = 23
input = [5, 2, 4] -> output = 11
input = [2, 1, 3] -> output = 6
input = [8, 4, 6] -> output = 18
"""

# Craft a prompt that asks the model for the function
prompt = f"""You are provided with input-output examples delimited by triple backticks. Write a python function that maps the inputs to the outputs.
```{examples}```"""

response = rs.get_response(0, prompt)
rs.print_response(response)