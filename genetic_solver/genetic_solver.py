from rubiks_cube import RubiksCube
import numpy as np
import random
from copy import deepcopy
import time

current_id = 0


class GeneticSolution(object):
        
    def __init__(self, cube, s=30, w=1.0):
        self.inital = deepcopy(cube)
        self.cube = deepcopy(cube)
        self.w = w
        #self.moves = [self.cube.get_random_move() for _ in range(s)]
        self.moves = []#None for _ in range(s)]
        self.costs = []
        self.apply_moves()
    
    def apply_moves(self):
        self.cube = deepcopy(self.inital)
        for move in self.moves:
            self.cube.apply_move(move)
            
    def delete_last_moves(self, n=1):
        self.cube.backtrack(self.moves[(-1*n):])
        self.moves = self.moves[:(-1*n)]
        
    def cost(self):
        return self.cube.calculate_cost()
        #cube_cost = self.cube.calculate_cost()
        #penalty_cost = len(self.moves)
        #total_cost = self.w*cube_cost + (1-self.w)*penalty_cost
        #return total_cost
    
    def is_solved(self):
        return self.cube.is_solved()
    
    def is_better_than(self, solution):
        is_better = self.cost() < solution.cost()
        return is_better
    
    def mutate_moves(self):
        n_moves_mutate = random.randint(1, 4)
        for _ in range(n_moves_mutate):
            if(random.randint(0, 2)==0):
                self.moves[random.randint(0, len(self.moves)-1)] = self.cube.get_random_move()
            elif(random.randint(0, 1)==0):
                self.moves[random.randint(0, len(self.moves)-1)] = None
            else:
                self.moves.append(self.cube.get_random_move())
        self.apply_moves()
        
    
    def mutate(self, p=0.05, randomness=0.05, max_tries = 1, max_steps=6):
        #print("Making Move: ({})".format(str(self)))
        if(random.random() < p and not self.is_solved()):
            i = 0
            while(i < max_tries):
                i = i+1
                old_cost = self.cost()
                random_moves = [self.cube.get_random_move() for i in range(random.randint(0, max_steps))]
                temp = deepcopy(self)
                temp.cube.apply_moves(random_moves)
                #temp.mutate_moves()
                new_cost = temp.cost()
                if(old_cost > new_cost or random.random() < randomness):
                    self.moves = self.moves + random_moves
                    #print("Accepting move", old_cost, new_cost)
                    self.cube.apply_moves(random_moves)
                    self.costs.append((new_cost, len(self.moves)))
                    assert new_cost == self.cost()
                    #self.moves = temp.moves
                    #self.apply_moves()
                    break
                else:
                    assert old_cost == self.cost()
                
            #print(old_cost, self.cost(), self.moves)
    
    
#cube = RubiksCube(3)
#start_time = time.time()              
#solution = GeneticSolution(cube, s=30, w=1.0)
#t = 0.2
#for i in range(0):
#    solution.mutate(p=1.0, randomness=t, max_tries = 1)
#    if(solution.is_solved()):
#        break
#    t = t*0.9
#print(time.time()-start_time)


