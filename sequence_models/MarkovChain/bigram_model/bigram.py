import sys

counts = dict()
context_counts = dict()

with open(sys.argv[1], 'r') as fh:
    for line in fh:
        words = line.split()
        words.append('</s>')
        words.insert(0, '<s>')
        for i in range(1, len(words)):
            bigram = '{x} {y}'.format(x=words[i-1],
                                      y=words[i])
            counts[bigram] = counts.get(bigram, 0) + 1
            context_counts[words[i-1]] = context_counts.get(words[i-1],
                                                            0) + 1
            counts[words[i]] = counts.get(words[i], 0) + 1
            context_counts[''] = context_counts.get('', 0) + 1
with open(sys.argv[2], 'w') as fh2:
    for ngram, count in counts.iteritems():
        ngramls = ngram.split()
        ngramls.pop()
        context = ' '.join(ngramls)
        probability = (counts.get(ngram, 0) * 1.0) /\
                      context_counts.get(context, 0)
        fh2.write('{ngram}: {probability}\n'.format(ngram=ngram,
                                                  probability=probability))
