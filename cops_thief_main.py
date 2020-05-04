import numpy as np
import random
import matplotlib.pyplot as plt
from random import randint
import time
#import threading
#import logging
#import queue
#import inspect
#import ctypes
#import copy
import cops_thief_threads
from enum import IntEnum
import copy


#from cargui import Gui

n = 22
T = 100 #przykladowo
k = 5 #ilosc planowanych moveow
number_of_gates = 2
gate_width = 2
gates_direction = 1 #kierunek moveu furtek
number_of_walls = 4
wall_width = 4
number_of_cops = 5
max_t = 0.5
probability_gm = 0.5 #probability of gate movement
probability_gd = 0.01 #prawdopodbienstwo zmiany kierunku moveu Gates
probability_wm = 0.75 #prawdopodbienstwo moveu Walls
probability_wd = 0.05 ##prawdopodbienstwo zmiany kierunku moveu Walls

class Direction(IntEnum):
	EMPTY = 0
	DOWN = 1
	RIGHT =	2
	UP = 3
	LEFT =  4

'''Oznaczenia na planszy
fence 1
gates 2
walls 3
thief 4
cops 5 
cop's range 6
'''
        
class World:
    def __init__(self):
        #random.seed(0)
        self.board = np.zeros((n, n))
        self.worlds_list = []
        self.gate = []
        self.wall = []
        self.worlds_list_copy = []
        self.plan = cops_thief_threads.Planner()
        
        for i in range(number_of_gates):
            self.gate.append(Gates())
        for i in range(number_of_walls):
            self.wall.append(Walls())
        self.replacement_zero()
        self.thief = cops_thief_threads.Thief(self.worlds_list_copy[len(self.worlds_list_copy)-1])
        self.cops = cops_thief_threads.Cops(self.worlds_list_copy)
        self.worlds_list_copy.pop()
        self.replacement()
        
    def replacement_zero(self):
        self.board = np.zeros((n, n))
        for i in range(n):
            self.board[i][0]=1
            self.board[i][n-1]=1
            self.board[0][i]=1
            self.board[n-1][i]=1
        for i in range(number_of_walls):
            for j in range(wall_width):
                a = int(self.wall[i].positionX[j])
                b = int(self.wall[i].positionY[j])
                self.board[a][b] = 3
        for i in range(number_of_gates):
            for j in range(gate_width):
                a = int(self.gate[i].positionX[j])
                b = int(self.gate[i].positionY[j])
                self.board[a][b] = 2
        self.worlds_list_copy.append(self.board)
        
    def move(self):
        for i in range(number_of_gates):
            self.gate[i].move(gates_direction)
        for i in range(number_of_walls):
            self.wall[i].move(self.worlds_list[len(self.worlds_list) - 1])
        if ((len(self.worlds_list_copy)-1) % k == 0):
            self.plan.thread_function(self.worlds_list_copy)
            self.show_moves()
            
        self.cops.move(self.plan.cops_planner.move_plan, self.worlds_list)
        self.thief.move(self.plan.thief_planner.move_plan, self.worlds_list)
        self.replacement()
        
            
    def show_moves(self):
        print("Planned moves for the thief:")
        for i in range(k):
            if (self.plan.thief_planner.move_plan[i]==Direction.DOWN):
                print("DOWN ", end = '')
            elif (self.plan.thief_planner.move_plan[i]==Direction.RIGHT):
                print("RIGHT ", end = '')
            elif (self.plan.thief_planner.move_plan[i]==Direction.LEFT):
                print("LEFT ", end = '')
            elif (self.plan.thief_planner.move_plan[i]==Direction.UP):
                print("UP ", end = '')    
            elif (self.plan.thief_planner.move_plan[i]==Direction.EMPTY):
                print("EMPTY ", end = '')
        print("")
        for i in range(number_of_cops):
            print("Planned moves for the cop", i, ":")
            for j in range(k):
                if (self.plan.cops_planner.move_plan[i][j]==Direction.DOWN):
                    print("DOWN ", end = '')
                elif (self.plan.cops_planner.move_plan[i][j]==Direction.RIGHT):
                    print("RIGHT ", end = '')
                elif (self.plan.cops_planner.move_plan[i][j]==Direction.LEFT):
                    print("LEFT ", end = '')
                elif (self.plan.cops_planner.move_plan[i][j]==Direction.UP):
                    print("UP ", end = '')
                elif (self.plan.cops_planner.move_plan[i][j]==Direction.EMPTY):
                    print("EMPTY ", end = '')
            print("")
        print("___________________________________________________________")
        
    def replacement(self):
        self.board = np.zeros((n, n))
        for i in range(n):
            self.board[i][0]=1
            self.board[i][n-1]=1
            self.board[0][i]=1
            self.board[n-1][i]=1

        for i in range(number_of_cops):
            a = int(self.cops.cops_list[i].positionX)
            b = int(self.cops.cops_list[i].positionY)
            if (self.board[a+1][b] == 0):
                self.board[a+1][b] = 6
            if (self.board[a-1][b] == 0):
                self.board[a-1][b] = 6
            if (self.board[a][b+1] == 0):
                self.board[a][b+1] = 6
            if (self.board[a][b-1] == 0):
                self.board[a][b-1] = 6
        
        for i in range(number_of_walls):
            for j in range(wall_width):
                a = int(self.wall[i].positionX[j])
                b = int(self.wall[i].positionY[j])
                self.board[a][b] = 3
        
        for i in range(number_of_gates):
            for j in range(gate_width):
                a = int(self.gate[i].positionX[j])
                b = int(self.gate[i].positionY[j])
                self.board[a][b] = 2
                
        for i in range(number_of_cops):
            a = int(self.cops.cops_list[i].positionX)
            b = int(self.cops.cops_list[i].positionY)
            self.board[a][b] = 5
        
        a = int(self.thief.positionX)
        b = int(self.thief.positionY)
        self.board[a][b] = 4
        
        self.worlds_list.append(self.board)
        self.worlds_list_copy.append(copy.copy(self))
 
