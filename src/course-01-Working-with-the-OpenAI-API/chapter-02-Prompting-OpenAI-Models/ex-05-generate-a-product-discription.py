from openai import OpenAI

client = OpenAI()

prompt = """Schreibe eine Produktbeschreibung für SonicPro Kopfhörer. Hebe die folgenden Besonderheiten hervor: Aktive Rauschunterdrückung (ARD), 40 Stunden Batterielaufzeit und klappbares Design."""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    # Experiment with max_completion_tokens and temperature settings
    max_completion_tokens=700,
    temperature=1)

print(response.choices[0].message.content)

