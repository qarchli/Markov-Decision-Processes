class MDP:
    def __init__(self, transitions={}, rewards={}, gamma=0.9):
        self.states = transitions.keys()
        self.transitions = transitions
        self.rewards = rewards
        self.gamma = gamma

    def R(self, state):
        """
        return the reward of being in a given state
        """
        return self.rewards[state]

    def A(self, state):
        """
        return set of actions that can be performed in the given state
        """
        return self.transitions[state].keys()

    def T(self, state, action):
        """
        return list of pairs (proba, state) corresponding to where we're 
        going to end up if we take a given action in a given state
        """
        return self.transitions[state][action]


class MDPSolver:
    def __init__(self, method='vi'):
        self.method = method

    def solve(self, mdp):
        """
        solve the mdp using the method specified in the constructor.
        """
        self.mdp = mdp
        if self.method == 'vi':
            return self.value_iteration()

    def value_iteration(self, epsilon=0.001, max_iter=1000):
        """
        Solves the given mdp by returning the optimal Value Function and its corresponding optimal policy
        """
        # extract mdp attributes
        states = self.mdp.states
        transitions = self.mdp.transitions
        rewards = self.mdp.rewards
        gamma = self.mdp.gamma
        A = self.mdp.A  # action function
        R = self.mdp.R  # reward function
        T = self.mdp.T  # transition function

        # initialize the value function to zeros
        V = {state: 0 for state in states}
        delta = 0  # for convergence testing
        iterations = 0

        # loop until convergence
        while True:
            # start from the old value function
            V_new = V.copy()

            for state in states:
                # bellman's update for a given state
                V_new[state] = max([
                    R(state) + gamma *
                    sum([p * V[state_p] for (p, state_p) in T(state, action)])
                    for action in A(state)
                ])

                # difference between the old and new value
                delta = max(delta, abs(V_new[state] - V[state]))

            # convergence test
            # if true, returns the optimal value function as well as its corresponding optimal policy
            if delta < epsilon or iterations >= max_iter:

                def optimal_policy(V):
                    """
                    returns the optimal policy given a value function
                    """
                    opt_policy = {}
                    for state in states:
                        opt_policy[state] = max(
                            A(state),
                            key=lambda action: R(state) + gamma * sum([
                                p * V[state_p] for (p, state_p) in T(
                                    state, action)
                            ]))

                    return opt_policy

                return V_new, optimal_policy(V_new)

            # update the old value function
            V = V_new.copy()

            # increment the iterations
            iterations += 1