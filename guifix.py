from tkinter import *
from tkinter import Tk, Canvas, Frame, BOTH
from AlCore import chose
root = Tk()
root.geometry("200x300")
x1 = Label(root,text = "jumlah\nresistor")
x2= Label(root,text = "jumlah\nresistor")
e1 = Entry(root,width=10)
e2 = Entry(root,width=10)
x1.place(x = 20, y = 20)
e1.place(x = 20, y = 70)
x2.place(x = 120, y = 20)
e2.place(x = 120, y = 70)

def seri():
    a=int(e1.get())
    chose('seri',a)
def paralel():
    b=int(e2.get())
    chose('par',b)


root.title('Menghitung Rangkaian Resistor')
b1 = Button(master = root, command = seri,height = 2, width = 10, text = "Seri")
b1.place(x = 10, y = 100)
b2 = Button(master = root, command = paralel, height = 2,  width = 10, text = "Paralel")
b2.place(x = 110, y = 100)

root.mainloop()