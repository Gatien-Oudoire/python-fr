from erreurs import ErreurDeConversion

class entier:
    
    contenu : int = 0

    chiffres = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    dictioChiffres = {"0": 0, "1": 1, "2": 2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}

    def __init__(self, o) -> None:
        
        if isinstance(o, int):
            self.contenu = o

        elif isinstance(o, str):
            for c in o:
                if not (c in self.chiffres):
                    raise ErreurDeConversion(f"Il faut uniquement des chiffres dans la chaine:  {o}")
            l = []
            for chiffre in o.__reversed__():
                self.contenu += self.dictioChiffres[chiffre]
        
        elif isinstance(o, float):
            o = str(o).split(".")[0]
            for chiffre in o.__reversed__():
                self.contenu += self.dictioChiffres[chiffre]

    def __eq__(self, o: object) -> bool:
        return self.contenu == o.contenu

    def __gt__(self, o: object) -> bool:
        return self.contenu > o.contenu

    def __lt__(self, o: object) -> bool:
        return self.contenu < o.contenu
