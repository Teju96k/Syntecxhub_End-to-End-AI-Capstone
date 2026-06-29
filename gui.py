import tkinter as tk
from tkinter import messagebox

from click import command

from click import command

from face_auth import authenticate_user
from chatbot import get_response
from commands import execute_command
from voice import speak, listen


class AssistantGUI:

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("AI Capstone Assistant")
        self.root.geometry("700x500")

        title = tk.Label(
            self.root,
            text="End-to-End AI Capstone",
            font=("Arial", 18, "bold")
        )
        title.pack(pady=10)

        self.auth_btn = tk.Button(
            self.root,
            text="Authenticate Face",
            command=self.authenticate,
            width=25
        )
        self.auth_btn.pack(pady=5)

        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack(pady=5)

        self.text_btn = tk.Button(
            self.root,
            text="Send Text Command",
            command=self.text_command,
            state="disabled"
        )
        self.text_btn.pack(pady=5)

        self.voice_btn = tk.Button(
            self.root,
            text="Voice Command",
            command=self.voice_command,
            state="disabled"
        )
        self.voice_btn.pack(pady=5)

        self.output = tk.Text(self.root, height=15, width=80)
        self.output.pack(pady=10)

    def authenticate(self):

        self.output.insert(tk.END, "Authenticating...\n")

        if authenticate_user():

            messagebox.showinfo(
                "Authentication",
                "Authentication Successful!"
            )

            speak("Authentication successful.")

            self.voice_btn.config(state="normal")
            self.text_btn.config(state="normal")

        else:

            messagebox.showerror(
                "Authentication",
                "Authentication Failed!"
            )

            speak("Authentication failed.")

    def process(self, command):

        if not command:
            return

        response = get_response(command)

        execute_command(command)

        self.output.insert(tk.END, f"You: {command}\n")
        self.output.insert(tk.END, f"Assistant: {response}\n\n")

        speak(response)

    def text_command(self):

        command = self.entry.get()

        self.entry.delete(0, tk.END)

        self.process(command)

    def voice_command(self):

        self.output.insert("end", "Listening for 5 seconds...\n")

        command = listen()

        if command:
            self.process(command)
        else:
            self.output.insert("end", "No voice command recognized.\n")

    def run(self):

        self.root.mainloop()


if __name__ == "__main__":

    app = AssistantGUI()

    app.run()