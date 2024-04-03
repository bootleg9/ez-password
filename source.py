import tkinter as tk
from tkinter import messagebox, filedialog
import string
import random
import os

def generate_password():
    password = ""
    if include_letters.get():
        password += string.ascii_letters
    if include_numbers.get():
        password += string.digits
    if include_characters.get():
        password += "!@#$%^&*()_+-=[]{}|;:,.<>?`~"
    
    if not password:
        messagebox.showerror("Error", "Please select at least one option.")
        return

    length = max_length_var.get()
    password = ''.join(random.choice(password) for i in range(length))
    save_location = save_location_entry.get()
    note = note_entry.get()

    if not save_location:
        messagebox.showerror("Error", "Please select a directory to save the password.")
        return

    file_path = os.path.join(save_location, "passwords.txt")

    # Ensure the directory exists, if not, create it
    if not os.path.exists(save_location):
        os.makedirs(save_location)

    # Read existing passwords
    existing_passwords = {}
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            for line in f:
                parts = line.strip().split(':')
                if len(parts) == 2:
                    existing_passwords[parts[0]] = parts[1]

    # Replace or add the new password
    existing_passwords[note] = password

    # Write the passwords to the file
    with open(file_path, 'w') as f:
        for note, password in existing_passwords.items():
            f.write(f"{note}:{password}\n")

    # Display the generated password in the GUI
    password_display.config(text=password)
    messagebox.showinfo("Password Generated", "Password saved successfully.")

def browse_directory():
    save_location = filedialog.askdirectory()
    save_location_entry.delete(0, tk.END)
    save_location_entry.insert(0, save_location)

root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x400")

font_style = "Helvetica 12 bold"
label_style = "Helvetica 10 bold"
entry_style = "Helvetica 10"
button_style = "Helvetica 10 bold"

include_letters = tk.BooleanVar()
include_numbers = tk.BooleanVar()
include_characters = tk.BooleanVar()
max_length_var = tk.IntVar()
note_var = tk.StringVar()

include_letters.set(True)
include_numbers.set(True)
include_characters.set(True)
max_length_var.set(8)

options_frame = tk.Frame(root)
options_frame.pack(pady=10)

tk.Checkbutton(options_frame, text="Include Letters", variable=include_letters, font=font_style).grid(row=0, column=0, sticky="w")
tk.Checkbutton(options_frame, text="Include Numbers", variable=include_numbers, font=font_style).grid(row=1, column=0, sticky="w")
tk.Checkbutton(options_frame, text="Include Special Characters", variable=include_characters, font=font_style).grid(row=2, column=0, sticky="w")

length_frame = tk.Frame(root)
length_frame.pack(pady=10)

tk.Label(length_frame, text="Max Length:", font=label_style).grid(row=0, column=0, padx=5)
tk.Entry(length_frame, textvariable=max_length_var, font=entry_style).grid(row=0, column=1, padx=5)

note_frame = tk.Frame(root)
note_frame.pack(pady=10)

tk.Label(note_frame, text="Note (optional):", font=label_style).grid(row=0, column=0, padx=5)
note_entry = tk.Entry(note_frame, textvariable=note_var, font=entry_style, width=40)
note_entry.grid(row=0, column=1, padx=5)

save_location_frame = tk.Frame(root)
save_location_frame.pack(pady=10)

tk.Label(save_location_frame, text="Save Location:", font=label_style).grid(row=0, column=0, padx=5)
save_location_entry = tk.Entry(save_location_frame, font=entry_style, width=40)
save_location_entry.grid(row=0, column=1, padx=5)

browse_button = tk.Button(save_location_frame, text="Browse", command=browse_directory, font=button_style)
browse_button.grid(row=0, column=2, padx=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password, font=button_style)
generate_button.pack(pady=10)

password_display_frame = tk.Frame(root)
password_display_frame.pack(pady=10)

password_display_label = tk.Label(password_display_frame, text="Generated Password:", font=label_style)
password_display_label.grid(row=0, column=0)

password_display = tk.Label(password_display_frame, text="", relief="solid", width=20, font=font_style)
password_display.grid(row=0, column=1)

root.mainloop()
