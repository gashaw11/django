import tkinter as tk

# Create the main window
root = tk.Toplevel()
root.title("Simple Tkinter App")
root.geometry("300x200")  # Set window size

# Create a label
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 14))
label.pack(pady=20)  # Add spacing

# Create a button
def on_click():
    label.config(text="Button Clicked!")

button = tk.Button(root, text="Click Me", command=on_click)
button.pack()

# Run the Tkinter event loop
root.mainloop()



