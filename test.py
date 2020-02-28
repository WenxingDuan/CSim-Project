from tkinter import*
import time

root = Tk()
root.geometry("250x150")

val = StringVar()
l1 = Label(root,textvariable = val)
l1.pack()
val = val.set("............")


l2 = Label(root,text = "ppp")
l2.pack()

for a in range(10000):
    i = str(a)
    #val = val.set("8888")
    l2.config(text=i)
    a += 1
    time.sleep(0.1)

root.mainloop()
