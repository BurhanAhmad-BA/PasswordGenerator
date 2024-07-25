import customtkinter as ctk
import random
import string
import pyperclip # package for clipboard functionality
import tkinter.messagebox as messagebox

# Function to generate password
def generated_pw():
    try:
        length = int(pw_length_entry.get())
        if length <= 0:
            raise ValueError
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        generated_pw_entry.delete(0, ctk.END)
        generated_pw_entry.insert(0, password)
    except ValueError:
        generated_pw_entry.delete(0, ctk.END)
        generated_pw_entry.insert(0, "Invalid Length")
# Function to copy_to_clipboard
def copy_to_clipboard():
    password = generated_pw_entry.get()
    pyperclip.copy(password)
    messagebox.showinfo("", "Copied")
# Funtion to reset all fields
def reset():
    username_entry.delete(0, ctk.END)
    pw_length_entry.delete(0, ctk.END)
    generated_pw_entry.delete(0, ctk.END)

# Create the main window
root = ctk.CTk()

# Set the title
root.title("Password Generator")

# Set the size of the window
root.geometry("700x600")

# Create a frame for the label and pack it
label_frame = ctk.CTkFrame(master=root)
label_frame.pack(fill="x")

# Create a label and center it within the label_frame
label = ctk.CTkLabel(master=label_frame, text="Password Generator", font=("Default", 30))
label.pack(pady=20)

# Create a frame for the username input
username_frame = ctk.CTkFrame(master=root)
username_frame.pack(pady=20)

# Create and pack the username label and entry side by side within the username_frame
username_label = ctk.CTkLabel(master=username_frame, text="Username")
username_label.pack(side="left", padx=5)

username_entry = ctk.CTkEntry(master=username_frame)
username_entry.pack(side="left", padx=5)

# Create a frame for the Password length input
pw_length_frame = ctk.CTkFrame(master=root)
pw_length_frame.pack(pady=20)

# Create and pack the password length label and entry side by side within the pw_length_frame
pw_length_label = ctk.CTkLabel(master=pw_length_frame, text="Enter Password Length")
pw_length_label.pack(side="left", padx=5)

pw_length_entry = ctk.CTkEntry(master=pw_length_frame)
pw_length_entry.pack(side="left", padx=5)

# Create a frame for the generated password
generated_pw_frame = ctk.CTkFrame(master=root)
generated_pw_frame.pack(pady=20)

# Create and pack the generated password label and entry side by side within the generated_pw_frame
generated_pw_label = ctk.CTkLabel(master=generated_pw_frame, text=" Generated Password")
generated_pw_label.pack(side="left", padx=5)

generated_pw_entry = ctk.CTkEntry(master=generated_pw_frame)
generated_pw_entry.pack(side="left", padx=5)
# Create a button and pack it
button = ctk.CTkButton(master=root, text="Generate", command=generated_pw)
button.pack(pady=10)

button = ctk.CTkButton(master=root, text="Copy to Clipboard", command= copy_to_clipboard)
button.pack(pady=10)

button = ctk.CTkButton(master=root, text="Reset", command= reset)
button.pack(pady=10)

# Run the application
root.mainloop()