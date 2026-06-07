import sys

def get_bot_response(user_input):
    cleaned_input = user_input.lower().strip()
    
    rules = {
        "hello": "Hello! How can I help you today?",
        "hi": "Hi there! What can I do for you?",
        "hey": "Hey! How's it going?",
        "your name": "I am a simple rule-based chatbot created in Python.",
        "who are you": "I am a rule-based virtual assistant.",
        "help": "You can ask me simple questions like 'hi', 'your name', or 'bye'.",
        "bye": "Goodbye! Have a wonderful day!",
        "exit": "Goodbye! Have a wonderful day!"
    }
    
    for keyword, response in rules.items():
        if keyword in cleaned_input:
            return response
            
    return "I am sorry, I do not understand that. Could you try phrasing it differently?"

def start_chat():
    print("Chatbot: Hello! Type 'bye' or 'exit' to end the conversation.")
    
    while True:
        try:
            user_input = input("You: ")
        except (KeyboardInterrupt, EOFError):
            print("\nChatbot: Goodbye!")
            sys.exit()
            
        if user_input.lower().strip() in ["bye", "exit"]:
            print(f"Chatbot: {get_bot_response(user_input)}")
            break
            
        response = get_bot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    start_chat()