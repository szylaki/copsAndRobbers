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

class Plansza:
    def __init__(self, n, lPolicjantow, lFurtek, sFurtki, lScian, dSciany, kZegar):
        for i in range(lFurtek):
            self.furtka[i] = Furtki(sFurtki, n, kZegar) 
        for i in range(lScian):
            self.sciana[i] = Sciany(dSciany, n)
        for i in range(lPolicjantow):
            self.policjant[i] = Zlodziej()
        self.zlodziej = Czlowiek()
        
    def ruch():
        poszczegolne ruchy

class Furtki:
    def __init__(self, sFurtki, n):
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
    def __init__(self, dSciany):
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
    def __init__(self, n):
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
    def __init__(self):
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



def checkWinningConditions():
  # firstly, we check if the thief has escaped
  for gate in gateTab:
    for i in range(len(gate.position)):
      if thiefu.position[0] is wallTab[gate.position[i]].position[0] and thiefu.position[1] is wallTab[gate.position[i]].position[1]:
        return 0, (2*T - t - 1)

  # next, we check if the policemans have captured the thief
  for policeman in policemanTab:
    # creating a surroundings, where the policeman can catch the thief
    tempPos = copy.deepcopy(policeman.position)
    catchField = [copy.deepcopy(tempPos)]
    tempPos[0] += 1
    catchField.append(copy.deepcopy(tempPos))
    tempPos[0] -= 2
    catchField.append(copy.deepcopy(tempPos))
    tempPos[0] += 1
    tempPos[1] += 1
    catchField.append(copy.deepcopy(tempPos))
    tempPos[1] -= 2
    catchField.append(copy.deepcopy(tempPos))

    for catchCoords in catchField:
      if thiefu.position[0] is catchCoords[0] and thiefu.position[1] is catchCoords[1]:
        return 1, t

  # lastly, the time might have expired
  if t is T-1:
    return 0, T

  # ... there battle might not have been settled either
  return -1, -1

def InitBoard():
  global thiefu
  random.seed(3)
  #creating walls - circled layout in order to easily handle gates movement
  for i in range(N+2):
    wallTab.append(Wall(i,0))
  for i in range(1,N+1):
    wallTab.append(Wall(N+1,i))
  for i in range(N+1,0,-1):
    wallTab.append(Wall(i,N+1))
  for i in range(N+1,0,-1):
    wallTab.append(Wall(0,i))

  # creating gates
  for i in range(gateAmount):
    newGateCoord = findPlaceForGate(gateTab)
    gateTab.append(Gate(newGateCoord))

  # creating obstacles
  for i in range(obstacleAmount):
    newObstacleOrientation = random.randint(0,1)
    newObstacleCoords = findPlaceForObstacle(obstacleTab, newObstacleOrientation)
    obstacleTab.append(Obstacle(newObstacleCoords,newObstacleOrientation))

  # creating a policemans
  ite = policemanAmount
  while ite > 0:
    ite = ite - 1
    policeCoords = [random.randint(1,N-2), random.randint(1,N-2)]
    while isPlaceFree(policeCoords, policemanTab=policemanTab, obstacleTab=obstacleTab) is False:
      policeCoords = [random.randint(1,N-2), random.randint(1,N-2)]
    #creating new policeman. Second argument is policeman's unique ID - thus, I add some value (20) to make them stand out
    policemanTab.append(Policeman(policeCoords, ite + 5))

  # creating a thief
  thiefCoords = [random.randint(1,N-2), random.randint(1,N-2)]
  thiefu = Thief(thiefCoords)
  while isPlaceFree(thiefCoords, obstacleTab=obstacleTab, policemanTab=policemanTab, policemanLapki=True) is False:
    thiefu.position = [random.randint(1,N-2), random.randint(1,N-2)]

  # return constructBoard(wallTab, gateTab, obstacleTab, thiefu, policemanTab)
  finalDict = getBoardStateDictionary()
  return finalDict

  # temporary game loop
  # while True:
  #   constructBoard(wallTab, gateTab, obstacleTab, thiefu, policemanTab, True)
  #   time.sleep(0.5)
  #   for gate in gateTab:
  #     gate.move()
  #   for obst in obstacleTab:
  #     obst.Move(thiefu, policemanTab)

# gateTab = []
# wallTab = []
# obstacleTab = []
# policemanTab = []
# thiefu = None

# retrieves all the objects' coordinates and stores them as a dictionary of arrays
def getBoardStateDictionary():
  gatesCoords = []
  for gate in gateTab:
    singleGate = []
    for i in gate.position:
      coords = wallTab[i].position
      singleGate.append(coords)
    gatesCoords.append(singleGate)

  obstaclesCoords = []
  for obstacle in obstacleTab:
    obstaclesCoords.append(obstacle.position)

  policemansCoords = []
  policemansID = []
  for policeman in policemanTab:
    policemansCoords.append(policeman.position)
    policemansID.append(policeman.ID)

  #building dictionary

  boardDictionary = {
    'gatesCoords': gatesCoords,
    'obstaclesCoords': obstaclesCoords,
    'thiefCoords': thiefu.position
  }
  for i,policeman in enumerate(policemanTab):
    boardDictionary['policeman' + str(i+1)] = {
      'ID': policeman.ID,
      'coords': policeman.position
    }

  return boardDictionary


