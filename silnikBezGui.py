import numpy as np
from random import randint
from random import randrange
import time

n = 20
lPolicjantow = 6
lFurtek = 2
sFurtki = 2
lScian = 4
dSciany = 4
T = 20 #przykladowo
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

"""Zadania
1.Jez˙ eli t % k = 0, to: dla kaz˙dego gracza utwórz wa˛tek opakowuja˛cy obiekt
gracza; uruchom wa˛tek z limitem czasu ; w wa˛tku wykonaj na obiekcie
metode˛ licza˛ca˛ plany k ruchów; gdy upłynie czas , odbierz plany.
2 Przesun´ graczy zgodnie z zaplanowanym ruchem. Jez˙ eli nowa pozycja
gracza pokrywa sie˛ ze s´ciana˛, to zaniechaj ruchu.
"""
#do naprawy:
#zlodziej musi wygenerowac nie na policjancie
#policjanci nie moga nakladac sie na siebie pod czas wygenerowania

def pozycjeFurtek(t, Furtki, kZegar):
    if (t==0):
        for i in range(lFurtek):
            r1 = randint(0, n-1)
            r2 = randint(0, n-1)
            if (i%2==1):
                Furtki[i][0][0]=r1
                if r2>((n-1)/2):
                    Furtki[i][0][1]=n-1
                else:
                    Furtki[i][0][1]=0
            else:
                Furtki[i][0][1]=r2
                if r1>((n-1)/2):
                    Furtki[i][0][0]=n-1
                else:
                    Furtki[i][0][0]=0
            if (kZegar == True):
                for j in range(1, sFurtki):
                    if (Furtki[i][j-1][0] == 0):
                        if (Furtki[i][j-1][1]+1<n):
                            Furtki[i][j][0] = Furtki[i][j-1][0]
                            Furtki[i][j][1] = Furtki[i][j-1][1]+1
                        else:
                            Furtki[i][j][0] = Furtki[i][j-1][0]+1
                            Furtki[i][j][1] = Furtki[i][j-1][1]
                    elif (Furtki[i][j-1][1] == n-1):
                        if (Furtki[i][j-1][0]+1<n):
                            Furtki[i][j][0] = Furtki[i][j-1][0]+1
                            Furtki[i][j][1] = Furtki[i][j-1][1]
                        else:
                            Furtki[i][j][0] = Furtki[i][j-1][0]
                            Furtki[i][j][1] = Furtki[i][j-1][1]-1
                    elif (Furtki[i][j-1][0] == n-1):#zle liczy
                        if (Furtki[i][j-1][1]-1>0):
                            Furtki[i][j][0] = Furtki[i][j-1][0]
                            Furtki[i][j][1] = Furtki[i][j-1][1]-1
                        else:
                            Furtki[i][j][0] = Furtki[i][j-1][0]-1
                            Furtki[i][j][1] = Furtki[i][j-1][1]
                    elif (Furtki[i][j-1][1] == 0):
                        if (Furtki[i][j-1][0]-1>0):
                            Furtki[i][j][0] = Furtki[i][j-1][0]-1
                            Furtki[i][j][1] = Furtki[i][j-1][1]
                        else:
                            Furtki[i][j][0] = Furtki[i][j-1][0]
                            Furtki[i][j][1] = Furtki[i][j-1][1]+1
                            
    else:
        if (prawdopodobienstwo(Pfz) == True):
            kZegar = False
        if (prawdopodobienstwo(Pfr) == True):
            if (kZegar == True):
                for i in range(lFurtek):
                    for j in range(sFurtki):
                        if (Furtki[i][j][0] == 0):
                            if (Furtki[i][j][1]+1<n):
                                Furtki[i][j][0] = Furtki[i][j][0]
                                Furtki[i][j][1] = Furtki[i][j][1]+1
                            else:
                                Furtki[i][j][0] = Furtki[i][j][0]+1
                                Furtki[i][j][1] = Furtki[i][j][1]
                        elif (Furtki[i][j][1] == n-1):
                            if (Furtki[i][j][0]+1<n):
                                Furtki[i][j][0] = Furtki[i][j][0]+1
                                Furtki[i][j][1] = Furtki[i][j][1]
                            else:
                                Furtki[i][j][0] = Furtki[i][j][0]
                                Furtki[i][j][1] = Furtki[i][j][1]-1
                        elif (Furtki[i][j][0] == n-1):
                            if (Furtki[i][j][1]-1>=0):
                                Furtki[i][j][0] = Furtki[i][j][0]
                                Furtki[i][j][1] = Furtki[i][j][1]-1
                            else:
                                Furtki[i][j][0] = Furtki[i][j][0]-1
                                Furtki[i][j][1] = Furtki[i][j][1]
                        elif (Furtki[i][j][1] == 0):
                            if (Furtki[i][j][0]-1>=0):
                                Furtki[i][j][0] = Furtki[i][j][0]-1
                                Furtki[i][j][1] = Furtki[i][j][1]
                            else:
                                Furtki[i][j][0] = Furtki[i][j][0]
                                Furtki[i][j][1] = Furtki[i][j][1]+1
            else:
                for i in range(lFurtek):
                    for j in range(sFurtki):
                        if (Furtki[i][j][0] == 0):
                            if (Furtki[i][j][1]-1>=0):
                                Furtki[i][j][0] = Furtki[i][j][0]
                                Furtki[i][j][1] = Furtki[i][j][1]-1
                            else:
                                Furtki[i][j][0] = Furtki[i][j][0]+1
                                Furtki[i][j][1] = Furtki[i][j][1]
                        elif (Furtki[i][j][1] == 0):
                            if (Furtki[i][j][0]+1 < n):
                                Furtki[i][j][0] = Furtki[i][j][0]+1
                                Furtki[i][j][1] = Furtki[i][j][1]
                            else:
                                Furtki[i][j][0] = Furtki[i][j][0]
                                Furtki[i][j][1] = Furtki[i][j][1]+1
                        elif (Furtki[i][j][0] == n-1):
                            if (Furtki[i][j][1]+1 <n):
                                Furtki[i][j][0] = Furtki[i][j][0]
                                Furtki[i][j][1] = Furtki[i][j][1]+1
                            else:
                                Furtki[i][j][0] = Furtki[i][j][0]-1
                                Furtki[i][j][1] = Furtki[i][j][1]
                        elif (Furtki[i][j][1] == n-1):
                            if (Furtki[i][j][0]-1>=0):
                                Furtki[i][j][0] = Furtki[i][j][0]-1
                                Furtki[i][j][1] = Furtki[i][j][1]
                            else:
                                Furtki[i][j][0] = Furtki[i][j][0]
                                Furtki[i][j][1] = Furtki[i][j][1]-1
    return Furtki

