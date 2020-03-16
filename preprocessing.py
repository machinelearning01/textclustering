import re
import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
cachedStopWords = stopwords.words("english")
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
from nltk.corpus import wordnet

def remove_unimportant_words(utterance, unimportant_words):
    for word in utterance.split():
        if word in unimportant_words:
            utterance = utterance.replace(word, "")
    return utterance

def perform(action, sentence):
    switcher = {
        "lowercase": sentence.lower(),
        "remove_url": re.sub(r'\b(?:(?:https?|ftp)://)?\w[\w-]*(?:\.[\w-]+)+\S*', '', sentence),
        "remove_email": re.sub(r'\S*@\S*\s?', '', sentence),
        "extract_only_text": " ".join(re.findall("[a-zA-Z]+", sentence)),
        "remove_stopwords": ' '.join([word for word in sentence.split() if word not in cachedStopWords]),
        "lemmatize": ' '.join([lemmatizer.lemmatize(word, "v") for word in sentence.split(" ")])
    }
    result = switcher.get(action, None)
    return re.sub(' +', ' ', result)


