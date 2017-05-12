import numpy as np
import pandas as pd


def viterbi(A, B, observ):
    """Hidden Markov models need to solve 3 fundamental problems:
1. For a given HMM model M and an observation sequence O, what is the likelihood of P(O|M);
2. For a given HMM model M and an observation sequence O, what is the best hidden state sequence Q(think of O as words, and Q as syntactic categories);
3. For an observation sequence O, and the set of hidden states, learn the HMM parameters A and B;

The viterbi aims at solving the second problem: for a given model and observation sequence, find out the most likely hidden state sequence.

The viterbi algorithm is very similar to the forward algorithm, except that within the inner for loop, it looks for the maximum value of the trellis instead of the sum of all trellises. It also keeps track of the path.

There are different ways to keep track of the largest path. The one I use here looks for the argmax of each column, and keep the x and y args in a tuple, and append this tuple to a list
----------------------------
params:
A: the transition probability matrix; probability to change from one syntactic category to the next
A type: pandas dataframe

B: the emission probability matrix; probability to emit a symbol given a syntactic category
B type: pandas dataframe

observ: the observed sequence of words
observ type: tuple of strings"""
    # initialization
    T = len(observ)
    N = B.shape[0]
    backpointer = [(0, 0)]
    vtb = pd.DataFrame(np.zeros((N+2, T+1)),
                       columns=('start',)+observ,
                       index=('start',)+tuple(B.index)+('end',))
    print vtb
    # viterbi algorithm
    for s in vtb.index[1:-1]:
        vtb.loc[s, observ[0]] = A.loc['start', s] * B.loc[s, observ[0]]
    for t in xrange(2, T+1):
        for s in xrange(1, N+1):
            vtb.iloc[s, t] = max(vtb.iloc[s_p, t-1] * A.iloc[s_p, s] * B.iloc[s-1, t-1]
                            for s_p in xrange(1, N+1))
    # find the argmax of each column and create a path
    pointers = [(vtb.loc[:, i].argmax(), i) for i in observ]
    backpointer.extend(pointers)
    vtb.iloc[-1, T] = max(vtb.iloc[s, T]* A.iloc[s, -1] for s in xrange(1, N+1))
    print vtb
    return backpointer

if __name__ == '__main__':
    # A = np.matrix(((0, 0.2, 0.8, 0),
    #                (0, 0.5, 0.4, 0.1),
    #                (0, 0.3, 0.6, 0.1),
    #                (0, 0, 0, 0)))
    # B = {2 : {1:0.2, 2:0.4, 3:0.4},
    #      1 : {1:0.5, 2:0.4, 3:0.1}}
    A_matrix = np.matrix(((0, 0.2767, 0.0006, 0.0031, 0.0453, 0.0449, 0.0510, 0.2026),
                          (0, 0.3777, 0.0110, 0.0009, 0.0084, 0.0584, 0.0090, 0.0025),
                          (0, 0.0008, 0.0002, 0.7968, 0.0005, 0.0008, 0.1698, 0.0041),
                          (0, 0.0322, 0.0005, 0.0050, 0.0837, 0.0615, 0.0514, 0.2231),
                          (0, 0.0366, 0.0004, 0.0001, 0.0733, 0.4509, 0.0036, 0.0036),
                          (0, 0.0096, 0.0176, 0.0014, 0.0086, 0.1216, 0.0177, 0.0068),
                          (0, 0.0068, 0.0102, 0.1011, 0.1012, 0.0120, 0.0728, 0.0479),
                          (0, 0.1147, 0.0021, 0.0002, 0.2157, 0.4744, 0.0102, 0.0017))
                        )
    A = pd.DataFrame(A_matrix,
                     columns=('start','NNP', 'MD', 'VB', 'JJ',
                              'NN', 'RB', 'DT'),
                     index=('start', 'NNP', 'MD', 'VB', 'JJ',
                            'NN', 'RB', 'DT'))
    B_matrix = {'NNP': {'Janet': 0.000032, 'will': 0, 'back': 0,
                 'the': 0.000048, 'bill': 0},
                'MD': {'Janet': 0, 'will': 0.308431, 'back': 0,
                'the': 0, 'bill': 0},
                'VB': {'Janet': 0, 'will': 0.000028, 'back': 0.000672,
                'the':0, 'bill':0.000028},
                'JJ': {'Janet': 0, 'will': 0, 'back': 0.000340,
                'the': 0.000097, 'bill': 0},
                'NN': {'Janet': 0, 'will': 0.0002, 'back': 0.000223,
                'the': 0.000006, 'bill': 0.002337},
                'RB': {'Janet': 0, 'will': 0, 'back': 0.010446,
                'the': 0, 'bill': 0},
                'DT': {'Janet': 0, 'will': 0, 'back': 0,
                'the': 0.506099, 'bill': 0}
        }
    B = pd.DataFrame(B_matrix).T.reindex(A.index[1:],
                                         columns=['Janet', 'will', 'back',
                                                  'the', 'bill'])
    # OBS1 = (3, 3, 1, 1, 2, 2, 3, 1, 3)
    # OBS2 = (3, 3, 1, 1, 2, 3, 3, 1, 2)
    # RESULT1 = viterbi(A, B, OBS1)
    # RESULT2 = viterbi(A, B, OBS2)
    # print RESULT1
    # print RESULT2
    #OBS3 = (3, 1, 3)
    #RESULT3 = viterbi(A, B, OBS3)
    #print RESULT3
    OBS4 = ('Janet', 'will', 'back', 'the', 'bill')
    RESULT4 = viterbi(A, B, OBS4)
    print RESULT4
