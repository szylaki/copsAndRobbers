from random import randint 
import cops_thief_main as c_t_m
#import time

class Thief_planner:
    def __init__(self):
        self.move_plan = [0, 0, 0, 0, 0]
    
    def cleaning(self):
        self.move_plan = [0, 0, 0, 0, 0]
    
    def algorithm(self, worlds_list_copy):
        for i in range(c_t_m.k):
            r = randint(0, 4)
            self.move_plan[i] = r