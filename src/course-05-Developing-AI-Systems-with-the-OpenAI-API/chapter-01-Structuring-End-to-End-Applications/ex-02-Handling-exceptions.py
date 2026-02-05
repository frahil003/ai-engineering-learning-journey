from openai import OpenAI
from openai import AuthenticationError

client = OpenAI()
#client = OpenAI(api_key="asdfasdfasdf")

message = {'role': 'user', 'content': 'Here are some made-up addresses and company names, write them in json format. PurpleLabs Solutions, 123 Main Street, Suite 100, Anytown, USA. InnovateNow Enterprises, 789 Oak Avenue, Suite 300, Innovation City, USA. PeakPerformance Inc., 456 Elm Street, Suite 200, Dreamville, USA'}

# Use the try statement
try:
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[message],
    # Specify the response format. Without format the model returns plain text with a JSON string inside.
    response_format={"type": "json_object"}
    )
    # Print the response
    print(response.choices[0].message.content)

# Use the except statement
except AuthenticationError as e:
    print(f"Please double check your authentication key and try again, the one provided is not valid: {e}")