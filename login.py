import sqlite3
from tkinter import *
from tkinter import ttk
from dashboard import *
class gimt:

    user = 'hmsipsi'
    passw ='optandon'

    def __init__(self,root):

        self.root = root
        self.root.title('LOGIN SCREEN')
        Label(root, text="Hospital Management System", font=('arial 40 bold'), fg='white',
              bg='black').place(x=330, y=10)
        Label(root, text="Admin Page", font=('arial 10 bold'), fg='yellow',
              bg='black').place(x=350,y=70)
        root.configure(bg='skyblue')

        photo2 = PhotoImage(file="amma.png")
        Label(root, image=photo2, width=1600, height=1000).place(x=-60, y=70)

        Label(text = ' Username: ',font=('arial 20 bold'),bg="sky blue").place(x=350,y=300)
        self.username = Entry(root,bg="sky blue",width=30,font=('arial 20 bold'))
        self.username.place(x=600,y=300)

        Label(text = ' Password: ',font=('arial 20 bold'),bg="sky blue").place(x=350,y=420)
        self.password = Entry(root,bg="sky blue",show='*',width =30,font=('arial 20 bold'))
        self.password.place(x=600,y=420)

        ttk.Button(text='LOGIN',command=self.login_user).place(x=630,y=520)


        root.mainloop()




    def login_user(self):

        '''Checking'''
        if self.username.get() == self.user and self.password.get() == self.passw:

            # Do the work done by the main of DBMSproject.py

            #Destroy the current window
            root.destroy()



            #Open new window
            newroot = Tk()
            application = dash(newroot)
            newroot.mainloop()



        else:

            '''Prompt user that either id or password is wrong'''
            self.message = Label(text = 'Username or Password incorrect. Try again!',font=('arial 20 bold'),fg = 'Red')
            self.message.place(x=450,y=600)

if __name__ == '__main__':

    root = Tk()
    root.geometry('1960x1080')
    application = gimt(root)


