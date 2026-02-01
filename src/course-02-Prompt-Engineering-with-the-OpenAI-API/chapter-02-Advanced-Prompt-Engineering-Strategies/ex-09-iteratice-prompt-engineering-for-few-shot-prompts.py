import responseHelper as rs

# Refine the following prompt
prompt = """
Instuctions: Determine the emotion expressed in the following sentences.
Provide only the emotion word as the answer. Possible emotions are: Happiness, Sadness, Fear. If no explicit emotion is expressed, respond with 'no explicit emotion'.
Receiving a promotion at work made me feel on top of the world -> Happiness
The movie's ending left me with a heavy feeling in my chest -> Sadness
Walking alone in the dark alley sent shivers down my spine -> Fear
He is running all day long -> no explicit emotion
Crafting a prompt is like building a house -> no explicit emotion
They watched a movie togehter -> no explicit emotion
They sat and ate their meal -> no explicit emotion
She couldn't help but smile when she saw the puppy ->
I ate a steak ->
"""

response = rs.get_response(0, prompt)

rs.print_response(response)