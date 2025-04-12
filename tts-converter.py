import pyttsx3
import tkinter as tk
from tkinter import messagebox

# Function to execute text-to-speech
def save_speech():
    # Get user inputs from the GUI
    text = text_entry.get("1.0", tk.END).strip()
    voice_choice = voice_var.get()
    filename = filename_entry.get().strip()

    # Ensure text and filename are not empty
    if not text:
        messagebox.showerror("Error", "Please enter some text.")
        return

    if not filename:
        filename = "output"

    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Get available voices
    voices = engine.getProperty('voices')

    # Set the chosen voice to male only
    for voice in voices:
        if "male" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break

    # Set speech rate and volume
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)

    # Save speech to file
    engine.save_to_file(text, filename + ".mp3")
    engine.runAndWait()

    # Notify the user
    messagebox.showinfo("Success", f"Audio saved as '{filename}.mp3'")

# Create the main window
root = tk.Tk()
root.title("Text-to-Speech Converter")

# Create a label for the text input
text_label = tk.Label(root, text="Enter text to convert to speech:")
text_label.pack(pady=5)

# Create a text box for input
text_entry = tk.Text(root, height=10, width=40)
text_entry.pack(pady=5)

# Create a label for voice selection
voice_label = tk.Label(root, text="Select voice:")
voice_label.pack(pady=5)

# Create radio buttons for voice selection (only Male)
voice_var = tk.StringVar(value="Male")
male_voice_rb = tk.Radiobutton(root, text="Male", variable=voice_var, value="Male")
male_voice_rb.pack()

# Create a label for filename input
filename_label = tk.Label(root, text="Enter output filename (without extension):")
filename_label.pack(pady=5)

# Create an entry box for filename input
filename_entry = tk.Entry(root, width=30)
filename_entry.pack(pady=5)

# Create a button to save speech
save_button = tk.Button(root, text="Convert to Speech", command=save_speech)
save_button.pack(pady=20)

# Run the GUI loop
root.mainloop()
