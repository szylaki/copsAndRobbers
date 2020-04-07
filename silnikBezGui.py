import numpy as np
import random
from random import randint
import time

n = 20
T = 20 #przykladowo
k = 5
lFurtek = 2
sFurtki = 2
kZegar = 1 #kierunek ruchu furtek
lScian = 4
dSciany = 4
lPolicjantow = 5

Pfr = 0.5 #prawdopodbienstwo ruchu furtki
Pfz = 0.01 #prawdopodbienstwo zmiany kierunku ruchu furtki
Psr = 0.75 #prawdopodbienstwo ruchu sciany
Psz = 0.05 ##prawdopodbienstwo zmiany kierunku ruchu sciany

'''Oznaczenia na planszy
bramki 1
furtki 2
sciany 3
zlodziej 4
policjanci 5 
'''

class Swiat:
    def __init__(self):
        self.plansza = np.zeros((n, n))
        self.furtka = []
        self.sciana = []
        self.policjant = []
        
        for i in range(lFurtek):
            self.furtka.append(Furtki())
        for i in range(lScian):
            self.sciana.append(Sciany())
        for i in range(lPolicjantow):
            self.policjant.append(Policjant(self.plansza))
        self.zlodziej = Zlodziej(self.plansza)
        self.podstawienie()
        
    def ruch(self, listaPlansz, t):
        if (t%5 == 1):
            self.zlodziej.planowanieRuchu(listaPlansz)
            #wielowatkowosc
            for i in range(lPolicjantow):
                self.policjant[i].planowanieRuchu(listaPlansz)
        for i in range(lFurtek):
            self.furtka[i].ruch(kZegar)
        for i in range(lScian):
            self.sciana[i].ruch(listaPlansz[t])
        for i in range(lPolicjantow):
            self.policjant[i].ruch(listaPlansz[t], t)
        self.zlodziej.ruch(listaPlansz[t], t)
        self.podstawienie()

    def podstawienie(self):
        self.plansza = np.zeros((n, n))
        for i in range(n):
            self.plansza[i][0]=1
            self.plansza[i][n-1]=1
            self.plansza[0][i]=1
            self.plansza[n-1][i]=1
        for i in range(lScian):
            for j in range(dSciany):
                a = int(self.sciana[i].pozycjaX[j])
                b = int(self.sciana[i].pozycjaY[j])
                self.plansza[a][b] = 3
        for i in range(lFurtek):
            for j in range(sFurtki):
                a = int(self.furtka[i].pozycjaX[j])
                b = int(self.furtka[i].pozycjaY[j])
                self.plansza[a][b] = 2
        for i in range(lPolicjantow):
            a = int(self.policjant[i].pozycjaX)
            b = int(self.policjant[i].pozycjaY)
            self.plansza[a][b] = 5
        a = self.zlodziej.pozycjaX
        b = self.zlodziej.pozycjaY
        self.plansza[a][b] = 4
        
    
