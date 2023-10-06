from tkinter import *

def click(event):
    global s1
    text=event.widget.cget("text")
    #print(text)
    if text=="=":
        if s1.get().isdigit():
            value=int(s1.get())
        else:
            value=eval(screen.get())

        s1.set(value)
        screen.update()

    elif text=="C":
        s1.set("")
        screen.update()
    else:
        s1.set(s1.get() + text)
        screen.update()



root=Tk()
root.geometry("350x350")
root.title("Calcutaor")

s1=StringVar()
s1.set("")
screen=Entry(root,textvar=s1,font=("bold",12))
screen.pack(fill=X,ipadx=8,pady=10,padx=10)

f1=Frame(root)
b1=Button(f1,text="9",padx=12,pady=8,font=("bold",16))
b1.pack(side=LEFT,padx=12,pady=5)
b1.bind("<Button-1>",click)

b1=Button(f1,text="8",padx=12,pady=8,font=("bold",16))
b1.pack(side=LEFT,padx=12,pady=5)
b1.bind("<Button-1>",click)

b1=Button(f1,text="7",padx=12,pady=8,font=("bold",16))
b1.pack(side=LEFT,padx=12,pady=5)
b1.bind("<Button-1>",click)

b1=Button(f1,text="+",padx=12,pady=8,font=("bold",16))
b1.pack(side=LEFT,padx=12,pady=5)
b1.bind("<Button-1>",click)

f1.pack()


f1=Frame(root)
b1=Button(f1,text="6",padx=12,pady=8,font=("bold",16))
b1.pack(side=LEFT,padx=12,pady=5)
b1.bind("<Button-1>",click)

b1=Button(f1,text="5",padx=12,pady=8,font=("bold",16))
b1.pack(side=LEFT,padx=12,pady=5)
b1.bind("<Button-1>",click)

b1=Button(f1,text="4",padx=12,pady=8,font=("bold",16))
b1.pack(side=LEFT,padx=12,pady=5)
b1.bind("<Button-1>",click)

b1=Button(f1,text="-",padx=15,pady=8,font=("bold",16))
b1.pack(side=LEFT,padx=12,pady=5)
b1.bind("<Button-1>",click)

f1.pack()

f1=Frame(root)
b1=Button(f1,text="3",padx=12,pady=8,font=("bold",16))
b1.pack(side=LEFT,padx=12,pady=5)
b1.bind("<Button-1>",click)

b1=Button(f1,text="2",padx=12,pady=8,font=("bold",16))
b1.pack(side=LEFT,padx=12,pady=5)
b1.bind("<Button-1>",click)

b1=Button(f1,text="1",padx=13,pady=8,font=("bold",16))
b1.pack(side=LEFT,padx=12,pady=5)
b1.bind("<Button-1>",click)

b1=Button(f1,text="*",padx=15,pady=8,font=("bold",16))
b1.pack(side=LEFT,padx=12,pady=5)
b1.bind("<Button-1>",click)
f1.pack()

f1=Frame(root)
b1=Button(f1,text="C",padx=12,pady=8,font=("bold",16))
b1.pack(side=LEFT,padx=12,pady=5)
b1.bind("<Button-1>",click)

b1=Button(f1,text="0",padx=12,pady=8,font=("bold",16))
b1.pack(side=LEFT,padx=12,pady=5)
b1.bind("<Button-1>",click)

b1=Button(f1,text="=",padx=13,pady=8,font=("bold",16))
b1.pack(side=LEFT,padx=12,pady=5)
b1.bind("<Button-1>",click)

b1=Button(f1,text="/",padx=17,pady=8,font=("bold",16))
b1.pack(side=LEFT,padx=10,pady=5)
b1.bind("<Button-1>",click)

f1.pack()
root.mainloop()