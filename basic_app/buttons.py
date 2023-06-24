import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Buttons")
window.geometry("600x400")

def radio_func():
    print(radio_ex_var.get())
    print(check_ex_var.get())
    check_ex_var.set(False)

def button_func():
    print("click")
    print(radio_var.get())

#button
button_string = tk.StringVar(value = "A button with stringvar")
button = ttk.Button(window, text = "A simple button",command = button_func, textvariable=button_string)
button.pack()

#chceckbutton
check_var = tk.IntVar(value=10)
check1 = ttk.Checkbutton(window,
                        text = "Checkbox 1",
                        command = lambda: print(check_var.get()),
                        variable = check_var,
                        onvalue = 10,
                        offvalue= 5)
check1.pack()

check2 = ttk.Checkbutton(window,
                         text = "Checkbox2",
                         command= lambda: print("test"))
check2.pack()

#radio buttons
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(window,
                         text = "Radiobutton 1", 
                         value = "radio 1", 
                         variable= radio_var,
                         command = lambda: print(radio_var.get()),)
radio1.pack()
radio2 = ttk.Radiobutton(window,
                         text = "Radiobutton 2", value = 2,
                         variable= radio_var)
radio2.pack()

#radio ex

radio_ex_var = tk.StringVar()

radio_ex1 = ttk.Radiobutton(window,
                           value= "A",
                           text="A",
                           variable=radio_ex_var,
                           command= radio_func)
radio_ex1.pack()

radio_ex2 = ttk.Radiobutton(window,
                           value= "B",
                           text="B",
                           variable=radio_ex_var,
                           command= radio_func)
radio_ex2.pack()

#checkbox ex

check_ex_var = tk.BooleanVar()

check_ex = ttk.Checkbutton(window,
                           text = check_ex_var.get(),
                           variable=check_ex_var,
                           command=lambda: print(radio_ex_var.get()))
check_ex.pack()


window.mainloop()