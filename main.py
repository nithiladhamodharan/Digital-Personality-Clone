import os
import requests
import pyttsx3


# Initialize the Perplexity client
client = Perplexity(api_key=os.environ.get("PERPLEXITY_API_KEY"))


def ask_perplexity(prompt):
    headers = {
        "Authorization": f"Bearer {os.environ.get('PERPLEXITY_API_KEY')}",
        "Content-Type": "application/json"
    }
    json_data = {
        "model": "sonar-pro",  # official model name from Perplexity docs
        "messages": [
            {"role": "system", "content": "You are a kind, empathetic assistant that supports the user's emotional wellbeing."},
            {"role": "user", "content": prompt}
        ]
    }
    response = requests.post(
        "https://api.perplexity.ai/chat/completions",
        headers=headers,
        json=json_data
    )
    print("DEBUG:", response.status_code, response.text)
    data = response.json()
    if "choices" in data:
        return data["choices"][0]["message"]["content"]
    else:
        return f"API Error: {data.get('error', data)}"


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Hello, I'm your assistant. How are you feeling today?")
    while True:
        user_input = input("You: ")
        if not user_input.strip():
            speak("I didn't catch that. Please try again.")
            continue
        if user_input.lower() in ["exit", "quit", "goodbye", "stop"]:
            speak("Take care! I'm always here to listen if you need me.")
            break
        response = ask_perplexity(user_input)
        print("Assistant:", response)
        speak(response)