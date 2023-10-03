from tkinter import *
def select(event):
    global val
    text=event.widget.cget("text")
    print(text)
    if text =="=":
        if val.get().isdigit():
            value= int(val.get())
        else:
             try:
                  value= eval(scr.get())
            
             except Exception as e:
                  val.set("ERROR")
                  scr.update()
        
        
         
        
        val.set(value)
        scr.update()     
    elif text == "C":
        val.set("")
        scr.update()
    else:
        val.set(val.get()+text)
        scr.update()


calc= Tk()
calc.geometry("370x420")
calc.title("SIMPLE CALCULATOR")
calc.configure(bg="yellow")
val= StringVar()
val.set("")
scr= Entry(calc, textvar=val,font="calibri 40 bold")
scr.pack(fill=X, ipadx=8, pady=10, padx=10)


f1=Frame(calc,bg="yellow")
b1= Button(f1,text="C",width=5,height=1,font="lucida 16 bold")
b1.pack(side=LEFT,padx=10,pady=20)
b1.bind("<Button-1>",select)

b1= Button(f1,text="/",width=5,height=1,font="lucida 16 bold")
b1.pack(side=LEFT,padx=10,pady=20)
b1.bind("<Button-1>",select)

b1= Button(f1,text="*",width=5,height=1,font="lucida 16 bold")
b1.pack(side=LEFT,padx=10,pady=20)
b1.bind("<Button-1>",select)

b1= Button(f1,text="-",width=5,height=1,font="lucida 16 bold")
b1.pack(side=LEFT,padx=10,pady=20)
b1.bind("<Button-1>",select)
f1.pack()

f1=Frame(calc,bg="yellow")
b1= Button(f1,text="7",width=5,height=1,font="lucida 16 bold")
b1.pack(side=LEFT,padx=10,pady=20)
b1.bind("<Button-1>",select)

b1= Button(f1,text="8",width=5,height=1,font="lucida 16 bold")
b1.pack(side=LEFT,padx=10,pady=20)
b1.bind("<Button-1>",select)

b1= Button(f1,text="9",width=5,height=1,font="lucida 16 bold")
b1.pack(side=LEFT,padx=10,pady=20)
b1.bind("<Button-1>",select)

b1= Button(f1,text="+",width=5,height=1,font="lucida 16 bold")
b1.pack(side=LEFT,padx=10,pady=20)
b1.bind("<Button-1>",select)
f1.pack()

f1=Frame(calc,bg="yellow")
b1= Button(f1,text="4",width=5,height=1,font="lucida 16 bold")
b1.pack(side=LEFT,padx=10,pady=20)
b1.bind("<Button-1>",select)

b1= Button(f1,text="5",width=5,height=1,font="lucida 16 bold")
b1.pack(side=LEFT,padx=10,pady=20)
b1.bind("<Button-1>",select)

b1= Button(f1,text="6",width=5,height=1,font="lucida 16 bold")
b1.pack(side=LEFT,padx=10,pady=20)
b1.bind("<Button-1>",select)

b1= Button(f1,text="=",width=5,height=1,font="lucida 16 bold")
b1.pack(side=LEFT,padx=10,pady=20)
b1.bind("<Button-1>",select)

f1.pack()

f1=Frame(calc,bg="yellow")
b1= Button(f1,text="1",width=5,height=1,font="lucida 16 bold")
b1.pack(side=LEFT,padx=10,pady=20)
b1.bind("<Button-1>",select)

b1= Button(f1,text="2",width=5,height=1,font="lucida 16 bold")
b1.pack(side=LEFT,padx=10,pady=20)
b1.bind("<Button-1>",select)

b1= Button(f1,text="3",width=5,height=1,font="lucida 16 bold")
b1.pack(side=LEFT,padx=10,pady=20)
b1.bind("<Button-1>",select)

b1= Button(f1,text="0",width=5,height=1,font="lucida 16 bold")
b1.pack(side=LEFT,padx=10,pady=20)
b1.bind("<Button-1>",select)
f1.pack()




calc.mainloop()