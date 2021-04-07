from rubiks_cube import RubiksCube, Solution
import numpy as np


class GeneticSolver(object):
    
    
    def __init__(self, cube=None, n=3, w=0.9, population_size=100):
        self.population_size = population_size
        self.cube = RubiksCube(n) if(cube == None) else cube
        self.solutions = [Solution(self.cube, w=w)  for _ in range(population_size)]
        
        
    def reduce_population(self, goal=None, randomness = 0.0):
        goal = goal if goal!=None else self.population_size
        
        
        


#cube = RubiksCube(3)

s = GeneticSolver(n=3, w=0.9, population=100)
print(s.cube)