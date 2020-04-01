from preprocessing import perform
from input_data import input_data
import identify_slots as i_s
import identify_synonyms as synant

replace_by_synonyms = {"queen": {"lady", "bird"}}
unimportant_words = ["policy"]

# Input data
excel_file_path=""
# or
# excel_file_path="./only_utterances.xlsx"
corpusx = input_data(excel_file_path)

def run(steps, utterances):
    corpus = []
    for utterance in utterances:
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
    return corpus

steps_1 = [
    "lowercase", # Lowercase
    "remove_url", # Remove urls
    "remove_email", # Remove email address
    "extract_only_text", # Extract only text (remove numbers and special characters)
    "remove_stopwords", # Remove stopwords
]

steps_2 = [
    "replace_by_synonyms", # Replace pre known synonyms by it's value
    "remove_unimportant_words", # Remove common words which may not help in clustering Ex: "policy" word is common in insurance or hr related utterances
    "lemmatize" # Identify and replace the base or dictionary form of a word
]
# 7. Create slots - collect synonyms and antonyms together.
# 8. Replace every word in the utterance by it's slot name

cleanup_data=run(steps_1, corpusx)
replace_by_synonyms = synant.get_synms_matching_utters(cleanup_data, replace_by_synonyms)
# print(replace_by_synonyms)
final_data=run(steps_2, cleanup_data)

sentences = []
for sentence in final_data:
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

# strong_relation_distance=2
# min_occurrences_of_neighbour_keys=3
# min_occurrences_of_keyword=3
# min_items_in_slot=3
idfy_slots=i_s.Identify_Slots(sentences, 1, 3, 2, 2)
lcr=idfy_slots.get_lcr()
print(uniqueVals(lcr))

idfy_slots=i_s.Identify_Slots(sentences, 1, 3, 2, 2)
crr=idfy_slots.get_crr()
print(uniqueVals(crr))

idfy_slots=i_s.Identify_Slots(sentences, 1, 3, 2, 2)
llc=idfy_slots.get_llc()
print(uniqueVals(llc))

