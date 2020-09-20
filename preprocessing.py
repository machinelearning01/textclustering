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

def replace_synonyms(sents, syns):
    res=[]
    for s in sents:
        for v, syn in syns.items():
            m=set(s.split(' ')).intersection(syn)
            if len(m)>=1:
                for i in syn:
                    s=(re.compile(r'\b'+i+r'\b')).sub(v,s)
        res.append(s)
    return res

def perform(action, sents, params):
    switcher = {
        "lowercase": lambda:[x.strip().lower() for x in sents],
        "remove_url": lambda: quick_replace(r'(https?ftp)\S+', sents),
        "remove_email": lambda: [' '.join(i for i in s.split() if '@' not in i) for s in sents],
        "alphanumeric": lambda: [' '.join(re.findall("[a-z0-9]+", s)) for s in sents],
        "extract_only_text": lambda: [' '.join(re.findall("[a-z]+", s)) for s in sents],
        "remove_stopwords": lambda: [' '.join([word for word in s.split() if word not in cachedStopWords]) for s in sents],
        "replace_by_synonyms": lambda: replace_synonyms(sents, params),
        "remove_unimportant_words": lambda: [' '.join([w for w in s.split() if w not in params]) for s in sents],
        "lemmatize": lambda: [' '.join([lemmatizer.lemmatize(word, "v") for word in s.split(" ")]) for s in sents]
    }
    return switcher.get(action, lambda: "invalid action")()

def quick_replace(regex, sents):
    w_pttrn = re.compile(regex)
    return [w_pttrn.sub('',s).strip() for s in sents]
