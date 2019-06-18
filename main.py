import os
from mdp import *
from utils import *


def main():
    # reading data
    root_dir = os.path.dirname(os.path.abspath(__file__))
    transition_file = root_dir + '/data/transitions.csv'
    rewards_file = root_dir + '/data/rewards.csv'
    transitions, rewards = read_data(transition_file, rewards_file)

    # initialize the mdp
    mdp = MDP(transitions, rewards)

    # initialize the solver
    solver = MDPSolver()

    # solve the mdp
    V_star, Pi_star = solver.solve(mdp)

    print('State - Value')
    for s in V_star:
        print(s, ' - ', V_star[s])

    print('\nOptimal policy is \nState - Action')
    for s in Pi_star:
        print(s, ' - ', Pi_star[s])


if __name__ == '__main__':
    main()
