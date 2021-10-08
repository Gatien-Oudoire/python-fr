from chaines import chaine
from decimaux import decimal
from entiers import entier

def afficher(*args) -> None:
    res : chaine = chaine()
    for a in args:
        if isinstance(a, chaine):
            res += a
        else:
            res += chaine(a)
    print(res)

def si(condition : bool, A, B = None, Aargs : list = [], Baargs : list = [], resultat=None):
    """
    Les fonctions entree dans cette fonction doivent avoir un argument qui est une liste si rien n est mis la liste sera vide
    """
    if condition:
        resultat = A(Aargs)
    else:
        resultat = B(Baargs)
