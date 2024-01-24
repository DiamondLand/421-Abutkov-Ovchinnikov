import math
import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk

root = tk.Tk()


root.geometry("600x600")

img = ImageTk.PhotoImage(Image.open("formula.jpg"))
panel = tk.Label(root, image=img)
panel.grid(row=0, column=0, columnspan=4)

tk.Label(text="X").grid(row=1, column=0)
entr1 = tk.Entry(width=20)
entr1.grid(row=1, column=1)

tk.Label(text="Y").grid(row=2, column=0)
entr2 = tk.Entry(width=20)
entr2.grid(row=2, column=1)

var = tk.IntVar()
var.set(0)
var1 = tk.Radiobutton(text="sh(x)", variable=var, value=0)
var2 = tk.Radiobutton(text="x^2", variable=var, value=1)
var3 = tk.Radiobutton(text="e^x", variable=var, value=2)

var1.grid(column=0, row=3)
var2.grid(column=1, row=3)
var3.grid(column=2, row=3)

txt1 = tk.Label(text="Ответ: ")
txt1.grid(row=5, column=0)
entr3 = tk.Entry(width=20)
entr3.grid(row=5, column=1)


def CallBack():
    global var, entr1, entr2, entr3
    print(var.get())
    print(entr1.get())
    print(entr2.get())
    x, y = int(entr1.get()), int(entr2.get())

    if x * y > 0:
        if var.get() == 0:
            res = ((math.sinh(x) + y) ** 2) - ((math.sinh(x) * y) ** (1 / 2))
        elif var.get() == 1:
            res = (((x**2) + y) ** 2) - (((x**2) * x) ** (1 / 2))
        else:
            res = (((math.e**x) + y) ** 2) - (((math.e**x) * y) ** (1 / 2))
    elif x * y < 0:
        if var.get() == 0:
            res = ((math.sinh(x) + y) ** 2) + ((abs(math.sinh(x) * y)) ** (1 / 2))
        elif var.get() == 1:
            res = (((x**2) + y) ** 2) + ((abs(x**2) * y) ** (1 / 2))
        else:
            res = (((math.e**x) + y) ** 2) + ((abs(math.e**x) * y) ** (1 / 2))
    else:
        if var.get() == 0:
            res = ((math.sinh(x) + y) ** 2) + 1
        elif var.get() == 1:
            res = (((x**2) + y) ** 2) + 1
        else:
            res = (((math.e**x) + y) ** 2) + 1
    otvet = str(res)
    entr3.delete(0, tk.END)  # deletes the current value
    entr3.insert(0, otvet + str(entr1.get()))


def Clear():
    global entr1, entr2, entr3
    entr1.delete(0, tk.END)
    entr2.delete(0, tk.END)
    entr3.delete(0, tk.END)


B = tk.Button(root, text="Посчитать", command=CallBack)
B1 = tk.Button(root, text="Почистить", command=Clear)
B.grid(row=4, column=0, columnspan=3)
B1.grid(row=6, column=0, columnspan=3)


root.mainloop()
