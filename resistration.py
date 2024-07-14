import tkinter
import tkinter.messagebox as Messagebox
from PIL import  Image,ImageTk
root=tkinter.Tk()
root.title("Login Page")
root.geometry("400x300")
root.configure(bg="light green")
l1=tkinter.Label(root,text="Login Page",bg="black",fg="white",font="Arial 14 bold")
l1.pack()

#------------------------background image
image=Image.open("E:\\pc\\c1.jpg")
photo=ImageTk.PhotoImage(image)
p1=tkinter.Label(root,image=photo)
p1.place(x=0,y=0)
#--------------------login page function 
def login():
    a=e1.get()
    b=e2.get()
    if a=="" and b=="":
        Messagebox.showerror("","Empty not allowed")
    if a=="ankit" and b=="singh":
    
        Messagebox.showinfo("","LOgin Successfully")
        #-----------page to page connectivity
        root.destroy()
        import resistration1
    else:
        Messagebox.showinfo("","LOgin Credential")



l2=tkinter.Label(root,text="User Name",fg="red",bg="light green",font="Arial 14")
l2.place(x=10,y=50)
e1=tkinter.Entry(bd="2")
e1.place(x=150,y=50)
l3=tkinter.Label(root,text="Password",fg="red",bg="light green",font="Arial 14")
l3.place(x=10,y=100)

e2=tkinter.Entry(show="*",bd="2")

e2.place(x=150,y=100)
b1=tkinter.Button(root,text="Login",font="Arial 12 italic",command=login)
b1.place(x=75,y=200)
b1=tkinter.Button(root,text="Cancel",font="Arial 12 italic",command=quit)
b1.place(x=150,y=200)


root.mainloop()