class Gates:
    def __init__(self):
        r1 = randint(0, n-1)
        r2 = randint(0, n-1)
        self.positionX = []
        self.positionY = []
        if ((r1+r2)%2==1):
            self.positionX.append(r1)
            if r2>((n-1)/2):
                self.positionY.append(n-1)
            else:
                self.positionY.append(0)
        else:
            self.positionY.append(r2)
            if r1>((n-1)/2):
                self.positionX.append(n-1)
            else:
                self.positionX.append(0)
        if (gates_direction == 1):
            for i in range(1, gate_width):
                if (self.positionX[i-1] == 0):
                    if (self.positionY[i-1]+1<n):
                        self.positionX.append(self.positionX[i-1])
                        self.positionY.append(self.positionY[i-1]+1)
                    else:
                        self.positionX.append(self.positionX[i-1]+1)
                        self.positionY.append(self.positionY[i-1])
                elif (self.positionY[i-1] == n-1):
                    if (self.positionX[i-1]+1<n):
                        self.positionX.append(self.positionX[i-1]+1)
                        self.positionY.append(self.positionY[i-1])
                    else:
                        self.positionX.append(self.positionX[i-1])
                        self.positionY.append(self.positionY[i-1]-1)
                elif (self.positionX[i-1] == n-1):
                    if (self.positionY[i-1]-1>=0):
                        self.positionX.append(self.positionX[i-1])
                        self.positionY.append(self.positionY[i-1]-1)
                    else:
                        self.positionX.append(self.positionX[i-1]-1)
                        self.positionY.append(self.positionY[i-1])
                elif (self.positionY[i-1] == 0):
                    if (self.positionX[i-1]-1>=0):
                        self.positionX.append(self.positionX[i-1]-1)
                        self.positionY.append(self.positionY[i-1])
                    else:
                        self.positionX.append(self.positionX[i-1])
                        self.positionY.append(self.positionY[i-1]+1)        
        elif (gates_direction==-1):
                for i in range(1, gate_width):
                    if (self.positionX[i-1] == 0):
                        if (self.positionY[i-1]-1>=0):
                            self.positionX.append(self.positionX[i-1])
                            self.positionY.append(self.positionY[i-1]-1)
                        else:
                            self.positionX.append(self.positionX[i-1]+1)
                            self.positionY.append(self.positionY[i-1])
                    elif (self.positionY[i-1] == 0):
                        if (self.positionX[i-1]+1<n):
                            self.positionX.append(self.positionX[i-1]+1)
                            self.positionY.append(self.positionY[i-1])
                        else:
                            self.positionX.append(self.positionX[i-1])
                            self.positionY.append(self.positionY[i-1]+1)
                    elif (self.positionX[i-1] == n-1):
                        if (self.positionY[i-1]+1<n):
                            self.positionX.append(self.positionX[i-1])
                            self.positionY.append(self.positionY[i-1]+1)
                        else:
                            self.positionX.append(self.positionX[i-1]-1)
                            self.positionY.append(self.positionY[i-1])
                    elif (self.positionY[i-1] == n-1):
                        if (self.positionX[i-1]-1>=0):
                            self.positionX.append(self.positionX[i-1]-1)
                            self.positionY.append(self.positionY[i-1])
                        else:
                            self.positionX.append(self.positionX[i-1])
                            self.positionY.append(self.positionY[i-1]-1) 
        
        
    def move(self, gates_direction):
        if random.random() < probability_gd:
            gates_direction *=(-1)
        if random.random() < probability_gm:
            if (gates_direction==1):
                for i in range(gate_width):
                    if (self.positionX[i] == 0):
                        if (self.positionY[i]+1<n):                 
                            self.positionX[i] = self.positionX[i]   #RIGHT
                            self.positionY[i] = self.positionY[i]+1
                        else:
                            self.positionX[i] = self.positionX[i]+1 #DOWN
                            self.positionY[i] = self.positionY[i]
                    elif (self.positionY[i] == n-1):
                        if (self.positionX[i]+1<n):
                            self.positionX[i] = self.positionX[i]+1 #DOWN
                            self.positionY[i] = self.positionY[i]
                        else:
                            self.positionX[i] = self.positionX[i]   #LEFT
                            self.positionY[i] = self.positionY[i]-1 
                    elif (self.positionX[i] == n-1):
                        if (self.positionY[i]-1>=0):
                            self.positionX[i] = self.positionX[i]   #LEFT
                            self.positionY[i] = self.positionY[i]-1
                        else:
                            self.positionX[i] = self.positionX[i]-1 #UP
                            self.positionY[i] = self.positionY[i]
                    elif (self.positionY[i] == 0):
                        if (self.positionX[i]-1>=0):
                            self.positionX[i] = self.positionX[i]-1 #UP
                            self.positionY[i] = self.positionY[i]
                        else:
                            self.positionX[i] = self.positionX[i]   #RIGHT
                            self.positionY[i] = self.positionY[i]+1
            elif (gates_direction==-1):
                for i in range(gate_width):
                    if (self.positionX[i] == 0):
                        if (self.positionY[i]-1>=0):
                            self.positionX[i] = self.positionX[i]   #LEFT
                            self.positionY[i] = self.positionY[i]-1
                        else:
                            self.positionX[i] = self.positionX[i]+1 #DOWN
                            self.positionY[i] = self.positionY[i]
                    elif (self.positionY[i] == 0):
                        if (self.positionX[i]+1<n):
                            self.positionX[i] = self.positionX[i]+1 #DOWN
                            self.positionY[i] = self.positionY[i]
                        else:
                            self.positionX[i] = self.positionX[i]   #RIGHT
                            self.positionY[i] = self.positionY[i]+1
                    elif (self.positionX[i] == n-1):
                        if (self.positionY[i]+1<n):
                            self.positionX[i] = self.positionX[i]   #RIGHT
                            self.positionY[i] = self.positionY[i]+1
                        else:
                            self.positionX[i] = self.positionX[i]-1 #UP
                            self.positionY[i] = self.positionY[i]
                    elif (self.positionY[i] == n-1):
                        if (self.positionX[i]-1>=0):
                            self.positionX[i] = self.positionX[i]-1 #UP
                            self.positionY[i] = self.positionY[i]
                        else:
                            self.positionX[i] = self.positionX[i]   #LEFT
                            self.positionY[i] = self.positionY[i]-1            
            
