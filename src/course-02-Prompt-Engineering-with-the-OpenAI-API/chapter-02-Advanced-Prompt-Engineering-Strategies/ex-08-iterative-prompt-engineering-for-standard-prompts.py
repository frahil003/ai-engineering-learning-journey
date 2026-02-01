import responseHelper as rs 

# Refine the following prompt
prompt = "Give me the top 10 pre-trained language models. create a table with the three columns 'Model Name', 'Release Year' und 'Owning Company'"

response = rs.get_response(0, prompt)

rs.print_response(response)