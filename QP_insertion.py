# encoding=utf-8

""" Classe QP_insertion
    Queue de priorité sur un tableau
    utilisant le tri par insertion """

class QP_insertion:
    
    # Constructeur
    def __init__ (self, cap):
        self._data = [None] * cap
        self._cap = cap
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
        return self._data[0]
        
    """Supprime et retourne la plus petite valeur de la file
       et trie la liste """
    def suivant (self):
        if self.is_empty():
            raise IndexError("Queue vide")
        delVal = self._data[0]
        self._data[0] = None
        for i in range(1,len(self),1):
            self._data[i-1] = self._data[i]
        self._size -= 1
        return delVal
    
    # Ajout d'un nouvelle valeur dans la file et tri par insertion
    # Adapté à partir de SortedListPriorityQueue.py, trouvé sur Studium    
    def triInsertion(self, valeur):
        if self.is_empty():
            self._data[0] = valeur
        else:
            self._data[len(self)] = valeur
            index = 0
            while valeur > self._data[index] and index < len(self):
                index += 1
            for i in range(len(self), index, -1):
                self._data[i] = self._data [i-1]
            self._data[index] = valeur
        self._size += 1
                        
    def liste (self):
        if self.is_empty():
            raise IndexError("Queue vide")  
        return self._data


if __name__ == '__main__':
    S = QP_insertion(8)
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