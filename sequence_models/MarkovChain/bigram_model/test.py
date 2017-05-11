import sys
import math

lambda1 = 0.05
lambda2 = 0
V = 1000000
W = 0
H = 0

probs = {}

with open(sys.argv[1], 'r') as fh1:
    for line in fh1:
        ngram, value = line.split(': ')
        probs[ngram] = float(value)

with open(sys.argv[2], 'r') as fh2:
    for line in fh2:
        words = line.split()
        words.append('</s>')
        words.insert(0, '<s>')
        uniques = set()
        for i in range(1, len(words)):
            for key in probs.keys():
                if (' ' in key) & (words[i] in key):
                   uniques.add(key)
                   c_unique = len(uniques)
            P1 = (1.0*lambda1) * probs.get('{}'.format(words[i]), 0) +\
                 (1.0 - lambda1)/V
            P2 = (1.0*lambda2) * probs.get('{} {}'.format(words[i-1], words[i]), 0) + (1.0 - lambda2)*P1
            H += - math.log(P2, 2)
            W += 1
print 'entropy = {:.2f}'.format(H/W)
