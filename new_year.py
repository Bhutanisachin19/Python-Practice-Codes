from tkinter import *
from time import sleep
x=0
root=Tk()
root.title("Happy New Year")
while x<200:
 x+=1
 label1=Label(root)
 label1['text']=2020
 label1['font']=("Times",x)
 label1.grid(row=0,column=0)
 root.update_idletasks()
 sleep(.05)
 