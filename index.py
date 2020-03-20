from preprocessing import perform, remove_unimportant_words
from synonyms import synonyms_n_antonyms
from input_data import input_data
from word2vec1 import word2vec
from operator import itemgetter

replace_by_synonyms = {"milewise": ["drivewise", "milewise", "drive-wise", "mile-wise", "dw", "mw"]}
unimportant_words = []

# Input data
corpusx = input_data()

steps = [
    "lowercase", # Lowercase
    "remove_url", # Remove urls
    "remove_email", # Remove email address
    "extract_only_text", # Extract only text (remove numbers and special characters)
    "remove_stopwords", # Remove stopwords
    "remove_unimportant_words", # Remove common words which may not help in clustering Ex: "policy" word is common in insurance or hr related utterances
    "lemmatize" # Identify and replace the base or dictionary form of a word
]
# 7. Create slots - collect synonyms and antonyms together.
# 8. Replace every word in the utterance by it's slot name


corpus = []
for utterance in corpusx:
    # print("input utterance -", utterance)
    for step in steps:
        # print("performing step -", step)
        if step == "remove_unimportant_words":
            utterance = remove_unimportant_words(utterance, unimportant_words)
        else:
            utterance = perform(step, utterance)
    corpus.append(utterance)
    # print("output utterance -", utterance)

# print(corpus)

sentences = []
for sentence in corpus:
    sentences.append(sentence.split())

words = []
for text in corpus:
    for word in text.split(' '):
        words.append(word)

unique_words = set(words)
# print("unique_words", unique_words)
print("sentences", sentences)


def get_lcr(sentences):
    lcr=[]
    for sentence in sentences:
        for i in range(len(sentence)):
            left = "" if i == 0 else sentence[i - 1]
            center = sentence[i]
            right = "" if i == len(sentence)-1 else sentence[i + 1]

            if left!="" and right!="":
                # print(left + ", " + right, " -> "+center)
                lcr.append([left+", "+right+" (C)", center])
    return lcr

def get_crr(sentences):
    crr=[]
    for sentence in sentences:
        for i in range(len(sentence)-2):
            center = sentence[i]
            right1 = "" if i == len(sentence)-1 else sentence[i + 1]
            right2 = "" if i == len(sentence)-2 else sentence[i + 2]

            if right1!="" and right2!="":
                crr.append([right1 + ", " + right2+" (R)", center])
    return crr

def get_llc(sentences):
    llc=[]
    for sentence in sentences:
        for i in range(2, len(sentence)):
            left1 = sentence[i - 2]
            left2 = sentence[i - 1]
            center = sentence[i]

            arr=[]
            if left1!="" and left2!="":
                llc.append([left1 + ", " + left2+" (L)", center])
    return llc


def get_likely_slots(arr):
    res = sorted(arr, key=itemgetter(0))

    dist_list = set(map(tuple, res))
    key_list=[]
    for item in dist_list:
        key_list.append(item[0])

    dist_key_list = set(key_list)
    # print(dist_key_list)

    likely_slots={}
    for key_item in dist_key_list:
        arr_res = [itm[1] for itm in dist_list if itm[0] == key_item]
        if len(arr_res) >= 2:
            likely_slots[key_item] = arr_res

    return likely_slots


lcr = get_lcr(sentences)
crr = get_crr(sentences)
llc = get_llc(sentences)

print(get_likely_slots(lcr))
print(get_likely_slots(crr))
print(get_likely_slots(llc))



########################################
# words = []
# for text in corpus:
#     for word in text.split(' '):
#         words.append(word)
#
# words = set(words)
#
# word2int = {}
#
# for i, word in enumerate(words):
#     word2int[word] = i
#
# sentences = []
# for sentence in corpus:
#     sentences.append(sentence.split())
#
# WINDOW_SIZE = 2
#
# data = []
# for sentence in sentences:
#     for idx, word in enumerate(sentence):
#         for neighbor in sentence[max(idx - WINDOW_SIZE, 0): min(idx + WINDOW_SIZE, len(sentence)) + 1]:
#             if neighbor != word:
#                 data.append([word, neighbor])
#
# import pandas as pd
# df = pd.DataFrame(data, columns = ['input', 'label'])
# print(df)
# print(word2int)
