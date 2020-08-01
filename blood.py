from tkinter import *

from tkinter import ttk


class bloood:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1960x1080')
        self.root.title('Hospital Management System')
        root.configure(bg='light blue')
        frame1 = Frame(root, width=1460, height=650, bg='light blue', highlightthickness=4,
                       highlightbackground="red").place(x=50, y=100)

        # def d2(self):
        Label(root,
              text="In our hospital all types of blood are available:",font=('arial 24 bold'),fg='green',bg='light blue').place(x=20, y=10)
        Label(root, text='> O+', font=('arial 25 bold'), fg='black', bg='light blue').place(x=120, y=150)
        Label(root, text='> O-', font=('arial 25 bold'), fg='black', bg='light blue').place(x=120, y=200)
        Label(root, text='> A+', font=('arial 25 bold'), fg='black', bg='light blue').place(x=120, y=250)
        Label(root, text='> A-', font=('arial 25 bold'), fg='black', bg='light blue').place(x=120, y=300)
        Label(root, text='> AB+', font=('arial 25 bold'), fg='black', bg='light blue').place(x=120, y=350)
        Label(root, text='> AB-', font=('arial 25 bold'), fg='black', bg='light blue').place(x=120, y=400)



        Label(root,text='For blood\r\n contact: 99803127944:\r\n 98640360754\r\nEmail: rahul56@yahoo.com',bg='light blue',fg='black',font=('arial 25 bold')).place(x=500, y=400)








# MAIN

if __name__ == '__main__':
    root = Tk()
    # root.geometry('10x500')
    application = bloood(root)
    root.mainloop()