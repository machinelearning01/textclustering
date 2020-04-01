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

def get_synms_matching_utters(corpus):
    sentences=[]
    for sentence in corpus:
        sentences.append(sentence.split())

    allwords = np.concatenate(sentences)

    synss={}
    for word in set(allwords):
        if len(word)>2:
            syn, ant = get_syn_ant(word)
            syns = [x.lower() for x in np.concatenate([syn, ant])]
            match = set(syns).intersection(allwords)
            if len(match):
                synss[word]=match
    return synss