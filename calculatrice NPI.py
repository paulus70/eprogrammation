
from tkinter import *

base=Tk()
base.title("Calculatrice NPI")
pile=[]
#entree init
value = IntVar()
value.set(0)
#entree zone
entree = Entry(base, textvariable=value, width=15, justify=RIGHT)
entree.grid(row=0,padx=20,pady=20,columnspan=5, sticky=W+E )
#suite
def valeur():
    data=float(entree.get())
    value.set(data)
    pile.append(data)
    print(pile)
def un():
    value.set(1)
def deux():
    value.set(2)    
def trois():
    value.set(3)
def quatre():
    value.set(4)
def cinq():
    value.set(5)
def six():
    value.set(6)
def sept():
    value.set(7)
def huit():
    value.set(8)
def neuf():
    value.set(9)
def zero():
    value.set(0)
def point():
    #value.set(".")
    pass
def rst():
    value.set(0)
    pile.clear()
    print(pile)
def plus():
    vaut=pile.pop()+ pile.pop()
    value.set(vaut)
    pile.append(vaut)
    print(pile)
def moins():
    vaut=pile.pop()- pile.pop()
    value.set(vaut)
    pile.append(vaut)
    print(pile)
def fois():
    vaut=pile.pop()* pile.pop()
    value.set(vaut)
    pile.append(vaut)
    print(pile)
def divi():
    vaut=pile.pop()/ pile.pop()
    value.set(vaut)
    pile.append(vaut)
    print(pile)
#pave numerique
bouton1=Button(base, text="1",padx=20,pady=15, borderwidth=5,command=un)
bouton1.grid(row=1,column=1)
bouton2=Button(base, text="2",padx=20,pady=15, borderwidth=5,command=deux)
bouton2.grid(row=1,column=2)
bouton3=Button(base, text="3",padx=20,pady=15, borderwidth=5,command=trois)
bouton3.grid(row=1,column=3)
bouton4=Button(base, text="4",padx=20,pady=15, borderwidth=5,command=quatre)
bouton4.grid(row=2,column=1)
bouton5=Button(base, text="5",padx=20,pady=15, borderwidth=5,command=cinq)
bouton5.grid(row=2,column=2)
bouton6=Button(base, text="6",padx=20,pady=15, borderwidth=5,command=six)
bouton6.grid(row=2,column=3)
bouton7=Button(base, text="7",padx=20,pady=15, borderwidth=5,command=sept)
bouton7.grid(row=3,column=1)
bouton8=Button(base, text="8",padx=20,pady=15, borderwidth=5,command=huit)
bouton8.grid(row=3,column=2)
bouton9=Button(base, text="9",padx=20,pady=15, borderwidth=5,command=neuf)
bouton9.grid(row=3,column=3)
bouton10=Button(base, text="C",padx=20,pady=15, borderwidth=5,command=rst)
bouton10.grid(row=4,column=1)
bouton11=Button(base, text="0",padx=20,pady=15, borderwidth=5,command=zero)
bouton11.grid(row=4,column=2)
bouton12=Button(base, text=". ",padx=20,pady=15, borderwidth=5,command=point)
bouton12.grid(row=4,column=3)
#bouton operateurs
bouton13=Button(base, text="+",padx=20,pady=15, borderwidth=5,command=plus)
bouton13.grid(row=1,column=4)
bouton14=Button(base, text="-",padx=20,pady=15, borderwidth=5,command=moins)
bouton14.grid(row=2,column=4)
bouton15=Button(base, text="*",padx=20,pady=15, borderwidth=5,command=fois)
bouton15.grid(row=3,column=4)
bouton16=Button(base, text="/",padx=20,pady=15, borderwidth=5,command=divi)
bouton16.grid(row=4,column=4)
#bouton return
bouton0=Button(base, text="enter",padx=10,pady=10, borderwidth=5, command=valeur)
bouton0.grid(row=6,columnspan=5,sticky=W+E )

base.mainloop()
