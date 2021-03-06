from typing import Any, List, Tuple

from .erreurs import ErreurArguments, TypeInconnu
from .chaines import chaine
from .entiers import entier


def si(condition: bool, A, B=None, Aargs: List = [], Baargs: List = []):
    """
    Les fonctions entree dans cette fonction doivent avoir un argument qui est une liste si rien n est mis la liste sera vide
    Retourne le resultat de la fonction
    """
    if condition:
        return A(Aargs)
    else:
        return B(Baargs)


def dans(a: bool, L: List) -> bool:
    for i in L:
        if i == a:
            return True
    return False


def imprimer(*args) -> None:
    """Traduction de la fonction print"""
    res = chaine()
    for a in args:
        if isinstance(a, chaine):
            res += a
        else:
            res += chaine(a)
    print(res)


def pour(fonction, *args):
    """Equivalent de la fonction for + ajout du support de l ecriture c de for"""
    res = 0
    if len(args) > 3:
        raise ErreurArguments(
            "La fonction a été appelée avec trop d arguments")
    elif len(args) == 0:
        raise ErreurArguments("La fonction nécessite au moins 2 argument")
    elif len(args) == 1:
        if isinstance(args[0], (list, tuple, str, chaine)):
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


def distance(*args) -> Tuple:
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


def tant_que(condition: bool, f, args: List = []):
    while condition:
        f(args)


def essayer(f, g, argsF: List = [], argsG: List = [], argsH: List = [],  h=None) -> Any:
    """ Essaye la fonction f si erreur execute g sinon execute h retourne le resultat de g ou h"""
    try:
        f(argsF)
    except:
        return g(argsG)
    else:
        return h(argsH)

