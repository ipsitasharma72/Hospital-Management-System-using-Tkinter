from tkinter import *
from d1 import *
from d2 import *
from d3 import *
from dashboard import *


from tkinter import ttk

class doc:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1960x1080')
        self.root.title('Hospital Management System')
        root.configure(bg="light pink")

        Label(root, text="DOCTOR'S DETAILS", font=('arial 48 bold'), fg='white',
              bg='black').place(x=400,y=20)

        frame1 = Frame(root, width=1370, height=670, bg='light grey', highlightthickness=4,highlightbackground="red").place(x=70, y=120)
        Label(root, text="List of Doctors", font=('arial 24 bold'), fg='red',
              bg='light pink').place(x=80,y=150)

        d1 = Button(text='Dr. Diganta',command =self.doc1 , bg='khaki', width=18, font=('arial 20 bold')).place(x=1000, y=230)
        d2 = Button(text='Dr. Ajay', command=self.doc2, bg='khaki', width=18, font=('arial 20 bold')).place(x=1000, y=320)
        d3 = Button(text='Dr. Neha',command=self.doc3, bg='khaki', width=18, font=('arial 20 bold')).place(x=1000, y=410)
        d4 = Button(text='Dr. Priya',command=self.doc4, bg='khaki', width=18, font=('arial 20 bold')).place(x=1000, y=500)
        d5 = Button(text='Dr. Pradip',command=self.doc5, bg='khaki', width=18, font=('arial 20 bold')).place(x=1000, y=590)
        d6 = Button(text='Dr. Vivek', command=self.doc6,bg='khaki', width=18, font=('arial 20 bold')).place(x=1000, y=680)

        photo = PhotoImage(file="doco.png")
        label = Label(root, image=photo,width=600, height=400).place(x=150, y=270)
        photo1 = PhotoImage(file="logodoc.png",width=50, height=50)
        label = Label(root, image=photo1).place(x=900, y=230)
        photo2 = PhotoImage(file="logodoc.png", width=50, height=50)
        label = Label(root, image=photo2).place(x=900, y=320)
        photo3 = PhotoImage(file="logodoc.png", width=50, height=50)
        label = Label(root, image=photo3).place(x=900, y=410)
        photo4 = PhotoImage(file="logodoc.png", width=50, height=50)
        label = Label(root, image=photo4).place(x=900, y=500)
        photo5 = PhotoImage(file="logodoc.png", width=50, height=50)
        label = Label(root, image=photo5).place(x=900, y=590)
        photo6 = PhotoImage(file="logodoc.png", width=50, height=50)
        label = Label(root, image=photo6).place(x=900, y=680)

        #Button(text='', command=self.doc6,bg='khaki', width=18, font=('arial 20 bold')).place(x=459, y=430)
        Button(text='Return To Dashboard', command=self.ret,bg='light green', width=18, font=('arial 20 bold')).place(x=300, y=720)
        root.mainloop()

    def doc1(self):

       # self.root.destroy()
        newroot = Tk()
        application = d1(newroot)
        newroot.mainloop()

    def doc2(self):
        # self.root.destroy()
         newroot = Tk()
         application = d2(newroot)
         newroot.mainloop()

    def doc3(self):
        #self.root.destroy()
        newroot = Tk()
        application = d3(newroot)
        newroot.mainloop()

    def doc4(self):
        #self.root.destroy()
        newroot = Tk()
        application = d4(newroot)
        newroot.mainloop()

    def doc5(self):
        #self.root.destroy()
        newroot = Tk()
        application = d5(newroot)
        newroot.mainloop()

    def doc6(self):
       # self.root.destroy()
        newroot = Tk()
        application = d6(newroot)
        newroot.mainloop()


    def ret(self):
       self.root.destroy()
       newroot = Tk()
       application = dash(newroot)
       newroot.mainloop()


# MAIN

if __name__ == '__main__':
    root = Tk()
    # root.geometry('10x500')
    application = doc(root)
    root.mainloop()