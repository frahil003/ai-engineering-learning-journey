from openai import OpenAI

client = OpenAI()

def get_response(temperature, prompt):
  # Create a request to the chat completions endpoint
  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}], 
    temperature = temperature)
  return response.choices[0].message.content

def print_response(response):
  print("\n" + "#" * 50)
  print("#         Response from the OpenAI API           #")
  print("#" * 50)
  print(f"\n{response}\n\n{'#' * 50}\n")