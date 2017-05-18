"""a simple implementation for the greedy Maximum Matching algorithm
"""

def max_matching(sentence, S):
    if not sentence:
        return list()
    for i in reversed(range(0, len(sentence)+1)):
        first_word = sentence[:i]
        remainder = sentence[i:]
        if first_word in S:
            return [first_word, max_matching(remainder, S)]
    first_word = sentence[0]
    remainder = sentence[1:]
    return [first_word, max_matching(remainder, S)]


if __name__ == '__main__':
    S = {'this', 'is', 'a', 'beautiful','day'}
    sentence = 'thisisabeautifulday'
    words = max_matching(sentence, S)
    print words
