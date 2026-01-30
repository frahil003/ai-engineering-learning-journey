from openai import OpenAI
client = OpenAI()

response = client.models.retrieve("gpt-5.2")

print(response)