class Furtki:
    def __init__(self):
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
                        self.pozycjaX.append(self.pozycjaX[i-1])
                        self.pozycjaY.append(self.pozycjaY[i-1]+1)        
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
                    if (self.pozycjaX[i] == 0):
                        if (self.pozycjaY[i]+1<n):
                            self.pozycjaX[i] = self.pozycjaX[i]
                            self.pozycjaY[i] = self.pozycjaY[i]+1
                        else:
                            self.pozycjaX[i] = self.pozycjaX[i]+1
                            self.pozycjaY[i] = self.pozycjaY[i]
                    elif (self.pozycjaY[i] == n-1):
                        if (self.pozycjaX[i]+1<n):
                            self.pozycjaX[i] = self.pozycjaX[i]+1
                            self.pozycjaY[i] = self.pozycjaY[i]
                        else:
                            self.pozycjaX[i] = self.pozycjaX[i]
                            self.pozycjaY[i] = self.pozycjaY[i]-1
                    elif (self.pozycjaX[i] == n-1):
                        if (self.pozycjaY[i]-1>0):
                            self.pozycjaX[i] = self.pozycjaX[i]
                            self.pozycjaY[i] = self.pozycjaY[i]-1
                        else:
                            self.pozycjaX[i] = self.pozycjaX[i]-1
                            self.pozycjaY[i] = self.pozycjaY[i]
                    elif (self.pozycjaY[i-1] == 0):
                        if (self.pozycjaX[i]-1>=0):
                            self.pozycjaX[i] = self.pozycjaX[i]-1
                            self.pozycjaY[i] = self.pozycjaY[i]
                        else:
                            self.pozycjaX[i] = self.pozycjaX[i]
                            self.pozycjaY[i] = self.pozycjaY[i]+1
            elif (kZegar==-1):
                for i in range(sFurtki):
                    if (self.pozycjaX[i] == 0):
                        if (self.pozycjaY[i]-1>=n):
                            self.pozycjaX[i] = self.pozycjaX[i]
                            self.pozycjaY[i] = self.pozycjaY[i]-1
                        else:
                            self.pozycjaX[i] = self.pozycjaX[i]+1
                            self.pozycjaY[i] = self.pozycjaY[i]
                    elif (self.pozycjaY[i] == 0):
                        if (self.pozycjaX[i]+1<n):
                            self.pozycjaX[i] = self.pozycjaX[i]+1
                            self.pozycjaY[i] = self.pozycjaY[i]
                        else:
                            self.pozycjaX[i] = self.pozycjaX[i]
                            self.pozycjaY[i] = self.pozycjaY[i]+1
                    elif (self.pozycjaX[i] == n-1):
                        if (self.pozycjaY[i]+1<n):
                            self.pozycjaX[i] = self.pozycjaX[i]
                            self.pozycjaY[i] = self.pozycjaY[i]+1
                        else:
                            self.pozycjaX[i] = self.pozycjaX[i]-1
                            self.pozycjaY[i] = self.pozycjaY[i]
                    elif (self.pozycjaY[i] == n-1):
                        if (self.pozycjaX[i]-1>=0):
                            self.pozycjaX[i] = self.pozycjaX[i]-1
                            self.pozycjaY[i] = self.pozycjaY[i]
                        else:
                            self.pozycjaX[i] = self.pozycjaX[i]
                            self.pozycjaY[i] = self.pozycjaY[i]+1            
            
class Sciany:
    def __init__(self):
        self.pozycjaX = []
        self.pozycjaY = []
        self.kierunkiScian = []
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
            elif (r==1):
                if ((self.pozycjaY[0] + dSciany-1)<(n-1)):
                    punktWe1 = True
                    for i in range(1, dSciany):
                        self.pozycjaX.append(self.pozycjaX[i-1])
                        self.pozycjaY.append(self.pozycjaY[i-1]+1)
            elif (r==2):
                if ((self.pozycjaX[0] - dSciany-1)>0):
                    punktWe1 = True
                    for i in range(1, dSciany):
                        self.pozycjaX.append(self.pozycjaX[0])
                        self.pozycjaY.append(self.pozycjaY[0])
                    for i in range(dSciany-1, 0, -1):
                        self.pozycjaX[i-1] = self.pozycjaX[i]-1
                        self.pozycjaY[i-1] = self.pozycjaY[i]
            elif (r==3):
                if ((self.pozycjaY[0] - dSciany-1)>0):
                    punktWe1 = True
                    for i in range(1, dSciany):
                        self.pozycjaX.append(self.pozycjaX[0])
                        self.pozycjaY.append(self.pozycjaY[0])
                    for i in range(dSciany-1, 0, -1):
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

            
    def ruch(self, plansza):
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
                    self.pozycjaX[i]+= self.kierunkiScian[0]
                    self.pozycjaY[i]+= self.kierunkiScian[1]
            

class Zlodziej:
    def __init__(self, plansza):
        punktWe1 = 0
        while (punktWe1 == 0):
            self.pozycjaX = randint(1, n-2)
            self.pozycjaY = randint(1, n-2)
            if (plansza[int(self.pozycjaX)][int(self.pozycjaY)]==0):
                punktWe1 = 1
        self.planRuchu = [0]
        
    def ruch(self, plansza, t):
        if (self.planRuchu[t] == 1):
            a = int(self.pozycjaX+1)
            b = int(self.pozycjaY)
            if (plansza[a][b] == 0 or plansza[a][b] == 2):
                self.pozycjaX+=1
        elif (self.planRuchu[t] == 2):
            a = int(self.pozycjaX)
            b = int(self.pozycjaY+1)
            if (plansza[a][b] == 0 or plansza[a][b] == 2):
                self.pozycjaY+=1
        elif (self.planRuchu[t] == 3):
            a = int(self.pozycjaX-1)
            b = int(self.pozycjaY)
            if (plansza[a][b] == 0 or plansza[a][b] == 2):
                self.pozycjaX-=1
        elif (self.planRuchu[t] == 4):
            a = int(self.pozycjaX)
            b = int(self.pozycjaY-1)
            if (plansza[a][b] == 0 or plansza[a][b] == 2):
                self.pozycjaY-=1
        
    def planowanieRuchu(self, listaPlansz):
        for i in range(k):
            self.planRuchu.append(randint(0, 4))
                    
