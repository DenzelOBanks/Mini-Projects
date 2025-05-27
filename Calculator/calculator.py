from tkinter import *
import ttkbootstrap

root = ttkbootstrap.Window(themename="darkly")
root.title("Calculator App")
root.geometry("400x400")

# Make the rows and columns expandable
for i in range(5):  # Rows 0 to 4
    root.grid_rowconfigure(i, weight=1)
for i in range(4):  # Columns 0 to 3
    root.grid_columnconfigure(i, weight=1)

# Function updates the input and output of the display
def update_display(text):
    current = display_text.get()
    if current == "0":
        display_text.set(text)
    else:
        display_text.set(current + text)

# Function to clear the label
def clear_display():
    display_text.set("0")

# Function turns the string into a result
def calc_sum():
    try:
        calc = eval(display_text.get())
        display_text.set(calc)
    except:
        display_text.set("Error")

# Label to display the numbers
display_text = ttkbootstrap.StringVar()
display_text.set("0")
display_label = ttkbootstrap.Label(root, textvariable=display_text, anchor="e", font=("Helvetica", 20), bootstyle="inverse-light")
display_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Buttons for keypad
btns = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("AC", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for (text, row, col) in btns:
    if text == "AC":
        action = clear_display
    elif text == "=":
        action = calc_sum
    else:
        action = lambda x=text: update_display(x)
    btn = ttkbootstrap.Button(root, text=text, command=action)
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Run application
root.mainloop()
