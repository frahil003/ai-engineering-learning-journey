# AI Engineering for Developers 🚀

## Setup and Configuration

---

1. Start a new Python-Project with the python-starter-kit
2. Create an API key in the OpenAI-Dashboard
3. Export the API key as an enviroment variable
   For example globally:
   ```
   nano ~/.bashrc
   export OPENAI_API_KEY="sk-xxxxxxxxxx"
   source ~/.bashrc
   ```
4. Installing the OpenAI SDK
   with python: Add module openai to requirements-dev.in:

   ```
   module a
   module b
   module c
   openai
   ```

   Generating <u>requirements-dev.txt</u> and installing dependencies:

   ```
   *bash*

   pip-compile requirements-dev.in
   pip install -r requirements-dev.txt
   ```

5. Creating a file test-api-call.py and testing a basic API request

   ```
    from openai import OpenAI
    client = OpenAI()

    response = client.responses.create(
    model="gpt-5-nano",
    input="Write a one-sentence bedtime story about a unicorn."
    )

    print(response.output_text)
   ```

Next steps will follow - stay tuned...
