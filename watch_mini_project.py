from tkinter import *
from tkinter.ttk import*     #It provides access to the themed widget set

from time import strftime    #Python date method,you can use to convert dates to strings. 

root=Tk()
root.title("Clock")

def time():
    string=strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000,time)
    
label=Label(root,font=("ds-digital",80),background="black",foreground="cyan")
label.pack(anchor='center')
time()

mainloop()
