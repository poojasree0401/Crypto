import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random

def encode_message():
    # Encoding logic here
    pass

def decode_message():
    encoded_message = entry_message.get()
    key = int(entry_key.get())
    attempts = 0

    decoded_message = ""
    for char in encoded_message:
        if char.isalpha():
            shifted = ord(char) - key
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            decoded_message += chr(shifted)
        else:
            decoded_message += char

    entry_result.delete(0, tk.END)
    entry_result.insert(tk.END, decoded_message)

    if decoded_message.lower() != "secret":
        attempts += 1
        if attempts >= 3:
            messagebox.showwarning("Warning", "You've exceeded the maximum attempts.")
            root.destroy()

root = tk.Tk()
root.geometry("400x300")
root.configure(bg='lightgray')

# Create a custom title bar
title_bar = ttk.Frame(root, height=30, style="CustomTitle.TFrame")
title_bar.pack(fill='x')

# Apply a style to the custom title bar
s = ttk.Style()
s.theme_use('clam')
s.configure("CustomTitle.TFrame", background='#663399')  # Background color of the title bar

# Add a label to the title bar
title_label = tk.Label(title_bar, text='Secret Message Encoder/Decoder', font=("Helvetica", 10, "bold"), bg='#663399', fg='white')
title_label.pack(pady=5)

frame = tk.Frame(root, bg='lightgray')
frame.pack(padx=20, pady=20)

label_message = tk.Label(frame, text="Enter Message:", bg='lightgray', font=("Helvetica", 10, "bold"))
label_message.grid(row=0, column=0, padx=10, pady=5)

entry_message = tk.Entry(frame, width=40, font=("Helvetica", 10, "bold"))
entry_message.grid(row=0, column=1, padx=10, pady=5)

label_key = tk.Label(frame, text="Enter Key:", bg='lightgray', font=("Helvetica", 10, "bold"))
label_key.grid(row=1, column=0, padx=10, pady=5)

entry_key = tk.Entry(frame, width=10, font=("Helvetica", 10, "bold"))
entry_key.grid(row=1, column=1, padx=10, pady=5)

def show_wrong_attempts():
    messagebox.showwarning("Warning", "You've exceeded the maximum attempts.")
    root.destroy()

button_encrypt = tk.Button(frame, text="Encrypt", command=encode_message, bg='red', fg='white', width=10, font=("Helvetica", 10, "bold"))
button_encrypt.grid(row=2, column=0, padx=0, pady=10, sticky="ew")

button_decrypt = tk.Button(frame, text="Decrypt", command=decode_message, bg='blue', fg='white', width=10, font=("Helvetica", 10, "bold"))
button_decrypt.grid(row=2, column=1, padx=0, pady=10, sticky="ew")

label_result = tk.Label(frame, text="Result:", bg='lightgray', font=("Helvetica", 10, "bold"))
label_result.grid(row=3, column=0, padx=10, pady=5)

entry_result = tk.Entry(frame, width=40, font=("Helvetica", 10, "bold"))
entry_result.grid(row=3, column=1, padx=10, pady=5)

button_reset = tk.Button(frame, text="Reset", command=lambda: [entry_message.delete(0, tk.END), entry_key.delete(0, tk.END),
                                                               entry_result.delete(0, tk.END)], bg='#CCCCCC', fg='black', width=10, font=("Helvetica", 10, "bold"))
button_reset.grid(row=4, column=0, padx=0, pady=5, sticky="ew")

button_exit = tk.Button(frame, text="Exit", command=root.destroy, bg='#CCCCCC', fg='black', width=10, font=("Helvetica", 10, "bold"))
button_exit.grid(row=4, column=1, padx=0, pady=5, sticky="ew")

root.mainloop()
