import os
import webbrowser
import subprocess
import datetime


def execute_command(command):
    command = command.lower()

    # Open Notepad
    if "open notepad" in command:
        try:
            os.system("notepad")
        except Exception:
            print("Unable to open Notepad.")

    # Open Calculator
    elif "open calculator" in command or "open calc" in command:
        try:
            os.system("calc")
        except Exception:
            print("Unable to open Calculator.")

    # Open Paint
    elif "open paint" in command:
        try:
            os.system("mspaint")
        except Exception:
            print("Unable to open Paint.")

    # Open Command Prompt
    elif "open command prompt" in command or "open cmd" in command:
        try:
            os.system("start cmd")
        except Exception:
            print("Unable to open Command Prompt.")

    # Open Chrome
    elif "open chrome" in command:
        try:
            chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            subprocess.Popen(chrome_path)
        except Exception:
            webbrowser.open("https://www.google.com")

    # Search Google
    elif "search" in command:
        search_query = command.replace("search", "").strip()

        if search_query == "":
            webbrowser.open("https://www.google.com")
        else:
            webbrowser.open(
                "https://www.google.com/search?q=" + search_query.replace(" ", "+")
            )

    # Open YouTube
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")

    # Open Gmail
    elif "open gmail" in command:
        webbrowser.open("https://mail.google.com")

    # Open GitHub
    elif "open github" in command:
        webbrowser.open("https://github.com")

    # Open LinkedIn
    elif "open linkedin" in command:
        webbrowser.open("https://linkedin.com")

    # Tell Time
    elif "time" in command:
        print(datetime.datetime.now().strftime("%I:%M %p"))

    # Tell Date
    elif "date" in command:
        print(datetime.datetime.now().strftime("%d-%m-%Y"))

    # Exit
    elif "exit" in command or "bye" in command:
        print("Closing Assistant...")
        exit()

    else:
        print("No matching system command found.")