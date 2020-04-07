import numpy as np
from random import randint
import time
import random
import sys
import copy


n = 20
lPolicjantow = 5
lFurtek = 2
sFurtki = 2
lScian = 4
dSciany = 4
T = 20 #przykladowo
Pfr = 0.5 #prawdopodbienstwo ruchu furtki
Pfz = 0.01 #prawdopodbienstwo zmiany kierunku ruchu furtki
Psr = 0.75 #prawdopodbienstwo ruchu sciany
Psz = 0.05 ##prawdopodbienstwo zmiany kierunku ruchu sciany
kZegar = 1

'''Oznaczenia na planszy
bramki 1
furtki 2
sciany 3
zlodziej 4
policjanci 5 
'''

GRANICA = 1
FURTKA = 2
SCIANA = 3
ZLODZIEJ = 4
POLICJANT = 5

class Swiat:
    def __init__(self, n, lPolicjantow, lFurtek, sFurtki, lScian, dSciany, kZegar):
        self.plansza = np.zeros((n, n))
        self.furtka = []
        self.sciana = []
        self.policjant = []
        for i in range(lFurtek):
            self.furtka.append(Furtki(sFurtki, n, kZegar))
        for i in range(lScian):
            self.sciana.append(Sciany(dSciany, n))
        for i in range(lPolicjantow):
            self.policjant.append(Policjant(n, self.plansza))
        self.zlodziej = Zlodziej(n, self.plansza)
        
    def ruch(self, n, lPolicjantow, lFurtek, sFurtki, lScian, dSciany, kZegar, listaSwiatow, t):
        for i in range(lFurtek):
            self.furtka[i].ruch(n, sFurtki, kZegar)
        for i in range(lScian):
            self.sciana[i].ruch(n, dSciany, kZegar, listaSwiatow[t])
        for i in range(lPolicjantow):
            self.policjant[i].ruch(n, listaSwiatow[t+1])
        self.zlodziej.ruch(n, listaSwiatow[t+1])

