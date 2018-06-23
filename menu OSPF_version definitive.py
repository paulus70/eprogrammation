# Projet Graphe - Base de la programmation - Eric Derasse (2017)
# Auteurs : Paulin Demiautte (2018)

import os
import networkx as nx
import matplotlib.pyplot as plt

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
            selectResultatsPNG()

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

''' recreation du graphe initial en mémoire via
    via readFile de la fct: "nx.petersen_graph()" '''

G = nx.read_gpickle("graphe.gpickle")
pos= nx.spring_layout(G)


def selectGénérerGraphe():          #  developement d'option possible au menu

    P = nx.petersen_graph()         #ici selection de types de graphes et/ou layouts
    
    arrêtes = list(P.edges)
    poids = [10]*15                 #ici poids et/ou nombre avec 'G.number_of_nodes()'
    L1 = arrêtes
    L2 = poids
    L3 = [None]*len(L1)             #  creation des futurs 3-tuples pondérés
    i=0
    while i<len(L1):
        L3[i] = L1[i]+(L2[i],)
        i=i+1
        
    P.add_weighted_edges_from(L3)

    #enregistrement graphe.dot ou .pickle
    nx.write_gpickle(P,"graphe.gpickle")

def selectAfficherGraphe():

    plt.plot()
    nx.draw(G, pos=pos, with_labels=True, font_weight='bold')
    edge_labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels, label_pos=0.5)
    plt.show()      

# extraction de l'arbre

def selectDéduireArbre():

    S = nx.dijkstra_path(G,0,9)
    nx.write_gpickle(S, "chemin.gpickle")
    T = nx.minimum_spanning_tree(G)
    nx.write_gpickle(T, "arbre.gpickle")

def selectAfficherArbre():

    T = nx.read_gpickle("arbre.gpickle")
    plt.plot()
    nx.draw(T, with_labels=True, font_weight='bold')
    plt.show()

# compilation des graphiques enregitrés

def edgesliste(S0):
    liste = S0
    n= len(liste)-1
    tuples=[(liste[i], liste[i+1]) for i in range(n)]
    return tuples

def selectResultatsPNG():

    S1 = nx.read_gpickle("chemin.gpickle")
    T1 = nx.read_gpickle("arbre.gpickle")
    L1 = edgesliste(S1)
    plt.subplot(221)
    pos= nx.spring_layout(G)
    nx.draw(G, pos=pos, with_labels=True, font_weight='bold')
    nx.draw_networkx_edges(G, pos=pos, edgelist=L1, edge_color='blue', width=5)
    plt.text(-1, 1.1, "Dijkstra")
    plt.text(-0.5, 1.1, S1)
    plt.text(1.5, 1.1,"Spanning Tree from [0]")
    plt.subplot(222)
    nx.draw(T1, with_labels=True, font_weight='bold')

    f= [(0, 4, 50), (4, 9, 50)]
    G.add_weighted_edges_from(f)
    S2 = nx.dijkstra_path(G, 0, 9)
    T2 = nx.minimum_spanning_tree(G)
    L2 = edgesliste(S2)
    plt.subplot(223)
    nx.draw(G, pos=pos, with_labels=True, font_weight='bold')
    nx.draw_networkx_edges(G, pos=pos, edgelist=L2, edge_color='blue', width=5)
    plt.text(-1.0, 1.1, "Dijkstra")
    plt.text(-0.5, 1.1, S2)
    plt.text(1.5, 1.1, "Spanning Tree from [0]")
    plt.subplot(224)
    nx.draw(T2, with_labels=True, font_weight='bold')
    
    plt.savefig("visu.png")
    plt.show()

def selectPageHTML():

    f = open('Résultats.html','w')
    message ="""<html>
    <head></head>
    <body>
    <h4> Demo fonction de Petersen </h4>
    <p>
    Cette fonction génère un graphe-3D non orienté<br>
    Constitué de 10 noeuds et 15 arrêtes<br>
    Le graphe estde degré 3 et d'ordre 10<br>
    </p>
    <h4> Demo algorithme de Dijkstra </h4>
    <p>
    L’algorithme du « chemin le plus court » fourni un tracé<br>
    de moindre pondération entre une source et une destination<br>
    voir l'image après un changement de poids sur le chemin 0-4-9<br>
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
''' PM: fichiers pickle '''
#**********************************************************************
# Programme principal
#**********************************************************************
Menu()
