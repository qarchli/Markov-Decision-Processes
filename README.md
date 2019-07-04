# Markov-Decision-Processes

This project implements some algorithms, such as **Value Iteration** and **Policy Iteration** for calculating the optimal policy of a given Markov Decision Process.

## Problem description

The problem we are trying to solve is a simple 2D grid world problem in which the agent starts off at the grid square (initial state) <i>(3 0)</i> and tries to move to other grid squares located elsewhere with the aim of reaching a terminal state <i>(3 1)</i> or <i>(3 2)</i> while maximizing its gains.

The agent is only allowed actions of moving in <i>up</i>, <i>down</i>, <i>left</i>, <i>right</i> directions by 1 grid square, with probabilities expressed in [transitions.csv](https://github.com/qarchli/Markov-Decision-Processes/blob/master/data/transitions.csv).

The cost of being in each state is shown in the figure below:

<p align="center">
  <img src="./gridworld.svg">
</p>


## Usage

`python main.py` or via the [notebook](https://github.com/qarchli/Markov-Decision-Processes/blob/master/Solving%20an%20mdp.ipynb)

## Data

**transition_file** contains tuple *(state, action, result-state, probability)*

**reward_file** contains tuple *(state, reward)*
