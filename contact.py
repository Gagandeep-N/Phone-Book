from tkinter import *
from tkinter import ttk

from setuptools import Command
from views import *
from tkinter import messagebox

clr0 = "#ffffff"
clr1 = "#000000"
clr2 = "#4456F0"

window = Tk()
window.title("Contact Book")
window.geometry("485x450")
window.configure(background=clr0)
window.resizable(width=FALSE,height=FALSE)


#=====frames======#
frame_up = Frame(window,width=500,height=50,bg=clr2)
frame_up.grid(row=0,column=0,padx=0,pady=1)

frame_down = Frame(window,width=500,height=150,bg=clr0)
frame_down.grid(row=1,column=0,padx=0,pady=1)

frame_table = Frame(window,width=500,height=100,bg=clr0,relief="flat")
frame_table.grid(row=2,column=0,padx=10,pady=1,columnspan=2,sticky=NW)

#functions#
def show():
    global tree
    list_header = ['Name', 'Gender', 'Telephone', 'Email']

    demo_list = view()

    tree = ttk.Treeview(frame_table,selectmode="extended",columns=list_header,show="headings")

    y_scroll = ttk.Scrollbar(frame_table,orient="vertical",command=tree.yview)
    x_scroll = ttk.Scrollbar(frame_table,orient="horizontal",command=tree.xview)
    tree.configure(yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)

    tree.grid(column=0,row=0,sticky='nsew')
    y_scroll.grid(column=1,row=0,sticky='ns')
    x_scroll.grid(column=0,row=1,sticky='ew')

    #tree head
    tree.heading(0,text='Name',anchor=NW)
    tree.heading(1,text='Gender',anchor=NW)
    tree.heading(2,text='Telephone',anchor=NW)
    tree.heading(3,text='E-mail',anchor=NW)

    #tree columns
    tree.column(0,width=120,anchor='nw')
    tree.column(1,width=50,anchor='nw')
    tree.column(2,width=100,anchor='nw')
    tree.column(3,width=180,anchor='nw')

    for item in demo_list:
        tree.insert('','end',values=item)

show()

def insert():
    Name = e_name.get()
    gender = c_gender.get()
    telephone = e_telephone.get()
    Email = e_email.get()

    data = [Name,gender,telephone,Email]

    if Name == '' or gender == '' or telephone == '' or Email == '':
        messagebox.showwarning('Error','Please fill all the fields!')
    else:
        add(data)
        messagebox.showinfo('Success','Data added successfully!')
        e_name.delete(0,'end')
        c_gender.delete(0,'end')
        e_telephone.delete(0,'end')
        e_email.delete(0,'end')

        show()


def to_update():
    try:
        tree_data = tree.focus()
        tree_dictionary = tree.item(tree_data)
        tree_list = tree_dictionary['values']

        Name = str(tree_list[0])
        Gender = str(tree_list[1])
        Telephone = str(tree_list[2])
        Email = str(tree_list[3])

        e_name.insert(0,Name)
        c_gender.insert(0,Gender)
        e_telephone.insert(0,Telephone)
        e_email.insert(0,Email)

        def confirm():
            new_name = e_name.get()
            new_gender = c_gender.get()
            new_telephone = e_telephone.get()
            new_email = e_email.get()

            data = [new_telephone,new_name,new_gender,new_telephone,new_email]

            update(data)
            messagebox.showinfo('Success','Data updated successfully!')

            e_name.delete(0,'end')
            c_gender.delete(0,'end')
            e_telephone.delete(0,'end')
            e_email.delete(0,'end')

            for widget in frame_table.winfo_children():
                widget.destroy()

            b_confirm.destroy()

            show()
        b_confirm = Button(frame_down,text="Confirm",width=10,height=1,bg=clr2,fg=clr0,font=('Ivy 8 bold'),command=confirm)
        b_confirm.place(x=290,y=110)
    except IndexError:
        messagebox.showerror('Error','Select one record from table!')

def to_remove():
    try:
        tree_data = tree.focus()
        tree_dictionary = tree.item(tree_data)
        tree_list = tree_dictionary['values']

        tree_telephone = str(tree_list[2])

        remove(tree_telephone)

        messagebox.showinfo('success','data has been deleted!')

        for widget in frame_table.winfo_children():
            widget.destroy()
        show()
    except IndexError:
        messagebox.showerror('Error','Select one record from table!')

def to_search():
    telephone = e_search.get()
    data = search(telephone)

    def delete_command():
        tree.delete(*tree.get_children())
    delete_command()

    for item in data:
        tree.insert('','end',values=item)

    e_search.delete(0,'end')



#======frame up widgets=====#
app_name = Label(frame_up,text="CONTACT BOOK",height=1,font=('Verdana 17 bold'),fg = clr0,bg=clr2)
app_name.place(x=5,y=5)

#=====frame down widgets=====#
l_name = Label(frame_down,text="Name *",width=20,height=1,font=('Ivy 10'),bg=clr0,anchor=NW)
l_name.place(x=10,y=20)
e_name = Entry(frame_down,width=25,justify="left",highlightthickness=1,relief="solid")
e_name.place(x=80,y=20)

l_gender = Label(frame_down,text="Gender *",width=20,height=1,font=('Ivy 10'),bg=clr0,anchor=NW)
l_gender.place(x=10,y=50)
c_gender = ttk.Combobox(frame_down,width=22)
c_gender['values'] = ['M','F','O']
c_gender.place(x=80,y=50)

l_telephone = Label(frame_down,text="Telephone*",width=20,height=1,font=('Ivy 10'),bg=clr0,anchor=NW)
l_telephone.place(x=10,y=80)
e_telephone = Entry(frame_down,width=25,justify="left",highlightthickness=1,relief="solid")
e_telephone.place(x=80,y=80)

l_email = Label(frame_down,text="E-mail *",width=20,height=1,font=('Ivy 10'),bg=clr0,anchor=NW)
l_email.place(x=10,y=110)
e_email = Entry(frame_down,width=25,justify="left",highlightthickness=1,relief="solid")
e_email.place(x=80,y=110)

b_search = Button(frame_down,text="Search",height=1,bg=clr2,fg=clr0,font=('Ivy 8 bold'),command=to_search)
b_search.place(x=290,y=20)
e_search = Entry(frame_down,width=16,justify="left",font=('Ivy 11'),highlightthickness=1,relief="solid")
e_search.place(x=347,y=20)

b_view = Button(frame_down,text="View",width=10,height=1,bg=clr2,fg=clr0,font=('Ivy 8 bold'),command=show)
b_view.place(x=290,y=50)

b_add = Button(frame_down,text="Add",command=insert,width=10,height=1,bg=clr2,fg=clr0,font=('Ivy 8 bold'))
b_add.place(x=400,y=50)

b_update = Button(frame_down,text="Update",command=to_update,width=10,height=1,bg=clr2,fg=clr0,font=('Ivy 8 bold'))
b_update.place(x=400,y=80)

b_delete = Button(frame_down,text="Delete",width=10,height=1,bg=clr2,fg=clr0,font=('Ivy 8 bold'),command=to_remove)
b_delete.place(x=400,y=110)








window.mainloop()