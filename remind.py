import Tkinter
import random

root = Tkinter.Tk()
root.configure(bg="white")
root.title("My Super To Do List")
root.geometry("500x500")
txt_input=StringVar()

def add_task():
   pass

def del_all():
   pass

def del_one():
   pass



lbl_title=Tkinter.Label(root,text="Reminder",bg="white")
lbl_title.pack()

lbl_display=Tkinter.Label(root,text=" ",bg="white")
lbl_display.pack()

txt=StringVar()
txt_input = Tkinter.Entry(root,width=15,textvariable=txt)
txt_input.pack()

btn_add_task=Tkinter.Button(root,text="Add task",fg='green',bg='white',command=add_task)
btn_add_task.pack()

btn_del_task=Tkinter.Button(root,text="Delete All",fg='green',bg='white',command=del_all)
btn_del_task.pack()

btn_del_one_task=Tkinter.Button(root,text="Delete One",fg='green',bg='white',command=del_one)
btn_del_one_task.pack()

btn_quit=Tkinter.Button(root,text="Exit",fg='green',bg='white',command=exit)
btn_quit.pack()

lb_tasks=Tkinter.Listbox(root)
lb_tasks.pack()


root.mainloop()
