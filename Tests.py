# encoding=utf-8

# Generateur de points aleatoires et test des classes

import random

from time import time
from Monceau import Monceau
from MP3 import MP3
from MP4 import MP4
from MP5 import MP5
from MPP import MPP
from QP_circulaire import QP_circulaire
from QP_insertion import QP_insertion

class Tests:
    
    # Génère k valeurs aléatoires de 1 à k
    def randomGen(self, k):
        for i in range(1,k+1):
            yield random.randint(0,k)
            
       
    def tests(self, data):
        for i in self.randomGen(10**6):
            data.ajouter(i)
    
    def monceaux(self):
        for i in [100, 1000, 5000,  10000, 25000, 50000, 100000, 500000]:
            monceau = Monceau(i)
            debut = time()
            self.tests(monceau)
            fin = time()
            print("Monceau binaire - n = " + str(i) + " - temps ecoule: " + str( fin - debut))
            
    def mp3(self):
        for i in [100, 1000, 5000,  10000, 25000, 50000, 100000, 500000]:
            monceau = MP3(i)
            debut = time()
            self.tests(monceau)
            fin = time()
            print("Monceau 3-aire - n = " + str(i) + " - temps ecoule: " + str( fin - debut))
    
    def mp4(self):
        for i in [100, 1000, 5000,  10000, 25000, 50000, 100000, 500000]:
            monceau = MP4(i)
            debut = time()
            self.tests(monceau)
            fin = time()
            print("Monceau 4-aire - n = " + str(i) + " - temps ecoule: " + str( fin - debut))
            
    def mp5(self):
        for i in [100, 1000, 5000,  10000, 25000, 50000, 100000, 500000]:
            monceau = MP5(i)
            debut = time()
            self.tests(monceau)
            fin = time()
            print("Monceau 5-aire - n = " + str(i) + " - temps ecoule: " + str( fin - debut))
            
    def mpp(self):
        for j in [2, 3, 4, 5, 7, 15, 31]:
            for [100, 1000, 5000,  10000, 25000, 50000, 100000, 500000]:
                monceau = MPP(i, j)        
                debut = time()
                self.tests(monceau)
                fin = time()
                print("Monceau p-aire - p = " + str(j) + ", n = " + str(i) + " - temps ecoule: " + str( fin - debut))
     
     
    def qp_insertion(self):
        for i in [100, 1000, 5000,  10000, 25000, 50000, 100000, 500000]:
            qp = QP_insertion(i)
            debut = time()
            self.tests(qp)
            fin = time()
            print("QP insertion - n = " + str(i) + " - temps ecoule: " + str( fin - debut))
            
    def qp_circulaire(self):
        for i in [100, 1000, 5000,  10000, 25000, 50000, 100000, 500000]:
            qp = QP_circulaire(i)
            debut = time()
            self.tests(qp)
            fin = time()
            print("QP circulaire - n = " + str(i) + " - temps ecoule: " + str( fin - debut))


if __name__ == '__main__':
    T = Tests()
    T.monceaux()
    T.mp3()
    T.mp4()
    T.mp5()
    T.mpp()
    T.qp_insertion()
    T.qp_circulaire()
                