# Classes

## Entier

Les entiers peuvent utiliser les opérateurs suivants : + \* - / // \*\* %

Ils peuvent être comparés avec : < <= == > >=

### Initialiseur:

```py
entier(valeur : int | str | float | entier | chaine | decimal)
```

### Attributs:

```py
contenu : int
chiffres : tuple[int]
dictioChiffres : dict[str, int]
```

### Méthodes:

```py
racine(self : entier, o : int | entier) -> decimal
vers_int(self : entier) -> int
```

## Décimal

Les décimaux peuvent utiliser les opérateurs suivants: +

Ils peuvent êtres comparés avec : ==

### Initialiseur:

```py
decimal(o : int | str | chaine | entier | float | decimal)
```

### Attributs:

```py
contenu : float
```

### Méthodes:

```py
racine(self : decimal, o : int | entier) -> decimal
```

## Chaines

Les chaines peuvent utiliser les opérateurs suivants: +

### Initialiseur:

```py
chaine(o : int | str | float | bool | entier | chaine | decimal | booleen)
```

### Attributs:

```py
contenu : str
taille : int
nombres : list[int]
```

### Autres

Les chaines sont itérables

## Booléen

Ils peuvent êtres comparés avec : == not

### Initialiseur:

```py
booleen(o : int | entier | bool | booleen)
```

### Attributs:

```py
contenu : bool
```

# Fonctions

## Dans

```py
dans(a : Any, L : List | Tuple | chaine | str)
```

## Imprimer

Permet d afficher des listes, des entiers, des chaines de caracteres et des decimaux dans la console

```py
imprimer(*args : Any)
```

## Si

Prend deux parametre un boolen et une fonction qui sera executee si le booleen est vrai
Si une fonction B est specifiee elle est executée si la condition est fausse

```py
si(condition: bool, A : function, B : function = None, Aargs: list = [], Baargs: list = []):
```

## Distance

Permet de generer un tuple pour l iterer
debut sera la valeur a l indice 0 du tuple
pas sera l ecart entre chaque valeur

```py
distance(debut : int = 0, fin : int, pas : int = 1)
```

## Pour

Permet d iterer chaque valeut du type
la fonction a chaque passage sera executee avec comme parametre la valeur de l iterable

```py
pour(A : function, *args : list | tuple | str | chaine)
```
