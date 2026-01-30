from datetime import datetime
from openai import OpenAI
client = OpenAI()

response = client.models.list()

print(f"{'ID':40} {'CREATED':20} {'OWNER'}")
print("-" * 80)

for model in response.data:

  created = datetime.fromtimestamp(model.created).strftime("%Y-%m-%d")
  print(f"{model.id:40} {created:20} {model.owned_by}")


  