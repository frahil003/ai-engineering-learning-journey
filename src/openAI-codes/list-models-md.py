from datetime import datetime
from openai import OpenAI
client = OpenAI()

response = client.models.list()

print("| Model ID | Created | Owner |")
print("|----------|---------|-------|")

for model in sorted(response.data, key=lambda m: m.id.lower()):

  created = datetime.fromtimestamp(model.created).strftime("%Y-%m-%d")
  print(f"| {model.id} | {created} | {model.owned_by} |")


  