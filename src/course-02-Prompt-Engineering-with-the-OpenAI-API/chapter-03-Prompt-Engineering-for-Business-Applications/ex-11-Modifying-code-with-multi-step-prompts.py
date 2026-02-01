import responseHelper as rs

function = """def calculate_area_rectangular_floor(width, length):
					return width*length"""

# Craft a multi-step prompt that asks the model to adjust the function
prompt = f"""Modify the function delimited by triple backticks as follows:
- Test if the inputs to the function are positive.
- If not display appropriate error messages
- Otherwise calculate the perimeter
- And finally display the area and the perimeter
```{function}```"""

response = rs.get_response(0, prompt)
rs.print_response(response)