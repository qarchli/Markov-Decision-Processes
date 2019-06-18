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
    solver = MDPSolver(method='pi')

    # solve the mdp
    print('Solving method:', {
        'vi': 'Value Iteration',
        'pi': 'Policy Iteration'
    }[solver.method])
    if solver.method == 'pi':
        Pi_init, V_star, Pi_star, iterations = solver.solve(mdp)
        print('\nIntial policy is \nState - Action')
        for s in Pi_init:
            print(s, ' - ', Pi_init[s])
        print()
    else:
        V_star, Pi_star, iterations = solver.solve(mdp)

    print('State - Value')
    for s in V_star:
        print(s, ' - ', V_star[s])

    print('\nOptimal policy is \nState - Action')
    for s in Pi_star:
        print(s, ' - ', Pi_star[s])

    print('\nConverged in {} iterations.'.format(iterations))


if __name__ == '__main__':
    main()
