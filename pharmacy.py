from tkinter import *
from tkinter import ttk


class pharm:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1960x1080')
        self.root.title('Hospital Management System')
        root.configure(bg='light blue')
        frame1 = Frame(root, width=1460, height=650, bg='light grey', highlightthickness=4,
                       highlightbackground="red").place(x=50, y=100)

        # def d2(self):
        Label(root,
              text="Pharmacy is in Ground floor \r \n Here all type of medicine are available. \r \nContact No of Pharmacist: 9980562399 9842773330 \r\n Email id: pharma67@gmail.com",
              font=('arial 24 bold'),fg='green',bg='light grey').place(x=330, y=380)
        Label(root, text='Pharmacy', font=('arial 25 bold'), fg='black', bg='light green').place(x=650, y=120)







# MAIN

if __name__ == '__main__':
    root = Tk()
    # root.geometry('10x500')
    application = pharm(root)
    root.mainloop()