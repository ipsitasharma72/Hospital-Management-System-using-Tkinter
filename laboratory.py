from tkinter import *
from tkinter import ttk

class lab:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1000x600')
        self.root.title('Hospital Management System')
        root.configure(bg='light blue')
        frame1 = Frame(root, width=870, height=500, bg='light blue', highlightthickness=4,
                       highlightbackground="dimgray").place(x=30, y=80)

        Label(root, text='Laboratory Department are:', font=('arial 18 bold'), fg='Red',
              bg='light blue').place(x=60, y=90)

        Label(root, text='Floor no.', font=('arial 18 bold'), fg='Red',
              bg='light blue').place(x=590, y=90)

        Label(root, text='1. Chemistry Lab:', font=('arial 10 bold'), fg='grey', bg='light blue').place(x=40,
                                                                                                                y=150)
        Label(root, text='2. Hematology Lab', font=('arial 10 bold'), fg='grey', bg='light blue').place(x=40,
                                                                                                                 y=180)

        Label(root, text='3. Radiology Lab:', font=('arial 10 bold'), fg='grey', bg='light blue').place(x=40,
                                                                                                                y=210)
        Label(root, text='4. Surgical pathology Lab:', font=('arial 10 bold'), fg='grey', bg='light blue').place(x=40,
                                                                                                                y=240)

        Label(root, text='5. Cytology Lab', font=('arial 10 bold'), fg='grey',
              bg='light blue').place(x=40,
                                     y=270)

        Label(root, text='6.Immunology Lab', font=('arial 10 bold'), fg='grey',
              bg='light blue').place(x=40,
                                     y=300)
        Label(root,text='Some Spcial test are done here:', font=('arial 18 bold'), fg='Red', bg='light blue').place(x=50, y=340)
        Label(root, text='1.Thyroid profile::', font=('arial 10 bold'), fg='gray', bg='light blue').place(
            x=40, y=390)
        Label(root, text='2.FSH,LH,prolactin:', font=('arial 10 bold'), fg='gray', bg='light blue').place(
            x=40, y=420)
        Label(root, text='3.Serum IgE,Serum Beta-HCG,Serum PSA:', font=('arial 10 bold'), fg='gray', bg='light blue').place(
            x=40, y=450)
        Label(root, text='4.Biopsy,FNAC,Bone Marrow Study:', font=('arial 10 bold'), fg='gray',
              bg='light blue').place(
            x=40, y=480)
        Label(root,text='**all the special test are done in ground floor', font=('arial 15 bold'), fg='red', bg='light blue').place(x=50, y=520)

        Label(root, text='2nd floor', font=('arial 10 bold'), fg='grey', bg='light blue').place(x=660,
                                                                                        y=150)
        Label(root, text='2nd floor', font=('arial 10 bold'), fg='grey', bg='light blue').place(x=660,
                                                                                         y=180)

        Label(root, text='2nd floor', font=('arial 10 bold'), fg='grey', bg='light blue').place(x=660,
                                                                                        y=210)
        Label(root, text='ground floor', font=('arial 10 bold'), fg='grey', bg='light blue').place(x=660,
                                                                                         y=240)

        Label(root, text='ground floor', font=('arial 10 bold'), fg='grey', bg='light blue').place(x=660,
                                                                                        y=270)
        Label(root, text='1st floor', font=('arial 10 bold'), fg='grey', bg='light blue').place(x=660,
                                                                                         y=300)

# MAIN

if __name__ == '__main__':
    root = Tk()
    # root.geometry('10x500')
    application = lab(root)
    root.mainloop()