class Furtki:
    def __init__(self, sFurtki, n, kZegar):
        r1 = randint(0, n-1)
        r2 = randint(0, n-1)
        self.pozycjaX = []
        self.pozycjaY = []
        if ((r1+r2)%2==1):
            self.pozycjaX.append(r1)
            if r2>((n-1)/2):
                self.pozycjaY.append(n-1)
            else:
                self.pozycjaY.append(0)
        else:
            self.pozycjaY.append(r2)
            if r1>((n-1)/2):
                self.pozycjaX.append(n-1)
            else:
                self.pozycjaX.append(0)
        if (kZegar == 1):
            for i in range(1, sFurtki):
                if (self.pozycjaX[i-1] == 0):
                    if (self.pozycjaY[i-1]+1<n):
                        self.pozycjaX.append(self.pozycjaX[i-1])
                        self.pozycjaY.append(self.pozycjaY[i-1]+1)
                    else:
                        self.pozycjaX.append(self.pozycjaX[i-1]+1)
                        self.pozycjaY.append(self.pozycjaY[i-1])
                elif (self.pozycjaY[i-1] == n-1):
                    if (self.pozycjaX[i-1]+1<n):
                        self.pozycjaX.append(self.pozycjaX[i-1]+1)
                        self.pozycjaY.append(self.pozycjaY[i-1])
                    else:
                        self.pozycjaX.append(self.pozycjaX[i-1])
                        self.pozycjaY.append(self.pozycjaY[i-1]-1)
                elif (self.pozycjaX[i-1] == n-1):
                    if (self.pozycjaY[i-1]-1>0):
                        self.pozycjaX.append(self.pozycjaX[i-1])
                        self.pozycjaY.append(self.pozycjaY[i-1]-1)
                    else:
                        self.pozycjaX.append(self.pozycjaX[i-1]-1)
                        self.pozycjaY.append(self.pozycjaY[i-1])
                elif (self.pozycjaY[i-1] == 0):
                    if (self.pozycjaX[i-1]-1>0):
                        self.pozycjaX.append(self.pozycjaX[i-1]-1)
                        self.pozycjaY.append(self.pozycjaY[i-1])
                    else:
                        self.pozycjaX[i] = self.pozycjaX[i-1]
                        self.pozycjaY[i] = self.pozycjaY[i-1]+1        
        elif (kZegar==-1):
                for i in range(1, sFurtki):
                    if (self.pozycjaX[i-1] == 0):
                        if (self.pozycjaY[i-1]-1>=n):
                            self.pozycjaX.append(self.pozycjaX[i-1])
                            self.pozycjaY.append(self.pozycjaY[i-1]-1)
                        else:
                            self.pozycjaX.append(self.pozycjaX[i-1]+1)
                            self.pozycjaY.append(self.pozycjaY[i-1])
                    elif (self.pozycjaY[i-1] == 0):
                        if (self.pozycjaX[i-1]+1<n):
                            self.pozycjaX.append(self.pozycjaX[i-1]+1)
                            self.pozycjaY.append(self.pozycjaY[i-1])
                        else:
                            self.pozycjaX.append(self.pozycjaX[i-1])
                            self.pozycjaY.append(self.pozycjaY[i-1]+1)
                    elif (self.pozycjaX[i-1] == n-1):
                        if (self.pozycjaY[i-1]+1<n):
                            self.pozycjaX.append(self.pozycjaX[i-1])
                            self.pozycjaY.append(self.pozycjaY[i-1]+1)
                        else:
                            self.pozycjaX.append(self.pozycjaX[i-1]-1)
                            self.pozycjaY.append(self.pozycjaY[i-1])
                    elif (self.pozycjaY[i-1] == n-1):
                        if (self.pozycjaX[i]-1>=0):
                            self.pozycjaX.append(self.pozycjaX[i-1]-1)
                            self.pozycjaY.append(self.pozycjaY[i-1])
                        else:
                            self.pozycjaX.append(self.pozycjaX[i-1])
                            self.pozycjaY.append(self.pozycjaY[i-1]+1) 
    
    def ruch(self, kZegar):
        if random.random() < Pfz:
            kZegar *=(-1)
        if random.random() < Pfr:
            if (kZegar==1):
                for i in range(sFurtki):
                    if (self.pozycjaX[i-1] == 0):
                        if (self.pozycjaY[i-1]+1<n):
                            self.pozycjaX[i] = self.pozycjaX[i-1]
                            self.pozycjaY[i] = self.pozycjaY[i-1]+1
                        else:
                            self.pozycjaX[i] = self.pozycjaX[i-1]+1
                            self.pozycjaY[i] = self.pozycjaY[i-1]
                    elif (self.pozycjaY[i-1] == n-1):
                        if (self.pozycjaX[i]+1<n):
                            self.pozycjaX[i] = self.pozycjaX[i-1]+1
                            self.pozycjaY[i] = self.pozycjaY[i-1]
                        else:
                            self.pozycjaX[i] = self.pozycjaX[i-1]
                            self.pozycjaY[i] = self.pozycjaY[i-1]-1
                    elif (self.pozycjaX[i-1] == n-1):
                        if (self.pozycjaY[i-1]-1>0):
                            self.pozycjaX[i] = self.pozycjaX[i-1]
                            self.pozycjaY[i] = self.pozycjaY[i-1]-1
                        else:
                            self.pozycjaX[i] = self.pozycjaX[i-1]-1
                            self.pozycjaY[i] = self.pozycjaY[i-1]
                    elif (self.pozycjaY[i-1] == 0):
                        if (self.pozycjaX[i]-1>0):
                            self.pozycjaX[i] = self.pozycjaX[i-1]-1
                            self.pozycjaY[i] = self.pozycjaY[i-1]
                        else:
                            self.pozycjaX[i] = self.pozycjaX[i-1]
                            self.pozycjaY[i] = self.pozycjaY[i-1]+1
            elif (kZegar==-1):
                for i in range(sFurtki):
                    if (self.pozycjaX[i-1] == 0):
                        if (self.pozycjaY[i-1]-1>=n):
                            self.pozycjaX[i] = self.pozycjaX[i-1]
                            self.pozycjaY[i] = self.pozycjaY[i-1]-1
                        else:
                            self.pozycjaX[i] = self.pozycjaX[i-1]+1
                            self.pozycjaY[i] = self.pozycjaY[i-1]
                    elif (self.pozycjaY[i-1] == 0):
                        if (self.pozycjaX[i]+1<n):
                            self.pozycjaX[i] = self.pozycjaX[i-1]+1
                            self.pozycjaY[i] = self.pozycjaY[i-1]
                        else:
                            self.pozycjaX[i] = self.pozycjaX[i-1]
                            self.pozycjaY[i] = self.pozycjaY[i-1]+1
                    elif (self.pozycjaX[i-1] == n-1):
                        if (self.pozycjaY[i-1]+1<n):
                            self.pozycjaX[i] = self.pozycjaX[i-1]
                            self.pozycjaY[i] = self.pozycjaY[i-1]+1
                        else:
                            self.pozycjaX[i] = self.pozycjaX[i-1]-1
                            self.pozycjaY[i] = self.pozycjaY[i-1]
                    elif (self.pozycjaY[i-1] == n-1):
                        if (self.pozycjaX[i]-1>=0):
                            self.pozycjaX[i] = self.pozycjaX[i-1]-1
                            self.pozycjaY[i] = self.pozycjaY[i-1]
                        else:
                            self.pozycjaX[i] = self.pozycjaX[i-1]
                            self.pozycjaY[i] = self.pozycjaY[i-1]+1            
            
