from tkinter import *
from tkinter import ttk

class room:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1960x1080')
        self.root.title('Hospital Management System')
        root.configure(bg='light blue')

        # def d2(self):
        frame1 = Frame(root, width=1450, height=768, bg='light blue', highlightthickness=4,highlightbackground="dimgray").place(x=30, y=10)
        Label(root,text="1.Our Hospital is 3 floor.\r\n 2.There are total 200 rooms for paitent.\r\n 3.In one room two paitent can stay.\r\n 4.Total paitent bad are 400.\r\n 5.some extra rooms are here for many purpose.\r\n 6.some of the rooms are for laboratory.\r\n7.There are total 7 ICU in ground floor.\r\n8.In ground floor there are 50 rooms.\r\n9.In 2nd floor there are 70 rooms.\r\n 10.In 3rd floor there are 80 romms.",
              font=('arial 24 bold'), fg='green', bg='light blue').place(x=400, y=65)
        Label(root, text='Rooms Details', font=('arial 25 bold'), fg='black', bg='light blue').place(x=650, y=15)



# MAIN

if __name__ == '__main__':
    root = Tk()
    # root.geometry('10x500')
    application = room(root)
    root.mainloop()
