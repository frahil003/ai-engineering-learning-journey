from openai import OpenAI

client = OpenAI()

# Define a multi-line prompt to classify sentiment
prompt = """Classify the sentiment of the following statements and use the numbers 1 (positive) to 5 (negative):
1. Unbelievably good!
2. Shoes fell apart on the second use.
3. The shoes look nice, but they aren't very comfortable.
4. Can't wait to show them off!"""

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "user", "content": prompt}],
  max_completion_tokens=100
)

print(response.choices[0].message.content)