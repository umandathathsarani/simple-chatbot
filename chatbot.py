import sys
import random

class RuleBasedChatbot:
    def __init__(self):
        self.rules = {
            "hello": ["Hello! How can I help you today?", "Hi! Great to see you.", "Greetings!"],
            "hi": ["Hi there! What can I do for you?", "Hello!", "Hey!"],
            "hey": ["Hey! How's it going?", "Hey there!", "What's up?"],
            "your name": ["I am a simple rule-based chatbot.", "You can call me Chatbot."],
            "who are you": ["I am a rule-based virtual assistant.", "Just a simple bot written in Python."],
            "help": ["You can ask me simple questions like 'hi', 'your name', or 'bye'."],
            "bye": ["Goodbye! Have a wonderful day!", "See you later!", "Bye!"],
            "exit": ["Goodbye! Have a wonderful day!", "See you later!"]
        }
        self.fallback_responses = [
            "I am sorry, I do not understand that.",
            "Could you try phrasing that differently?",
            "I'm still learning. Can you rephrase?"
        ]

    def get_response(self, user_input):
        cleaned_input = user_input.lower().strip()
        
        for keyword, responses in self.rules.items():
            if keyword in cleaned_input:
                return random.choice(responses)
                
        return random.choice(self.fallback_responses)

    def start_chat(self):
        print("Chatbot: Hello! Type 'bye' or 'exit' to end the conversation.")
        
        while True:
            try:
                user_input = input("You: ")
            except (KeyboardInterrupt, EOFError):
                print("\nChatbot: Goodbye!")
                sys.exit()
                
            if user_input.lower().strip() in ["bye", "exit"]:
                print(f"Chatbot: {self.get_response(user_input)}")
                break
                
            response = self.get_response(user_input)
            print(f"Chatbot: {response}")

if __name__ == "__main__":
    bot = RuleBasedChatbot()
    bot.start_chat()