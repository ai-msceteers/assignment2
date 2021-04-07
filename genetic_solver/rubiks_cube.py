import numpy as np
import random
from copy import deepcopy
from collections import Counter


class Solution(object):
 
    moves = []
    
    def __init__(self, cube, w=1.0):
        self.inital = deepcopy(cube)
        self.cube = deepcopy(cube)
        self.w = w
        
    def add(self, move):
        self.moves.append(move)
        self.cube.apply_move(move)
        return self.cost()
        
    def cost(self):
        cube_cost = self.cube.cost
        penalty_cost = len(self.moves)
        total_cost = self.w*cube_cost + (1-self.w)*penalty_cost
        return total_cost
    
    def is_solved(self):
        return self.cube.is_solved()
    
    def is_better_than(self, solution):
        is_better = self.cost() < solution.cost()
        return is_better
    
    
        


class RubiksCube(object):
    
    # Faces stores in 6 NxN faces stored as a numpy matrix in cube 
    # 0 : front
    # 1 : top
    # 2 : back
    # 3 : bottom
    # 4 : left
    # 5 : right
    
    random_moves = []
    cost = 0
    
    def __init__(self, n=3, randomize=True):
        self.n = n
        self.cube = np.stack([np.ones((n,n))*i for i in range(6)])   
        if(randomize):
            self.randomize()            

    def __str__(self):
        return str(self.face())
    
    def __repr__(self):
        return str(self.face())
        
    def face(self):
        return self.cube[0]
    
    def is_solved(self):
        return self.cost == 0
    
    
    # TODO: Look for a better cost function
    def calulate_cost(self):
        total_cost = 0
        for i in range(6):
            _, most_common_count = Counter(self.cube[i].ravel()).most_common()[0]
            current_face_cost = self.n**2 - most_common_count
            total_cost += current_face_cost
            
        self.cost = total_cost
        return self.cost

    
    def get_random_move(self):
        row = random.randint(0,self.n-1)
        direction = random.choice(["u", "d", "l", "r"])
        move = (row, direction)
        return move

        
    def randomize(self, n_moves_range = (30, 50)):
        self.random_moves = []
        for i in range(random.randint(*n_moves_range)):
            move = self.get_random_move()
            self.random_moves.append(move)
            self.apply_move(move)
    
    
    def backtrack(self, moves):
        reverse_move_dict = {"u":"d", "d":"u", "l":"r", "r":"l"}
        for move in moves[::-1]:
            reverse_move = (move[0], reverse_move_dict[move[1]])
            self.apply_move(reverse_move)     
        return self.face()
      
            
    def apply_move(self, move):
        row, direction = move
        
        if(direction=="u"):
            order = [0, 1, 2, 3, 0]
        elif(direction=="d"):
            order = [0, 3, 2, 1, 0]
        elif(direction=="l"):
            order = [0, 4, 2, 5, 0]
        elif(direction=="r"):
            order = [0, 5, 2, 4, 0]
            
        temp_cube = deepcopy(self.cube)
        for i in range(len(order)-1):
            i1, i2 = order[i], order[i+1]
            if(direction in ["u", "d"]):
                self.cube[i2,:, row] = temp_cube[i1, :, row]
            elif(direction in ["l", "r"]):
                self.cube[i2, row, :] = temp_cube[i1, row, :] 
        self.cost = self.calulate_cost()
        
        return self.face()
    
    
    def apply_moves(self, moves):
        for move in moves:
            self.apply_move(move)     
    
    
    

    
    
    