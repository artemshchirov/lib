from tkinter import *

def click():
    label.configure(text="Hello World")

root=Tk()
button=Button(root,text="Click Me",command=click, underline=6)
button.pack()
label=Label(root)
label.pack()
root.bind('<Alt_L><m>', lambda e:click())
root.mainloop()
