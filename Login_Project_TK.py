# import tkinter as tk
# from tkinter import *
# from tkinter import messagebox
#
# root=tk.Tk()
# root.title("Login Page")
# root.geometry("600x600")
# global e1
# global e2
#
# lable1=Label(root,text="User Name").place(x=10,y=10)
# lable2=Label(root,text="Password").place(x=10,y=40)
#
# e1=Entry(root)
# e1.place(x=140,y=10)
#
# e2=Entry(root)
# e2.place(x=140,y=40)
# e2.config(show="*")
#
# def Ok():
#     uname= e1.get()
#     Password= e2.get()
#
#     if uname =="" and Password=="":
#         messagebox.showinfo("","Please provide uname and password")
#     elif uname=="admin" and Password=="123":
#         messagebox.showinfo("login Sucess")
#         root.destroy()
#     else:
#         messagebox.showinfo("","Incorrect uname and Password")
#
# Button(root,text="Login",command=Ok,width=10,height=2).place(x=10,y=100)
# root.mainloop()
