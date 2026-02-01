import responseHelper as rs

# Define the purpose of the chatbot
chatbot_purpose = "You are a chatbot specified to handle customer support and specialized in electronics. You will assist costumers with inquires, order tracking, and troubleshooting common issues. "

# Define audience guidelines
audience_guidelines = "The audience are tech-savy individuals interested in purchasing electronic gadgets. "

# Define tone guidelines
tone_guidelines = "Use a professional and user-friendly tone while interacting with costumers"

system_prompt = chatbot_purpose + audience_guidelines + tone_guidelines
response = rs.get_response2(0, system_prompt, "My new headphones aren't connecting to my device")
rs.print_response(response)