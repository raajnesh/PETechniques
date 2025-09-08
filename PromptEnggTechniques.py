# Demonstrating different prompt engineering styles

prompts = {
    "zero_shot": "Who won the ICC Cricket World Cup in 2019?",
    "few_shot": """Q: Who won the ICC Cricket World Cup in 2015?
A: Australia
Q: Who won the ICC Cricket World Cup in 2019?
A:""",
    "role_instruction": "You are a cricket expert. Answer concisely: Who won the ICC Cricket World Cup in 2019?",
    "chain_of_thought": "Let's think step by step. Who won the ICC Cricket World Cup in 2019?",
    "contextual": "Given the following context: 'England defeated New Zealand in the final.' Who won the ICC Cricket World Cup in 2019?"
}

def ask_with_prompt(prompt):
    # ...existing code...
    import os
    import requests
    from dotenv import load_dotenv

    load_dotenv()
    API_KEY = os.getenv("GROQ_API_KEY")
    API_URL = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "openai/gpt-oss-20b",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code == 200:
        answer = response.json()["choices"][0]["message"]["content"]
        return answer
    else:
        return f"Error: {response.status_code} - {response.text}"

if __name__ == "__main__":
    for style, prompt in prompts.items():
        print(f"\nPrompt style: {style}")
        print(f"Prompt:\n{prompt}")
        print("Response:")
        print(ask_with_prompt(prompt))
