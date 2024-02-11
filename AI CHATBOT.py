import nltk
import random
from nltk.chat.util import Chat, reflections

# Define patterns and responses
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hey there!', 'Hi!']),
    (r'how are you?', ['I am doing well, thank you!', 'I\'m fine, thanks!', 'Pretty good, thanks for asking.']),
    (r'what is your name?', ['You can call me Chatbot.', 'My name is Chatbot.']),
    (r'quit', ['Bye, take care!', 'Goodbye!', 'See you later!']),
    # Add more patterns and responses here
]

# Create a chatbot
chatbot = Chat(patterns, reflections)

def main():
    print("Welcome to the Chatbot!")
    print("Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("Chatbot:", response)
        if user_input.lower() == 'quit':
            break

if __name__ == "__main__":
    main()
