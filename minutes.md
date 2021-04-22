# 2021-04-22 Thursday 20:30-22:45

- Fionntán, Will, and Basil present.

- Status updates
  + Will has been doing backround reading on the algorithms, and has about a
    third of a draft report ready.
  + Fionntán has spent a lot of time tuning a hybrid annealing approach that
    solves cubes of both size 2 and 3.
  + Basil has [DeepCubeA](https://github.com/ai-msceteers/DeepCubeA) solving
    cubes of size 3 using the provided DNN, and is training a model for cubes of
    size 2.

- Most of the meeting comprised Fionntán and Basil walking Will through their
  theory and code.

- Agreed to submit by original extended deadline of 25th April.

- Todos
  + Basil to generate graphs for DeepCubeA under different configurations.
  + Will to continue writeup and call on others for input, notes, etc.

# 2021-04-15 Thursday 20:00-22:00

- Talha, Fionntán, and Basil present.

- Discussed progress to date and concerns.
  + Talha succeeded in solving a cube of size 2 with a genetic algorithm.
  + Talha and Fionntán discussed issues with their cost functions, and possible
    mitigations in the possible move sets.
  + Basil suggested informing the cost function with domain-specific knowledge
    like tile adjacency invariants.
  + Talha was concerned about poor performance of genetic and simulated
    annealing approaches with cubes of size 3.
  + Talha suggested switching projects to a different, more feasible topic.
  + Basil suggested it's too late to switch because everyone has already done a
    lot of research into their respective approaches.  In the worst case, a
    negative result in the n=3 case is still an interesting result when compared
    to other algorithms.  We may lose some marks for technical soundness, but
    ideally it won't be too dire.  The key is to make a decent comparison.

- Agreed to try and have most of the implementations done over the weekend so
  that we can then focus on the report and presentation.

# 2021-04-01 Thursday 17:00-18:00

- Everyone present.
- Fionntán looked into parameters of the assignment.
- Talha, Will, and Basil found relatively recent papers on a few different
  puzzles/games.
- Will came across Arcade Learning Environment AI research framework.

- Consensus for simple but interesting enough games/puzzles.
  + Considered:
    - Adversarial snakebattle
    - Travelling salesman
    - OpenGym - Mario
    - Rubik's Cube
    - 2048
    - Minesweeper
- Converged on looking initially into Rubik's.
  + There seems to be recent enough literature:
    - Genetic algorithms
    - Simulated annealing
    - Reinforcement learning
    - [CSP?]

- Meet again next week, with intention of having most of an implementation of a
  different approach by then, so that there is time for evaluation and writeup.
  + Talha to look into genetic algorithms.
  + Fionntán to look into simulated annealing.
  + Will & Basil to look into reinforcement learning.
  + Everyone to look into evaluation environments.
