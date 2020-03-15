from nltk.corpus import wordnet

# rs=[synonyms_n_antonyms(word) for word in utterance.split()]
# print(rs)


def replace_synonyms(utterance, synonyms):
    for value, synonym in synonyms.items():
        for item in synonym:
            utterance = utterance.replace(item, value)
    return utterance


def synonyms_n_antonyms(word):
    synonyms = []
    antonyms = []
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
    return synonyms, antonyms