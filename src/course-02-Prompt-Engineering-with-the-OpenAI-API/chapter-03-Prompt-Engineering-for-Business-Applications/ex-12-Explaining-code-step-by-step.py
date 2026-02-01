import responseHelper as rs

# Craft a chain-of-thought prompt that asks the model to explain what the function does
prompt = f"""Explain what the function delimited by triple backticks does.
Let's think step by step.
```{function}```"""
 
response = rs.get_response(0, prompt)
rs.print_response(response)