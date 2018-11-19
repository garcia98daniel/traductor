import sys
from tkinter import *
def mhello():
	mtext = ment.get()
	mlabel2 = Label(mGui,text=" ").pack()
	mlabel2 = Label(mGui,text=mtext).pack()
	

mGui = Tk()
ment = StringVar()

mGui.geometry("450x450")
mGui.title("TRADUCTOR")

mlabel = Label(mGui,text="CAMILO GARCIA Y DANIEL GARCIA",bg="orange").pack()

mbutton = Button(mGui,text = "TRADUCIR", command = mhello,fg="blue",bg="lightblue").pack()

mEntry = Entry(mGui,textvariable=ment).pack()

mGui.mainloop()