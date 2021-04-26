                 Rubik's Cube: Artificially Intelligent Solvers
                           CS7IS2 Project (2020/2021)

1. Repositories
===============

1. https://github.com/ai-msceteers/assignment2

   Includes:

   - Report
   - Custom genetic algorithm code
   - Custom simulated annealing code
   - Modified DeepCubeA fork as a Git submodule; see next item

2. https://github.com/ai-msceteers/DeepCubeA

   This is a fork of the DRL+BWAS implementation by Agostinelli et al., which
   came with a ready-trained DNN for cubes of size 3.

   Our fork lifts the n=3 restriction in the original environment, and adds:

   - DNN trained for cubes of size 2
   - Test data and scripts for running the evaluation and plotting results
   - A minor bugfix in the original code :)

2. Team and Contributions
=========================

All members did initial research into potential topics and environments, met
periodically with the rest of the team, and contributed in some way to the
project.

1. William O'Sullivan

   Responsible for leading the team and putting together the report and
   presentation.  To this end, researched all of the topics both in
   collaboration with the rest of the team, and as extensive personal literature
   review.

2. Talha Ijaz

   Responsible for the genetic algorithm approach, its difficult custom
   implementation informed by extensive personal literature review, and its
   evaluation.  Mentored other members during the implementation phase.

3. Fionntán Ó Suibhne

   Responsible for the simulated annealing approach, its difficult custom
   implementation informed by extensive personal literature review, and its
   evaluation.

4. Basil Contovounesios

   Responsible for general project bookkeeping and the deep reinforcement
   learning approach.  Made the necessary changes to the existing DeepCubeA
   project to train and evaluate DNNs for different cube sizes.  Reviewed and
   copy-edited every revision of the report and presentation after extensive
   personal literature review.
