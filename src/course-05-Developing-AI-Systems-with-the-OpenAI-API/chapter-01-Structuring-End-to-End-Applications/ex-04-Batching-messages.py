from openai import OpenAI

client = OpenAI()

messages = []

def get_response(model, message):
    response = client.chat.completions.create(
      model=model,
      messages=message
    )
    return response.choices[0].message.content

# Provide a system message and user messages to send the batch
messages.append({"role": "system", "content": "You are given a list of measurements in kilometers. Convert all measurements from kilometers into miles. Response a table containing both the original and converted measurements."})

# Append measurements to the message
measurements = [5.2, 6.3, 3.7]
[messages.append({"role": "user", "content": str(i)}) for i in measurements]

response = get_response("gpt-4o-mini", messages)
print(response)