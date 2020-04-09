from tkinter import *
import ledger_bk
window = Tk()
window.title("Account Management")

def __init__(self, master):
        self.master = master
        self.left = Frame(master, width=1000, height=500, bg='olivedrab1')
        self.left.pack(side=LEFT)
 
def view_command():
    lb.delete(0,END)
    for row in ledger_bk.viewall():
        lb.insert(END,row)

def search_command():
    lb.delete(0,END)
    for row in ledger_bk.search(name=name.get(),user=user.get(),password=password.get(),category=category.get()):
        lb.insert(END,row)

def add_command():
    ledger_bk.add(name.get(),user.get(),password.get(),category.get(),cdate.get())
    lb.delete(0,END)
    lb.insert(END,name.get(),user.get(),password.get(),category.get(),cdate.get())

def get_selected_row(event):
    try:
        global selected_tuple
        index=lb.curselection()[0]
        selected_tuple = lb.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
        e5.delete(0,END)
        e5.insert(END,selected_tuple[5])
    except IndexError:
        pass

def update_command():
    ledger_bk.update(selected_tuple[0],name.get(),user.get(),password.get(),category.get(),cdate.get())
    view_command()

def delete_command():
    ledger_bk.delete(selected_tuple[0])
    view_command()
    #lb.delete(END,get_selected_row.selected_tuple)
def clear_command():
    lb.delete(0,END)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)

l1 = Label(window,text="Name",width=10,height=2,font=(' algerian',15),bg='mistyrose3')
l1.grid(row=0,column=0,columnspan=1)
l2 = Label(window,text="Email",width=10,height=2,font=(' algerian',15),bg='grey')
l2.grid(row=1,column=0,columnspan=1)
l3 = Label(window,text="Password",width=10,height=2,font=(' algerian',15),bg='mistyrose3')
l3.grid(row=2,column=0,columnspan=1)
l4 = Label(window,text="Category",width=10,height=2,font=(' algerian',15),bg='grey')
l4.grid(row=3,column=0,columnspan=1)
l5 = Label(window,text="Date",width=10,height=2,font=(' algerian',15),bg='mistyrose3')
l5.grid(row=4,column=0,columnspan=1)

name=StringVar()
e1 = Entry(window,textvariable=name,width=50)
e1.grid(row=0,column=0,columnspan=15)

user=StringVar()
e2 = Entry(window,textvariable=user,width=50)
e2.grid(row=1,column=0,columnspan=15)

password=StringVar()
e3 = Entry(window,textvariable=password,show='*',width=50)
e3.grid(row=2,column=0,columnspan=15)

category=StringVar()
e4 = Entry(window,textvariable=category,width=50)
e4.grid(row=3,column=0,columnspan=15)

cdate=StringVar()
e5 = Entry(window,textvariable=cdate,width=50)
e5.grid(row=4,column=0,columnspan=15)

b1 = Button(window,text="Add",width=23,height=2,bg='Lemonchiffon4',command=add_command)
b1.grid(row=5,column=0)

b2 = Button(window,text="Update",width=23,height=2,bg='Lemonchiffon3',command=update_command)
b2.grid(row=5,column=1)

b3 = Button(window,text="Search",width=23,height=2,bg='Lemonchiffon4',command=search_command)
b3.grid(row=5,column=2)

b4 = Button(window,text="View All",width=23,height=2,bg='Lemonchiffon3',command=view_command)
b4.grid(row=5,column=3)

b5 = Button(window,text="Delete",width=23,height=2,bg='Lemonchiffon4',command=delete_command)
b5.grid(row=5,column=4)

b6 = Button(window,text="Cancel",width=23,height=2,bg='Lemonchiffon3',command=window.destroy)
b6.grid(row=5,column=5)

b7 = Button(window,text="Clear All",width=20,height=1,bg='Lemonchiffon4',command=clear_command)
b7.grid(row=0,column=5)

lb=Listbox(window,height=30,width=150)
lb.grid(row=6,column=0,columnspan=6)

sb=Scrollbar(window)
sb.grid(row=6,column=6,rowspan=6)

lb.configure(yscrollcommand=sb.set)
sb.configure(command=lb.yview)

lb.bind('<<ListboxSelect>>',get_selected_row)
window.geometry('1000x1000')
window.mainloop()

