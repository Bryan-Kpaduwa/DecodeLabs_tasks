"""
Simple Rule-Based Chatbot"""

def get_response(user_input):
    """Return a bot response based on simple keyword matching."""
    text = user_input.lower().strip()

    # --- Greetings ---
    if text in ("hi", "hello", "hey", "hola", "yo"):
        return "Hello there! How can I help you today?"

    elif "how are you" in text:
        return "I'm just a program, but I'm running smoothly! How about you?"

    elif "your name" in text:
        return "I'm ChatBot 1.0, a simple rule-based assistant."

    # --- Small talk ---
    elif "weather" in text:
        return "I can't check live weather, but I hope it's nice where you are!"

    elif "help" in text:
        return "I can chat about greetings, my name, the weather, or jokes. Try me!"

    elif "joke" in text:
        return "Why did the programmer quit? Because they didn't get arrays!"

    elif "thank you" in text:
        return "You're welcome!"

    # --- Exit commands ---
    elif text in ("exit", "quit", "bye", "goodbye", "stop"):
        return "EXIT"

    # --- Fallback ---
    else:
        return "Sorry, I didn't quite understand that. Could you rephrase?"


def run_chatbot():
    print("=" * 50)
    print(" Simple Rule-Based Chatbot")
    print(" Type 'exit', 'quit', or 'bye' to end the chat.")
    print("=" * 50)

    while True:
        user_input = input("You: ")

        if not user_input.strip():
            print("Bot: Please type something!")
            continue

        response = get_response(user_input)

        if response == "EXIT":
            print("Bot: Goodbye! Have a great day.")
            break
        else:
            print(f"Bot: {response}")


if __name__ == "__main__":
    run_chatbot()