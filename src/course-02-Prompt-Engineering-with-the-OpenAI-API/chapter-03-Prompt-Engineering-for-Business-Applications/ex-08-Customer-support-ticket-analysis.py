import responseHelper as rs

ticket_4 ="Greetings, I am facing technical difficulties with your software, ABC Editor. My name is Sarah Lee, and I recently upgraded to the latest version. However, whenever I try to save my work, the software crashes. Can you please help me resolve this problem?"

# Craft a few-shot prompt to get the ticket's entities
prompt = f"""
Ticket: {ticket_1} -> Entities: {entities_1}
Ticket: {ticket_2} -> Entities: {entities_2}
Ticket: {ticket_3} -> Entities: {entities_3}
Ticket: {ticket_4} -> Entities: """

response = get_response(prompt)

print("Ticket: \n", ticket_4)
print("Entities: \n", response)