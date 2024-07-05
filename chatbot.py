import tkinter as tk
from tkinter import ttk

class ResponsiveChatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("Responsive FAQ Chatbot")
        self.root.geometry("600x400")
        self.root.configure(bg="#2c3e50")

        self.style = ttk.Style()
        self.style.configure('TLabel', background="#2c3e50", foreground="#ecf0f1", font=("Arial", 12))
        self.style.configure('TButton', background="#2980b9", foreground="#ecf0f1", font=("Arial", 12))
        self.style.configure('TEntry', font=("Arial", 12))

        self.chat_frame = ttk.Frame(root)
        self.chat_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        self.chat_history = tk.Text(self.chat_frame, state='disabled', wrap='word', bg="#34495e", fg="#ecf0f1", font=("Arial", 12), bd=0, padx=10, pady=10)
        self.chat_history.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        self.entry_frame = ttk.Frame(root)
        self.entry_frame.pack(pady=10, padx=10, fill=tk.X)

        self.entry = ttk.Entry(self.entry_frame, font=("Arial", 12))
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        self.entry.bind("<Return>", self.send_message)

        self.send_button = ttk.Button(self.entry_frame, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.LEFT, padx=5)

        self.faqs = {
            "What is your name?": "I am a simple FAQ Chatbot.",
            "How do you work?": "I respond to predefined questions with appropriate answers.",
            "What can you do?": "I can answer basic questions that have been programmed into me.",
            "Who created you?": "I was created by lord Shami.",
            "How can I quit?": "You can quit the application by closing the window."
        }

    def send_message(self, event=None):
        user_message = self.entry.get()
        if user_message:
            self.display_message(f"You: {user_message}", "#ecf0f1")
            self.entry.delete(0, tk.END)
            self.respond(user_message)

    def respond(self, user_message):
        response = self.faqs.get(user_message, "Sorry, I don't understand that question.")
        self.display_message(f"Bot: {response}", "#3498db")

    def display_message(self, message, color):
        self.chat_history.config(state='normal')
        self.chat_history.insert(tk.END, f"{message}\n", ('color',))
        self.chat_history.tag_config('color', foreground=color)
        self.chat_history.config(state='disabled')
        self.chat_history.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ResponsiveChatbot(root)
    root.mainloop()
