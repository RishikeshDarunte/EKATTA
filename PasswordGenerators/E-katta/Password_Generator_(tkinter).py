import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(entry.get())
        if length < 5:
            messagebox.showwarning("Invalid Input", "Password length must be at least 5.")
            return
        
        alpha_count = length * 50 // 100
        num_count = length * 30 // 100
        special_count = length - (alpha_count + num_count)
        
        alphabets = random.choices(string.ascii_letters, k=alpha_count)
        numbers = random.choices(string.digits, k=num_count)
        specials = random.choices("@#$%&*", k=special_count)
        
        password_list = alphabets + numbers + specials
        random.shuffle(password_list)
        
        password = ''.join(password_list)
        result_label.config(text=f"Generated Password: {password}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Enter Password Length:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

result_label = tk.Label(root, text="Generated Password: ", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()

