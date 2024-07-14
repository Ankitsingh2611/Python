

import tkinter
root=tkinter.Tk()
root.title("College Managment System")
root.geometry('400x500')
def reg():
    top=tkinter.Toplevel(root)
    top.title("registration")

    top.geometry("400x300")
    top.mainloop()

def adm():
    top=tkinter.Toplevel(root)
    top.title("Admission")

    top.geometry("400x300")
    top.mainloop()
def rreg():
    top=tkinter.Toplevel(root)
    top.title("re-Admission")

    top.geometry("400x300")
    top.mainloop()
def res():
    top=tkinter.Toplevel(root)
    top.title("Result")
    
    top.geometry("400x300")
    top.mainloop()


l1=tkinter.Label(root,text="College managment System",font="Arial 14 bold").pack()
b1=tkinter.Button(root,text="Registration",bg="black",fg="white",font="arial 14",command=reg)
b1.place(x=10,y=50)
b1=tkinter.Button(root,text="Admission",bg="black",fg="white",font="arial 14",command=adm)
b1.place(x=10,y=100)
b1=tkinter.Button(root,text="Re-Admission",bg="black",fg="white",font="arial 14",command=rreg)
b1.place(x=10,y=150)
b1=tkinter.Button(root,text="Result",bg="black",fg="white",font="arial 14",command=res)
b1.place(x=10,y=200)




root.mainloop()