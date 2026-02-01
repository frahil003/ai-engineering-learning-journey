import responseHelper as rs

# Craft a prompt that asks the model for the function
prompt = "Write a python function. The function receives a list of 12 floats representing monthly sales data. The function should return the month with the highest sales."

response = rs.get_response(0, prompt)
rs.print_response(response)