def pozycjeScian(t, Sciany, KierunkiScian, PlanszaOld):
    if (t==0):
        for i in range(lScian):
            Sciany[i][0][0] = randint(1, n-2)
            Sciany[i][0][1] = randint(1, n-2)
            punktWe1 = False
            while (punktWe1 == False):
                r = randint(0, 3)
                if (r==0):
                    if ((Sciany[i][0][0] + dSciany-1)<(n-1)):
                        punktWe1 = True
                        for j in range(1, dSciany):
                            Sciany[i][j][0] = Sciany[i][j-1][0]+1
                            Sciany[i][j][1] = Sciany[i][j-1][1]
                if (r==1):
                    if ((Sciany[i][0][1] + dSciany-1)<(n-1)):
                        punktWe1 = True
                        for j in range(1, dSciany):
                            Sciany[i][j][0] = Sciany[i][j-1][0]
                            Sciany[i][j][1] = Sciany[i][j-1][1]+1
                if (r==2):
                    if ((Sciany[i][0][0] - dSciany-1)>0):
                        punktWe1 = True
                        Sciany[i][dSciany-1][0] = Sciany[i][0][0]
                        Sciany[i][dSciany-1][1] = Sciany[i][0][1]
                        print(Sciany[i][dSciany-1])
                        for j in range(dSciany-1, 0, -1):
                            Sciany[i][j-1][0] = Sciany[i][j][0]-1
                            Sciany[i][j-1][1] = Sciany[i][j][1]
                if (r==3):
                    if ((Sciany[i][0][1] - dSciany-1)>0):
                        punktWe1 = True
                        Sciany[i][dSciany-1][0] = Sciany[i][0][0]
                        Sciany[i][dSciany-1][1] = Sciany[i][0][1]
                        for j in range(dSciany-1, 0, -1):
                            Sciany[i][j-1][0] = Sciany[i][j][0]
                            Sciany[i][j-1][1] = Sciany[i][j][1]-1
    elif (t == 1):
        for i in range(lScian):
            punktWe1 = False
            while(punktWe1 == False):
                r = randint(1, 4)
                if (r == 1):
                    KierunkiScian[i] = [1, 0]
                elif (r == 2):
                    KierunkiScian[i] = [0, 1]
                elif (r==3): 
                    KierunkiScian[i] = [-1, 0]
                elif (r==4):
                    KierunkiScian[i] = [0, -1]
                punktWe2 = 0
                for j in range(dSciany):
                    a = Sciany[i][j]+KierunkiScian[i]
                    if (PlanszaOld[int(a[0])][int(a[1])] == 0 or PlanszaOld[int(a[0])][int(a[1])] == 3):
                        punktWe2 +=1
                if (punktWe2 == dSciany):
                    for j in range(dSciany):
                        Sciany[i][j]+=KierunkiScian[i] 
                        punktWe1 = True
    else:
        for i in range(lScian):
            if (prawdopodobienstwo(Psz) == True):
                r = randint(1, 4)
                if (r == 1):
                    KierunkiScian[i] = [1, 0]
                elif (r == 2):
                    KierunkiScian[i] = [0, 1]
                elif (r==3): 
                    KierunkiScian[i] = [-1, 0]
                elif (r==4):
                    KierunkiScian[i] = [0, -1]
            if (prawdopodobienstwo(Psr) == True):
                punktWe2 = 0
                for j in range(dSciany):
                    a = Sciany[i][j]+KierunkiScian[i]
                    if (PlanszaOld[int(a[0])][int(a[1])] == 0 or PlanszaOld[int(a[0])][int(a[1])] == 3):
                        punktWe2 += 1
                    elif (PlanszaOld[int(a[0])][int(a[1])] == 2 or PlanszaOld[int(a[0])][int(a[1])] == 1):
                        KierunkiScian[i] = KierunkiScian[i]*(-1)
                        punktWe2 += 1
                if (punktWe2 == dSciany):
                    for j in range(dSciany):
                        Sciany[i][j]+=KierunkiScian[i] 
                        punktWe1 = True
    return Sciany

