import json
import tkinter as tk
import tkinter.ttk as ttk
from src.src import get_sentiment

class SentimentChatbotGUI:
    def __init__(self, master):
        self.master = master
        master.title("Sentiment Analysis Chatbot")
        master.geometry("600x400")

        self.chat_frame = tk.Frame(master, bg="gray")
        self.chat_frame.pack(expand=True, fill="both")

        self.output_text = scrolledtext.ScrolledText(self.chat_frame, wrap=tk.WORD, width=60, height=10)
        self.output_text.pack(side=tk.TOP, fill="both", expand=True, padx=10, pady=10)

        # Entry with rounded edges
        self.input_entry = ttk.Entry(self.chat_frame, style="Rounded.TEntry")
        self.input_entry.pack(side=tk.TOP, fill="both", expand=True, padx=10, pady=10)

        self.analyze_button = tk.Button(master, text="Analyze", command=self.analyze_sentence, bg="green", fg="black", padx=10)
        self.analyze_button.pack(side=tk.LEFT, padx=(10, 5), pady=5)

        self.exit_button = tk.Button(master, text="Exit", command=self.master.destroy, bg="green", fg="black", padx=10)
        self.exit_button.pack(side=tk.RIGHT, padx=(5, 10), pady=5)

        # Configure style for rounded Entry
        style = ttk.Style()
        style.configure("Rounded.TEntry", padding=(10, 5), relief="flat", background="gray", borderwidth=5, focuscolor="green", focusthickness=2)

        self.input_entry.bind("<Return>", lambda event: self.analyze_sentence())
        #self.master.bind("<Return>", lambda event: self.analyze_sentence())

    def analyze_sentence(self):
        sentence = self.input_entry.get()
        if sentence:
            response = chatbot_response(sentence)
            self.output_text.insert(tk.END, f"You: \"{sentence}\"\nChatbot: {response}\n\n")
            self.output_text.yview(tk.END)
            self.input_entry.delete(0, tk.END)

def chatbot_response(sentence: str) -> str:
    data = get_sentiment(sentence)
    json_data = json.dumps(data, indent=4, separators=(',', ': '))
    return f"\n{json_data}"

def main():
    root = tk.Tk()
    gui = SentimentChatbotGUI(root)
    gui.analyze_button.configure(bg="green")
    gui.exit_button.configure(bg="green")
    root.mainloop()

if __name__ == "__main__":
    main()

