import numpy as np
import random
from copy import deepcopy
from collections import Counter

        

class RubiksCube(object):
    
    # Faces stores in 6 NxN faces stored as a numpy matrix in cube 
    # 0 : front
    # 1 : top
    # 2 : back
    # 3 : bottom
    # 4 : left
    # 5 : right
    
    
    
    def __init__(self, n=3, randomize=True):
        self.n = n
        self.worst_cost = 48
        self.random_moves = []
        self.cost = 0
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
    def calulate_cost_v1(self):
        total_cost = 0
        for i in range(6):
            _, most_common_count = Counter(self.cube[i].ravel()).most_common()[0]
            current_face_cost = self.n**2 - most_common_count
            total_cost += current_face_cost
            
        self.cost = total_cost
        return self.cost
    
    def calculate_cost(self):
        #print()
        #print()
        self.worst_cost = ((self.n*self.n*(self.n-1)) + 1)*6

        get_n_colors_func = lambda x: len(set(x)) - 1 
        binary_cost_func = lambda x: int(len(set(x))!= 1)
        cost_func = get_n_colors_func
        #cost_func = binary_cost_func
        
        def face_cost_func(face):
            #print(face)
            rows_cost = np.apply_along_axis(cost_func, 1, face).sum()
            cols_cost = np.apply_along_axis(cost_func, 0, face).sum()
            is_solved = (rows_cost + cols_cost) == 0
            current_face_cost = rows_cost + cols_cost + (not is_solved)
            #print(rows_cost, cols_cost, is_solved, current_face_cost)
            return current_face_cost
        
        total_cost = np.sum([face_cost_func(self.cube[i]) for i in range(6)])
        #print(total_cost)
        
        #for i in range(6):
        #    current_face_cost = face_cost_func(self.cube[i])
        #    total_cost += current_face_cost
            
        self.cost = total_cost
        return self.cost

    
    def get_random_move(self):
        row = random.randint(0,self.n-1)
        direction = random.choice(["u", "d", "l", "r"])
        move = (row, direction)
        return move

        
    def randomize(self, n_moves_range = (30, 40)):
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
        if(move==None):
            return self.face()
        
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
        self.cost = self.calculate_cost()
        
        return self.face()
    
    
    def apply_moves(self, moves):
        for move in moves:
            self.apply_move(move)     
    
    
cube = RubiksCube(3, randomize=True)
orginal = deepcopy(cube)
random_moves = [cube.get_random_move() for i in range(random.randint(0, 6))]
cube = RubiksCube(3, randomize=True)
orginal = deepcopy(cube)
cube.apply_moves(random_moves)
cube.backtrack(random_moves)
#print(cube.cube)
#cube.apply_move(cube.get_random_move())
#cube.apply_move(cube.get_random_move())
#print(cube.calculate_cost())
    
    

    
    
    