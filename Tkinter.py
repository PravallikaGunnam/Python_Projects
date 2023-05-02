"""
import tkinter
from tkinter import *
root=tkinter.Tk()
#title
root.title('demo')

#size
root.geometry('700x700')

#label/Title
# label=tkinter.Label(root,text="sample GUI page").pack()

#button
b=Button(root,text="Submit",bg="orange",fg="red")
b.grid(column=1,row=1)

#Radio Button
r=Radiobutton(root,text="java",value=1)
r.grid(column=1,row=2)

#multiple Radio buttons
r1=Radiobutton(root,text="Python",value=2)
r1.grid(column=2,row=2)

r2=Radiobutton(root,text="c",value=3)
r2.grid(column=3,row=2)

r3=Radiobutton(root,text="SQL",value=4)
r3.grid(column=4,row=2)

#entry/text box
t=Entry(root,width=20)
t.grid(column=1,row=3)



#messagebox
from tkinter import messagebox
def Message():
    messagebox.showinfo("status","POP up message")
b=Button(root,text="show pop up message",command=Message)
b.pack()
root.mainloop()
"""
import tkinter
# import tkinter as tk
# from tkinter import  ttk
# from tkinter import *
# root=tk.Tk()
# root.title("comboBox")
# root.geometry("600x600")
# ttk.Label(root, text="newcombo", background="orange", foreground="yellow",
#           font="Arial").grid(row=0,column=1)

#combo box/drop down list
# n=StringVar
# course=ttk.Combobox(root,width=30,textvariable=n)
# course["values"]=("python","java","django","ML")
# course.grid(column=1,row=2)
#### course.current()

######Scrollbar
# from tkinter import scrolledtext
# text=scrolledtext.ScrolledText(root,wrap=tk.WORD,width=40,height=10)
# text.grid(column=2,row=1,padx=30,pady=50)
# ######### text.focus()
# root.mainloop()
# x=0
# while x<=18:
#     x=x+3
# print(x)

a=2*2//2
b=3//2*3
print(a,b)