# Projet Graphe - Base de la programmation - Eric Derasse (2017)
# Auteurs : Paulin Demiautte (2018)

import os
import matplotlib.pyplot as plt
import networkx as nx

#**********************************************************************
# Couche application
#**********************************************************************

# Selection des fonctions
def Menu(): 
    reponse = 0
    
    while reponse < 10: 
			
        print("Menu : ")
        print("------")
        print("")
        print("1. Générer Graphe")
        print("2. Afficher Graphe")
        print("3. Déduire Arbre")
        print("4. Afficher Arbre")
        print("5. Résultats")
        print("6. Page Web")
        print("9. Sauver Graphe")	
        print("10.Quitter")
		
	#"nomFichier = ""
        reponse = int(input("Faites votre choix : "))
        
        if reponse == 1 :
            selectGénérerGraphe()
			
        elif reponse == 2 :
            selectAfficherGraphe()
				
        elif reponse == 3 :
            selectDéduireArbre()

        elif reponse == 4 :
            selectAfficherArbre()

        elif reponse == 5:
            selectResultatsHTML()

        elif reponse == 6:
            selectPageHTML()

        elif reponse == 9 :
            pass
		
        elif reponse == 10 :
            break
		
        #input("Appuyez sur une touche pour continuer ... ")
        #os.system('cls')

#**********************************************************************
# Couche logique (functions)
#**********************************************************************

# creation du graphe initial en mémoire

G = nx.petersen_graph()

def selectGénérerGraphe():

    e= [(0, 1, 10), (0, 4, 10), (0, 5, 10), (1, 2, 10), (1, 6, 10), (2, 3, 10),
    (2, 7, 10),(3, 4, 10), (3, 8, 10), (4, 9, 10), (5, 7, 10), (5, 8, 10),
    (6, 8, 10), (6, 9, 10), (7, 9, 10)]
    
    G.add_weighted_edges_from(e)
    
def selectAfficherGraphe():

    plt.plot()
    nx.draw(G, with_labels=True, font_weight='bold')
    #afficher poids sur dessin
    #S = nx.dijkstra_path(G, 0, 9) // mettre chemin en gras
    plt.show()
    
# extraction de l'arbre

def selectDéduireArbre():
    
    #S = nx.dijkstra_path(G, 0, 9)    // à supprimer
    T = nx.minimum_spanning_tree(G)
    
def selectAfficherArbre():
    
    #S = nx.dijkstra_path(G, 0, 9)    // à supprimer
    T = nx.minimum_spanning_tree(G)
    plt.plot()
    nx.draw(T, with_labels=True, font_weight='bold')
    plt.show()

# compilation des graphiques enregitrés

def selectResultatsHTML():

    S = nx.dijkstra_path(G, 0, 9)
    T = nx.minimum_spanning_tree(G)
    plt.subplot(121)
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.text(-1, 1.1, "Dijkstra")
    plt.text(-0.5, 1.1, S)
    plt.text(1.5, 1.1,"Spanning Tree from [0]")
    plt.subplot(122)
    nx.draw(T, with_labels=True, font_weight='bold')
    plt.savefig("visu.png")
    plt.show()

def selectPageHTML():

    f = open('Résultats.html','w')
    message ="""<html>
    <head></head>
    <body>
    <h4> Demo fonction de Petersen </h4>
    <p>
    Cette fonction génère un graphe-3D non orienté
    Constitué de 10 noeuds et 15 arrêtes
    Le graphe est d'ordre 10 et de degré 3
    </p>
    <h4>image comparative<h4>
    <img src="visu.png" alt="graphe" width="640" height="480">
    </body>
    </html>"""
    f.write(message)
    f.close()

#**********************************************************************
# Couche données (Data)
#**********************************************************************	
''' Néant, tout se fait en mémoire'''
#**********************************************************************
# Programme principal
#**********************************************************************
Menu()
