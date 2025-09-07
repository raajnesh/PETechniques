import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
print(API_KEY)
API_URL = "https://api.groq.com/openai/v1/chat/completions"  # Example endpoint

def ask_cricket_question(question):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "openai/gpt-oss-20b",  # Example model name
        "messages": [
            {"role": "user", "content": question}
        ]
    }
    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code == 200:
        answer = response.json()["choices"][0]["message"]["content"]
        return answer
    else:
        return f"Error: {response.status_code} - {response.text}"





if __name__ == "__main__":
    question = input("Ask any cricket question: ")
    print(ask_cricket_question(question))