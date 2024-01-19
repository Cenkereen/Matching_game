import tkinter as tk
import random
from tkinter import messagebox

liste=[1,1,2,2,3,3,4,4,5,5,6,6]
random.shuffle(liste)
count=0
turn=0
puan=0


def click(n,m):
    global count,say1,say2
    if n["text"] == " ":
        if count==2:
            count+=1
            check()
        if count<2:
            n["text"]=liste[m]
            count += 1
        if count == 1:
            say1=n
        if count == 2:
            say2=n
            check()
        if count ==3:
            count=0

def check():
    global count,turn,puan

    if say1["text"] == say2["text"]:
        say1["bg"]="red"
        say2["bg"]="red"
        count=0
        turn+=1
        puan+=20
        var.set("Puan:"+str(puan))
    if count==3:
        say1["text"] = " "
        say2["text"] = " "
        puan-=10
        var.set("Puan:" + str(puan))
    if turn == 6:
        response = messagebox.askyesno("Eşleştir","Puan:"+str(puan)+"\nTekrar?")
        if response:
            reset()
            puan=0
            var.set("Puan:" + str(puan))
            turn=0
        else:
            form.quit()


form = tk.Tk()
form.title("Eşleştir")
form.geometry("460x404+700+250")
var=tk.StringVar()
var.set("Puan:" + str(puan))


def reset():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12

    label = tk.Label(form, textvariable=var, font="Times 20")
    label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
    b1=tk.Button(form,text=" ",font="Times 20",bg="white",height=3,width=7,command=lambda:click(b1,0))
    b1.grid(row=1,column=0)
    b2=tk.Button(form,text=" ",font="Times 20",bg="white",height=3,width=7,command=lambda:click(b2,1))
    b2.grid(row=1,column=1)
    b3=tk.Button(form,text=" ",font="Times 20",bg="white",height=3,width=7,command=lambda:click(b3,2))
    b3.grid(row=1,column=2)
    b4=tk.Button(form,text=" ",font="Times 20",bg="white",height=3,width=7,command=lambda:click(b4,3))
    b4.grid(row=1,column=3)
    b5=tk.Button(form,text=" ",font="Times 20",bg="white",height=3,width=7,command=lambda:click(b5,4))
    b5.grid(row=2,column=0)
    b6=tk.Button(form,text=" ",font="Times 20",bg="white",height=3,width=7,command=lambda:click(b6,5))
    b6.grid(row=2,column=1)
    b7=tk.Button(form,text=" ",font="Times 20",bg="white",height=3,width=7,command=lambda:click(b7,6))
    b7.grid(row=2,column=2)
    b8=tk.Button(form,text=" ",font="Times 20",bg="white",height=3,width=7,command=lambda:click(b8,7))
    b8.grid(row=2,column=3)
    b9=tk.Button(form,text=" ",font="Times 20",bg="white",height=3,width=7,command=lambda:click(b9,8))
    b9.grid(row=3,column=0)
    b10=tk.Button(form,text=" ",font="Times 20",bg="white",height=3,width=7,command=lambda:click(b10,9))
    b10.grid(row=3,column=1)
    b11=tk.Button(form,text=" ",font="Times 20",bg="white",height=3,width=7,command=lambda:click(b11,10))
    b11.grid(row=3,column=2)
    b12=tk.Button(form,text=" ",font="Times 20",bg="white",height=3,width=7,command=lambda:click(b12,11))
    b12.grid(row=3,column=3)

reset()
form.mainloop()