from tkinter import *
from tkinter import ttk
from biki1 import *
from payment import *


class app:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1960x1080')
        var = IntVar()
        self.root.title('Hospital Management System')
        root.configure(bg='light blue')
        #frame1 = Frame(root, width=870, height=480, bg='light blue', highlightthickness=4,
                      # highlightbackground="dimgray").place(x=30, y=97)
        frame1 = Frame(root, width=1460, height=650, bg='light blue', highlightthickness=4,
                       highlightbackground="red").place(x=50, y=100)

        # def d2(self):
        Label(root,text='APPOINTMENT',font=('arial 34 bold'),fg='green',bg='light blue').place(x=40, y=30)
        Label(root, text='Name', font=('arial 20 bold'), fg='black', bg='light blue').place(x=240, y=220)
        Label(root, text='Refer To-', font=('arial 20 bold'), fg='black', bg='light blue').place(x=240, y=270)
        Label(root, text='Check up', font=('arial 20 bold'), fg='black', bg='light blue').place(x=240, y=320)
        Entry(root, bg='light blue', fg='blue', font=('arial 20 bold'),width=30).place(x=420, y=220)
        Entry(root, bg='light blue', fg='blue', font=('arial 20 bold'),width=30).place(x=420, y=270)
       # Entry(root, bg='sky blue', fg='blue', width=).place(x=120, y=120)
        Radiobutton(root, text='YES', value=1,font=('arial 17 bold'), variable=var, bg='light blue', fg='black').place(x=420, y=320)
        Radiobutton(root, text='NO', value=2, variable=var, font=('arial 17 bold'),bg='light blue', fg='black').place(x=520, y=320)
        Label(root, text='Token no.', font=('arial 20 bold'), fg='black', bg='light blue').place(x=240, y=370)
        Entry(root, bg='light blue', fg='blue', font=('arial 20 bold'),width=5).place(x=420, y=370)
        Button(text='For new patient',command= self.no, bg='yellow', width=20).place(x=240, y=420)
        Button(text='Submit',command= self.click, bg='yellow',font=('arial 20 bold'), width=20).place(x=440, y=600)

    def click(self):
        #Button(text='Submit', command=self.click, bg='yellow', width=15, font=('arial 10 bold')).place(x=310, y=360)

        Label(text='Appointment successful:', fg='red', font=('arial 15 bold')).place(x=450, y=690)

    def no(self):

        self.root.destroy()
        newroot = Tk()
        application = Hos_Portal(newroot)
        newroot.mainloop()


# MAIN

if __name__ == '__main__':
    root = Tk()
    # root.geometry('10x500')
    application = app(root)
    root.mainloop()