#!/usr/bin/python3.0
#-*- coding: utf-8 -*-

from tkinter import *
from tkinter.messagebox import *
base=Tk()
base.title("Calculatrice NPI")

pile=[]
boulvar= True

#'Entry' init var
valeur = StringVar()
valeur.set("0")
liste = StringVar()
liste.set("0")

#'zones' entree-sortie et vue pile
entree = Entry(base, textvariable=valeur, width=11, justify=RIGHT)
entree.grid(row=0,padx=20,pady=20,columnspan=5, sticky=E)
acumul = Entry(base, textvariable=liste, width=12, justify=LEFT)
acumul.grid(row=0,padx=20,pady=20,columnspan=3, sticky=E)

#chiffres,operateurs,symboles
def un():
    global boulvar
    if boulvar:
        entree.delete(0,END)
        boulvar= False
    entree.insert(END,1)
def deux():
    global boulvar
    if boulvar:
        entree.delete(0,END)
        boulvar= False
    entree.insert(END,2)    
def trois():
    global boulvar
    if boulvar:
        entree.delete(0,END)
        boulvar= False
    entree.insert(END,3)
def quatre():
    global boulvar
    if boulvar:
        entree.delete(0,END)
        boulvar= False
    entree.insert(END,4)
def cinq():
    global boulvar
    if boulvar:
        entree.delete(0,END)
        boulvar= False
    entree.insert(END,5)
def six():
    global boulvar
    if boulvar:
        entree.delete(0,END)
        boulvar= False
    entree.insert(END,6)
def sept():
    global boulvar
    if boulvar:
        entree.delete(0,END)
        boulvar= False
    entree.insert(END,7)
def huit():
    global boulvar
    if boulvar:
        entree.delete(0,END)
        boulvar= False
    entree.insert(END,8)
def neuf():
    global boulvar
    if boulvar:
        entree.delete(0,END)
        boulvar= False
    entree.insert(END,9)
def zero():
    global boulvar
    if boulvar:
        entree.delete(0,END)
        boulvar= False
    entree.insert(END,0)
    
def point():
    entree.insert(END,".")
def rst():
    pile.clear()
    valeur.set("0")
    liste.set("0")
def entrer():
    data=float(entree.get())
    pile.append(data)
    valeur.set("0")
    liste.set(pile)
    global boulvar
    boulvar= True
    
def plus():
    vaut= pile.pop()+ pile.pop()
    valeur.set(vaut)
    pile.append(vaut)
    liste.set(pile)
    global boulvar
    boulvar= True
def moins():
    vaut= -pile.pop() +pile.pop()
    valeur.set(vaut)
    pile.append(vaut)
    liste.set(pile)
    global boulvar
    boulvar= True
def fois():
    try:
        vaut= pile.pop()* pile.pop()
        valeur.set(vaut)
        pile.append(vaut)
        liste.set(pile)
        global boulvar
        boulvar= True
    except IndexError:
        showwarning(base,"minimum deux nombres dans la pile")
        rst()
def divi():
    try:
        vaut= 1/pile.pop() *pile.pop()
        valeur.set(vaut)
        pile.append(vaut)
        liste.set(pile)
        global boulvar
        boulvar= True
    except ZeroDivisionError:
        showwarning(base,"ne pas diviser par zero")
        rst()

#construction du pave numerique de la calculatrice
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
bouton0=Button(base, text="enter",padx=10,pady=10, borderwidth=5,command=entrer)
bouton0.grid(row=6,columnspan=5,sticky=W+E )

#boucle principle de la fenetre
base.mainloop()
