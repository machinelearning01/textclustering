
from preprocessing import perform
from input_data import input_data
from file_mgmt import write_excel
from identify_slots import identify_possible_slots
import identify_synonyms as synant
from cosine_sim import Cosine_Sim

synonyms_generating_types = {
    "auto_generate_synonyms": "auto_generate_synonyms",
    "upload_synonyms":"upload_synonyms",
    "apply_global_synonyms":"apply_global_synonyms"
}

output_utterances_type = {
    "alphanumeric": "alphanumeric",
    "extract_only_text": "extract_only_text"
}

auto_generate_synonym_modes = {
    "strict" : [[1,3,3,4], [2,3,3,4], [2,3,3,4]],
    "moderate" : [[1,3,2,4], [2,2,2,4], [2,2,2,4]],
    "loose" : [[1,2,2,4], [1,2,1,4], [1,2,1,4]]
}

steps = {
            "alphanumeric": [
                "lowercase", # Lowercase
                "remove_url", # Remove urls
                "remove_email", # Remove email address
                "alphanumeric", # Alphanumeric
                ],
            "extract_only_text": [
                "extract_only_text" # Extract only text (remove numbers and special characters)
                ],
            "lemmatize": [
                "remove_stopwords", # Remove stopwords
                "remove_unimportant_words", # Remove common words which may not help in clustering Ex: "policy" word is common in insurance or hr related utterances
                "lemmatize" # Identify and replace the base or dictionary form of a word
                ],
            "replace_by_synonyms": [
                "replace_by_synonyms"
                ]
        }

class BotClusters:
    def __init__(self, botname, excel_data, synonyms_generating_type, auto_generate_synonyms_mode,
                 remove_unimportant_word, output_alphanumeric_utterances, each_cluster_min_length,
                 max_utterances_similarity, min_utterances_similarity, lowest_similarity_limit):
        self.botname = botname
        self.excel_data = excel_data
        self.synonyms_generating_type = synonyms_generating_type
        self.replace_by_synonyms = {}
        self.auto_generate_synonyms_mode = auto_generate_synonyms_mode
        self.remove_unimportant_word = remove_unimportant_word
        self.output_utterances_type = output_alphanumeric_utterances
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
                    if self.synonyms_generating_type == "auto_generate_synonyms":
                        # Replace every word in the utterance by it's slot name
                        self.replace_by_synonyms = self.identify_matching_words("identify_slots")
                    elif self.synonyms_generating_type == "apply_global_synonyms":
                        # Replace every word in the utterance by it's synonyms identified from the corpus
                        self.replace_by_synonyms = self.identify_matching_words("identify_synonyms_antonyms")
                    params = self.replace_by_synonyms
                elif step == "remove_unimportant_words":
                    params = self.remove_unimportant_words

                utterance = perform(step, utterance, params)
            corpus.append(utterance)
        return corpus

    def identify_matching_words(self, type):
        if type == "identify_synonyms_antonyms":
            return synant.identify_synonyms_matching_utters(self.app_dict["cleanup_sentences"])
        elif type == "identify_slots":
            return identify_possible_slots(self.app_dict["cleanup_sentences"], self.auto_generate_synonyms_mode)

    def execute(self):
        self.app_dict["step_output"] = ""
        for key, value in self.steps.items():
            if self.app_dict["step_output"] == "":
                self.app_dict["step_output"] = self.excel_data
            self.app_dict["step_output"] = self.run(value, self.app_dict["step_output"])
            if key == self.output_utterances_type:
                self.app_dict["output_sentences"] = self.app_dict["step_output"]

        print("total_utterances_" + str(len(self.app_dict["step_output"])))

        cc = Cosine_Sim()
        # slot_replaced_sentences, cleanup_sentences, min_length_clusters, max_similarity, min_similarity, others_limit=100
        intents = cc.clusters(self.app_dict["step_output"], self.app_dict["output_sentences"],
                              self.each_cluster_min_length, self.max_utterances_similarity,
                              self.min_utterances_similarity, self.lowest_similarity_limit)
        # for ky, vl in intents.items():
        #     print(ky, vl)
        write_excel(intents, self.botname+'_output.csv')
        self.finalise()

    def finalise(self):
        self.app_dict.clear()
        self.steps.clear()
        self.excel_data.clear()

# # manually add if you have any
# replace_by_custom_synonyms = {} # {"ruler": {"queen", "king"}, "worrier": {"soldier", "sainik"}}
# remove_unimportant_words = []
#
# # do not modify this. these are global variables
# replace_by_synonyms = {}
# replace_by_slotnames = {}
#
# # strong_relation_distance=1
# # min_occurrences_of_neighbour_keys=2
# # min_occurrences_of_keyword=2
# # min_items_in_slot=3
# slots_config = [[1, 2, 2, 2]]
#
# # Input data
# excel_file_path=""
# # or
# # excel_file_path="./only_utterances.xlsx"
# corpusx = input_data(excel_file_path)


# print(corpusx)