class Sciany:
    def __init__(self, n, dSciany):
        self.pozycjaX = []
        self.pozycjaY = []
        self.pozycjaX.append(randint(1, n-2))
        self.pozycjaY.append(randint(1, n-2))
        punktWe1 = False
        while (punktWe1 == False):
            r = randint(0, 3)
            if (r==0):
                if ((self.pozycjaX[0] + dSciany-1)<(n-1)):
                    punktWe1 = True
                    for i in range(1, dSciany):
                        self.pozycjaX.append(self.pozycjaX[i-1]+1)
                        self.pozycjaY.append(self.pozycjaY[i-1])
            if (r==1):
                if ((self.pozycjaY[0] + dSciany-1)<(n-1)):
                    punktWe1 = True
                    for i in range(1, dSciany):
                        self.pozycjaX[i] = self.pozycjaX[i-1]
                        self.pozycjaY[i] = self.pozycjaY[i-1]+1
            if (r==2):
                if ((self.pozycjaX[0] - dSciany-1)>0):
                    punktWe1 = True
                    self.pozycjaX[dSciany-1] = self.pozycjaX[0]
                    self.pozycjaY[dSciany-1] = self.pozycjaY[0]
                    for j in range(dSciany-1, 0, -1):
                        self.pozycjaX[i-1] = self.pozycjaX[i]-1
                        self.pozycjaY[i-1] = self.pozycjaY[i]
            if (r==3):
                if ((self.pozycjaY[0] - dSciany-1)>0):
                    punktWe1 = True
                    self.pozycjaX[dSciany-1] = self.pozycjaX[0]
                    self.pozycjaY[dSciany-1] = self.pozycjaY[0]
                    for j in range(dSciany-1, 0, -1):
                        self.pozycjaX[i-1] = self.pozycjaX[i]
                        self.pozycjaY[i-1] = self.pozycjaY[i]-1
        r = randint(1, 4)
        if (r == 1):
            self.kierunkiScian = [1, 0]
        elif (r == 2):
            self.kierunkiScian = [0, 1]
        elif (r==3): 
            self.kierunkiScian = [-1, 0]
        elif (r==4):
            self.kierunkiScian = [0, -1] 
    def ruch(self, n, dSciany, kZegar, plansza):
        if random.random() < Psz:
            r = randint(1, 4)
            if (r == 1):
                self.kierunkiScian = [1, 0]
            elif (r == 2):
                self.kierunkiScian = [0, 1]
            elif (r==3): 
                self.kierunkiScian = [-1, 0]
            elif (r==4):
                self.kierunkiScian = [0, -1]
        if random.random() < Psr:
            punktWe2 = 0
            for i in range(dSciany):
                a = self.pozycjaX[i]+self.kierunkiScian[0]
                b = self.pozycjaY[i]+self.kierunkiScian[1]
                if (plansza[int(a)][int(b)] == 0 or plansza[int(a)][int(b)] == 3):
                    punktWe2 += 1
                elif (plansza[int(a)][int(b)] == 2 or plansza[int(a)][int(b)] == 1):
                    self.kierunkiScian[0]*=(-1)
                    self.kierunkiScian[1]*=(-1)
                    punktWe2 += 1
            if (punktWe2 == dSciany):
                for i in range(dSciany):
                    self.pozycjaX[i] = self.kierunkiScian[0]
                    self.pozycjaY[i] = self.kierunkiScian[1]

