import tkinter as tk
from tkinter import ttk

def get_pos(event):
    print(f"x:{event.x} y:{event.y}")

#setup
window = tk.Tk()
window.geometry("600x500")
window.title("Event binding")


entry_string = tk.StringVar(value="test")

#widgets
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window, textvariable= entry_string)
entry.pack()

button = ttk.Button(window,text = "button")
button.pack()

#events
# button.bind("<Alt-KeyPress-a>", lambda event: print(event))
# text.bind("<Motion>", get_pos)

# window.bind("<KeyPress>", lambda event: print(f"pressed {event.char}"))

entry.bind("<FocusIn>", lambda event: print("entry field was selected"))
entry.bind("<FocusOut>", lambda event: print("entry field was selected"))

#https://www.pythontutorial.net/tkinter/tkinter-event-binding/

#run
window.mainloop()