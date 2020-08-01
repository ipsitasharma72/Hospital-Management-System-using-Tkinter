from tkinter import *
from biki1 import *
from payment import *
from Doctors import *
from nurses import *
from pharmacy import *
from blood import *
from room import *
from laboratory import *
from Appointment import *

class dash:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1960x1080')
        self.root.title('Dashboard')
        root.configure(bg="khaki")
        Label(root, text='DashBoard', bg='khaki', fg='RED', font=('arial 60 bold'), width=30).place(x=10)


        frame1 = Frame(root, width=1370, height=650, bg='khaki', highlightthickness=4,highlightbackground="dimgray").place(x=80, y=120)
        photo = PhotoImage(file="patient.png")
        label = Label(root, image=photo).place(x=500, y=140)

        photo1 = PhotoImage(file="nurse1.png")
        label = Label(root, image=photo1).place(x=810, y=140)

        photo2 = PhotoImage(file="doctor(1).png")
        label = Label(root, image=photo2).place(x=190, y=140)

        photo3 = PhotoImage(file='lab.png')
        label = Label(root, image=photo3).place(x=1100, y=140)

        photo4 = PhotoImage(file='pharmacy.png')
        label = Label(root, image=photo4).place(x=190, y=390)

        photo5 = PhotoImage(file='room.png')
        label = Label(root, image=photo5).place(x=500, y=390)

        photo6 = PhotoImage(file='appointment.png')
        label = Label(root, image=photo6).place(x=810, y=390)

        photo7 = PhotoImage(file='blood.png')
        label = Label(root, image=photo7).place(x=1100, y=390)

        Button(text='Doctors', bg='yellow',command=self.doctor, width=19, font=('arial 10 bold')).place(x=190, y=300)
        Button(text='Patient',  bg='yellow', command=self.all, width=18, font=('arial 10 bold')).place(x=500, y=300)
        Button(text='Nurses', bg='yellow',command=self.nus, width=18, font=('arial 10 bold')).place(x=810, y=300)
        Button(text='Lab',command=self.test, bg='yellow', width=18, font=('arial 10 bold')).place(x=1100, y=300)
        Button(text='Pharmacy',command=self.medicn,  bg='yellow', width=18, font=('arial 10 bold')).place(x=190, y=550)
        Button(text='Rooms',command=self.rum, bg='yellow', width=18, font=('arial 10 bold')).place(x=500, y=550)
        Button(text='Appointentment',command=self.apu, bg='yellow', width=18, font=('arial 10 bold')).place(x=810, y=550)
        Button(text='Blood Bank',command=self.bd, bg='yellow', width=18, font=('arial 10 bold')).place(x=1100, y=550)
        root.mainloop()






    def all(self):
         self.root.destroy()
         newroot=Tk()
         application = Hos_Portal(newroot)
         newroot.mainloop()


    def doctor(self):
         self.root.destroy()
         newroot=Tk()
         application = doc(newroot)
         newroot.mainloop()

    def nus(self):
        # self.root.destroy()
         newroot=Tk()
         application = nurses(newroot)
         newroot.mainloop()
    def medicn(self):
        # self.root.destroy()
         newroot=Tk()
         application = pharm(newroot)
         newroot.mainloop()

    def bd(self):
        # self.root.destroy()
        newroot = Tk()
        application = bloood(newroot)
        newroot.mainloop()

    def rum(self):
        # self.root.destroy()
        newroot = Tk()
        application =room(newroot)
        newroot.mainloop()

    def test(self):
        # self.root.destroy()
        newroot = Tk()
        application =lab(newroot)
        newroot.mainloop()


    def apu(self):
        self.root.destroy()
        newroot = Tk()
        application = app(newroot)
        newroot.mainloop()



#MAIN

if __name__ == '__main__':
    root = Tk()



   # photo2 = PhotoImage(file="doctor(1).png")
   # label = Label(root, image=photo2).place(x=90, y=140)




    #label.pack()
    #root.geometry('10x500')
    application = dash(root)
    root.mainloop()
