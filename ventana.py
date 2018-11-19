import sys
from tkinter import *
def mhello():
	mtext = ment.get()
	mlabel2 = Label(mGui,text=" ").pack()
	mlabel2 = Label(mGui,text=mtext).pack()
	return

mGui = Tk()
ment = StringVar()

mGui.geometry("450x450")
mGui.title("TRADUCTOR")

mlabel = Label(mGui,text="My Label").pack()

mbutton = Button(mGui,text = "TRADUCIR", command = mhello,fg="red",bg="blue").pack()

mEntry = Entry(mGui,textvariable=ment).pack()

mGui.mainloop()