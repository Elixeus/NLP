#!coding:utf-8
"""The Maximum Entropy Markov Model (MEMM) is variant of the Maximum Entropy (multinomial logistic regression) classifier adapted to a sequence. It's a discriminative sequence model, meaning that it computes the posterior P(T|W) directly based on the previous tag and the observed word P(t_i|w_i, t_(i-1)), instead of computing the likelihood of the joint probability of P(T|W) P(W|T)P(T) and select the tag that maximize the P(T|W).
What makes the discriminative models more attractive for POS tagging task, besides the potential of having higher accuracy, is its relatively easiness to incorporate knowledge from other sources other than previous tag and observed words.
A basic MEMM POS tagger incorporates information about the observation word, neighbouring words, previous tags and various combinations with the following feature template:

<t_i, w_(i-2)>, <t_i, w_(i-1)>, <t_i, w_i>, <t_i, w_(i+1)>, <t_i, w_(i+2)>, <t_i, t_(i-1)>
<t_i, t_(i-2), t_(i-1)>
<t_i, t_(i-1), w_i>, <t_i, w_(i-1), w_i>, <t_i, w_i, w_(i+1)>

feature template will automatically populate the set of features

We can also use word shape features:
word that contains certain prefix/suffix; number; upper-case-letter; hyphen; all-upper-case;'s word shape; 's short word shape; upper case and has digit and dash (CFC-12); upper case and followed within 3 words by Co., Inc., etc.

T^ = argmax(P(T|W)) = argmax pi (exp(sum(w_i*f_i(t_i, w_(i+l,i-l), t(i-1, i-k))))/ sum(exp(sum(w_i*f_i*(t', w_(i+l, i-l), t_(i-1, i-k))))))
"""
def MEMM_decoding_viterbi(W, P):



