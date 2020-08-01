from tkinter import *

from tkinter import ttk


class d2:
    def __init__(self, root):
        self.root = root
        self.root.geometry('850x600')
        self.root.title('Hospital Management System')
        root.configure(bg='light blue')

        # def d2(self):
        frame1 = Frame(root, width=700, height=500, bg='light blue', highlightthickness=4,
                       highlightbackground="dimgray").place(x=100, y=75)

        Label(root,
              text="MBBS (AIIMs Delhi)\r\nMumbai\r\n ajay12@ymail.com\r\n EYE Specialist\r\n 9980232345\r\n10AM- 2PM & 4PM - 8PM",
              font=('arial 24 bold'),fg='green',bg='light blue').place(x=340, y=120)
        Label(root, text='From:', font=('arial 25 bold'), fg='black', bg='light blue').place(x=180, y=120)
        Label(root, text='Address:', font=('arial 22 bold'), fg='black', bg='light blue').place(x=180, y=190)
        Label(root, text='email:', font=('arial 25 bold'), fg='black', bg='light blue').place(x=160, y=268)
        Label(root, text='Specialist:', font=('arial 25 bold'), fg='black', bg='light blue').place(x=150, y=342)
        Label(root, text='Contact No:', font=('arial 25 bold'), fg='black', bg='light blue').place(x=130, y=415)
        Label(root, text='Visiting Hours:', font=('arial 25 bold'), fg='black', bg='light blue').place(x=110, y=489)





# MAIN

if __name__ == '__main__':
    root = Tk()
    # root.geometry('10x500')
    application = d2(root)
    root.mainloop()