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
    synonyms = params["synonyms"]
    for value, synonym in synonyms.items():
        match = set(utterance.split(" ")).intersection(synonym)
        if len(match) >= 1:
            for item in synonym:
                utterance = utterance.replace(item, value)
    return utterance

def perform(action, sentence, params):
    switcher = {
        "lowercase": lambda: sentence.lower(),
        "remove_url": lambda: re.sub(r'\b(?:(?:https?|ftp)://)?\w[\w-]*(?:\.[\w-]+)+\S*', '', sentence),
        "remove_email": lambda: re.sub(r'\S*@\S*\s?', '', sentence),
        "extract_only_text": lambda: " ".join(re.findall("[a-zA-Z]+", sentence)),
        "remove_stopwords": lambda: ' '.join([word for word in sentence.split() if word not in cachedStopWords]),
        "replace_by_synonyms": lambda: replace_synonyms(sentence, params),
        "remove_unimportant_words": lambda: remove_unimportant_words(sentence, params),
        "lemmatize": lambda: ' '.join([lemmatizer.lemmatize(word, "v") for word in sentence.split(" ")])
    }
    result = switcher.get(action, lambda: "invalid action")()
    return re.sub(' +', ' ', result)


