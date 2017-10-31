from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk import ConditionalFreqDist, pos_tag, tokenize
import nltk.data
from re import sub

def replaceCommon(text):
    token_text = pos_tag(word_tokenize(text))
    dist = ConditionalFreqDist((tag, word.lower()) for (word, tag) in token_text)

    # Move to another place
    # probably can get rid of the generator
    common_nouns = dist['NN'].most_common()
    common_verbs = dist['VBN'].most_common()
    print(common_verbs)
    ## Replacing action going on
    text = sub(common_nouns[0][0], 'dogbreeder', text, 88, re.I);
    text = sub(common_nouns[1][0], 'cat therapist', text, 88, re.I);
    return text


# Some authorship will be used for the humor bit
# The humor portion needs to be cheated a bit.
# We define reserve words that relate to DMX related things
# Some of the things on that list will be replaced with other things on a different list.
# This is part of the seed for a DMX timeline
reserve_nouns = ['rapper', 'rehab', 'cocaine']
replace_nouns = ['dog breeder', 'therapist', 'chew toy', 'glamour girl']

replace_verbs = ['arrested', '']
with open('test.txt', 'r') as ioFile:
    text = ioFile.read()
    print(replaceCommon(text))
