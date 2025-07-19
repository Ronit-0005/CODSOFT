def simple_chatbot():

    print("Hello!!! I'm a simple ChatBot.")
    print("Type 'hi'/'hello'/'hey' to continue.")
    print("Type help for help.")
    print("Type 'stop' to end the conversation.")

    while True:
        user_input = input("You: ").lower()

        if user_input in ['hi', 'hello', 'hey']:
            print("Bot: Hello! How can I help you today?")

        elif "your name" in user_input:
            print("Bot: I am a simple chatbot name Rio created by a Ronit!")

        elif 'how are you' in user_input:
            print("Chatbot: I'm doing great — Thanks for asking! 😊")

        elif 'time' in user_input:
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M")
            print(f"Chatbot: The current time is {current_time}.")

        elif 'thank' in user_input:
            print("Chatbot: You're welcome! Is there anything else I can help with?")

        elif "help" in user_input:
            print("Bot: Sure! You can ask me things like:\n - What's your name?\n - How are you?\n - what is the time?\n - Say Hi/hello/thank")

        elif user_input == 'stop':
            print("Chatbot: Goodbye! Have a nice day!")
            break

        else:
            print("Chatbot: I'm sorry, I didn't understand that. Could you try asking something else?")

simple_chatbot()