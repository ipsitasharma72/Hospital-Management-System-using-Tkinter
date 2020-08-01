from tkinter import *

from tkinter import ttk


class d3:
    def __init__(self, root):
        self.root = root
        self.root.geometry('850x600')
        self.root.title('Hospital Management System')
        root.configure(bg='light blue')

        # def d2(self):
        frame1 = Frame(root, width=700, height=500, bg='light blue', highlightthickness=4,
                       highlightbackground="dimgray").place(x=100, y=75)
        Label(root,
              text="MBBS (AIIMs Delhi)\r\nDelhi\r\n Neha12@ymail.com\r\n Skin Specialist\r\n 99802555807\r\n10AM- 2PM & 4PM - 8PM",
              font=('arial 24 bold'),fg='green',bg='light blue').place(x=350, y=120)
        Label(root, text='From:', font=('arial 25 bold'), fg='black', bg='light blue').place(x=180, y=120)
        Label(root, text='Address:', font=('arial 22 bold'), fg='black', bg='light blue').place(x=180, y=190)
        Label(root, text='email:', font=('arial 25 bold'), fg='black', bg='light blue').place(x=160, y=268)
        Label(root, text='Specialist:', font=('arial 25 bold'), fg='black', bg='light blue').place(x=150, y=342)
        Label(root, text='Contact No:', font=('arial 25 bold'), fg='black', bg='light blue').place(x=130, y=415)
        Label(root, text='Visiting Hours:', font=('arial 25 bold'), fg='black', bg='light blue').place(x=110, y=489)


class d4:
    def __init__(self, root):
        self.root = root
        self.root.geometry('850x600')
        self.root.title('Hospital Management System')
        root.configure(bg='light blue')

        # def d2(self):
        frame1 = Frame(root, width=700, height=500, bg='light blue', highlightthickness=4,
                       highlightbackground="dimgray").place(x=100, y=75)
        Label(root,
              text="BDS+ MDS (GMCH Guwahati)\r\nKamrup\r\n priyaprakash@ymail.com\r\n Dental Specialist\r\n 76541783541\r\n10AM- 2PM & 4PM - 8PM",
              font=('arial 24 bold'),fg='green',bg='light blue').place(x=310, y=120)
        Label(root, text='From:', font=('arial 25 bold'), fg='black', bg='light blue').place(x=180, y=120)
        Label(root, text='Address:', font=('arial 22 bold'), fg='black', bg='light blue').place(x=180, y=195)
        Label(root, text='email:', font=('arial 25 bold'), fg='black', bg='light blue').place(x=156, y=268)
        Label(root, text='Specialist:', font=('arial 25 bold'), fg='black', bg='light blue').place(x=150, y=342)
        Label(root, text='Contact No:', font=('arial 25 bold'), fg='black', bg='light blue').place(x=130, y=415)
        Label(root, text='Visiting Hours:', font=('arial 25 bold'), fg='black', bg='light blue').place(x=110, y=489)



class d5:
    def __init__(self, root):
        self.root = root
        self.root.geometry('850x600')
        self.root.title('Hospital Management System')
        root.configure(bg='light blue')

        # def d2(self):
        frame1 = Frame(root, width=700, height=500, bg='light blue', highlightthickness=4,
                       highlightbackground="dimgray").place(x=100, y=75)
        Label(root,
              text="MBBS (AIIMs Delhi)\r\nKolkata\r\n pradeepdutta@ymail.com\r\n Gyno  Specialist\r\n 8011998365\r\n10AM- 2PM & 4PM - 8PM",
              font=('arial 24 bold'),fg='green',bg='light blue').place(x=350, y=120)
        Label(root, text='From:', font=('arial 25 bold'), fg='black', bg='light blue').place(x=180, y=120)
        Label(root, text='Address:', font=('arial 22 bold'), fg='black', bg='light blue').place(x=180, y=190)
        Label(root, text='email:', font=('arial 25 bold'), fg='black', bg='light blue').place(x=156, y=268)
        Label(root, text='Specialist:', font=('arial 25 bold'), fg='black', bg='light blue').place(x=150, y=342)
        Label(root, text='Contact No:', font=('arial 25 bold'), fg='black', bg='light blue').place(x=130, y=415)
        Label(root, text='Visiting Hours:', font=('arial 25 bold'), fg='black', bg='light blue').place(x=110, y=489)



class d6:
    def __init__(self, root):
        self.root = root
        self.root.geometry('850x600')
        self.root.title('Hospital Management System')
        root.configure(bg='light blue')

        # def d2(self):
        frame1 = Frame(root, width=700, height=500, bg='light blue', highlightthickness=4,
                       highlightbackground="dimgray").place(x=100, y=75)

        Label(root,
              text="MBBS + PG (AIIMs Delhi)\r\nAmingaon\r\n vivekrajandas@ymail.com\r\n SKIN Specialist\r\n 9880232345\r\n10AM- 2PM & 4PM - 8PM",
              font=('arial 24 bold'),fg='green',bg='light blue').place(x=350, y=120)
        Label(root, text='From:', font=('arial 25 bold'), fg='black', bg='light blue').place(x=180, y=120)
        Label(root, text='Address:', font=('arial 22 bold'), fg='black', bg='light blue').place(x=180, y=190)
        Label(root, text='email:', font=('arial 25 bold'), fg='black', bg='light blue').place(x=156, y=268)
        Label(root, text='Specialist:', font=('arial 25 bold'), fg='black', bg='light blue').place(x=150, y=342)
        Label(root, text='Contact No:', font=('arial 25 bold'), fg='black', bg='light blue').place(x=130, y=415)
        Label(root, text='Visiting Hours:', font=('arial 25 bold'), fg='black', bg='light blue').place(x=110, y=489)







# MAIN

if __name__ == '__main__':
    root = Tk()
    # root.geometry('10x500')
    application = d3(root)
    root.mainloop()