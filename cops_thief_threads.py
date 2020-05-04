#import numpy as np
#import random
#import matplotlib.pyplot as plt
from random import randint
import time
import threading
#import logging
#import queue
import inspect
import ctypes
#import copy
import cops_algorithm
import thief_algorithm
import cops_thief_main as c_t_m

class Cops:
    def __init__(self, worlds_list_copy):
        self.cops_list = []
        for i in range(c_t_m.number_of_cops):
            self.cops_list.append(Cop(worlds_list_copy[len(worlds_list_copy)-1]))

    def move(self, move_plan, worlds_list_copy):
        for i in range(c_t_m.number_of_cops):
            self.cops_list[i].move(move_plan[i], worlds_list_copy)

class Cop:
    def __init__(self, board):
        flag1 = 0
        while (flag1 == 0):
            self.positionX = randint(1, c_t_m.n-2)
            self.positionY = randint(1, c_t_m.n-2)
            if (board[int(self.positionX)][int(self.positionY)]==0):
                flag1 = 1
    
    def move(self, move_plan, worlds_list):
        t = len(worlds_list) - 1
        board = worlds_list[t]
        if (move_plan[t%c_t_m.k] == c_t_m.Direction.DOWN):
            a = int(self.positionX+1)
            b = int(self.positionY)
            if (board[a][b] == 0 or board[a][b] == 6):
                self.positionX+=1
        elif (move_plan[t%c_t_m.k] == c_t_m.Direction.RIGHT):
            a = int(self.positionX)
            b = int(self.positionY+1)
            if (board[a][b] == 0 or board[a][b] == 6):
                self.positionY+=1
        elif (move_plan[t%c_t_m.k] == c_t_m.Direction.UP):
            a = int(self.positionX-1)
            b = int(self.positionY)
            if (board[a][b] == 0 or board[a][b] == 6):
                self.positionX-=1
        elif (move_plan[t%c_t_m.k] == c_t_m.Direction.LEFT):
            a = int(self.positionX)
            b = int(self.positionY-1)
            if (board[a][b] == 0 or board[a][b] == 6):
                self.positionY-=1
    
    
class Thief:
    def __init__(self, board):
        flag1 = 0
        while (flag1 == 0):
            self.positionX = randint(1, c_t_m.n-2)
            self.positionY = randint(1, c_t_m.n-2)
            if (board[int(self.positionX)][int(self.positionY)]==0):
                flag1 = 1
    
    def move(self, move_plan, worlds_list):
        t = len(worlds_list) - 1
        board = worlds_list[t]
        if (move_plan[t%c_t_m.k] == c_t_m.Direction.DOWN):
            a = int(self.positionX+1)
            b = int(self.positionY)
            if (board[a][b] == 0 or board[a][b] == 2 or board[a][b] == 6):
                self.positionX+=1
        elif (move_plan[t%c_t_m.k] == c_t_m.Direction.RIGHT):
            a = int(self.positionX)
            b = int(self.positionY+1)
            if (board[a][b] == 0 or board[a][b] == 2 or board[a][b] == 6):
                self.positionY+=1
        elif (move_plan[t%c_t_m.k] == c_t_m.Direction.UP):
            a = int(self.positionX-1)
            b = int(self.positionY)
            if (board[a][b] == 0 or board[a][b] == 2 or board[a][b] == 6):
                self.positionX-=1
        elif (move_plan[t%c_t_m.k] == c_t_m.Direction.LEFT):
            a = int(self.positionX)
            b = int(self.positionY-1)
            if (board[a][b] == 0 or board[a][b] == 2 or board[a][b] == 6):
                self.positionY-=1


def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    if not inspect.isclass(exctype):
        raise TypeError("Only types can be raised (not instances)")
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(tid),
            ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, 0)
        raise SystemError("PyThreadState_SetAsyncExc failed")

class Planner:
    def __init__(self):
        self.cops_planner = cops_algorithm.Cops_planner()
        self.thief_planner = thief_algorithm.Thief_planner()       

    def thread_function(self, worlds_list_copy):
        self.worlds_list_copy = worlds_list_copy[len(worlds_list_copy)-c_t_m.k:]
        
        self.cops_planner.cleaning()
        self.thief_planner.cleaning()
        
        
        th1 = threading.Thread(target=self.cop_plans, args=())
        th2 = threading.Thread(target=self.thief_plans, args=())
        th1.start()
        th2.start()
        
        t_start = time.time()
        th1.join(c_t_m.max_t)
        if th1.is_alive():
            _async_raise(th1.ident, TimeoutError)
            th1.join()

        th2.join(c_t_m.max_t - (time.time() - t_start))
        if th2.is_alive():
            _async_raise(th2.ident, TimeoutError)
            th2.join()

    def cop_plans(self):
        t_start = time.time()
        try:
            self.cops_planner.algorithm(self.worlds_list_copy)
            t_end = (time.time() - t_start)
            print("Calculation for cops completed, time:", t_end)
        except TimeoutError:
            t_end = (time.time() - t_start)
            print("Calculation for cops is interrupted:", t_end)

    def thief_plans(self):
        t_start = time.time()
        try:
            self.thief_planner.algorithm(self.worlds_list_copy)
            t_end = (time.time() - t_start)
            print("Calculation for thief completed, time:", t_end)
        except TimeoutError:
            t_end = (time.time() - t_start)
            print("Calculation for thief is interrupted:", t_end)


    
        
        
        