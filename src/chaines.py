class chaine:
    """
    Pour les chaines de caracteres
    """
    contenu : str = ""
    taille : int = 0
    nombresStr = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def __init__(self, o=""):
        res = []
        if type(o) == int:
            i = 10
            while o > i:
                res.append(o%i)
                i *= 10
            res.append(o%i)
            res.reverse()
            for n in res:
                self.contenu += self.nombresStr[n]
                self.taille += 1
        
        elif type(o) == str:
            self.contenu = o
            print("o:", o)
            for _ in self.contenu:
                self.taille += 1


    def __add__(self, o : object):
        res = ""
        for c in self.contenu:
            res += c
        for c in o.contenu:
            res += c
        print(res)
        return chaine(res)

    def __iadd__(self, o : object):
        res = ""
        for c in self.contenu:
            res += c
        for c in o.contenu:
            res += c
        print(self.contenu)
        return chaine(res)

    def __str__(self) -> str:
        return self.contenu          
            
