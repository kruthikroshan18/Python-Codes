from tkinter import*
master=Tk()
l1=(master,text="first name").grid(row=0)
l1=(master,text="last name").grid(row=1)
e1=enter(master)
e2=enter(master)
e1.grid(row=0,column=1)
e2.grid(row=1,column=2)
mainloop()