class GeneticSolver(object):
    
    
    def __init__(self, cube=None, n=3, w=0.9, population_size=100):
        self.population_size = population_size
        self.cube = RubiksCube(n) if(cube == None) else cube
        self.solutions = np.array([GeneticSolution(self.cube, w=w)  for _ in range(population_size)])
        self.get_costs = np.vectorize(lambda x: x.cost())
        
        
        
    def get_offspring(self, parent1, parent2):
        #print("Getting offspring: ", parent1, parent2)
        child  = deepcopy(parent1)
        i = random.randint(5, min(len(parent1.moves), len(parent2.moves)))
        child.moves = parent1.moves[:i] + parent2.moves[i:] 
        child.apply_moves()
        #print(parent1.cost(), parent2.cost(), child.cost())
        return child
      
        
    def crossover_population(self, solutions, n=None):
        if(n==None):
            n = len(solutions)
        if(n == 0):
            return []
        costs = self.cube.worst_cost - self.get_costs(solutions)
        prob_dist = costs/np.sum(costs)
        solutions_selected = np.random.choice(solutions, int(n), p=prob_dist, replace=False)
        
        selected_costs = self.cube.worst_cost - self.get_costs(solutions_selected)
        selected_prob_dist = selected_costs/np.sum(selected_costs)
        solutions_pairs = np.random.choice(solutions_selected, n*2, p=selected_prob_dist, replace=True).reshape((n, 2))
        #print(selected_prob_dist)
        #print(solutions_pairs)
        #print(solutions_pairs.shape)
        next_generation = [self.get_offspring(solutions_pairs[i,0], solutions_pairs[i,1]) for i in range(solutions_pairs.shape[0])]
        next_generation = np.array(next_generation).reshape((1,-1))
        return next_generation
    
    
    def reduce_population(self, goal=None, randomness = 0.0):
        goal = goal if goal!=None else self.population_size
        current_size = len(self.solutions)
        if(goal < current_size):
            costs = self.get_costs(self.solutions)
            argsort = np.argsort(costs)
            #print(argsort)
            n_random = int(randomness*goal)
            #print(n_random)
            if(n_random > 0):
                randomly_exclude = np.random.randint(0, goal, (n_random, 1))
                randomly_include = np.random.randint(goal, current_size, (n_random, 1))
                switch_pairs = np.hstack((randomly_exclude, randomly_include)) 
                #print(switch_pairs)
                def switch_func(row): 
                    #print("Row: ", row)
                    argsort[row[0]], argsort[row[1]] = argsort[row[1]], argsort[row[0]] 
                np.apply_along_axis(switch_func , 1, switch_pairs)
                #print(argsort)
                #print(argsort[:goal])
                self.solutions = self.solutions[argsort[:goal]]
                
                
    def run(self, max_iterations=10, p_crossover=0.8, p_elites=0.1, p_mutate=0.1, randomness=0.1, max_steps=6):
        
        time_started = time.time()
        print(self.get_costs(self.solutions))
        self.best_solution_yet = deepcopy(self.solutions[0])
        for i in range(max_iterations):  
            list(map(lambda x: x.mutate(p=p_mutate, randomness=randomness, max_tries=1, max_steps=max_steps), self.solutions))
            costs = self.get_costs(self.solutions)
            argsort = np.argsort(costs)     
            
            if(min(costs)>self.best_solution_yet.cost()):
                self.solutions[argsort[-1]] = deepcopy(self.best_solution_yet)
            
            if(min(costs) < self.best_solution_yet.cost()):
                self.best_solution_yet = deepcopy(self.solutions[argsort[0]])
                
            if(False):
                n_children = int(p_crossover*self.population_size)
                n_elites = int(p_elites*self.population_size)
                n_non_elites =  max(0, self.population_size -  n_children - n_elites)
            
                children = self.crossover_population(self.solutions, n=n_children)
                elites = self.solutions[argsort[:n_elites]].reshape((1,-1))
                non_elites = self.solutions[argsort[n_elites:]]
                                           
                if(n_non_elites > 0):
                    non_elite_efficiency = self.cube.worst_cost - self.get_costs(non_elites)
                    prob_dist = non_elite_efficiency/np.sum(non_elite_efficiency)
                    non_elites_chosen = np.random.choice(non_elites, n_non_elites, p=prob_dist, replace=False).reshape((1,-1))
                    combine_tuple = (elites, non_elites_chosen, children) if len(children)!=0 else (elites, non_elites_chosen)
                else:
                    combine_tuple = (elites, children) if len(children)!=0 else (elites)
                    
                #self.solutions = np.hstack(combine_tuple).ravel()
                
            if(min(costs)==0):
                break
            
            if(i%20==0):
                print(str(i)+"  Current Best: ", min(costs), " ",  self.best_solution_yet.cost(), "    ", time.time()-time_started)
                
            #print(len(self.solutions))
        
            #moves = np.vectorize(lambda x: x.moves)(self.solutions)
        time_taken = round(time.time()-time_started, 4)
        print("Time Taken: ", time_taken, 2)
        costs = self.get_costs(self.solutions)
        print(costs)
        print(min(costs))
        
        return self.best_solution_yet, time_taken
        
                             
                             
            
        
        
    
        


#cube = RubiksCube(3)

s = GeneticSolver(n=2, w=1, population_size=50)
print(s.cube)
best, t = s.run(max_iterations=2000, 
                p_crossover=0.0, 
                p_elites=1.0, 
                p_mutate=1, 
                randomness=0.02,
                max_steps=6)
print(s.cube)

s.best_solution_yet











