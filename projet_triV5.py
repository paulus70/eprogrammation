# Projet Tri - Base de la programmation - Eric Derasse (2017)
# Auteurs :

# codage utilisé pour les accents
# coding=utf-8

import os  
import random
import time

#**********************************************************************
# Couche application (Graphique)
#**********************************************************************

# Selection des fonctions
def Menu(): 
    # Déclaration du tableau principal + secondaire
    maTable = []
    monTemps= []
    reponse = 1

    while reponse < 9: 
			
        print("Menu : ")
        print("------")
        print("")
        print("01. Initialiser")
        print("02. Charger")
        print("03. Tri rapide")
        print("04. Renverser")
        print("05. Dessiner")
        print("09. Sauver")	
        print("10. Quitter")
		
	#nomFichier = ""
        reponse = int(input("Faites votre choix : "))
        
        if reponse == 1 : 
            selectMenuInit()
			
        elif reponse == 2 :
            selectMenuCharger(maTable)
				
        elif reponse == 3 :
            selectMenuTriRapide(maTable,monTemps)

        elif reponse == 4 :
            selectMenuReverse(maTable)

        elif reponse == 5:
            selectMenuGraphe(monTemps)  

        elif reponse == 9 :
            selectMenuSauvegarde(maTable)
		
        elif reponse == 10 :
            break
		
        input("Appuyez sur une touche pour continuer ... ")
        os.system('cls')
	
def selectMenuInit() :
	
    nomFichier = input("Quel est le nom de votre fichier ?  ")
    nb = int(input("Combien de nombres voulez-vous ? "))
	
    if not nomFichier.isalpha():
        nomFichier="iniTab.txt"
		
    initTab(nomFichier,nb)
	
def selectMenuCharger(maTable):
        
    nomFichier = input("Quel est le nom de votre fichier ? ")
    nb = int(input("Combien de nombres voulez-vous ? "))

    if not nomFichier.isalpha():
            nomFichier="iniTab.txt"
	    
    maTable.clear()	
    loadTab(maTable,nomFichier,nb)
    print("Voici les nombres selectionnes : ",maTable)
    
def selectMenuTriRapide(maTable,monTemps):
    
    data=open("./data.txt", "a")
    print ("Voici les nombres selectionnes : ")
    print (maTable)
    #chronométrage du tri
    start_time = time.time()
    triRapide(maTable,0,len(maTable)-1)
    process=(time.time() - start_time)
    print("Voici les nombres tries : ")
    print (maTable)
    #enregistrement des résultats
    data.write("," + str(process) )
    print("Temps de calcul : ")
    print(process)
   
def selectMenuReverse(maTable):
    
    print ("Voici les nombres selectionnes : ")
    print(maTable)
    print ("Voici les nombres inversés : ")
    Reverse(maTable)
    
def selectMenuSauvegarde(maTable):
    
    nomFichier = input("Quel est le nom de votre fichier de sauvegarde ? ")

    if not nomFichier.isalpha():
        nomFichier="saveTab.txt"
	    
    saveTab(maTable,nomFichier)


def selectMenuGraphe(monTemps):
    import matplotlib.pyplot as plt
    
    #relecture des chiffres
    nomFichier="source"
    monTemps=readTemps(nomFichier)
    print ("Voici les mesures realisées : ")
    print(monTemps)
    monNbre=[0, 100, 1000, 10000, 100000, 1000000]
    print ("Voici les quantités utilisées: ")
    print(monNbre)
    #dessin du graphique
    plt.plot(monNbre,monTemps)
    plt.xlabel('nombres')
    plt.ylabel('temps')
    plt.title('Complexite tri-rapide')
    plt.show()
    
#**********************************************************************
# Couche logique (Métier)
#**********************************************************************

def Reverse(maTable):
    x = len(maTable)-1
    i = 0
    while i < x:
        temp = maTable[i]
        maTable[i] = maTable[x]
        maTable[x] = temp
        i = i + 1
        x = x - 1
    print (maTable)
        
#def triRapide(maTable, left, right):
    
    #méthode de tri rapide récursive à complèter

def partition(myList, start, end):
    pivot = myList[start]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
            #print(myList)
        else:
            # swap places
            memo=myList[left]
            myList[left]=myList[right]
            myList[right]=memo
    # swap start with myList[right]
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp
    return right

def triRapide(myList, start, end):
    if start < end:
        # partition the list
        split = partition(myList, start, end)
        # sort both halves
        triRapide(myList, start, split-1)
        triRapide(myList, split+1, end)
    return myList

#**********************************************************************
# Couche données (Data)
#**********************************************************************			

# Génération des nombres entier aléatoires et sauvegarde dans un fichier

def initTab(fichier,nb):
	fichier = open(fichier,"w")
	for i in range(0,nb):
		nombre = random.randint(0,nb)
		print ((nombre), file = fichier)
	fichier.close()        
	
# Chargement du fichier dans un tableau en mémoire

def loadTab(maTable,fichier,nb):
	fichier = open(fichier,"r")
	for i in range(nb):
		var = fichier.readline()
		maTable.append(int(var))
	fichier.close()

# Sauvegarde du tableau en mémoire dans un fichier

def saveTab(maTable,fichier):
	fichier = open(fichier,"w")	
	for i in range(0,len(maTable)-1):
		print ((maTable[i]), file = fichier)
	fichier.close()

#relecture des temps de calcul chronométrés

def readTemps(fichier):
    source=open("data.txt", "r")
    texte= source.read()
    ligne = texte.split(",")
    tableau = [float(i) for i in ligne]
    montemps=tableau
    source.close()
    return montemps
    

#**********************************************************************
# Programme principal
#**********************************************************************	
Menu()
