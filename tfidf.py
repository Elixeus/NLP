#!/usr/bin/env python

from collections import Counter
import numpy as np


def TFIDF(term, string, collection):
    '''
    hand-made tfidf calculator.

    parameters:
    -----------

    term: the term string
    string: the document string
    collection: the whole collection of documents'''
    tf = Counter(string.strip().split()).get(term, 0)
    idf = np.log10(1.0 * len(collection) / sum(term in i for i in collection))
    try:
        return tf * idf
    except TypeError:
        print 'Term not exist'
