import numpy as np


def forward_backward():
    """Hidden Markov models need to solve 3 fundamental problems:
1. For a given HMM model M and an observation sequence O, what is the likelihood of P(O|M);
2. For a given HMM model M and an observation sequence O, what is the best hidden state sequence Q(think of O as words, and Q as syntactic categories);
3. For an observation sequence O, and the set of hidden states, learn the HMM parameters A and B;

the forward_backward algorithm (aka Baum-Welch algorithm) gives an answer to the 3rd question: how to learn the parameters A and B of the model lambda given the observation sequence O and the set of hidden states. The forward_backward algorithm is a special case of the Expectation Maximization algorithm. It's an iterative algorithm. It starts with an estimate of the transitional probability matrix A and an emission probability matrix B, and derive better probability with the initial estimates going through iterations.

There are 2 intuitions behind the forward_backward algorithm: 1. iteratively estimate the counts; 2. compute the forward probability for an observation for the estimated probabilities, and divide the probability mass among all paths that contributed to this forward probability.

Backward probability beta: the probability of seeing the observations from time t+1 to the end, given state i at time t and model lambda
Beta_t_i = P(O_t+1, O_t+2...Ot|q_t =i, lambda)"""
