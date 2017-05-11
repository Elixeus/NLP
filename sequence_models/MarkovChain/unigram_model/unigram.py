import sys

counts = {}
total_count = 0

# read in the files
TRAINING = open(sys.argv[1], 'r')

# process the data
for line in TRAINING:
    words = line.split()
    words.append('</s>')
    for word in words:
        counts[word] = counts.get(word, 0) + 1
        total_count += 1
TRAINING.close()

MODEL = open(sys.argv[2], 'w')
for word, count in counts.items():
    probability = (counts[word]*1.0)/total_count
    out_string = '{word}:{probability}\n'.format(word=word,
                                                 probability=probability)
    MODEL.write(out_string)
MODEL.close()
