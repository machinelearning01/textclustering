
from preprocessing import perform
from input_data import input_data
from identify_slots import identify_possible_slots
import identify_synonyms as synant
import numpy as np
from cosine_sim import similar

# manually add if you have any
replace_by_custom_synonyms = {} # {"ruler": {"queen", "king"}, "worrier": {"soldier", "sainik"}}
unimportant_words = []

# do not modify this. these are global variables
replace_by_synonyms={}
replace_by_slotnames = {}

# strong_relation_distance=1
# min_occurrences_of_neighbour_keys=2
# min_occurrences_of_keyword=2
# min_items_in_slot=3
slots_config = [[1, 2, 2, 2]]

# Input data
excel_file_path=""
# or
# excel_file_path="./only_utterances.xlsx"
corpusx = input_data(excel_file_path)

def run(steps, utterances):
    corpus = []
    for utterance in utterances:
        for step in steps:
            params=""
            if step == "replace_by_synonyms":
                params = replace_by_synonyms
            elif step == "replace_by_custom_synonyms":
                step = "replace_by_synonyms"
                params = replace_by_custom_synonyms
            elif step == "replace_by_slotnames":
                step = "replace_by_synonyms"
                params = replace_by_slotnames
            elif step == "remove_unimportant_words":
                params = unimportant_words

            utterance = perform(step, utterance, params)
        corpus.append(utterance)
    return corpus

def identify_matching_words(type):
    if type == "identify_synonyms_antonyms":
        return synant.identify_synonyms_matching_utters(cleanup_sentences)
    elif type == "identify_slots":
        return identify_possible_slots(cleanup_sentences, slots_config)

steps_0 = [
    "lowercase", # Lowercase
    "remove_url", # Remove urls
    "remove_email", # Remove email address
    "extract_only_text" # Extract only text (remove numbers and special characters)
]

steps_1 = [
    "remove_stopwords", # Remove stopwords
    "remove_unimportant_words", # Remove common words which may not help in clustering Ex: "policy" word is common in insurance or hr related utterances
    "lemmatize", # Identify and replace the base or dictionary form of a word
    "replace_by_custom_synonyms", # Replace pre known synonyms by it's value
]

steps_2 = [
    "replace_by_slotnames" # Replace every word in the utterance by it's slot name
    # "replace_by_synonyms" # Replace every word in the utterance by it's synonyms identified from the corpus
]

# print(corpusx)
brushup_sentences=run(steps_0, corpusx)
cleanup_sentences=run(steps_1, brushup_sentences)
replace_by_slotnames = identify_matching_words("identify_slots")
print("replace_by_slotnames", replace_by_slotnames)
# replace_by_synonyms = identify_matching_words("identify_synonyms_antonyms")
# print("replace_by_synonyms", replace_by_synonyms)
replaced_sentences=run(steps_2, cleanup_sentences)
print(replaced_sentences)

def clusters(arr_sentences, min_length_clusters):
    similarity_matrix = similar(arr_sentences)
    # print(similarity_matrix)
    dct=[]
    clusts = {}
    clustCount=1
    otherSolos=[]
    for arr in similarity_matrix:
        temp=[]
        for i in range(len(arr)):
            if arr[i] >= 0.5:
                if arr_sentences[i] not in dct:
                    # print(arr_sentences[i] + "  ||  " + corpusx[i])
                    dct.append(arr_sentences[i])
                    temp.append(brushup_sentences[i])
        if len(temp) < min_length_clusters:
            otherSolos.extend(temp)
        elif len(temp) >= min_length_clusters:
            clusts["C"+str(clustCount)+"_"+str(len(temp))] = temp
            clustCount= clustCount + 1

    clusts["Others_"+str(len(otherSolos))]=otherSolos
    return clusts

intents = clusters(replaced_sentences, 2)
for ky,vl in intents.items():
    print(ky, vl)