# Markov-Decision-Processes

This project implements some algorithms, such as **Value Iteration** and **Policy Iteration** for calculating the optimal policy of a given Markov Decision Process.

## Problem description

The problem we are trying to solve is a simple gridworld problem in which the agent should figure out the best path to reach the terminal state, corresponding to the gain +10, starting from the state (3 0).

The cost of being in each state is shown in the figure below:

<img src="./gridworld.svg">


## Usage

`python main.py` or via the [notebook](https://github.com/qarchli/Markov-Decision-Processes/blob/master/Solving%20an%20mdp%20.ipynb)

## Data

**transition_file** contains tuple *(state, action, result-state, probability)*

**reward_file** contains tuple *(state, reward)*
