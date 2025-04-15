def load_responses():
    responses = {
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm just a program, but I'm functioning as expected!",
        "what is your name": "I'm your friendly chatbot.",
        "bye": "Goodbye! Have a great day!",
        "what is ai": "AI stands for Artificial Intelligence, the simulation of human intelligence in machines.",
        "what is machine learning": "Machine learning is a subset of AI that involves training algorithms to learn from data."
    }
    return responses
def main():
    print("Chatbot: Hello! Type 'bye' to end the chat.")
    responses = load_responses()
    while True:
        user_input = input("You: ").lower()
        if user_input == "bye":
            print("Chatbot: Goodbye!")
            break
        print("Chatbot:", responses.get(user_input, "Sorry, I didn't understand that."))
if __name__ == "__main__":
    main()