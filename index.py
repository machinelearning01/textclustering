"""
Text Clustering: BotClusters

Author: Jinraj K R <jinrajkr@gmail.com>
Created Date: 1-Apr-2020
Modified Date: 1-May-2020
===================================

This class constructor takes array of utterances and other required parameters,
> performs cleaning the utterances like given in the global variable ``steps``.
> identify synonyms and replace the words in the utterances by synonym name
> generates maximum number of clusters
and returns clustered utterances

``execute`` is the main method which initiates the execution
"""

from preprocessing import perform
from identify_slots import identify_possible_slots
import identify_synonyms as synant
from cosine_sim import Cosine_Sim

# class global variables

"""
```auto_generate_synonym_modes```
It has 3 different modes based on which it looks at the utterances for similar words to create slots.
The combination of 4 different parameter values makes a mode. The values in array of array represent that respectively below
- strong_relation_distance=1
- min_occurrences_of_neighbour_keys=2
- min_occurrences_of_keyword=2
- min_items_in_slot=3
"""
auto_generate_synonym_modes = {
    "strict": [[1, 3, 3, 4]],
    "moderate": [[1, 3, 2, 4]],
    "loose": [[1, 2, 2, 4]]
}

"""
```steps```
These are the steps executed in the order they are given
"""
steps = {
    "alphanumeric": [
        "lowercase",  # Lowercase
        "remove_url",  # Remove urls
        "remove_email",  # Remove email address
        "alphanumeric",  # Alphanumeric
    ],
    "extract_only_text": [
        "extract_only_text"  # Extract only text (remove numbers and special characters)
    ],
    "lemmatize": [
        "remove_stopwords",  # Remove stopwords
        "remove_unimportant_words",
        # Remove common words which may not help in clustering Ex: "policy" word is common in insurance or hr related utterances
        "lemmatize"  # Identify and replace the base or dictionary form of a word
    ],
    "replace_by_synonyms": [
        "replace_by_synonyms"
    ]
}

"""
```synonyms_generating_types```
These are the ways of generating the synonyms. Choose one as per your need.
> custom_synonyms - If you already have synonyms
> auto_generate_synonyms - Selecting this, the model looks for the pattern of words appearing 
in the utterances to find synonyms on its own
> apply_global_synonyms - If you want to search for related synonyms and antonyms of words in the utterances
and identify them as slots
"""
synonyms_generating_types = ["auto_generate_synonyms", "custom_synonyms", "apply_global_synonyms"]

class BotClusters:
    def __init__(self, botname, excel_data, synonyms_generating_type, custom_synonyms, auto_generate_synonyms_mode,
                 remove_unimportant_words, output_utterances_type, each_cluster_min_length,
                 max_utterances_similarity, min_utterances_similarity, lowest_similarity_limit):
        self.botname = botname
        self.excel_data = excel_data
        self.synonyms_generating_type = synonyms_generating_type
        self.replace_by_synonyms = custom_synonyms
        self.auto_generate_synonyms_mode = auto_generate_synonyms_mode
        self.remove_unimportant_words = remove_unimportant_words
        self.output_utterances_type = output_utterances_type
        self.each_cluster_min_length = each_cluster_min_length
        self.max_utterances_similarity = max_utterances_similarity
        self.min_utterances_similarity = min_utterances_similarity
        self.lowest_similarity_limit = lowest_similarity_limit
        self.app_dict = {}
        self.steps = steps

    def run(self, steps, utterances):
        corpus = []
        for utterance in utterances:
            for step in steps:
                params = ""
                if step == "replace_by_synonyms":
                    if self.synonyms_generating_type == synonyms_generating_types[0]:
                        # Replace every word in the utterance by it's slot name
                        params = self.identify_matching_words("identify_slots")
                    elif self.synonyms_generating_type == synonyms_generating_types[1]:
                        params = self.replace_by_synonyms
                    elif self.synonyms_generating_type == synonyms_generating_types[2]:
                        # Replace every word in the utterance by it's synonyms identified from the corpus
                        params = self.identify_matching_words("identify_synonyms_antonyms")
                elif step == "remove_unimportant_words":
                    params = self.remove_unimportant_words
                utterance = perform(step, utterance, params)
            corpus.append(utterance)
        return corpus

    def identify_matching_words(self, type):
        if type == "identify_synonyms_antonyms":
            return synant.identify_synonyms_matching_utters(self.app_dict["step_output"])
        elif type == "identify_slots":
            return identify_possible_slots(self.app_dict["step_output"], auto_generate_synonym_modes[self.auto_generate_synonyms_mode])

    def execute(self):
        self.app_dict["step_output"] = ""
        for key, value in self.steps.items():
            if self.app_dict["step_output"] == "":
                self.app_dict["step_output"] = self.excel_data
            self.app_dict["step_output"] = self.run(value, self.app_dict["step_output"])
            if key == self.output_utterances_type:
                # distinct_set = [val for val in set(self.app_dict["step_output"])]
                # duplicates = len(self.app_dict["step_output"]) - len(distinct_set)
                # if duplicates > 0:
                #     print("removed "+str(duplicates)+" duplicates")
                self.app_dict["output_sentences"] = self.app_dict["step_output"]
                # self.app_dict["step_output"] = distinct_set
                # print(key, self.app_dict["step_output"])

        print("total_utterances_" + str(len(self.app_dict["step_output"])))
        # print("params ", self.app_dict["step_output"], self.app_dict["output_sentences"])
        cc = Cosine_Sim()
        # slot_replaced_sentences, cleanup_sentences, min_length_clusters, max_similarity, min_similarity, others_limit=100
        intents = cc.clusters(self.app_dict["step_output"], self.app_dict["output_sentences"],
                              self.each_cluster_min_length, self.max_utterances_similarity,
                              self.min_utterances_similarity, self.lowest_similarity_limit)
        out_count = 0
        for ky, vl in intents.items():
            out_count = out_count + len(vl)
            print(ky, vl)

        print("removed "+str(len(self.excel_data) - out_count) + " duplicate utterances")
        self.finalise()
        return intents

    def finalise(self):
        self.app_dict.clear()
        self.steps.clear()
        self.excel_data.clear()





