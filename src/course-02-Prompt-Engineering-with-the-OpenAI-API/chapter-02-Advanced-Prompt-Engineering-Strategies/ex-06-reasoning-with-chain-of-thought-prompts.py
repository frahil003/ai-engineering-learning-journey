import responseHelper as rs

# Create the chain-of-thought prompt
prompt = """Q: Determine my friend's fahter age in 10 years. Currently he is twice my frined's age and my friend is 20.
A: Let's think step by step"""

response = rs.get_response(0, prompt)

rs.print_response(response)