import datetime


def get_response(command):
    command = command.lower().strip()

    # Greetings
    if "hello" in command or "hi" in command:
        return "Hello! How can I help you today?"

    elif "how are you" in command:
        return "I'm doing great. Thanks for asking!"

    elif "your name" in command:
        return "I am your AI Capstone Assistant."

    # Date & Time
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."

    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%d %B %Y")
        return f"Today's date is {current_date}."

    # Help
    elif "help" in command:
        return (
            "You can ask me to:\n"
            "- Open Notepad\n"
            "- Open Calculator\n"
            "- Open Chrome\n"
            "- Search Google\n"
            "- Tell the time\n"
            "- Tell the date\n"
            "- Say hello"
        )

    # Exit
    elif "bye" in command or "exit" in command:
        return "Goodbye! Have a nice day."

    # Default response
    else:
        return (
            "Sorry, I don't understand that command. "
            "Type 'help' to see available commands."
        )