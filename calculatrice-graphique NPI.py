
from tkinter import *
from tkinter.messagebox import *
base=Tk()
base.title("Calculatrice NPI")
pile=[]
#'Entry' init var
value = StringVar()
value.set("0")
liste = StringVar()
liste.set("0")
#entree-sortie zones
entree = Entry(base, textvariable=value, width=11, justify=RIGHT)
entree.grid(row=0,padx=20,pady=20,columnspan=5, sticky=E)
sortie = Entry(base, textvariable=liste, width=12, justify=LEFT)
sortie.grid(row=0,padx=20,pady=20,columnspan=3, sticky=E)
#suite chiffres,operateurs,symboles
def valeur():
    data=float(entree.get())
    #value.set(data)
    pile.append(data)
    value.set("0")
    liste.set(pile)
    #liste.set(pile[len(pile)-1])
    print(pile)
def un():
    entree.insert(END,1)
def deux():
    entree.insert(END,2)    
def trois():
    entree.insert(END,3)
def quatre():
    entree.insert(END,4)
def cinq():
    entree.insert(END,5)
def six():
    entree.insert(END,6)
def sept():
    entree.insert(END,7)
def huit():
    entree.insert(END,8)
def neuf():
    entree.insert(END,9)
def zero():
    entree.insert(END,0)
def point():
    entree.insert(END,".")
def rst():
    pile.clear()
    value.set("0")
    liste.set("0")
    print(pile)
def plus():
    vaut=pile.pop()+ pile.pop()
    value.set(vaut)
    #pile.append(vaut)
    liste.set(pile)
    #liste.set("0")
    #value.set(pile)
    print(pile)
def moins():
    vaut=pile.pop()- pile.pop()
    value.set(vaut)
    pile.append(vaut)
    liste.set(pile)
    print(pile)
def fois():
    try:
        vaut=pile.pop()* pile.pop()
        value.set(vaut)
        pile.append(vaut)
        liste.set(pile)
        print(pile)
    except IndexError:
        showwarning(base,"minimum deux nombres dans la pile")
        rst()
        print("minimum deux nombres dans la pile")
def divi():
    try:
        vaut=pile.pop()/ pile.pop()
        value.set(vaut)
        pile.append(vaut)
        liste.set(pile)
        print(pile)
    except ZeroDivisionError:
        showwarning(base,"ne pas diviser par zero")
        rst()
        print("ne pas diviser par zero")
#edition du pave numerique de la calculatrice
#bouton chiffres
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
#boucle de scrutation de la fenetre
base.mainloop()
