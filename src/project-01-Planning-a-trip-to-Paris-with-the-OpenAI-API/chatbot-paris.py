from openai import OpenAI

client = OpenAI()

# Define the model to use
model = "gpt-4o-mini"

# Define the client
client = OpenAI()

# Start coding here
# Add as many cells as you like

# Define the temperatur
temperatur = 0.0

# Define the maximum number of tokens
max_tokens = 100

# Define list of dictionaries containing the messages and responses from the model
# Define the purpose of the chatbot
chatbot_purpose = "You are a Parisian expert and also a travel guide for the culturally rich city of Paris. You are able to deliver valuable insights into the city's iconic landmarks and hidden treasures. You will assist travellers to explore the city of Paris. "

response_guidelines = "If the question is related to the city of Paris, you answer to the best of your knowledge. Otherwise, you just response with 'Sorry! As a Parisian expert I am only able to answer to questions which related to the city of Paris.' "

# Define the audience guidelines
audience_guidelines = "The audience are travellers which never been before in Paris. "

# Define the tone guidelines
tone_guidelines = "Use a professional, inspiring and user-friendly tone while interacting with costumers."
# Define the complete system prompt
system_prompt = chatbot_purpose + response_guidelines + audience_guidelines + tone_guidelines

conversation = [{"role": "system", "content": system_prompt}]

user_questions = ["How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?",
                  "Where is the Arc de Triomphe?",
                  "What are the must-see artworks at the Louvre Museum?"]

for q in user_questions:
    print("User: ", q, "\n")
    user_dict = {"role":"user", "content": q}
    conversation.append(user_dict)

    response = client.chat.completions.create(
        model=model,
        messages=conversation,
        temperature=temperatur,
        max_completion_tokens=max_tokens
    )
    assistant_dict = {"role": "assistant", "content": response.choices[0].message.content}
    conversation.append(assistant_dict)
    print("Assistant: ", response.choices[0].message.content, "\n")