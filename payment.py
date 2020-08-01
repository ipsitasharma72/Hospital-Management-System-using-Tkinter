from tkinter import *

class pay:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1960x1080')
        self.root.title('Payment Section')
        root.configure(bg="sky blue")

        Label(root, text='Billing section ', bg='sky blue', fg='black', font=('arial 33 bold'), width=30).place(x=8)
        label = Label(root, text="Date:", width=10, bg='sky blue', fg='black')
        label.place(x=100, y=125)
        self.e6 = Entry(root, bg='sky blue', fg='blue', width=15)
        self.e6.place(x=155, y=125)


        label = Label(root, text="Ref to:", width=10, bg='sky blue', fg='black')
        label.place(x=100, y=160)
        c = StringVar()
        list = ['Dr.Diganto(ENT spc.)', 'Dr. Ajoy(EYE spc.)', 'Dr. Neha(Skin spc.)', 'Dr. Priya(Child spc.)', 'Dr. Pradip(Medicn spc.)', 'Dr.Vivek(anastasia spc.)']

        self.droplist = OptionMenu(root, c, *list)

        self.droplist.config(width=20, bg='tan')
        c.set('Doctors')
        self.droplist.place(x=170, y=150)
         
        #c = StringVar()
        var = IntVar()

        Label(root, text='Payment Method:', bg='sky blue', fg='black', font=('arial 20 bold')).place(x=100, y=230)
        Radiobutton(root, text='Cash', value=1, variable=var, bg='sky blue', fg='black', font=('arial 20 bold') ).place(x=350, y=230)
        Radiobutton(root, text='Card', value=2, variable=var, bg='sky blue', fg='black', font=('arial 20 bold')).place(x=480, y=230)

        Button(text='Submit', command=self.click, bg='yellow', width=15, font=('arial 10 bold')).place(x=310, y=360)
    def click(self):
        #Button(text='Submit', command=self.click, bg='yellow', width=15, font=('arial 10 bold')).place(x=310, y=360)

        Label(text='your amount is Rs.400/-:', fg='red', font=('arial 15 bold')).place(x=250, y=460)





















#MAIN

if __name__ == '__main__':
    root = Tk()
    #root.geometry('10x500')
    application = pay(root)
    root.mainloop()
