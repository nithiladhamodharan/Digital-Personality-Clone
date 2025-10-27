# app.py
# Digital Personality Clone - Basic Chatbot using OpenAI

import openai

# Replace with your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

print("🤖 Digital Personality Clone Ready! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Goodbye 👋")
        break

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )

    print("AI:", response["choices"][0]["message"]["content"])
