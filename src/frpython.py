from chaines import chaine
from decimaux import decimal
from entiers import ent

def afficher(*args):
    res = chaine()
    for a in args:
        res += chaine(a)
    print(res)

def si(condition, A, B=None, Aargs=None, Baargs=None, resultat=None):
    if condition:
        resultat = A(Aargs)
    else:
        resultat = B(Baargs)