def findPlaceForGate(gateTab):
  # Finding first new spot
  gatePos = random.randint(0,realN-1)
  while isFarEnough(gatePos, gateTab) is False:
    gatePos = random.randint(0,realN-1)

  newGateTab = [gatePos]
  if gateWidth < 2:
    return newGateTab
  
  ite = 0
  while ite < gateWidth-1:
    gatePos = newGateTab[ite] - 1
    if gatePos < 0:
      gatePos = realN-1
    newGateTab.append(gatePos)
    ite = ite + 1
  return newGateTab

def findPlaceForObstacle(obstacleTab, obstacleOrientation):
  coordY = 0
  coordX = 0
  while True:
    if obstacleOrientation == 0:
      coordY = random.randint(1,N-2)
      coordX = random.randint(1,N-obstacleWidth-2)
      for i in range(obstacleWidth):
        if isPlaceFree([coordY,coordX+i], obstacleTab=obstacleTab) is False:
          continue
    else:
      coordY = random.randint(1,N-obstacleWidth-2)
      coordX = random.randint(1,N-2)
      for i in range(obstacleWidth):
        if isPlaceFree([coordY+i,coordX], obstacleTab=obstacleTab) is False:
          continue

    break
  
  tab = []
  for i in range(obstacleWidth):
    if obstacleOrientation == 0:
      tab.append([coordY,coordX+i])
    else:
      tab.append([coordY+i,coordX])

  return tab



def isFarEnough(x, gateTab):
  ite = gateWidth
  while ite > -1:
    ite = ite - 1
    for gatee in gateTab:
      for i in range(len(gatee.position)):
        if x == gatee.position[i]:
          return False
    x = x - 1
    if x < 0:
      x = realN-1
  return True

def isPlaceFree(coords, thieff=False, policemanTab=False, obstacleTab=False, policemanLapki=False):
  if thieff is not False:
    if isEqual(coords, thieff.position):
      return False

  if policemanTab is not False:
    for police in policemanTab:
      if isEqual(coords, police.position):
        return False

  if policemanLapki is not False:
    for police in policemanTab:
      # creating a surroundings, where the policeman can catch the thief
      tempPos = copy.deepcopy(police.position)
      catchField = [copy.deepcopy(tempPos)]
      tempPos[0] += 1
      catchField.append(copy.deepcopy(tempPos))
      tempPos[0] -= 2
      catchField.append(copy.deepcopy(tempPos))
      tempPos[0] += 1
      tempPos[1] += 1
      catchField.append(copy.deepcopy(tempPos))
      tempPos[1] -= 2
      catchField.append(copy.deepcopy(tempPos))

      for catchCoords in catchField:
        if coords[0] is catchCoords[0] and coords[1] is catchCoords[1]:
          return False
  
  if obstacleTab is not False:
    for obst in obstacleTab:
      for j in range(len(obst.position)):
        if isEqual(coords, obst.position[j]):
          return False

  return True

def isEqual(A,B):
  if A[0] == B[0] and A[1] == B[1]:
    return True
  return False

def constructBoard(wallTab, gateTab, obstacleTab, thieff, policemanTab, draw=False):
  board = np.zeros([N+2,N+2])
  for wall in wallTab:
    board[wall.position[0],wall.position[1]] = 1

  for gate in gateTab:
    for i in gate.position:
      coords = wallTab[i].position
      board[coords[0], coords[1]] = 2

  for obst in obstacleTab:
    for i in range(len(obst.position)):
      coords = obst.position[i]
      board[coords[0], coords[1]] = 3

  board[thieff.position[0], thieff.position[1]] = 4

  for pol in policemanTab:
    board[pol.position[0], pol.position[1]] = pol.ID

  if draw == True:
    if colorful == 1:
      printColorful(board)
    else:
      print(board)
      print('')

  return board

def printColorful(board):
  _ = system('cls')
  toPrint = ''
  for i in range(len(board)):
    for j in range(len(board)):
      x = int(board[i][j])
      if x == 0:
        toPrint = toPrint + ' ' + str(x) + ' '
      elif x == 1:
        toPrint = toPrint  + ' ' + str(x) + ' '
      elif x == 2:
          toPrint = toPrint + ' ' + str(x) + ' '
      elif x == 3:
          toPrint = toPrint + ' ' + str(x) + ' '
      elif x == 4:
          toPrint = toPrint + ' ' + str(x) + ' '
      else:
          toPrint = toPrint + ' ' + x + ' '
    toPrint = toPrint + '\n'
  print(toPrint)
  print('')