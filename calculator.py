from tkinter import *
w = Tk()
w.geometry("320x370")
w.title("Calculator")
w.configure(bg = "black")

ex = ""
n = 0
def click(num):
    global ex
    ex = ex + str(num)
    var.set(ex)

def clr():
    global ex
    ex=""
    var.set(ex)

def bs():
    global ex
    ex = ex[0:n-1]
    var.set(ex)

def eq():
    global ex
    ex = str(eval(ex))
    var.set(ex)

var = StringVar()    
f1 = Frame(w)
f1.pack()
e1 = Entry(f1,font=("arial",23,"bold"),justify = RIGHT, textvariable = var)
e1.pack()

f2=Frame(w)
f2.pack()
b1=Button(f2,text="C",font=("arial",25,"bold"),width=6, command = clr)
b1.pack(side=LEFT)
b1=Button(f2,text="Bksp",font=("arial",25,"bold"),width=6, command = bs)
b1.pack(side=LEFT)
b2=Button(f2,text="/",font=("arial",25,"bold"),width=4,command = lambda:click("/"))
b2.pack(side=LEFT)

f3=Frame(w)
f3.pack()
b4=Button(f3,text="9",font=("arial",25,"bold"),width=4,command = lambda:click("9"))
b4.pack(side=LEFT)
b5=Button(f3,text="8",font=("arial",25,"bold"),width=4,command = lambda:click("8"))
b5.pack(side=LEFT)
b6=Button(f3,text="7",font=("arial",25,"bold"),width=3,command = lambda:click("7"))
b6.pack(side=LEFT)
b7=Button(f3,text="*",font=("arial",25,"bold"),width=4,command = lambda:click("*"))
b7.pack(side=LEFT)

f4=Frame(w)
f4.pack()
b8=Button(f4,text="6",font=("arial",25,"bold"),width=4,command = lambda:click("6"))
b8.pack(side=LEFT)
b9=Button(f4,text="5",font=("arial",25,"bold"),width=4,command = lambda:click("5"))
b9.pack(side=LEFT)
b10=Button(f4,text="4",font=("arial",25,"bold"),width=3,command = lambda:click("4"))
b10.pack(side=LEFT)
b11=Button(f4,text="+",font=("arial",25,"bold"),width=4,command = lambda:click("+"))
b11.pack(side=LEFT)

f5=Frame(w)
f5.pack()
b12=Button(f5,text="3",font=("arial",25,"bold"),width=4,command = lambda:click("3"))
b12.pack(side=LEFT)
b13=Button(f5,text="2",font=("arial",25,"bold"),width=4,command = lambda:click("2"))
b13.pack(side=LEFT)
b14=Button(f5,text="1",font=("arial",25,"bold"),width=3,command = lambda:click("1"))
b14.pack(side=LEFT)
b15=Button(f5,text="-",font=("arial",25,"bold"),width=4,command = lambda:click("-"))
b15.pack(side=LEFT)

f6=Frame(w)
f6.pack()
b16=Button(f6,text="0",font=("arial",25,"bold"),width=6,command = lambda:click("0"))
b16.pack(side=LEFT)
b16=Button(f6,text=".",font=("arial",25,"bold"),width=6,command = lambda:click("."))
b16.pack(side=LEFT)
b17=Button(f6,text="=",font=("arial",25,"bold"),width=4,command = eq)
b17.pack(side=LEFT)



w.mainloop()
