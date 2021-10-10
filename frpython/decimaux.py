from frpython.erreurs import TypeInconnu


class decimal:

    contenu: float

    def __init__(self, o: object) -> None:
        if isinstance(o, (float, decimal)):
            if type(o) == float:
                a = o
            else:
                a = o.contenu
            self.contenu = a
        
        elif isinstance(o, int):
            self.contenu = float(o)

    def racine(self, o : int = 2):
        return self.contenu ** (1/o)

    def __gt__(self, o: object) -> bool:
        if isinstance(o, float):
            return self.contenu > o
        return self.contenu > o.contenu

    def __lt__(self, o: object) -> bool:
        if isinstance(o, float):
            return self.contenu < o
        return self.contenu < o.contenu

    def __eq__(self, o: object) -> bool:

        if isinstance(o, float):
            return self.contenu == o

        elif isinstance(o, decimal):
            return self.contenu == o.contenu

        else:
            raise TypeInconnu(f"Impossible de comparer ces deux types (decimal et {o.__class__}")

    def __add__(self, o: object):
        if isinstance(o, float):
            return decimal(self.contenu + o)
        return decimal(self.contenu + o.contenu)
    
    def __sub__(self, o : object) -> object:
        if isinstance(o, float):
            return decimal(self.contenu - o)
        return decimal(self.contenu - o.contenu)