def prawdopodobienstwo(lPrawdopodobienstwa):
    r = randint(1, 100)
    if (r <= 100*lPrawdopodobienstwa):
        return True
    else: return False

def pozycjaZlodzieja(t, Zlodziej, Plansza):
    if (t == 0):
        punktWe1 = 0
        while (punktWe1 == 0):
            Zlodziej[0] = randint(1, n-2)
            Zlodziej[1] = randint(1, n-2)
            a = int(Zlodziej[0]+1)
            b = int(Zlodziej[1])
            if (Plansza[a][b]==0):
                punktWe1 = 1
    else:
        punktWe1 = 0
        while (punktWe1 == 0):
            r = randint(0, 4)
            if (r==0):
                punktWe1 = 1
            if (r==1):
                a = int(Zlodziej[0]+1)
                b = int(Zlodziej[1])
                if (Plansza[a][b] == 0 or Plansza[a][b] == 2):
                    Zlodziej[0] = Zlodziej[0]+1
                    punktWe1 = 1
            elif (r==2):
                a = int(Zlodziej[0])
                b = int(Zlodziej[1]+1)
                if (Plansza[a][b] == 0 or Plansza[a][b] == 2):
                    Zlodziej[1] = Zlodziej[1]+1
                    punktWe1 = 1
            elif (r==3):
                a = int(Zlodziej[0]-1)
                b = int(Zlodziej[1])
                if (Plansza[a][b] == 0 or Plansza[a][b] == 2):
                    Zlodziej[0] = Zlodziej[0]-1
                    punktWe1 = 1
            elif (r==4):
                a = int(Zlodziej[0])
                b = int(Zlodziej[1]-1)
                if (Plansza[a][b] == 0 or Plansza[a][b] == 2):
                    Zlodziej[1] = Zlodziej[1]-1
                    punktWe1 = 1
    return Zlodziej