class Walls:
    def __init__(self):
        self.positionX = []
        self.positionY = []
        self.walls_direction = []
        self.positionX.append(randint(1, n-2))
        self.positionY.append(randint(1, n-2))
        flag1 = False
        while (flag1 == False):
            r = randint(0, 3)
            if (r==0):
                if ((self.positionX[0] + wall_width-1)<(n-1)):
                    flag1 = True
                    for i in range(1, wall_width):
                        self.positionX.append(self.positionX[i-1]+1)
                        self.positionY.append(self.positionY[i-1])         
            elif (r==1):
                if ((self.positionY[0] + wall_width-1)<(n-1)):
                    flag1 = True
                    for i in range(1, wall_width):
                        self.positionX.append(self.positionX[i-1])
                        self.positionY.append(self.positionY[i-1]+1)
            elif (r==2):
                if ((self.positionX[0] - wall_width-1)>0):
                    flag1 = True
                    for i in range(1, wall_width):
                        self.positionX.append(self.positionX[0])
                        self.positionY.append(self.positionY[0])
                    for i in range(wall_width-1, 0, -1):
                        self.positionX[i-1] = self.positionX[i]-1
                        self.positionY[i-1] = self.positionY[i]
            elif (r==3):
                if ((self.positionY[0] - wall_width-1)>0):
                    flag1 = True
                    for i in range(1, wall_width):
                        self.positionX.append(self.positionX[0])
                        self.positionY.append(self.positionY[0])
                    for i in range(wall_width-1, 0, -1):
                        self.positionX[i-1] = self.positionX[i]
                        self.positionY[i-1] = self.positionY[i]-1
        r = randint(1, 4)
        if (r == 1):
            self.walls_direction = [1, 0]
        elif (r == 2):
            self.walls_direction = [0, 1]
        elif (r==3): 
            self.walls_direction = [-1, 0]
        elif (r==4):
            self.walls_direction = [0, -1]

            
    def move(self, board):
        if random.random() < probability_wd:
            r = randint(1, 4)
            if (r == 1):
                self.walls_direction = [1, 0]
            elif (r == 2):
                self.walls_direction = [0, 1]
            elif (r==3): 
                self.walls_direction = [-1, 0]
            elif (r==4):
                self.walls_direction = [0, -1]
        if random.random() < probability_wm:
            flag2 = 0
            for i in range(wall_width):
                a = self.positionX[i]+self.walls_direction[0]
                b = self.positionY[i]+self.walls_direction[1]
                if (board[int(a)][int(b)] == 0 or board[int(a)][int(b)] == 3 or board[int(a)][int(b)] == 6):
                    flag2 += 1
                elif (board[int(a)][int(b)] == 2 or board[int(a)][int(b)] == 1):
                    self.walls_direction[0]*=(-1)
                    self.walls_direction[1]*=(-1)
                    flag2 += 1
            if (flag2 == wall_width):
                for i in range(wall_width):
                    self.positionX[i]+= self.walls_direction[0]
                    self.positionY[i]+= self.walls_direction[1]

