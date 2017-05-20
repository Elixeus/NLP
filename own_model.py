from nltk.corpus import treebank
from nltk.tag import tnt, CRFTagger


# split training data from test data
train_data = treebank.tagged_sents()[:3000]
test_data = treebank.tagged_sents()[3000:]

# train a trigram N tagger (TnT)
tnt_pos_tagger = tnt.TnT()
tnt_pos_tagger.train(train_data)
print tnt_pos_tagger.evaluate(test_data)

# train a CRF tagger
crf_tagger = CRFTagger()
crf_tagger.train(train_data,
                 '~/Documents/NLP/NLP/crf_model.txt')
print crf_tagger.evaluate(test_data)
