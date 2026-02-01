import responseHelper as rs

marketing_message = "Introducing our latest collection of premium leather handbags. Each bag is meticulously crafted using the finest leather, ensuring durability and elegance. With a variety of designs and colors, our handbags are perfect for any occasion. Shop now and experience the epitome of style and quality."

# Craft a prompt that translates
prompt = f"""Translate the marketing message delimited in triple backticks to French, Spanish, and Japanese.
```{marketing_message}```
French:
Spanish:
Japanese:"""
 
response = rs.get_response(0, prompt)

print("English:", marketing_message)
print(response)