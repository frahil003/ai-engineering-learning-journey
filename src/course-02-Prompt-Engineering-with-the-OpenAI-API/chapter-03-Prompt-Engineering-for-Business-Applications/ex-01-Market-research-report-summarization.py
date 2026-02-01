import responseHelper as rs

# Craft a prompt to summarize the report
prompt = f"""Summarize the report given in triple backticks in maximum five sentences. Focus on aspects which are related to 'AI' und 'data privacy'. This is the report: ```{report}```"""

response = rs.get_response(0, prompt)

print("Summarized report: \n", response)