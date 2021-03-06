from .entiers import entier


class chaine:
    """
    Pour les chaines de caracteres
    """
    contenu: str = ""
    taille: int = 0
    nombresStr = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def __init__(self, o=""):
        res = []
        if isinstance(o, int):
            i = 10
            while o > i:
                res.append(o % i)
                i *= 10
            res.append(o % i)
            res.reverse()
            for n in res:
                self.contenu += self.nombresStr[n]
                self.taille += 1

        elif isinstance(o, str):
            self.contenu = o
            for _ in self.contenu:
                self.taille += 1

        elif isinstance(o, entier):
            i = 10
            while o.contenu > i:
                res.append(o.contenu % i)
                i *= 10
            res.append(o.contenu % i)
            res.reverse()
            for n in res:
                self.contenu += self.nombresStr[n]
                self.taille += 1

    def __add__(self, o: object):
        res = ""
        for c in self.contenu:
            res += c
        for c in o.contenu:
            res += c
        return chaine(res)

    def __str__(self) -> str:
        return self.contenu

    def __iter__(self):
        i = 0
        res = []
        while i < self.taille:
            res.append(self.contenu[i])
        return iter(res)

    def __eq__(self, o: object) -> bool:
        if isinstance(o, str):
            return self.contenu == o
        return self.contenu == o.contenu

    def a_l_envers(self) -> object:
        res = []
        for c in self.contenu:
            res.append(c)
        res.reverse()
        return chaine(res)
