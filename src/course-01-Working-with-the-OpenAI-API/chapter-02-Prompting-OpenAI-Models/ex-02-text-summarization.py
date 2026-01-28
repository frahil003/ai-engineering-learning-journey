from openai import OpenAI

client = OpenAI()

# Text to summarize
text_to_summarize = """Die Rollen und Verantwortlichkeiten eines AI Engineers umfassen vor allem die Überführung von KI in den produktiven Einsatz:
- Integration von KI-Modellen in Software- und Produktarchitekturen
- Aufbau von Datenpipelines (Ingestion, Vorverarbeitung, Qualitätssicherung)
- Deployment & MLOps (CI/CD, Versionierung, Rollbacks)
- Monitoring & Wartung (Performance, Drift, Kosten, Latenz)
- Output Control & Sicherheit (Guardrails, Prompting, Reduktion von Halluzinationen)
- Skalierung & Optimierung (Ressourcen, Kosten, Effizienz)
- Zusammenarbeit mit Data Scientists, Product und Engineering
- Compliance & Responsible AI (Datenschutz, Fairness, Nachvollziehbarkeit)
Die Rollen und Verantwortlichkeiten eines AI Engineers umfassen die Konzeption, Entwicklung, Integration und den Betrieb von KI-Systemen, die reale Probleme lösen. AI Engineers bauen und integrieren Machine-Learning-Modelle, implementieren Datenpipelines für Sammlung, Bereinigung und Aufbereitung von Daten und sorgen für sauberes Training, Testen und Optimieren der Modelle. Ein zentraler Schwerpunkt liegt auf Deployment, Skalierung und MLOps, einschließlich Monitoring von Performance, Drift, Latenz und Kosten sowie der Fehleranalyse im Betrieb. Darüber hinaus verantworten sie Sicherheit, Output Control und Responsible AI (z. B. Datenschutz, Fairness, Nachvollziehbarkeit). In enger Zusammenarbeit mit Data Scientists, Software Engineers, Product Ownern und weiteren Stakeholdern stellen AI Engineers sicher, dass KI-Lösungen zuverlässig, effizient und an den Geschäftszielen ausgerichtet sind."""

# Use an f-string to format the prompt
prompt = f"""Summarize the following text into two concise bullet points:
{text_to_summarize}"""

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "user", "content": prompt}],
  max_completion_tokens=800            
)

print(response.choices[0].message.content)
