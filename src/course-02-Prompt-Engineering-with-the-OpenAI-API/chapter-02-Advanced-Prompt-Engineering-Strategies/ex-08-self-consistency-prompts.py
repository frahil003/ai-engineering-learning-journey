import responseHelper as rs

# Create the self_consistency instruction
self_consistency_instruction = "Act as three independent experts. Each expert solve the problem on his own way. Combine the results with a majority vote. "

# Create the problem to solve
problem_to_solve = "If you own a store that sells laptops and mobile phones. You start your day with 50 devices in the store, out of which 60% are mobile phones. Throughout the day, three clients visited the store, each of them bought one mobile phone, and one of them bought additionally a laptop. Also, you added to your collection 10 laptops and 5 mobile phones. How many laptops and mobile phones do you have by the end of the day?"

# Create the final prompt
prompt = self_consistency_instruction + problem_to_solve

response = rs.get_response(0, prompt)

rs.print_response(response)