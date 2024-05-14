
import tkinter as tk
import string
import secrets

def assess_strength(password_length):
    if password_length < 6:
        return "Weak"
    elif 6 <= password_length <= 10:
        return "Medium"
    else:
        return "Very Strong"

def generate_password():
    password_length = secrets.randbelow(14) + 2  # Random length between 2 and 15
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(password_length))
    result_label.config(text=password)
    strength_label.config(text=f"Strength: {assess_strength(password_length)}")

# Create main window
root = tk.Tk()
root.title("Password Generator")

# Welcome message
welcome_message = tk.Label(root, text="Welcome to Tex Password Generator!")
welcome_message.pack(pady=10)

# Create widgets
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

strength_label = tk.Label(root, text="")
strength_label.pack(pady=10)

# Start the main loop
root.mainloop()
