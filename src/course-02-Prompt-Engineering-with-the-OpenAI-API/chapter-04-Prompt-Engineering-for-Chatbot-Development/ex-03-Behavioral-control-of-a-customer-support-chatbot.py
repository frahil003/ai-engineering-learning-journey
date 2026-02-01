import responseHelper as rs

# Define the purpose of the chatbot
chatbot_purpose = "You are a chatbot specified to handle customer support and specialized in electronics. You will assist costumers with inquires, order tracking, and troubleshooting common issues. "

# Define audience guidelines
audience_guidelines = "The audience are tech-savy individuals interested in purchasing electronic gadgets. "

# Define tone guidelines
tone_guidelines = "Use a professional and user-friendly tone while interacting with costumers"

base_system_prompt = chatbot_purpose + audience_guidelines + tone_guidelines

# ---------------------------------------------------

# Define the order number condition
order_number_condition = "If the customer submitted a query about an order without providing an order number, ask for their order number. "

# Define the technical issue condition
technical_issue_condition = "If the customer is reporting a technical issue always start the conservation with: I'm sorry to hear about your issue with... "

# Create the refined system prompt
refined_system_prompt = base_system_prompt + order_number_condition + technical_issue_condition

response_1 = rs.get_response2(0, refined_system_prompt, "My laptop screen is flickering. What should I do?")
response_2 = rs.get_response2(0, refined_system_prompt, "Can you help me track my recent order?")

rs.print_response(response_1)
rs.print_response(response_2)