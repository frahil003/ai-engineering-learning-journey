import responseHelper

story = """Once upon a time in a land far, far away, there lived a curious cat named Whiskers. Whiskers loved to explore the dense forests and climb the tallest trees."""

# Create a prompt that completes the story
prompt = f"""Complete the story delimited by triple backticks.
```{story}```"""

# Get the generated response 
response = responseHelper.get_response(1, prompt)

print("\n Original story: \n", story)
print("\n Generated story: \n", response)