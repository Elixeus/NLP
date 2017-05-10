import numpy as np


def forward(A, B, observ):
    """The difficulty lies in aligning the indices t and s. Note that the
first observation is 0, and the second observation is 1, etc. So in the inner fwd matrix calculation, we should take the value B[s][t-1] instead of B[s][t]"""
    T = len(observ)
    N = len(B)
    fwd = np.zeros((N+2, T+1))
    # initialize the first column
    for s in xrange(1, N+1):
        fwd[s, 1] = A[0, s] * B[s][observ[0]]
    for t in xrange(2, T+1):
        for s in xrange(1, N+1):
            fwd[s, t] = sum(fwd[s_p, t-1] * A[s_p, s] * B[s][observ[t-1]]
                           for s_p in xrange(1, N+1))
            # print 's: {}'.format(s)
            # print 't: {}'.format(t)
            # for s_p in xrange(1, N+1):
            #     print 'fwd[{}, {}]: {}'.format(s_p, t-1, fwd[s_p, t-1])
            #     print 'A[{}, {}]: {}'.format(s_p, s, A[s_p, s])
            #     print 'B[{}, {}]: {}'.format(s, observ[t-1], B[s][observ[t-1]])
            #     fwd[s, t] += fwd[s_p, t-1] * A[s_p, s] * B[s][observ[t-1]]
#                print 'fwd[{}, {}]: {}'.format(s, t, fwd[s, t])
    fwd[N+1, T] = sum(fwd[s, T] * A[s, -1] for s in xrange(1, N+1))
    print fwd
    return fwd[-1, T]

if __name__ == '__main__':
    # transitional probability matrix
    # A = np.matrix(((0, 0.8, 0.2, 0),
    #                (0, 0.6, 0.3, 0.1),
    #                (0, 0.4, 0.5, 0.1),
    #                (0, 0, 0, 0)))

    A = np.matrix(((0, 0.2, 0.8, 0),
                   (0, 0.5, 0.4, 0.1),
                   (0, 0.3, 0.6, 0.1),
                   (0, 0, 0, 0)))
    # hidden layer: state-to-observation probability
    # B = {1 : {1:0.2, 2:0.4, 3:0.4},
    #      2 : {1:0.5, 2:0.4, 3:0.1}}
    B = {2 : {1:0.2, 2:0.4, 3:0.4},
         1 : {1:0.5, 2:0.4, 3:0.1}}
    
    OBS1 = (3, 3, 1, 1, 2, 2, 3, 1, 3)
    OBS2 = (3, 3, 1, 1, 2, 3, 3, 1, 2)
    
    RESULT1 = forward(A, B, OBS1)
    RESULT2 = forward(A, B, OBS2)

#    OBS3 = (3, 1, 3)
#    RESULT3 = forward(A, B, OBS3)

#    OBS4 = (3,)
#    RESULT4 = forward(A, B, OBS4)
    
    print RESULT1
    print RESULT2
    def print_observation(obs):
        print 'the observation {} is more likely to happen.'.format(obs)
    if RESULT1 > RESULT2:
        print_observation(OBS1)
    else:
        print_observation(OBS2)
#    print RESULT3
#    print RESULT4
