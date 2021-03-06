from random import randint
import cops_thief_main as c_t_m

class Cops_planner:
    def __init__(self):
        self.move_plan_vector = [0, 0, 0, 0, 0]
        self.move_plan = []
        for i in range(c_t_m.number_of_cops):
            self.move_plan.append(self.move_plan_vector)
    
    def cleaning(self):
        for i in range(c_t_m.number_of_cops):
            self.move_plan[i] = self.move_plan_vector
    
    def algorithm(self, worlds_list_copy):
        self.move_plan = [[0, 0, 0, 0, 0] for i in range(c_t_m.number_of_cops)]    
        for i in range(c_t_m.number_of_cops):
            for j in range(c_t_m.k):
                self.move_plan[i][j] = randint(0, 4)
