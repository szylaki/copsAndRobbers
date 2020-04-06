import numpy as np
from random import randint
from random import randrange
import time

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

class Swiat:
    def __init__(self, n, lPolicjantow, lFurtek, sFurtki, lScian, dSciany, kZegar):
        for i in range(lFurtek):
            self.furtka[i] = Furtki(sFurtki, n, kZegar) 
        for i in range(lScian):
            self.sciana[i] = Sciany(dSciany, n)
        for i in range(lPolicjantow):
            self.policjant[i] = Policjant(n, plansza)
        self.zlodziej = Zlodziej(n, plansza)
        
    def ruch():
        for i in range(lFurtek):
            self.furtka[i].ruch(n, sFurtki, kZegar, )
        for i in range(lScian):
            self.sciana[i].ruch(n, dSciany, kZegar)
        for i in range(lPolicjantow):
            self.policjant[i].ruch()
        self.zlodziej.ruch()

class Furtki:
    def __init__(self, sFurtki, n, kZegar):
        r1 = randint(0, n-1)
        r2 = randint(0, n-1)
        if (i%2==1):
            self.pozycjaX[0] = r1
            if r2>((n-1)/2):
                self.pozycjaY[0] = n-1
            else:
                self.pozycjaY[0] = 0
        else:
            self.pozycjaY[0] = r2
            if r1>((n-1)/2):
                self.pozycjaX[0] = n-1
            else:
                self.pozycjaX[0] = 0
        if (kZegar == 1):
            for i in range(1, sFurtki):
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
                for i in range(1, sFurtki):
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
    
    def ruch(self):
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
        self.pozycjaX[0] = randint(1, n-2)
        self.pozycjaY[0] = randint(1, n-2)
        punktWe1 = False
        while (punktWe1 == False):
            r = randint(0, 3)
            if (r==0):
                if ((self.pozycjaX[0] + dSciany-1)<(n-1)):
                    punktWe1 = True
                    for i in range(1, dSciany):
                        self.pozycjaX[i] = self.pozycjaX[i-1]+1
                        self.pozycjaY[i] = self.pozycjaY[i-1]
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
        punktWe1 = False
        while(punktWe1 == False):
            r = randint(1, 4)
            if (r == 1):
                self.kierunkiScian = [1, 0]
            elif (r == 2):
                self.kierunkiScian = [0, 1]
            elif (r==3): 
                self.kierunkiScian = [-1, 0]
            elif (r==4):
                self.kierunkiScian = [0, -1] 
    def ruch():
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
            for j in range(dSciany):
                a = self.pozycjaX[i]+self.kierunkiScian[0]
                b = self.pozycjaY[i]+self.kierunkiScian[1]
                if (PlanszaOld[int(a)][int(b)] == 0 or PlanszaOld[int(a)][int(b)] == 3):
                    punktWe2 += 1
                elif (PlanszaOld[int(a)][int(b)] == 2 or PlanszaOld[int(a)][int(b)] == 1):
                    self.kierunkiScian[0]*=(-1)
                    self.kierunkiScian[1]*=(-1)
                    punktWe2 += 1
            if (punktWe2 == dSciany):
                for j in range(dSciany):
                    self.pozycjaX[] = self.kierunkiScian[0]
                    self.pozycjaY[] = self.kierunkiScian[1]

class Zlodziej:
    def __init__(self, n, plansza):
        punktWe1 = 0
        while (punktWe1 == 0):
            self.pozycjaX = randint(1, n-2)
            self.pozycjaY = randint(1, n-2)
            if (Plansza[int(self.pozycjaX)][int(self.pozycjaY)]==0):
                punktWe1 = 1
        
    def ruch():
        punktWe1 = 0
        while (punktWe1 == 0):
            r = randint(0, 4)
            if (r==0):
                punktWe1 = 1
            if (r==1):
                a = int(self.pozycjaX+1)
                b = int(self.pozycjaY)
                if (Plansza[a][b] == 0 or Plansza[a][b] == 2):
                    self.pozycjaX+=1
                    punktWe1 = 1
            elif (r==2):
                a = int(self.pozycjaX)
                b = int(self.pozycjaY+1)
                if (Plansza[a][b] == 0 or Plansza[a][b] == 2):
                    self.pozycjaY+=1
                    punktWe1 = 1
            elif (r==3):
                a = int(self.pozycjaX-1)
                b = int(self.pozycjaY)
                if (Plansza[a][b] == 0 or Plansza[a][b] == 2):
                    self.pozycjaX-=1
                    punktWe1 = 1
            elif (r==4):
                a = int(self.pozycjaX)
                b = int(self.pozycjaY-1)
                if (Plansza[a][b] == 0 or Plansza[a][b] == 2):
                    self.pozycjaY-=1
                    punktWe1 = 1
                    
class Policjant:
    def __init__(self, n, dSciany):
        punktWe1 = 0
        while (punktWe1 == 0):
            self.pozycjaX = randint(1, n-2)
            self.pozycjaY = randint(1, n-2)
            if (Plansza[int(self.pozycjaX)][int(self.pozycjaY)]==0):
                punktWe1 = 1
        
    def ruch():
        punktWe1 = 0
        while (punktWe1 == 0):
            r = randint(0, 4)
            if (r==0):
                punktWe1 = 1
            if (r==1):
                a = int(self.pozycjaX+1)
                b = int(self.pozycjaY)
                if (Plansza[a][b] == 0):
                    self.pozycjaX+=1
                    punktWe1 = 1
            elif (r==2):
                a = int(self.pozycjaX)
                b = int(self.pozycjaY+1)
                if (Plansza[a][b] == 0):
                    self.pozycjaY+=1
                    punktWe1 = 1
            elif (r==3):
                a = int(self.pozycjaX-1)
                b = int(self.pozycjaY)
                if (Plansza[a][b] == 0):
                    self.pozycjaX-=1
                    punktWe1 = 1
            elif (r==4):
                a = int(self.pozycjaX)
                b = int(self.pozycjaY-1)
                if (Plansza[a][b] == 0):
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