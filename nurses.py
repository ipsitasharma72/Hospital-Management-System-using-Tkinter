from tkinter import *
from tkinter import ttk


class nurses:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1960x1080')
        self.root.title('Hospital Management System')
        root.configure(bg='light blue')

        frame1 = Frame(root, width=1370, height=550, bg='light blue', highlightthickness=4,highlightbackground="red").place(x=80, y=200)
        # def d2(self):
        Label(root,
              text='Nurses',font=('arial 34 bold'),fg='green',bg='light blue').place(x=70, y=30)
        Label(root, text='Here we have Almost 200 nurses for different purpose.', font=('arial 25 bold'), fg='black', bg='light blue').place(x=40, y=100)
        Label(root, text='Nurses', font=('arial 18 bold'), fg='Red',
              bg='light blue').place(x=200, y=150)
        Label(root, text='Number of Nurses', font=('arial 18 bold'), fg='Red',
              bg='light blue').place(x=900, y=150)
        Label(root, text='1. Registered nurses (RN)', font=('arial 20 bold'), fg='grey', bg='light blue').place(x=150, y=210)
        Label(root, text='2. Labor & delivery nurses', font=('arial 20 bold'), fg='grey', bg='light blue').place(x=150,
                                                                                                                y=260)
        Label(root, text='3. Travel nurses (TN)', font=('arial 20 bold'), fg='grey', bg='light blue').place(x=150,
                                                                                                                y=310)
        Label(root, text='4. Radiological nurses',font=('arial 20 bold'), fg='grey', bg='light blue').place(x=150,
                                                                                                                y=350)
        Label(root, text='5. Intensive Care unit register nurses (ICU)',font=('arial 20 bold'), fg='grey', bg='light blue').place(x=150,
                                                                                                            y=390)
        Label(root, text='6. Medical surgical nurses', font=('arial 20 bold'), fg='grey', bg='light blue').place(x=150,
                                                                                                            y=430)
        Label(root, text='7. Emergency room nurses', font=('arial 20 bold'), fg='grey', bg='light blue').place(x=150,
                                                                                                            y=470)
        Label(root, text='8. Operating room (OR) nurses', font=('arial 20 bold'), fg='grey', bg='light blue').place(x=150,
                                                                                                            y=510)
        Label(root, text='9. Home health nurses',font=('arial 20 bold'), fg='grey', bg='light blue').place(x=150,
                                                                                                            y=550)
        Label(root, text='10.Dialysis nurses', font=('arial 20 bold'), fg='grey', bg='light blue').place(x=150,
                                                                                                            y=590)

        Label(root, text='5', font=('arial 20 bold'), fg='grey', bg='light blue').place(x=1000,
                                                                                                         y=210)
        Label(root, text='30', font=('arial 20 bold'), fg='grey', bg='light blue').place(x=1000,
                                                                                                         y=260)
        Label(root, text='10', font=('arial 20 bold'), fg='grey', bg='light blue').place(x=1000,
                                                                                                         y=310)
        Label(root, text='50', font=('arial 20 bold'), fg='grey', bg='light blue').place(x=1000,
                                                                                                         y=350)
        Label(root, text='20', font=('arial 20 bold'), fg='grey', bg='light blue').place(x=1000,
                                                                                                         y=390)
        Label(root, text='50', font=('arial 20 bold'), fg='grey', bg='light blue').place(x=1000,
                                                                                                         y=430)
        Label(root, text='10', font=('arial 20 bold'), fg='grey', bg='light blue').place(x=1000,
                                                                                                         y=470)
        Label(root, text='10', font=('arial 20 bold'), fg='grey', bg='light blue').place(x=1000,
                                                                                                         y=510)
        Label(root, text='25', font=('arial 20 bold'), fg='grey', bg='light blue').place(x=1000,
                                                                                                         y=550)
        Label(root, text='10', font=('arial 20 bold'), fg='grey', bg='light blue').place(x=1000,
                                                                                                         y=590)









# MAIN

if __name__ == '__main__':
    root = Tk()
    # root.geometry('10x500')
    application = nurses(root)
    root.mainloop()