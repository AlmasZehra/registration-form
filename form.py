from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("                                                    Registration Form")
root.geometry('800x800')
bg= PhotoImage(file="D:\\N\\register.png")

my_label= Label(root, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

label_1 = Label(root, text="Full Name",fg='white',bg="brown", width=16,font=("bold", 12))
label_1.place(x=60,y=60)
entry_1 = Entry(root)  #writing space
entry_1.place(x=220,y=60) # x is left to right and y is up and down

label_2 = Label(root, text="Email",fg='white',bg="brown", width=16,font=("bold", 12))
label_2.place(x=60,y=110) # y is at difference of 50
entry_2 = Entry(root)
entry_2.place(x=220,y=110)

label_3 = Label(root, text="Gender",fg='white',bg="brown", width=16,font=("bold", 12))
label_3.place(x=60,y=160)
var = IntVar()
Radiobutton(root, text="MALE",padx = 2, variable=var, value=1, font=("bold", 10), bg="grey").place(x=220,y=160)
Radiobutton(root, text="FEMALE",padx = 4, variable=var, value=2, font=("bold", 10), bg="grey").place(x=290,y=160)

label_4 = Label(root, text="Age",fg='white',bg="brown",width=16,font=("bold", 12))
label_4.place(x=60,y=210)
entry_2 = Entry(root)
entry_2.place(x=220,y=210)

passwordLabel = Label(root, text="Password",fg='white',bg="brown", width=16,font=("bold", 12))
passwordLabel.place(x=60,y=260)
password = StringVar()
passwordEntry = Entry(root, textvariable=password, show='*')
passwordEntry.place(x=220,y=260)  

def btnclick():
    messagebox.showinfo("Message", "Registration Done")
photo = PhotoImage(file="D:\\N\\sub.png")
btn= Button(root, image= photo, command=btnclick, border=0, bg="black")
btn.place(x=280,y=320)
root.mainloop()
