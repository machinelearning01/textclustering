"""
Text Clustering: identify_synonyms

Author: Jinraj K R <jinrajkr@gmail.com>
Created Date: 1-Apr-2020
Modified Date: 1-May-2020
===================================

``get_syn_ant`` identifies the synonyms and antonyms for a given word
``identify_synonyms_matching_utters`` takes the array of utterances and identifies
the global synonyms and antonyms of collect the similar words to form slots
"""

from nltk.corpus import wordnet
import numpy as np

def get_syn_ant(word):
    synonyms=[]
    antonyms=[]
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
    return synonyms, antonyms

def identify_synonyms_matching_utters(corpus):
    sentences=[]
    for sentence in corpus:
        sentences.append(sentence.split())

    allwords = np.concatenate(sentences)

    synss={}
    unique_no=0
    for word in set(allwords):
        if len(word)>2:
            syn, ant = get_syn_ant(word)
            syns = [x.lower() for x in np.concatenate([syn, ant])]
            if len(syns) >= 2:
                match = list((set(syns)).intersection(allwords))
                if len(match) >= 2:
                    if match not in synss.values():
                        if word in synss:
                            synss[word+unique_no]=match
                            unique_no=unique_no+1
                        else:
                            synss[word]=match

    return synss