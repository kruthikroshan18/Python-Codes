import tkinter  
m=tkinter.Tk()
m.title("PSSP")
m.geometry("400x400")
def add():
    print("hai")
b1=tkinter.Button(m,text="submit",fg='red',command=add)
def add():
    print("good morning")
b2=tkinter.Button(m,text="open",bg="yellow",command=add)
def add():
    print("closed")
b3=tkinter.Button(m,text="close",fg="green",command=add)
b1.grid(row=1 ,column=1)
b2.grid(row=2,column=2)
b3.grid(row=3,column=3)

m.mainloop()