def pozycjePolicjantow(t, Policjanci, Plansza): 
    if (t==0):
        for i in range(lPolicjantow):
            Policjanci[i][0] = randint(1, n-2)
            Policjanci[i][1] = randint(1, n-2)
    else:
        for i in range(lPolicjantow):
            punktWe1 = 0
            while (punktWe1 == 0):
                r = randint(0, 4)
                if (r==0):
                    punktWe1 = 1
                elif (r==1):
                    a = int(Policjanci[i][0]+1)
                    b = int(Policjanci[i][1])
                    if (Plansza[a][b]==0):
                        Policjanci[i][0] = Policjanci[i][0]+1
                        punktWe1 = 1
                elif (r==2):
                    a = int(Policjanci[i][0])
                    b = int(Policjanci[i][1]+1)
                    if (Plansza[a][b]==0):
                        Policjanci[i][1] = Policjanci[i][1]+1
                        punktWe1 = 1
                elif (r==3):
                    a = int(Policjanci[i][0]-1)
                    b = int(Policjanci[i][1])
                    if (Plansza[a][b]==0):
                        Policjanci[i][0] = Policjanci[i][0]-1
                        punktWe1 = 1
                elif (r==4):
                    a = int(Policjanci[i][0])
                    b = int(Policjanci[i][1]-1)
                    if (Plansza[a][b]==0):
                        Policjanci[i][1] = Policjanci[i][1]-1
                        punktWe1 = 1
    return Policjanci 

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
    Furtki = np.zeros((lFurtek, sFurtki, 2))
    kZegar = True
    Sciany = np.zeros((lScian, dSciany, 2))
    KierunkiScian = np.zeros((lScian, 2))
    Zlodziej = np.zeros((2))
    punktyZlodzieja = 0
    Policjanci = np.zeros((lPolicjantow, 2))
    
    PlanszaOld = np.zeros((n, n))
    for i in range(n):
        PlanszaOld[i][0]=1
        PlanszaOld[i][n-1]=1
        PlanszaOld[0][i]=1
        PlanszaOld[n-1][i]=1
    
    for t in range(T):
        tStart = time.time()
        Plansza = np.zeros((n, n))
        for i in range(n):
            Plansza[i][0]=1
            Plansza[i][n-1]=1
            Plansza[0][i]=1
            Plansza[n-1][i]=1
        
        Furtki = pozycjeFurtek(t, Furtki, kZegar)#2
        for i in range(lFurtek):
            for j in range(sFurtki):
                a = Furtki[i][j]
                Plansza[int(a[0])][int(a[1])] = 2
        Sciany = pozycjeScian(t, Sciany, KierunkiScian, PlanszaOld)#3
        for i in range(lScian):
            for j in range(dSciany):
                a = int(Sciany[i][j][0])
                b = int(Sciany[i][j][1])
                Plansza[a][b] = 3
        
        Zlodziej = pozycjaZlodzieja(t, Zlodziej, Plansza)#4
        a = int(Zlodziej[0])
        b = int(Zlodziej[1])
        Plansza[a][b] = 4
        
        Policjanci = pozycjePolicjantow(t, Policjanci, Plansza)#5
        for i in range(lPolicjantow):
            a = int(Policjanci[i][0])
            b = int(Policjanci[i][1])
            Plansza[a][b] = 5
        
        PlanszaOld = Plansza
        print(Plansza)
        print("--------------------------------")
        punktyZlodzieja = 0
        """
        if (sprawdzanieZlapania(Zlodziej, Policjanci) == 3):
            print("Zlodziej zostal zlapany") #gui
            punktyZlodzieja = t
            break
        elif (sprawdzanieUcieczki(Furtki, Zlodziej) == 2):
            print("Zlodziej uciekl") #gui
            if (t+1 == T):
                punktyZlodzieja = T-1
            else:
                punktyZlodzieja = 2*T-t-1
            break
        """
        tStop = time.time()
        tDelta = tStop - tStart
        if (tDelta < 0.4):
            time.sleep(0.4 - tDelta)
    print("GRA SKONCZONA")
    print("Uzyskane punkty:", punktyZlodzieja) #gui
if __name__ == '__main__':
    main()

