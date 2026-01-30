def chatbot():
    print("Bot: Hello! I'm a simple chatbot.")
    print("Bot: Type 'hi' to start the chat")
    print("Bot: Type 'bye' to end the chat.\n")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "bye":
            print("Bot: Goodbye! Have a nice day 😊")
            break

        elif "hello" in user_input or "hi" in user_input:
            print("Bot: Hi there! How can I help you?")

        elif "how are you" in user_input:
            print("Bot: I'm doing great! Thanks for asking.")

        elif "your name" in user_input:
            print("Bot: I'm a beginner-friendly chatbot 🤖")

        elif "help" in user_input:
            print("Bot: I can respond to greetings, simple questions, and say bye.")

        else:
            print("Bot: Sorry, I didn't understand that.")

chatbot()