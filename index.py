from preprocessing import perform, remove_unimportant_words
from input_data import input_data
from identify_slots import possible_slots

replace_by_synonyms = {"add": ["add", "signup"]}
unimportant_words = ["policy"]

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
# print("sentences", sentences)


poss_slots = possible_slots(sentences)
print(poss_slots)


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
