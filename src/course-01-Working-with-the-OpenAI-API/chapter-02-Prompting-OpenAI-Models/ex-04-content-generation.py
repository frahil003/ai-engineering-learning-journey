from openai import OpenAI

client = OpenAI()

# the prompt
prompt = "Erstelle einen Slogan für ein neues italisches Fastfood-Restaurant"

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "user", "content": prompt}],
  max_completion_tokens=100          
)

print(response.choices[0].message.content)
