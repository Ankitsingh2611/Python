
import tkinter
import tkinter.messagebox as Messagebox
from PIL import  Image,ImageTk
root=tkinter.Tk()
root.title("Login Page")
root.geometry("400x300")
root.configure(bg="light green")
l1=tkinter.Label(root,text="pizza Page",bg="black",fg="white",font="Arial 14 bold")
l1.pack()


def goBack():
    root.destroy()
    import pp
#------------------------background image
image=Image.open("E:\\pc\\brand_pic3.jpg")
photo=ImageTk.PhotoImage(image)
p1=tkinter.Label(root,image=photo)
p1.place(x=0,y=0)
#--------------------login page function 
def login():
    a=e1.get()
    b=e2.get()
    c=e3.get()
    d=e4.get()
    e=e5.get()

    if a=="" and b=="" and c=="" and d=="" and e=="":
        Messagebox.showerror("","Empty not allowed")
    if a=="denny" and b=="ankit" and c=="carlos" and d=="carlos" and e=="ankittchauhan4@gmail.com":
            
        Messagebox.showinfo("","LOgin Successfully")
        #root.destroy()
        #import resistration2
            
    else:
        Messagebox.showinfo("","LOgin Credential")



l2=tkinter.Label(root,text="Name",fg="black",bg="white",font="Arial 14")
l2.place(x=10,y=50)
e1=tkinter.Entry(bd="2")
e1.place(x=150,y=50)
l3=tkinter.Label(root,text="username",fg="black",bg="white",font="Arial 14")
l3.place(x=10,y=100)

e2=tkinter.Entry(bd="2")

e2.place(x=150,y=100)

l4=tkinter.Label(root,text="password",fg="black",bg="white",font="Arial 14")
l4.place(x=10,y=150)
e3=tkinter.Entry(show="*",bd="2")
e3.place(x=150,y=150)

l5=tkinter.Label(root,text="retype password",fg="black",bg="white",font="Arial 12")
l5.place(x=10,y=200)
e4=tkinter.Entry(show="*",bd="2")
e4.place(x=150,y=200)

l6=tkinter.Label(root,text="email",fg="black",bg="white",font="Arial 14")
l6.place(x=10,y=250)
e5=tkinter.Entry(bd="2")
e5.place(x=150,y=250)



b1=tkinter.Button(root,text="Login",font="Arial 12 italic",command=login)
b1.place(x=75,y=300)
b1=tkinter.Button(root,text="Cancel",font="Arial 12 italic",command=quit)
b1.place(x=150,y=300)
b1=tkinter.Button(root,text="back",font="Arial 12 italic",command=goBack)
b1.place(x=300,y=300)

root.mainloop()