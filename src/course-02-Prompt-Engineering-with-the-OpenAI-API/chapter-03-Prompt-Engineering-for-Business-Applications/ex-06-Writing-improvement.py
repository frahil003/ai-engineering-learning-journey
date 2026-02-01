import responseHelper as rs

text = """Hey guys, wanna know a cool trick? Here's how u can up your productivity game! First, download this awesome app, it's like the best thing ever! Then, just start using it and u'll see the difference. Its super easy and fun, trust me! So, what are u waiting for? Try it out now!"""

# Craft a prompt to transform the text
prompt = f"""Transform the text delimited by triple backticks with the following two steps:
Step 1 - Proofread the text without changing its structure
Step 2 - Adjust the tone to be formal and friendly
```{text}```"""

response = rs.get_response(0, prompt)

print("Before transformation:\n", text)
print("After transformation:\n", response)