import re

# Steps
# 1. Lowercase
# 2. Remove urls and email address etc...
# 3. Extract only text (remove numbers and special characters)
# 4. Remove stopwords
# 5. Remove common words which may not help in clustering
#    Ex: "policy" word is common in insurance or hr related utterances

# 6. Create slots - collect synonyms and antonyms together.
# 7. Replace every word in the utterance by it's slot name

import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
cachedStopWords = stopwords.words("english")
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
from nltk.corpus import wordnet

def synonyms_antonyms(word):
    synonyms = []
    antonyms = []
    hypernyms = ""
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
    return synonyms, antonyms


def perform(action, sentence):
    switcher = {
        "remove_url": re.sub(r'\b(?:(?:https?|ftp)://)?\w[\w-]*(?:\.[\w-]+)+\S*', '', sentence),
        "remove_email": re.sub(r'\S*@\S*\s?', '', sentence),
        "only_text": " ".join(re.findall("[a-zA-Z]+", sentence)),
        "remove_stopwords": ' '.join([word for word in sentence.split() if word not in cachedStopWords]),
        "lemmatize": ' '.join([lemmatizer.lemmatize(word, "v") for word in sentence.split(" ")])
    }
    return switcher.get(action, None)


utterance = "Hello 44535, my emailing added is jro9@allstate.com and my website is https://www.jinraj.com"
utterance = utterance.lower()
utterance = perform("remove_url",utterance)
utterance = perform("remove_email",utterance)
utterance = perform("only_text",utterance)
utterance = perform("lemmatize",utterance)
print(synonyms_antonyms("enrol"))
