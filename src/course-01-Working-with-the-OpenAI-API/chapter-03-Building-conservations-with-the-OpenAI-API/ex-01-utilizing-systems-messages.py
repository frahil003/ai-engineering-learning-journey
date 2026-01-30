from openai import OpenAI

client = OpenAI()

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    max_completion_tokens=150,
    messages=[
        {"role": "system", "content": "You are a study planning assistant that creates plans for learning new skills."},
        {"role": "user", "content": "I want to learn to speak Dutch."}
    ]
)

# Extract the assistant's text response
print(response.choices[0].message.content)


