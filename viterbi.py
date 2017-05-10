import numpy as np


def viterbi(A, B, observ):
    """Hidden Markov models need to solve 3 fundamental problems:
1. For a given HMM model M and an observation sequence O, what is the likelihood of P(O|M);
2. For a given HMM model M and an observation sequence O, what is the best hidden state sequence Q(think of O as words, and Q as syntactic categories);
3. For an observation sequence O, and the set of hidden states, learn the HMM parameters A and B;

The viterbi aims at solving the second problem: for a given model and observation sequence, find out the most likely hidden state sequence.

The viterbi algorithm is very similar to the forward algorithm, except that within the inner for loop, it looks for the maximum value of the trellis instead of the sum of all trellises. It also keeps track of the path.

There are different ways to keep track of the largest path. The one I use here looks for the argmax of each column, and keep the x and y args in a tuple, and append this tuple to a list
"""
    # initialization
    T = len(observ)
    N = len(B)
    backpointer = [(0, 0)]
    vtb = np.zeros((N+2, T+1))
    # viterbi algorithm
    for s in xrange(1, N+1):
        vtb[s, 1] = A[0, s] * B[s][observ[0]]
    for t in xrange(2, T+1):
        for s in xrange(1, N+1):
            vtb[s, t] = max(vtb[s_p, t-1] * A[s_p, s] * B[s][observ[t-1]]
                            for s_p in xrange(1, N+1))
    # find the argmax of each column and create a path
    pointers = [(vtb[:, i].argmax(), i) for i in xrange(1, T+1)]
    backpointer.extend(pointers)
    vtb[-1, T] = max(vtb[s, T]* A[s, -1] for s in xrange(1, N+1))
    print vtb
    return backpointer

if __name__ == '__main__':
    A = np.matrix(((0, 0.2, 0.8, 0),
                   (0, 0.5, 0.4, 0.1),
                   (0, 0.3, 0.6, 0.1),
                   (0, 0, 0, 0)))
    B = {2 : {1:0.2, 2:0.4, 3:0.4},
         1 : {1:0.5, 2:0.4, 3:0.1}}
    # OBS1 = (3, 3, 1, 1, 2, 2, 3, 1, 3)
    # OBS2 = (3, 3, 1, 1, 2, 3, 3, 1, 2)    
    # RESULT1 = viterbi(A, B, OBS1)
    # RESULT2 = viterbi(A, B, OBS2)
    # print RESULT1
    # print RESULT2
    OBS3 = (3, 1, 3)
    RESULT3 = viterbi(A, B, OBS3)
    print RESULT3
