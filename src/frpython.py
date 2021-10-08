from chaines import chaine
from decimaux import decimal
from entiers import entier
from erreurs import *

def afficher(*args) -> None:
    res = chaine()
    for a in args:
        if isinstance(a, chaine):
            res += a
        else:
            res += chaine(a)
    print(res)

imprimer = afficher

def si(condition : bool, A, B = None, Aargs : list = [], Baargs : list = []):
    """
    Les fonctions entree dans cette fonction doivent avoir un argument qui est une liste si rien n est mis la liste sera vide
    Retourne le resultat de la fonction
    """
    if condition:
        return A(Aargs)
    else:
        return B(Baargs)

def distance(*args) -> tuple:
    """Remplacement de la fonction range"""
    res = []
    if len(args) > 3:
        raise ErreurArguments("La fonction a été appelée avec trop d arguments")
    elif len(args) == 0:
        raise ErreurArguments("La fonction nécessite au moins 1 argument")

    if len(args) == 1: 
        a = 0
        max = args[0]
    else:
        a = args[0]
        max = args[1]
    
    if len(args) == 3:
        pas = args[2]
    else:
        pas = 1

    while a != max:
        res.append(a)
        a += pas
    return tuple(res)

