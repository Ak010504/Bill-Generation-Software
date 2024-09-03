import tkinter as tk
from tkinter import filedialog

def open_file_dialog():
    file_path = filedialog.askopenfilename()
    if file_path:
        print(f"Selected file: {file_path}")
        # You can do further processing with the selected file path here

# Create the main window
root = tk.Tk()
root.title("File Selection Demo")

# Create a button to trigger file selection
button = tk.Button(root, text="Open File", command=open_file_dialog)
button.pack(pady=20)

# Run the main event loop
root.mainloop()