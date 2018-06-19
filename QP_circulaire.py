Q# encoding=utf-8

""" Classe QP_circulaire
    Queue de priorité sur un tableau circulaire"""

class QP_circulaire:
    
    # Constructeur
    def __init__ (self, cap):
        self._data = [None] * cap
        self._cap = cap
        self._premier = 0
        self._size = 0
    
    # Retourne la longueur de la file    
    def __len__ (self):
        return self._size
    
    # Retourne True si la file est vide    
    def is_empty(self):
        return len(self) == 0
    
    """Ajoute une valeur à la file si elle n'est pas à capacité
       ou si la valeur est plus grande que la valeur minimale
       de la file """
    def ajouter (self, valeur):
        if len(self) < self._cap:
            self.triInsertion(valeur)
        elif valeur > self.valMin():
            self.suivant()
            self.triInsertion(valeur)
         
    # Retourne la plus petite valeur dans la file
    def valMin(self):
        if self.is_empty():
            raise IndexError("Queue vide")
        return self._data[self._premier]
        
    """Supprime et retourne la plus petite valeur de la file
    et trie la liste """
    # Adapté à partir de ArrayQueue.py, trouvé sur Studium
    def suivant (self):
        if self.is_empty():
            raise IndexError("Queue vide")
        premierVal = self._data[self._premier]
        self._data[self._premier] = None    
        self._premier = (self._premier + 1) % self._cap
        self._size -= 1
        return premierVal
    
    # Ajout d'un nouvelle valeur dans la file et tri par insertion
    def triInsertion(self, valeur):
        dispo = (self._premier + len(self)) % self._cap
        self._data[dispo] = valeur
        self._size += 1
        index = self._premier
        while valeur > self._data[index]:
            index = (index + 1) % self._cap

        for i in range((len(self)+self._premier)-1, index-1, -1):
            self._data[i % self._cap] = self._data[(i-1) % self._cap]
            if (i % len(self)) == index:
                break
        self._data[index] = valeur
                
                
    def liste (self):
        if self.is_empty():
            raise IndexError("Queue vide")
        return self._data

if __name__ == '__main__':

    S = QP_circulaire(8)
    S.ajouter(3)
    print(S.valMin())   # Output 3
    S.ajouter(5)
    S.ajouter(2)
    print(S.suivant())  # Output 2
    S.ajouter(4)
    S.ajouter(6)
    S.ajouter(1)
    S.ajouter(9)
    S.ajouter(10)
    S.ajouter(8)
    S.ajouter(12)
    S.ajouter(11)
    S.ajouter(2)
    S.ajouter(0)
    S.ajouter(7)
    print(S.liste())
    print(S.suivant())  # Output 5
    print(S.suivant())  # Output 6
    print(S.suivant())  # Output 7
    print(S.suivant())  # Output 8
    print(S.suivant())  # Output 9
    print(S.suivant())  # Output 10
    print(S.suivant())  # Output 11
    print(S.suivant())  # Output 12
    print(S.is_empty()) # Output True
    try:
        print(S.suivant())  # Empty
    except IndexError:
        print("Erreur - Queue vide")