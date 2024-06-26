from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "Error"
                
            scvalue.set(value)
            screen.update()
            
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()
        
    
        

root = Tk()
root.geometry("450x510")
root.title("Calculator - Using Tkinter")
root.configure(bg="black")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 40 bold", bg="Teal")
screen.pack(fill=X, padx=8, pady=10, ipadx=10)

f = Frame(root, bg="Teal")

b = Button(f, text="9", font="lucida 15 bold", padx=20, pady=12, bg="DarkCyan")
b.pack(side=LEFT, padx=12, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="8", font="lucida 15 bold", padx=19, pady=12, bg="DarkCyan")
b.pack(side=LEFT, padx=12, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="7", font="lucida 15 bold", padx=19, pady=12, bg="DarkCyan")
b.pack(side=LEFT, padx=12, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="*", font="lucida 15 bold", padx=20, pady=12, bg="DarkCyan")
b.pack(side=LEFT, padx=12, pady=12)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="Teal")

b = Button(f, text="6", font="lucida 15 bold", padx=20, pady=12, bg="DarkCyan")
b.pack(side=LEFT, padx=12, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="5", font="lucida 15 bold", padx=20, pady=12, bg="DarkCyan")
b.pack(side=LEFT, padx=12, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="4", font="lucida 15 bold", padx=20, pady=12, bg="DarkCyan")
b.pack(side=LEFT, padx=12, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="/", font="lucida 15 bold", padx=20, pady=12, bg="DarkCyan")
b.pack(side=LEFT, padx=12, pady=12)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="Teal")

b = Button(f, text="3", font="lucida 15 bold", padx=20, pady=12, bg="DarkCyan")
b.pack(side=LEFT, padx=12, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="2", font="lucida 15 bold", padx=20, pady=12, bg="DarkCyan")
b.pack(side=LEFT, padx=12, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="1", font="lucida 15 bold", padx=20, pady=12, bg="DarkCyan")
b.pack(side=LEFT, padx=12, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="-", font="lucida 15 bold", padx=20, pady=12, bg="DarkCyan")
b.pack(side=LEFT, padx=12, pady=12)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="Teal")

b = Button(f, text=".", font="lucida 15 bold", padx=18, pady=12, bg="DarkCyan")
b.pack(side=LEFT, padx=12, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="0", font="lucida 15 bold", padx=19, pady=12, bg="DarkCyan")
b.pack(side=LEFT, padx=12, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="00", font="lucida 15 bold", padx=19, pady=12, bg="DarkCyan")
b.pack(side=LEFT, padx=12, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="+", font="lucida 15 bold", padx=18, pady=12, bg="DarkCyan")
b.pack(side=LEFT, padx=12, pady=12)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="Teal")

b = Button(f, text="%", font="lucida 15 bold", padx=20, pady=12, bg="DarkCyan")
b.pack(side=LEFT, padx=12, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="C", font="lucida 15 bold", padx=20, pady=12, bg="DarkCyan")
b.pack(side=LEFT, padx=12, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="=", font="lucida 15 bold", padx=20, pady=12, bg="DarkCyan")
b.pack(side=LEFT, padx=12, pady=12)
b.bind("<Button-1>", click)

f.pack()

root.mainloop()