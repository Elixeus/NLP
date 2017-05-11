from bigram import Bigram
import os
import re

if __name__ == '__main__':
    bg = Bigram()
    bg.train(os.path.abspath('../darksouls_training.txt'))
    print 'model trained'
    # for key, item in bg.get_model().iteritems():
    #     print key, item
    bg.test('../darksouls_test.txt')
    print 'The entropy for the test set is: {:.2f}.'.format(bg.entropy)
    print 'The perplexity for the test set is: {:.2f}.'.format(bg.perplexity)