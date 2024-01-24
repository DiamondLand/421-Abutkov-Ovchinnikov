import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk

image1 = Image.open("formula.jpg")
root = tk.Tk()


root.geometry("600x600")

img = ImageTk.PhotoImage(Image.open("formula.jpg"))
panel = tk.Label(root, image=img)
panel.grid(row=0, column=0, columnspan=4)

tk.Label(text="X").grid(row=1, column=0)
entr1 = tk.Entry(width=20)
entr1.grid(row=1, column=1)

tk.Label(text="M").grid(row=2, column=0)
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


def CallBack():
    global var, entr1, entr2
    print(var.get())
    print(entr1.get())
    print(entr2.get())


B = tk.Button(root, text="Hello", command=CallBack)
B.grid(row=4, column=0, columnspan=3)

txt1 = tk.Label(text="Ответ: ")
txt1.grid(row=5, column=0)
root.mainloop()
