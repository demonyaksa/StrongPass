import random
import string
import tkinter as tk

def generate_password():
    password_length = int(length_entry.get())
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for _ in range(password_length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_password():
    password = password_entry.get()
    root.clipboard_clear()
    root.clipboard_append(password)

root = tk.Tk()
root.title("Password Generator")

# Center the window on the screen
window_width = 300
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)
root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))

length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0)

length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2)

password_label = tk.Label(root, text="Generated Password:")
password_label.grid(row=2, column=0)

password_entry = tk.Entry(root)
password_entry.grid(row=2, column=1)

copy_button = tk.Button(root, text="Copy Password", command=copy_password)
copy_button.grid(row=3, column=0, columnspan=2)

root.mainloop()
