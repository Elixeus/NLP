import math
import re


class Bigram(object):
    """The Bigram class takes in a training set as input, and creates a
    bigram model which can be used to predict the probablity of new sentences.
    --------------------------
    Methods:
    1. train(self, input_file)
       return: void
       
    2. entropy(self, test_file)
       return: the entropy of the test file
       
    3. perplexity(self, test_file)"""

    def __init__(self):
        """Initialize a bigram class
        """
        self.counts = dict()
        self.context_counts = dict()
        self.model = dict()
        self.H = 0
        self.W = 0

    def train(self, training_file):
        """train the bigram model based on the data of the input file
        :param input_file: the file where the training data is stored.The only punctuation allowed in the file is period.
        :return: void
        """
        with open(training_file, 'r') as fh:
            for line in fh:
                words = line.split()
                words.append('</s>')
                words.insert(0, '<s>')
                for i in range(1, len(words)):
                    bigram = '{x} {y}'.format(x=words[i-1],
                                              y=words[i])
                    self.counts[bigram] = self.counts.get(bigram, 0) + 1
                    self.context_counts[words[i - 1]] = self.context_counts.get(words[i-1], 0) + 1
                    self.counts[words[i]] = self.counts.get(words[i], 0) + 1
                    self.context_counts[''] = self.context_counts.get('', 0) + 1

        for ngram, count in self.counts.iteritems():
            ngramls = ngram.split()
            ngramls.pop()
            context = ' '.join(ngramls)
            probability = (self.counts.get(ngram, 0) * 1.0) /\
                          self.context_counts.get(context, 0)
            self.model[ngram] = (probability, count)

    def get_model(self):
        """the get_model method returns the bigram model in a dictionary format
        :return: {word: probability}
        """
        model_copy = dict(zip(self.model.keys(),
                              map(lambda ls: ls[0],
                                  self.model.values())))
        return model_copy

    def get_counts(self):
        """the get_counts method returns the count for each bigram
        :return: 
        """
        model_count = dict(zip(self.model.keys(),
                               map(lambda ls: ls[1],
                                   self.model.values())))
        return model_count

    def test(self, test_file, lambda1=0.95, V=1000000):
        '''
        The test method evaluates the bigram model on the test data set, and updates the evaluation results
        :param test_file: the test data set file directory
               lambda1: the expected proportion of known words
        :return: void
        '''
        counts = self.get_counts()
        probs = self.get_model()
        with open(test_file, 'r') as fh:
            for line in fh:
                words = line.split()
                words.append('</s>')
                words.insert(0, '<s>')
                for i in range(1, len(words)):
                    count_w  = counts.get(words[i])
                    pat = re.compile('^{} \s.+'.format(words[i]))
                    unique_w = len([1 for x in counts.keys() if re.search(pat, x)]) # look for unique combos of
                    lambda2 = 1.0 - ((1.0 * unique_w) / (count_w + unique_w))
                    P1 = lambda1 * probs.get('{}'.format(words[i]), 0) + \
                         (1.0 - lambda1) / V
                    P2 = lambda2 * probs.get('{} {}'.format(words[i-1], words[i]),\
                                             0) + (1.0 - lambda2)*P1
                    self.H += -math.log(P2, 2)
                    self.W += 1

    @property
    def H(self):
        '''the perplexity method is a getter that returns the perplexity score of the bigram model
        :return: 
        '''
        return self.H

    def entropy(self):
        '''the entropy method is a getter that returns the entropy score of the bigram model
        :return: float
        '''
        return self.H/self.W