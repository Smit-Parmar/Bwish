import tkinter as tk
from tkinter import messagebox as mb
import time
screen = tk.Tk()
screen.geometry("200x130")
strvar = tk.StringVar(screen)
lst = []
def check():
   num = mo.get()
   dt = clicked.get()
   m = clicked2.get()
   name = nm.get()
   if num.isnumeric() and name and dt.isnumeric() and m.isnumeric():
      return True
   else:
      return False
def setvar(value,color="black"):
    strvar.set(value)
    tk.Label(screen, textvariable= strvar,fg=color).place(x = 100,y = 70)
def onClick():
   setvar("")
   if check():
      file=open("Data.txt","a+")
      firstname=nm.get()
      #print(firstname)
      dt=clicked.get()
      m=clicked2.get()
      m = int(m)
      dt = int(dt)
      if m in range(1,10):
         m = "0"+str(m)
      if dt in range(1,10):
         dt = "0"+str(dt)
      mobilenumber=mo.get()
      #print(mobilenumber)
      file.writelines("Name: %s Birthdate:%s/%s MO:%s\n"%(firstname,dt,m,mobilenumber))
      file.close()
      time.sleep(1)
      setvar("Saved","green")
      nm.delete(0,"end")
      mo.delete(0,"end")
      clicked2.set("MM")
      clicked.set("DD")
   else:
      setvar("Invalid Input","red")


name=tk.Label(screen,text="Name").grid(row=0,column=0)
nm=tk.Entry(screen)
nm.grid(row=0,column=1)

clicked=tk.StringVar()
clicked.set("DD")
for num in range(1,32):
   lst.append(num)

number=tk.Label(screen,text="Ph. Number").grid(row=1,column=0)
mo=tk.Entry(screen)
mo.grid(row=1,column=1)

bd=tk.Label(screen,text="Birthdate").place(x = 5,y = 47)
dates=tk.OptionMenu(screen,clicked,*lst)
dates.place(x = 67,y = 41)
clicked.set(clicked.get())
lst = []

for num in range(1,13):
   lst.append(num)
########
clicked2=tk.StringVar()
clicked2.set("MM")
months=tk.OptionMenu(screen,clicked2,*lst)
months.place(x = 130,y = 41)
clicked2.set(clicked2.get())

stts = tk.Label(screen,text="Status: ").place(x = 10,y = 70)

btn=tk.Button(screen,text="Add",command=onClick,width=7).place(x = 30,y = 95)
btn2=tk.Button(screen,text="Cancel",command=screen.quit,width=7).place(x = 110,y = 95)



screen.mainloop()
