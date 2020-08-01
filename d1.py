from tkinter import *

from tkinter import ttk

class d1:
    def __init__(self, root):
        self.root = root
        self.root.geometry('850x600')
        self.root.title('Hospital Management System')
        root.configure(bg='light blue')

    #def d1(self):
        frame1 = Frame(root, width=700, height=500, bg='light blue', highlightthickness=4,
                       highlightbackground="dimgray").place(x=80, y=75)
        Label(root, text="MBBS (AIIMs Delhi)\r\nGoalpara\r\n diganta12@ymail.com\r\n ENT Specialist\r\n 9980237188\r\n10AM- 4PM", font=('arial 24 bold'), fg='green',
              bg='light blue').place(x=350,y=120)
        Label(root, text='From:',font=('arial 25 bold'),fg='black', bg = 'light blue').place(x=180, y=120)
        Label(root, text='Address:',font=('arial 22 bold'),fg='black', bg = 'light blue').place(x=180, y=190)
        Label(root, text='email:',font=('arial 25 bold'),fg='black', bg = 'light blue').place(x=160, y=268)
        Label(root, text='Specialist:',font=('arial 25 bold'),fg='black', bg = 'light blue').place(x=150, y=342)
        Label(root, text='Contact No:',font=('arial 25 bold'),fg='black', bg = 'light blue').place(x=130, y=415)
        Label(root, text='Visiting Hours:',font=('arial 29 bold'),fg='black', bg = 'light blue').place(x=100, y=480)




















# MAIN

if __name__ == '__main__':
    root = Tk()
    # root.geometry('10x500')
    application = d1(root)
    root.mainloop()