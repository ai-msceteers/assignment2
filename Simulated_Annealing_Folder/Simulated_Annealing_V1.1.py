#/**
# *\file      Simulated_Annealing.py
# *\brief     This code contains the simulated annealing algorithm implemented
# *           to solve the Assignment 2, group project, rubix cube problem
# *           - Solves both n=2, n=3 cubes
# *           - Utilises calculate_cost() function based on number of missplaced cube element faces
# *           - Utilises a mixture of Annealing and Tempering to obtain a solved cube state
# *\Note      - Cost value has a maximum and minimum and is descret for our purposes, resulting in many delta=0
# *\Author    F.OSuibhne
# *\Version   V1.1
# *\Date      10-04-21
# */

from rubiks_cube import RubiksCube
#from solve_random_cubes import random_cube, run #< Dont beleive run is used anymore
import time
#import numpy as np
import random
import math
from copy import deepcopy   


def Simulated_Annealing():

    start = time.time()         #< Timer activated for runtime 
    T_0 = 35                  #< Starting Temperature, n=2 Temp= 2.86 / in theory: n=3 Temp= 35 see STD_cost() below
    Temp = T_0
    Cooling_Rate = .99          #< Determines how fast algorithm completes (longer more likley to obtain goal)
                                #  should be a positive value, between 0-1 Ideally should be considered with the max temperature
                                #  and probability value, if too high much time is wasted, too low and local minimum are not avoided
    
    Current_State = RubiksCube(n=3, randomize = True)  #< Call for new random rubix cube state of size nxnxn
    print("Cube Start State\n",Current_State.cube, "\n\n\n")                #< Dont remove without uncommenting line 32
    #Current_State.cube 
    print("Initial Cube of cost = ", Current_State.calculate_cost())

    N_Moves = 0                 #< Initialise counter, no. of accepted moves to reach goal
    MKV_Chain_Count = 0         #< Initialise counter, consecutive itterations without improvement

    Current_Best_State = deepcopy(Current_State)    #< Initialise
    Best_Cost = Current_Best_State.calculate_cost() #< Initialise 
    Initial_Best_Cost = deepcopy(Best_Cost)         #< Retaining copy of initial state

    #________ Checks for Unmixed Cube ___________ 
    if Current_State.is_solved()==True:    #Checks for goal state
        print("Failure: Initialised random state is alread goal") #< Failure because algorithm didnt do anything
        return Current_State

    while Temp > .001:    #< Set final Temperature ~0, cant be 0 (Temp = Temp*Cooling_Rate) wouldn't solve 
        MKV_Chain = 0   #< Reset counter

        while MKV_Chain < 20:   #< length of each markov chain, (I think should be 18^2, confused on formula)
            #_________ Make & Evaluate Move ________ 
            Next_State = deepcopy(Current_State)
            Next_State.apply_move(Next_State.get_random_move()) #Apply_Random_Move(Current_State)    # Get 1 of 18 random next moves, apply and obtain the state
            Current_Cost = Current_State.calculate_cost() 
            Next_Cost = Next_State.calculate_cost()
            Delta_Cost =  Next_Cost - Current_Cost          #< Calculate gain or loss of accepting move 
                                                            #  Goal is cost reduction smaller cost is better
                                                            #  delta would be negative if Next is desirable

            #_________ Checks for Goal State __________
            if Next_State.is_solved() == True:              #< Accepts if at final goal state
                Current_Best_State = deepcopy(Next_State)   
                duration = time.time() - start              #< Calculate run time
                print("Goal state reached after", N_Moves, " Moves after ", duration, " seconds")
                return Current_Best_State.cube              #< Returns whole goal state cube

            #__________ Annealing Steps ____________
            if Delta_Cost < 0:                             #< If improvment always accept next state
                                                            #< NOTE: very discrete cost values mean delta of 0 is common
                                                            #  this poses an issue with the probability calculation later
                Current_State = deepcopy(Next_State)
                N_Moves=N_Moves+1   
            else:
                if Delta_Cost == 0:
                    Delta_Cost = .1                                           
                
                probability = math.exp(-(Delta_Cost/Temp))   #< A value between 0-1, approaches 1 as T increases
                rando = random.uniform(0,1)
                if probability > rando:          #< Accepts non-benificial actions based on probability, as Temp
                                                 #  Decreases probability of acceptance must reduce
                    Current_State = deepcopy(Next_State)
                    N_Moves=N_Moves+1      
            
            #___________ Save Record _____________
            if Best_Cost > Current_Cost:    #< If new record, save updated state info
                Current_Best_State = deepcopy(Current_State)
                Best_Cost = Current_Cost
            
            MKV_Chain = MKV_Chain+1           #< Counter 
        Temp = Temp*Cooling_Rate              #< Itterativly decrementing temperature

        #__________ Tempering Steps __________
        if Best_Cost == Initial_Best_Cost:      
            MKV_Chain_Count = MKV_Chain_Count+1 #< Counter for non-improvemet
        else: 
            Initial_Best_Cost = Best_Cost 
            MKV_Chain_Count = 0 #< Reset counter
        
        if MKV_Chain_Count == 20:   #< if no improvment for fixed no. of itterations
            Temp = 2.86              #< Reset annealing temperature
            MKV_Chain_Count = 0   
    
    
    duration = time.time() - start  #< Calculate run time
    print("Failed to reach goal state, Best cost obtained was", Best_Cost)
    print("State reached after", N_Moves, " Moves after ", duration, " seconds")
    return(Current_Best_State.cube)                  #< Returns Non-Goal final state

print(Simulated_Annealing())



#__________ Utilised to calculate a mean and std individually _________
def STD_cost():
    x=0
    Total=0
    sum=0
    while x<200:
        Current_State =  RubiksCube(n=3, randomize = True) 
        Cost = Current_State.calculate_cost()
        #Total = Total+Cost
        sum = sum + (Cost-25.3)*(Cost-25.3)
        x=x+1
    #mean = Total/200
    sigma= math.sqrt(sum/200)
    return (sigma)
    #_Resulting std used for 
    #for n=2x2x2 cube, mean = 25.99, sigma = 2.684
    #for n=3x3x3 cube, mean = 59.41, sigma = 35.09

#print(STD_cost())