class Zlodziej:
    def __init__(self, n, plansza):
        punktWe1 = 0
        while (punktWe1 == 0):
            self.pozycjaX = randint(1, n-2)
            self.pozycjaY = randint(1, n-2)
            if (plansza[int(self.pozycjaX)][int(self.pozycjaY)]==0):
                punktWe1 = 1
        
    def ruch(self, n, plansza):
        punktWe1 = 0
        while (punktWe1 == 0):
            r = randint(0, 4)
            if (r==0):
                punktWe1 = 1
            if (r==1):
                a = int(self.pozycjaX+1)
                b = int(self.pozycjaY)
                if (plansza[a][b] == 0 or plansza[a][b] == 2):
                    self.pozycjaX+=1
                    punktWe1 = 1
            elif (r==2):
                a = int(self.pozycjaX)
                b = int(self.pozycjaY+1)
                if (plansza[a][b] == 0 or plansza[a][b] == 2):
                    self.pozycjaY+=1
                    punktWe1 = 1
            elif (r==3):
                a = int(self.pozycjaX-1)
                b = int(self.pozycjaY)
                if (plansza[a][b] == 0 or plansza[a][b] == 2):
                    self.pozycjaX-=1
                    punktWe1 = 1
            elif (r==4):
                a = int(self.pozycjaX)
                b = int(self.pozycjaY-1)
                if (plansza[a][b] == 0 or plansza[a][b] == 2):
                    self.pozycjaY-=1
                    punktWe1 = 1
                    
class Policjant:
    def __init__(self, n, dSciany, plansza):
        punktWe1 = 0
        while (punktWe1 == 0):
            self.pozycjaX = randint(1, n-2)
            self.pozycjaY = randint(1, n-2)
            if (plansza[int(self.pozycjaX)][int(self.pozycjaY)]==0):
                punktWe1 = 1
        
    def ruch(self, n, plansza) :
        punktWe1 = 0
        while (punktWe1 == 0):
            r = randint(0, 4)
            if (r==0):
                punktWe1 = 1
            if (r==1):
                a = int(self.pozycjaX+1)
                b = int(self.pozycjaY)
                if (plansza[a][b] == 0):
                    self.pozycjaX+=1
                    punktWe1 = 1
            elif (r==2):
                a = int(self.pozycjaX)
                b = int(self.pozycjaY+1)
                if (plansza[a][b] == 0):
                    self.pozycjaY+=1
                    punktWe1 = 1
            elif (r==3):
                a = int(self.pozycjaX-1)
                b = int(self.pozycjaY)
                if (plansza[a][b] == 0):
                    self.pozycjaX-=1
                    punktWe1 = 1
            elif (r==4):
                a = int(self.pozycjaX)
                b = int(self.pozycjaY-1)
                if (plansza[a][b] == 0):
                    self.pozycjaY-=1
                    punktWe1 = 1

def sprawdzanieUcieczki(Furtki, Zlodziej):
    for i in range(lFurtek):
        for j in range(sFurtki):
            if (Furtki[i][j][0] == Zlodziej[0] and Furtki[i][j][1] == Zlodziej[1]):
                return 2

def sprawdzanieZlapania(Zlodziej, Policjanci):
    for i in range(lPolicjantow):
        if (Policjanci[i][0] == Zlodziej[0] and Policjanci[i][1] == Zlodziej[1]):
            return 3
        elif (Policjanci[i][0]+1 == Zlodziej[0] and Policjanci[i][1] == Zlodziej[1]):
            return 3
        elif (Policjanci[i][0]-1 == Zlodziej[0] and Policjanci[i][1] == Zlodziej[1]):
            return 3
        elif (Policjanci[i][1]+1 == Zlodziej[1] and Policjanci[i][0] == Zlodziej[0]):
            return 3
        elif (Policjanci[i][1]-1 == Zlodziej[1] and Policjanci[i][0] == Zlodziej[0]):
            return 3
        
def main():
    swiat = Swiat(n, lPolicjantow, lFurtek, sFurtki, lScian, dSciany, kZegar)
    listaPlansz = []
    listaPlansz.append(swiat.plansza)
    for t in range(T):
        tStart = time.time()
        swiat.ruch(listaPlansz, t)
        listaPlansz.append(swiat.plansza)
        sprawdzanieZlapania()
        sprawdzanieUcieczki()
        tStop = time.time()
        tDelta = tStop - tStart
        print(swiat)
        if (tDelta < 0.4):
            time.sleep(1 - tDelta)
        
        
if __name__ == '__main__':
    main()        
        
        
        
        
        
        
        