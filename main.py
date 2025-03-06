import openai

# Set your OpenAI API key
OPENAI_API_KEY = "your_openai_api_key"

openai.api_key = OPENAI_API_KEY

def chat_with_ai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    print("🤖 NexusAI Chatbot is running! Type 'exit' to stop.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye! 👋")
            break
        
        ai_response = chat_with_ai(user_input)
        print("NexusAI:", ai_response)
