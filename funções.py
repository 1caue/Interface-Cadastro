from tkinter import *
from functools import partial

def botão(a, b, w, x, y):
    bt = Button(a, width=w, text=b)
    bt.place(x=x, y=y)

def caixa(a, x, y):
    ed = Entry(a)
    ed.place(x=x, y=y)

def frase(a, b, x, y):
    lb = Label(a, text=b)
    lb.place(x=x, y=y)
