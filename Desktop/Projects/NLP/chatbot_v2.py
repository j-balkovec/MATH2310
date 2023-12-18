"""_Sentiment Analysis ChatBot_
@author:
    Jakob Balkovec

@date:
    December 16th, 2023

@version:
    2.0

@license:
    This code is licensed under the MIT License.

@file:
    chatbot_v2.py

@description:
    This script implements a sentiment analysis algorithm that determines the sentiment 
    polarity (positive, negative, or neutral) of textual data. 
    The data is displayed in a neat looking GUI made with the customtkinter module.
    
@usage:
    Run this script with the necessary dependencies installed and provide the text data to be analyzed. 
    The algorithm will output the sentiment polarity score for each input.
    
@note:
Python 3.11.2 64-bit env to run customtkinter module
"""

"""__imports__"""
import json
import tkinter as tk
from src.src import get_sentiment
from tkinter import *
import customtkinter as ctk

"""__constants__"""
WINDOW_SIZE: str = "600x400"
WINDOW_TITLE: str = "Sentiment Analysis Chatbot"

FONT_FAMILY: str = "Menlo"
FONT_SIZE: int = 12

UNI_WIDTH: int = 500 #Universal Width
HEIGHT: int = 220

ENTER_KEY: str = "<Return>"

"""__padding_constants__"""
CTK_ENTRY_X_PADDING: int = 50
CTK_ENTRY_Y_PADDING: int = 50

CTK_TEXTBOX_X_PADDING: int = 20
CTK_TEXTBOX_Y_PADDING: int = 20

CTK_BUTTON_X_PADDING: int = 50
CTK_BUTTON_Y_PADDING: int = 5

class SentimentChatbotGUI(ctk.CTkFrame):
  """
  A GUI class for a Sentiment Analysis Chatbot.

  Attributes:
    master (ctk.CTkFrame): The main frame of the GUI.
    input_entry (ctk.CTkEntry): The entry field for user input.
    output_text (ctk.CTkTextbox): The text box for displaying chatbot responses.
    analyze_button (ctk.CTkButton): The button for analyzing user input.
    exit_button (ctk.CTkButton): The button for exiting the chatbot.
  """

  def __init__(self, root):
    """
    Initializes the SentimentChatbotGUI.

    Args:
      root: The root window of the GUI.
    """
    root.geometry(WINDOW_SIZE)
    root.title(WINDOW_TITLE)

    """__frame__
    Initializes the main frame of the GUI.
    """
    self.master = ctk.CTkFrame(root)
    self.master.pack(expand=True, fill="both")

    """__font__
    Initializes the font for the GUI.
    """
    my_font = ctk.CTkFont(family=FONT_FAMILY, size=FONT_SIZE)

    """__entry__
    Initializes the entry field for user input.
    """
    self.input_entry = ctk.CTkEntry(self.master, placeholder_text="Message SA Chatbot...", width=UNI_WIDTH, font=my_font)
    self.input_entry.pack(side=tk.BOTTOM, padx=(CTK_ENTRY_X_PADDING, CTK_ENTRY_X_PADDING), pady=(0, CTK_ENTRY_Y_PADDING), fill=tk.X)

    """__textbox__
    Initializes the text box for displaying chatbot responses.
    """
    self.output_text = ctk.CTkTextbox(self.master, width=UNI_WIDTH, height=HEIGHT, font=my_font)
    self.output_text.pack(side=tk.TOP, padx=(CTK_TEXTBOX_X_PADDING, CTK_TEXTBOX_X_PADDING), pady=(CTK_TEXTBOX_Y_PADDING, 0), fill=tk.Y)

    """__buttons__
    Initializes the buttons for analyzing user input.
    """
    self.analyze_button = ctk.CTkButton(self.master, text="Analyze", command=self.analyze_sentence, font=my_font)
    self.analyze_button.pack(side=tk.LEFT, padx=(CTK_BUTTON_X_PADDING, CTK_BUTTON_Y_PADDING), pady=5)

    """__buttons__
    Exit button.
    """
    self.exit_button = ctk.CTkButton(self.master, text="Exit", command=root.destroy, font=my_font)
    self.exit_button.pack(side=tk.RIGHT, padx=(CTK_BUTTON_Y_PADDING, CTK_BUTTON_X_PADDING), pady=5)

    """__bind__
    Binds the ENTER_KEY to the input entry field.
    """
    self.input_entry.bind(ENTER_KEY, lambda event: self.analyze_sentence())

  def analyze_sentence(self):
    """
    Analyzes the user input and displays the chatbot's response.
    """
    sentence = self.input_entry.get()
    if sentence:
      response = chatbot_response(sentence)
      self.output_text.insert(tk.END, f"You: \"{sentence}\"\nChatbot: {response}\n\n")
      self.output_text.yview(tk.END)
      self.input_entry.delete(0, tk.END)

def chatbot_response(sentence: str) -> str:
  """
  Generates a response from the chatbot based on the given sentence.

  Args:
    sentence (str): The input sentence to generate a response for.

  Returns:
    str: The generated response in JSON format.
  """
  data = get_sentiment(sentence)
  json_data = json.dumps(data, indent=4, separators=(',', ': '))
  return f"\n{json_data}"

def main():
  """
  Main function to initialize and run the sentiment chatbot GUI.

  This function sets the appearance mode and color theme of the GUI,
  creates the root window, and initializes the SentimentChatbotGUI object.
  Finally, it starts the main event loop to handle user interactions.

  Args:
    None

  Returns:
    None
  """
  ctk.set_appearance_mode("dark")
  ctk.set_default_color_theme("green")
  root = ctk.CTk()
  gui = SentimentChatbotGUI(root)
  root.mainloop()

if __name__ == "__main__":
  main()
