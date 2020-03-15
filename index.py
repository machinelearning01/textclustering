import re
import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
cachedStopWords = stopwords.words("english")
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
from nltk.corpus import wordnet

unimportant_words = ["drivewise", "milewise", "policy"]

def synonyms_n_antonyms(word):
    synonyms = []
    antonyms = []
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
    return synonyms, antonyms

synonyms = {"milewise": ["drivewise", "milewise", "drive-wise", "mile-wise", "dw", "mw"]}
def replace_synonyms(utterance, synonyms):
    for value, synonym in synonyms.items():
        for item in synonym:
            utterance = utterance.replace(item, value)
    return  utterance


def remove_unimportant_words(utterance):
    for word in utterance.split():
        if word in unimportant_words:
            utterance = utterance.replace(word, "")
    return utterance

def perform(action, sentence):
    switcher = {
        "remove_url": re.sub(r'\b(?:(?:https?|ftp)://)?\w[\w-]*(?:\.[\w-]+)+\S*', '', sentence),
        "remove_email": re.sub(r'\S*@\S*\s?', '', sentence),
        "only_text": " ".join(re.findall("[a-zA-Z]+", sentence)),
        "remove_stopwords": ' '.join([word for word in sentence.split() if word not in cachedStopWords]),
        "lemmatize": ' '.join([lemmatizer.lemmatize(word, "v") for word in sentence.split(" ")]),
        "remove_unimportant_words": remove_unimportant_words(utterance)
    }
    result = switcher.get(action, None)
    return re.sub(' +', ' ', result)

utterance = "what are the steps to moved a drivewise to a new vehicle from an old one?"
# Steps
# 1. Lowercase
utterance = utterance.lower()

# 2. Remove urls and email address etc...
utterance = perform("remove_url",utterance)
utterance = perform("remove_email",utterance)

# 3. Extract only text (remove numbers and special characters)
utterance = perform("only_text",utterance)

# 4. Remove stopwords
utterance = perform("remove_stopwords",utterance)

# 5. Remove common words which may not help in clustering
#    Ex: "policy" word is common in insurance or hr related utterances
utterance = perform("remove_unimportant_words", utterance)

# 6. Identify and replace the base or dictionary form of a word
utterance = perform("lemmatize", utterance)
print(utterance)

# 6. Create slots - collect synonyms and antonyms together.
# 7. Replace every word in the utterance by it's slot name

rs=[synonyms_n_antonyms(word) for word in utterance.split()]
print(rs)
