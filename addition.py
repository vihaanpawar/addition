from tkinter import *
root=Tk()

root.title("addition")
root.geometry('600x400')

lbl1=Label(root,text="adding two numbers")
lbl1.pack()

showResults=Label(root)
showResults.pack()


def add():
    a=5
    b=4
    r=a+b
    showResults["text"]="the result of 5+4 is "+str(r)

btn=Button(root,text="show result",command=add)
btn.pack()

root.mainloop()