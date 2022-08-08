
def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())

import tkinter
from tkinter import  ttk
root=tkinter.Tk()
root.configure(bg="DarkSalmon")
root.title("NAVGURUKUL")
frame_tasks=tkinter.Frame(root)
listbox_tasks1=ttk.Label(frame_tasks,text="NAVGURUKUL BANGALORE CAMPUS TEAM LIST",font="normal 11 bold",background="pink",)

label=tkinter.Label(root,text="TEAM PROJECT",font=("Arial Bold",60),fg="Tomato").pack(pady=30,padx=30)
root.geometry("600x600")


def run_animation():
    while True:
        try:
            global photo
            global frame
            global label
            photo = tkinter.PhotoImage(
                file = photo_path,
                format = "gif - {}".format(frame)
                )

            label.configure(image = "saiphoto.gif")

            frame = frame + 1

        except Exception:
            frame = 1
            break

photo_path = "/home/dhanashri/Desktop/saiphoto.gif"

photo = tkinter.PhotoImage(
    file = photo_path,
    )
label = tkinter.Label(
    image = photo
    )
animate = tkinter.Button(
    root,
    text = "animate",
    command = run_animation
    )

label.pack(side=tkinter.LEFT)

def submit():
    items=[]
    for index in listbox.curselection():
        items.insert(index,listbox.get(index))
    
    print("selection of item:","Will be displayed here")
    
    for index in items:
        print(index)

def delete():
    for index in reversed (listbox.curselection()):
        listbox.delete(index)
    
    listbox.config(height=listbox.size())

listbox=tkinter.Listbox(root,fg="blue",bg="Aquamarine",
                        font=("constantia",35),
                        width=12,
                        selectmode=tkinter.MULTIPLE)
listbox.pack(padx=34,pady=34)

listbox.insert(1,"Banana")
listbox.insert(2,"Apple")
listbox.insert(3,"Strawberry")
listbox.insert(4,"Grapes")
listbox.insert(5,"Oranges")

listbox.config(height=listbox.size())

entryBox=tkinter.Entry(root,bg="PaleVioletRed",font=("Arial BOLD",15),width=15)
entryBox.pack()

submitButton=tkinter.Button(root,text="submit",command=submit,bg="green",fg="pink",font=("Arial BOLD",30))
submitButton.pack(padx=38,pady=38)

addButton=tkinter.Button(root,text="add",command=add,font=("Arial BOLD",30),bg="SkyBlue",fg="red")
addButton.pack(padx=24,pady=24)

deleteButton=tkinter.Button(root,text="delete",command=delete,font=("Arial BOLD",30),bg="Crimson",fg="white")
deleteButton.pack(padx=14,pady=14)

root.mainloop()