class Policjant:
    def __init__(self, plansza):
        punktWe1 = 0
        while (punktWe1 == 0):
            self.pozycjaX = randint(1, n-2)
            self.pozycjaY = randint(1, n-2)
            if (plansza[int(self.pozycjaX)][int(self.pozycjaY)]==0):
                punktWe1 = 1
        self.planRuchu = [0]
        
    def ruch(self, plansza, t) :
        if (self.planRuchu[t] == 1):
            a = int(self.pozycjaX+1)
            b = int(self.pozycjaY)
            if (plansza[a][b] == 0):
                self.pozycjaX+=1
        elif (self.planRuchu[t] == 2):
            a = int(self.pozycjaX)
            b = int(self.pozycjaY+1)
            if (plansza[a][b] == 0):
                self.pozycjaY+=1
        elif (self.planRuchu[t] == 3):
            a = int(self.pozycjaX-1)
            b = int(self.pozycjaY)
            if (plansza[a][b] == 0):
                self.pozycjaX-=1
        elif (self.planRuchu[t] == 4):
            a = int(self.pozycjaX)
            b = int(self.pozycjaY-1)
            if (plansza[a][b] == 0):
                self.pozycjaY-=1
    
    def planowanieRuchu(self, listaPlansz):
        for i in range(k):
            self.planRuchu.append(randint(0, 4))

def sprawdzanieZlapania(zlodziej, policjant):
    for i in range(lPolicjantow):
        if (policjant[i].pozycjaX == zlodziej.pozycjaX and policjant[i].pozycjaY == zlodziej.pozycjaY):
            return 3
        elif (policjant[i].pozycjaX+1 == zlodziej.pozycjaX and policjant[i].pozycjaY == zlodziej.pozycjaY):
            return 3
        elif (policjant[i].pozycjaX-1 == zlodziej.pozycjaX and policjant[i].pozycjaY == zlodziej.pozycjaY):
            return 3
        elif (policjant[i].pozycjaY+1 == zlodziej.pozycjaX and policjant[i].pozycjaX == zlodziej.pozycjaY):
            return 3
        elif (policjant[i].pozycjaY-1 == zlodziej.pozycjaX and policjant[i].pozycjaX == zlodziej.pozycjaY):
            return 3
        
def sprawdzanieUcieczki(furtka, zlodziej):
    for i in range(lFurtek):
        for j in range(sFurtki):
            if (furtka[i].pozycjaX[j] == zlodziej.pozycjaX and furtka[i].pozycjaY[j] == zlodziej.pozycjaY):
                return 2       

def main():
    punktyZlodzieja = T
    swiat = Swiat()
    listaPlansz = []
    for t in range(T):
        tStart = time.time()
        print(swiat.plansza)
        listaPlansz.append(swiat.plansza)
        swiat.ruch(listaPlansz, t)
        if (sprawdzanieZlapania(swiat.zlodziej, swiat.policjant) == 3):
            punktyZlodzieja = t
            print("Zlodziej zostal zlapany") #gui
            break
        if (sprawdzanieUcieczki(swiat.furtka, swiat.zlodziej) == 2):
            if (t+1 == T):
                punktyZlodzieja = T-1
            else:
                punktyZlodzieja = 2*T-t-1
            print("Zlodziej uciekl") #gui
            break
        tStop = time.time()
        tDelta = tStop - tStart
        if (tDelta < 0.4):
            time.sleep(1 - tDelta)
    print("Uzyskane punkty:", punktyZlodzieja) #gui
        
if __name__ == '__main__':
    main()        
        
        
        
        
        
        
        