import tkinter as tk
from tkinter import ttk

def button_func():
    #get the content of the entry
    entry_text = entry.get()
    # label.config(text = "Eloi") 
    label.configure(text = entry_text) # <== better to use
    # label["text"] = "Eloi" #same as config <== better to use

    entry["state"] = "disabled"

def button_func2():
    #get the content of the entry
    entry_text = "Label"

    label.configure(text = entry_text)

    entry["state"] = "enabled"

#window
window = tk.Tk()

window.title("Getting and setting widgets")

#widgets
label = ttk.Label(master = window, text = "Label")
label.pack()

entry = ttk.Entry(master = window)
entry.pack()

button = ttk.Button(master = window, text = "Button", command = button_func)
button.pack()

button2 = ttk.Button(master = window, text = "Back", command = button_func2)
button2.pack()

#run
window.mainloop()



