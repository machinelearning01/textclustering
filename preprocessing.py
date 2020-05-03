"""
Text Clustering: preprocessing

Author: Jinraj K R <jinrajkr@gmail.com>
Created Date: 1-Apr-2020
Modified Date: 1-May-2020
===================================

``perform`` is the key performer of the application
It takes each utterance and performs the action asked to perform

"""

import re
import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
cachedStopWords = stopwords.words("english")
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

def remove_unimportant_words(utterance, unimportant_words):
    for word in utterance.split():
        if word in unimportant_words:
            utterance = utterance.replace(word, "")
    return utterance

def replace_synonyms(utterance, params):
    synonyms = params
    # print("replace_synonyms", utterance, synonyms)
    for value, synonym in synonyms.items():
        match = set(utterance.split(" ")).intersection(synonym)
        if len(match) >= 1:
            for item in synonym:
                rjx = re.compile(r'\b' + item + r'\b')
                utterance = re.sub(rjx, value, utterance)
    return utterance

def perform(action, sentence, params):
    switcher = {
        "lowercase": lambda: sentence.lower(),
        "remove_url": lambda: re.sub(r'\b(?:(?:https?|ftp)://)?\w[\w-]*(?:\.[\w-]+)+\S*', '', sentence),
        "remove_email": lambda: re.sub(r'\S*@\S*\s?', '', sentence),
        "alphanumeric": lambda: " ".join(re.findall("[a-zA-Z0-9]+", sentence)),
        "extract_only_text": lambda: " ".join(re.findall("[a-zA-Z]+", sentence)),
        "remove_stopwords": lambda: ' '.join([word for word in sentence.split() if word not in cachedStopWords]),
        "replace_by_synonyms": lambda: replace_synonyms(sentence, params),
        "remove_unimportant_words": lambda: remove_unimportant_words(sentence, params),
        "lemmatize": lambda: ' '.join([lemmatizer.lemmatize(word, "v") for word in sentence.split(" ")])
    }
    result = switcher.get(action, lambda: "invalid action")()
    # print("performing ["+action+"] => ", sentence, " || ",  result)
    return re.sub(' +', ' ', result.strip())


