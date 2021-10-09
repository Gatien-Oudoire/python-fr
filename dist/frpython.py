from typing import List, Tuple
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


def si(condition: bool, A, B=None, Aargs: list = [], Baargs: list = []):
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
        raise ErreurArguments(
            "La fonction a été appelée avec trop d arguments")
    elif len(args) == 0:
        raise ErreurArguments("La fonction nécessite au moins 1 argument")

    for v in args:
        if not isinstance(v, (int, entier)):
            raise TypeInconnu("Les arguments doivent etre des entiers")

    a = 0
    max = args[0]
    pas = 1

    if len(args) != 1:
        a = args[0]
        max = args[1]

    if len(args) == 3:
        pas = args[2]

    while a != max:
        res.append(a)
        a += pas
    return tuple(res)


def pour(fonction, *args):
    """Equivalent de la fonction for + ajout du support de l ecriture c de for"""
    res = 0
    if len(args) > 3:
        raise ErreurArguments(
            "La fonction a été appelée avec trop d arguments")
    elif len(args) == 0:
        raise ErreurArguments("La fonction nécessite au moins 2 argument")
    elif len(args) == 1:
        if isinstance(args[0], (List, Tuple, str, chaine)):
            i = 0
            while i < len(args[0]):
                fonction(args[0][i])
                i += 1
        elif isinstance(args[0], (int, entier)):
            i = 0
            r = distance(args[0])
            while i < len(r):
                fonction(r[i])
                i += 1
    elif isinstance(args[0], (int, entier)):
        i = 0
        if len(args) == 2:
            r = distance(args[0], args[1])
        else:
            r = distance(args[0], args[1], args[2])
        while i < len(r):
            fonction(r[i])
            i += 1