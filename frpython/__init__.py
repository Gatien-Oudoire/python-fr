from .erreurs import *
from .decimaux import decimal
from .booleen import booleen
from .chaines import chaine
from .entiers import entier
from .fonctions import dans, distance, pour, si, imprimer

def fr_python_info():
    try:
        imprimer("La librairie est prete")
    except:
        print("Erreur dans la librairie")


