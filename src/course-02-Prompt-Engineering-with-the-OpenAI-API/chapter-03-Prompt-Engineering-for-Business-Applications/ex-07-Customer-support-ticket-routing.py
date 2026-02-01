import responseHelper as rs

ticket = """Subject: Urgent - Login Error

Hi Support Team,

I'm having trouble accessing my account with the username "example_user." Every time I try to log in, I encounter an error message. I've already attempted to reset my password, but the issue persists. I need to resolve this problem urgently, as I have pending tasks that require immediate attention.

Please investigate and assist promptly.

Thanks,
John."""

# Craft a prompt to classify the ticket
prompt = f"""Classify the ticket delimited by triple backticks as 'technical issue', 'billing inquiry', or 'product feedback'
```{ticket}```"""

response = rs.get_response(0, prompt)

print("Ticket: ", ticket)
print("Class: ", response)