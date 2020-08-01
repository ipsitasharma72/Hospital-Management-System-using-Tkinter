
from tkinter import *
import sqlite3

from tkinter import ttk
import datetime
import time

import tkinter.messagebox
from payment import *


class Hos_Portal:


    def __init__(self, root):
        self.root = root
        self.root.geometry('1960x1080')
        self.root.title('Hospital Management System')
        root.configure(bg="dark blue")

        frame1 = Frame(root, width=1460, height=650, bg='light grey', highlightthickness=4,highlightbackground="red").place(x=50, y=100)

        Fullname = StringVar()
        dr = StringVar()
        var = IntVar()
        c = StringVar()
        var1 = IntVar()
        Mobile = IntVar()
        Dl = StringVar()
        Pan = StringVar()

        def database():
            ##top = Toplevel()
            ## top.title("Successfully Registered.")
            ## top.geometry("300x300+120+120")
            ##button1 = Button(top, text="Successfully signed up. ", command=open_window())

            ## button1.pack()
            root.geometry("300x300+120+120")

            name1 = Fullname.get()
            dro = dr.get()
            gender = var.get()
            country = c.get()
            prog = var1.get()
            conn = sqlite3.connect("papi.db")
            with conn:
                cursor = conn.cursor()
            cursor.execute(
                'CREATE TABLE IF NOT EXISTS Student (Fullname TEXT,Email TEXT)')
            cursor.execute('INSERT INTO Student (FullName,Email) VALUES(?,?)',
                           (name1, dro))
            conn.commit()

        def query():
            frame1 = Frame(root, width=310, height=450, bg='light grey', highlightthickness=4,
                           highlightbackground="red").place(x=1200, y=220)
            conn = sqlite3.connect("papi.db")
            with conn:
                cursor = conn.cursor()

                cursor.execute("SELECT * , oid FROM Student")
                records = cursor.fetchall()
                #print(records)
                print_records = ''


                for record in records:

                    print_records += str(record[0]) + "\n"

                query_label = Label(root,  font=('arial 18 bold'),bg= 'light grey',fg = 'green',text = print_records)
                query_label.place(x=1220, y= 230)




                conn.commit()




        Label(root, text="Patient Registration Form", font=('arial 46 bold'), fg='white',
              bg='black').place(x=350, y=10)
        label_1 = Label(root, text="FullName",font=('arial 15 bold'), bg='grey', fg='black', width=20)
        label_1.place(x=270, y=130)

        entry_1 = Entry(root, font=('arial 15 bold'),width = 40,textvar=Fullname)
        entry_1.place(x=580, y=130)


        label_2 = Label(root, text="Gender", width=20, bg='grey', fg='black', font=('arial 15 bold'))
        label_2.place(x=270, y=180)

        Radiobutton(root, text="Male", variable=var, width =5,font=('arial 11 bold'),value=1).place(x=660, y=180)
        Radiobutton(root, text="Female",variable=var,font=('arial 11 bold'), value=2).place(x=780, y=180)

        label_3 = Label(root, text="Phone No. ", width=20, bg='grey', font=('arial 15 bold'))
        label_3.place(x=270, y=230)

        list1 = ['+91', '+12', '+90', '+0', '+85', '+10'];

        droplist = OptionMenu(root, c, *list1)

        droplist.config(width=3,font=('arial 11 bold'))
        c.set('std')
        droplist.place(x=580, y=230)
        entry_10 = Entry(root, font=('arial 15 bold'))
        entry_10.place(x=680, y=230)

        label_4 = Label(root, text="Age ", width=20, bg='grey', font=('arial 15 bold'))
        label_4.place(x=270, y=280)
        entry_11 = Entry(root, font=('arial 15 bold'))
        entry_11.place(x=580, y=280)

        label_5 = Label(root, text="Address ", width=20, bg='grey', font=('arial 15 bold'))
        label_5.place(x=270, y=330)
        entry_11 = Entry(root, font=('arial 15 bold'))
        entry_11.place(x=580, y=330)

        label_6 = Label(root, text="State ", width=20, bg='grey', font=('arial 15 bold'))
        label_6.place(x=270, y=380)
        entry_12 = Entry(root, font=('arial 15 bold'))
        entry_12.place(x=580, y=380)

        label_7 = Label(root, text="District ", width=10, bg='grey', font=('arial 15 bold'))
        label_7.place(x=270, y=430)
        entry_13 = Entry(root, font=('arial 15 bold'))
        entry_13.place(x=420, y=430)

        label_7 = Label(root, text="Pincode ", width=10, bg='grey', font=('arial 15 bold'))
        label_7.place(x=670, y=430)
        entry_13 = Entry(root, font=('arial 15 bold'))
        entry_13.place(x=830, y=430)

        label_7 = Label(root, text="Health Problem ", width=20, bg='grey', font=('arial 15 bold'))
        label_7.place(x=270, y=480)
        entry_13 = Entry(root, font=('arial 15 bold'))
        entry_13.place(x=580, y=480)

        label_7 = Label(root, text="Payment Mode", width=20, bg='grey', font=('arial 15 bold'))
        label_7.place(x=270, y=530)
        Radiobutton(root, text="CARD", variable=var, width=5, font=('arial 11 bold'), value=1).place(x=530, y=530)
        Radiobutton(root, text="CASH", variable=var, font=('arial 11 bold'), value=2).place(x=640, y=530)

        label_7 = Label(root, text="Refer To:", width=20, bg='grey', font=('arial 15 bold'))
        label_7.place(x=270, y=580)
        list2 = ['Dr. Diganta', 'Dr. Ajay', 'Dr. Pradeep', 'Dr. Neha', 'Dr. Vivek', 'Dr. Kamal'];

        drop= OptionMenu(root, dr, *list2)

        drop.config(width=10, font=('arial 11 bold'))
        dr.set('Doctors')
        drop.place(x=580, y=580)








        button = Button(root, text='SUBMIT', width=20, bg='Green',  font=('arial 15 bold'),fg='white', command=database).place(x=600, y=690)

        query_btn = Button(root,  font=('arial 15 bold'),text= 'Show records',command=query)
        query_btn.place(x=1300, y=180)




if __name__ == '__main__':
    root = Tk()
    #root.geometry('10x500')
    application = Hos_Portal(root)
    root.mainloop()
