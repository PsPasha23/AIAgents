from llm_service import ask_ai

messages = [
    {"role": "system", 
     "content": "You are a friendly AI tutor. Explain concepts in simple terms and provide examples when possible."
    },
]

print("Welcome to the AI Tutor!")
print("Type 'exit' or 'quit' to quit.")

while True: 
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    messages.append({"role": "user", "content": user_input})
    response = ask_ai(messages)
   
    messages.append({"role": "assistant", "content": response})
    print(f"AI Tutor: {response}")
    
    