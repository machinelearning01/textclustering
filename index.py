from preprocessing import perform
from input_data import input_data
import identify_slots as i_s

replace_by_synonyms = {"add": ["add", "signup"]}
unimportant_words = ["policy"]

# Input data
excel_file_path="./only_utterances.xlsx"
corpusx = input_data(excel_file_path)

steps = [
    "lowercase", # Lowercase
    "remove_url", # Remove urls
    "remove_email", # Remove email address
    "extract_only_text", # Extract only text (remove numbers and special characters)
    "remove_stopwords", # Remove stopwords
    "replace_by_synonyms", # Replace pre known synonyms by it's value
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
        params=""
        if step == "replace_by_synonyms":
            params = replace_by_synonyms
        elif step == "remove_unimportant_words":
            params = unimportant_words

        utterance = perform(step, utterance, params)
    corpus.append(utterance)
# print(corpus)

sentences = []
for sentence in corpus:
    sentences.append(sentence.split())
# print("sentences", sentences)

def uniqueVals(data):
    duplicateValues=list()
    uniqueValues=list()
    for x in data.values():
        if x not in uniqueValues:
            uniqueValues.append(x)
        # else:
        #     duplicateValues.append(x)
    return uniqueValues

idfy_slots=i_s.Identify_Slots(sentences, 1,2,4)
lcr=idfy_slots.get_lcr()
print(uniqueVals(lcr))

idfy_slots=i_s.Identify_Slots(sentences, 1,2,4)
crr=idfy_slots.get_crr()
print(uniqueVals(crr))

idfy_slots=i_s.Identify_Slots(sentences, 1,2,4)
llc=idfy_slots.get_llc()
print(uniqueVals(llc))

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
