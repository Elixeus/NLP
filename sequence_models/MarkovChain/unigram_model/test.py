import sys
import math
from load import load_model

lambda1 = 0.95
lambda_unk = 1 - lambda1
V = 1000000.0
W = 0.0
H = 0.0
unk = 0

model = load_model(sys.argv[1])
# test the model
with open('test.txt', 'r') as test_file:
    for line in test_file:
        words = line.split()
        words.append('</s>')
        for word in words:
            W += 1
            P = lambda_unk / V
            if model.get(word):
                P += lambda1 * model[word]
            else:
                unk += 1
            H += -(math.log(P, 2))
print 'entropy = {}'.format(H/W)
print 'coverage = {}'.format((W - unk)/W)
