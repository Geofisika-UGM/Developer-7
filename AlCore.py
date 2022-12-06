from tkinter import *
from tkinter import Canvas
import threading
def chose(jns,jml):
    def cetak_ser(j):
        root=Tk()
        root.title('Rangkaian Seri')
        res = []
        root.geometry("300x{}".format(j*50+30))
        for i in range(j):
            bawah=i*50
            bwhbwh= bawah+20
            x = Label(root,text='Resistor {}'.format(i+1))
            x.place(x=20,y=bawah)
            en = Entry(root)
            en.place(x=20,y=bwhbwh)
            res.append(en)

        def hitung():
            resfix=[]
            for i in res:
                resfix.append(float(i.get()))
            r=0
            for i in resfix:
                r+=i
            pr(r)
        def pr(txt):
            root=Tk()
            root.title('Hasil')
            root.geometry("50x50")
            canvas = Canvas(root, width=50, height=50)
            canvas.create_text(25, 25, text=txt, fill="black", font=('Helvetica 15 bold'))
            canvas.pack()
            root.mainloop()

        Button(root,text="Hitung",command=hitung).place(x=20, y=j*50)
        root.mainloop()

    def cetak_par(j):
        root=Tk()
        root.title('Rangkaian Paralel')
        res = []
        root.geometry("300x{}".format(j*50+30))
        for i in range(j):
            bawah=i*50
            bwhbwh= bawah+20
            x = Label(root,text='Resistor {}'.format(i+1))
            x.place(x=20,y=bawah)
            en = Entry(root)
            en.place(x=20,y=bwhbwh)
            res.append(en)

        def hitung():
            resfix=[]
            for i in res:
                resfix.append(float(i.get()))
            r=0
            for i in resfix:
                r+=1/i
            rfix=r**(-1)
            pr(rfix)
        def pr(txt):
            root=Tk()
            root.title('Hasil')
            root.geometry("50x50")
            canvas = Canvas(root, width=50, height=50)
            canvas.create_text(25, 25, text=txt, fill="black", font=('Helvetica 15 bold'))
            canvas.pack()
            root.mainloop()
        Button(root,text="Hitung",command=hitung).place(x=20, y=j*50)
        root.mainloop()
    jmlh=jml
    if jns=='seri':
        cetak_ser(jmlh)
        
    if jns=='par':
        cetak_par(jmlh)