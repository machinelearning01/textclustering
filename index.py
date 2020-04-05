from preprocessing import perform
from input_data import input_data
import identify_slots as i_s
import identify_synonyms as synant
import numpy as np

replace_by_custom_synonyms = {} # {"ruler": {"queen", "king"}, "worrier": {"soldier", "sainik"}}
replace_by_synonyms={}
replace_by_slotnames = {}
unimportant_words = []

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

steps_1 = [
    "lowercase", # Lowercase
    "remove_url", # Remove urls
    "remove_email", # Remove email address
    "extract_only_text", # Extract only text (remove numbers and special characters)
    "remove_stopwords", # Remove stopwords
    "remove_unimportant_words", # Remove common words which may not help in clustering Ex: "policy" word is common in insurance or hr related utterances
    "lemmatize", # Identify and replace the base or dictionary form of a word
    "replace_by_custom_synonyms", # Replace pre known synonyms by it's value
]


steps_2 = [
    "replace_by_slotnames", # Replace every word in the utterance by it's slot name
    "replace_by_synonyms"
]

cleanup_sentences=run(steps_1, corpusx)
print(cleanup_sentences)

# identify synonyms and antonyms
replace_by_synonyms = synant.identify_synonyms_matching_utters(cleanup_sentences)
print("replace_by_synonyms", replace_by_synonyms)

# identify possible slots
split_sentences = []
for sentence in cleanup_sentences:
    split_sentences.append(sentence.split())
idfy_slots=i_s.Identify_Slots(split_sentences, 1, 2, 2, 2)
identify_possible_slots = idfy_slots.possible_slots()
print("identify_possible_slots", identify_possible_slots)

# strong_relation_distance=2
# min_occurrences_of_neighbour_keys=3
# min_occurrences_of_keyword=3
# min_items_in_slot=3
# idfy_slots=i_s.Identify_Slots(split_sentences, 1, 2, 2, 2)
# lcr=idfy_slots.get_lcr()
# print(idfy_slots.uniqueVals(lcr))
#
# idfy_slots=i_s.Identify_Slots(split_sentences, 1, 2, 2, 2)
# crr=idfy_slots.get_crr()
# print(idfy_slots.uniqueVals(crr))
#
# idfy_slots=i_s.Identify_Slots(split_sentences, 1, 2, 2, 2)
# llc=idfy_slots.get_llc()
# print(idfy_slots.uniqueVals(llc))

# identify_possible_slots = idfy_slots.uniqueVals(lcr) + idfy_slots.uniqueVals(crr) + idfy_slots.uniqueVals(llc)
# print("identified_slots", identify_possible_slots)

# remove dictionary item whose values are duplicated

# remove the subsets and create dictionary
def remove_subsets(ips):
    for k, v in ips.items():
        for key, value in ips.items():
            if v != value:
                if set(v).issubset(set(value)):
                    del ips[k]
                    remove_subsets(ips)
    return ips
ips = remove_subsets(identify_possible_slots)
print(ips)

# final_data=run(steps_2, cleanup_sentences)




