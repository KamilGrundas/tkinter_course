import tkinter as tk
from tkinter import ttk

def button_func():
    print("click")

#create window
window = tk.Tk()
window.title("Window and widgets") #title of window
window.geometry("800x500") #size of window

#ttk widgets
label = ttk.Label(master = window,
                  text = "Test")
label.pack()

#create widgets tk.text
text = tk.Text(master = window)
text.pack()


#ttk entry
entry = ttk.Entry(master=window)
entry.pack()

#ttk button

button = ttk.Button(master = window, text="Button", command = button_func) #functions
button2 = ttk.Button(master = window, text="Button2", command = lambda: print("hello")) #simple

button.pack()
button2.pack()
#

#run
window.mainloop() #updates gui, wait for interactions