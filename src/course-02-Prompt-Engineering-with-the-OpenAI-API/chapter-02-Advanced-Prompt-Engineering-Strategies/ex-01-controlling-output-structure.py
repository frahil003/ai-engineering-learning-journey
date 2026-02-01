import responseHelper

# Create a one-shot prompt
prompt = """Q: Extract odd numbers from the set {1,3,7,12,19} A: The odd numbers are {1,3,7,19}
Q: extract odd numbers from set {3,5,11,12,16} A:"""

response = responseHelper.get_response(0, prompt)

responseHelper.print_response(response)