def catch_check(thief, cops):
    for i in range(number_of_cops):
        if (cops.cops_list[i].positionX == thief.positionX and cops.cops_list[i].positionY == thief.positionY):
            return 3
        elif (cops.cops_list[i].positionX+1 == thief.positionX and cops.cops_list[i].positionY == thief.positionY):
            return 3
        elif (cops.cops_list[i].positionX-1 == thief.positionX and cops.cops_list[i].positionY == thief.positionY):
            return 3
        elif (cops.cops_list[i].positionY+1 == thief.positionY and cops.cops_list[i].positionX == thief.positionX):
            return 3
        elif (cops.cops_list[i].positionY-1 == thief.positionY and cops.cops_list[i].positionX == thief.positionX):
            return 3
        
def escape_check(gate, thief):
    for i in range(number_of_gates):
        for j in range(gate_width):
            if (gate[i].positionX[j] == thief.positionX and gate[i].positionY[j] == thief.positionY):
                return 2       

def main():
    thief_score = T
    world = World()
    plt.imshow(world.worlds_list[0])
    plt.show()
    for t in range(1, T):
        tStart = time.time()
        world.move()
        plt.imshow(world.worlds_list[t])
        plt.show()
        if (catch_check(world.thief, world.cops) == 3):
            thief_score = t
            print("A cop caught a thief") #gui
            break
        if (escape_check(world.gate, world.thief) == 2):
            if (t+1 == T):
                thief_score = T-1
            else:
                thief_score = 2*T-t-1
            print("A thief has escaped") #gui
            break
        
        tStop = time.time()
        tDelta = tStop - tStart
        if (tDelta < 0.4):
            time.sleep(0.4 - tDelta)
    
    print("Score:", thief_score) #gui
        
if __name__ == '__main__':
    main()        
        
