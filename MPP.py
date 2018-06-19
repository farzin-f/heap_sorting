# encoding=utf-8

# Monceau p-aire (p donné en paramètre)
    
class MPP:
    
    # Constructeur
    def __init__(self, cap, p):
        self._data = [None] * cap
        self._cap = cap
        self._size = 0
        self._p = p
    
    # Retourne la longueur de la file
    def __len__(self):
        return self._size
    
    # Retourne True si la file est vide
    def is_empty(self):
        return len(self) == 0

    """Ajoute une valeur à la file si elle n'est pas à capacité
       ou si la valeur est plus grande que la valeur minimale
       de la file """
    def ajouter (self, valeur):
        if len(self) < self._cap:
            self._data[len(self)] = valeur
            self._size += 1
            self.upheap(len(self)-1)
        elif valeur > self.valMin():
            self.suivant()
            self._data[len(self)] = valeur
            self._size += 1
            self.upheap(len(self)-1)
         
    # Retourne la plus petite valeur dans la file
    def valMin(self):
        if self.is_empty():
            raise IndexError('Monceau vide')
        return self._data[0]
        
    """Supprime et retourne la plus petite valeur de la file
       et trie la liste """        
    def suivant (self):
        if self.is_empty():
            raise IndexError('Monceau vide')
        self.swap(0,(len(self)-1))
        result = self._data[len(self)-1]
        self._data[len(self)-1] = None
        self._size -= 1
        self.downheap(0)
        return result
    
    # Adapté à partir de ArrayHeapPriorityQueue.py, trouvé sur Studium
    def upheap(self, index):
        parent = self._parent(index)
        if (index > 0) and (self._data[index] < self._data[parent]):
            self.swap(index, parent)
            self.upheap(parent)
    
    # Adapté à partir de ArrayHeapPriorityQueue.py, trouvé sur Studium
    def downheap(self, index):
        children = self.nbChild(index)
        if children > 0:
            idxMinChild = self._p * index + 1
            for i in range(1,children+1):
                idxChildVerif = self.getChild(index, i)
                if self._data[idxChildVerif] < self._data[idxMinChild]:
                    idxMinChild = idxChildVerif
            if self._data[idxMinChild] < self._data[index]:
                self.swap(index, idxMinChild)
                self.downheap(idxMinChild)

    # Retourne l'index de l'enfant k du noeud à l'index demandé           
    def getChild (self, index, k):
        return self._p * index + k
    
    # Retourne le nombre d'enfants du noeud à l'index demandé
    def nbChild (self, index):
        if len(self) > (self._p * index + self._p):
            return self._p
        elif len(self) == (self._p * index + 1):
            return 0
        else:
            return len(self) - (self._p * index + 1)
    
    # Échange les valeurs contenues à deux index
    def swap (self, index1, index2):
        self._data[index1], self._data[index2] = self._data[index2], self._data[index1]
        
    # Retourne l'index du parent du noeud à l'index demandé
    def _parent (self, index):
        if index > 0:
            return (index-1) // self._p
        else:
            return 0
            
    def liste (self):
        return self._data
    
if __name__ == '__main__':
    S = MPP(8, 2)
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
        print("Erreur - Monceau vide")