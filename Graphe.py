
# coding=utf-8
# codage utilisé pour les accents

#******************************************************************
# votre nom, version xxx, 2017 
#******************************************************************


def lireData():
    source=open("data.txt", "r")
    texte= source.read()
    ligne = texte.split(",")   #dans un tableau
    tableau = [float(i) for i in ligne]
    monTemps=tableau
    source.close()
    return monTemps

def dessiner():
    import matplotlib.pyplot as plt
    monTemps=lireData()
    plt.plot(monTemps)
    plt.xlabel('nombres')
    plt.ylabel('temps')
    plt.show()


dessiner()
