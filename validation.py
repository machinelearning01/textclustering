"""
Text Clustering: validation

Author: Jinraj K R <jinrajkr@gmail.com>
Created Date: 1-Apr-2020
Modified Date: 1-May-2020
===================================

This function takes input paramters and validates
Returns a alert message if there is any invalid parameter
If the validation gets success, it creates an instance of BotClusters and returns the object

"""

from index import BotClusters, auto_generate_synonym_modes, synonyms_generating_types, steps

def validate(params):
    botname = ""
    excel_data = []
    synonyms_generating_type = synonyms_generating_types[0]
    custom_synonyms = {}
    auto_generate_synonyms_mode = "moderate"
    remove_unimportant_word = []
    output_utterances_type = "extract_only_text"
    each_cluster_min_length = 10
    max_utterances_similarity = 0.6
    min_utterances_similarity = 0.2
    lowest_similarity_limit = 1

    if "botname" in params:
        if (params["botname"]).strip()=="" or " " in (params["botname"]).strip():
            return "botname is alphanumeric with underscores. Must not contain any space. ex- pizza_bot_01"
        else:
            botname = params["botname"]
    else:
        return "botname is required"

    if "excel_data" in params:
        if len(params["excel_data"]) >= 10:
            excel_data = params["excel_data"]
        else:
            return "excel_data must contain atleast 10 utterances"
    else:
        return "excel_data is required"

    if "adv_settings" in params:
        if "synonyms_generating_type" in params["adv_settings"]:
            if params["adv_settings"]["synonyms_generating_type"] in synonyms_generating_types:
                synonyms_generating_type = params["adv_settings"]["synonyms_generating_type"]
                if synonyms_generating_type == synonyms_generating_types[1]:
                    if synonyms_generating_types[1] in params["adv_settings"]:
                        if type(params["adv_settings"][synonyms_generating_types[1]]) is dict:
                            if bool(params["adv_settings"][synonyms_generating_types[1]]):
                                custom_synonyms = params["adv_settings"][synonyms_generating_types[1]]
                            else:
                                return "custom_synonyms cannot be empty"
                        else:
                            return "custom_synonyms must be dictionary"
                    else:
                        return "custom_synonyms is required of synonyms_generating_type = custom_synonyms"
            else:
                return "synonyms_generating_type is not valid"

        if "auto_generate_synonyms_mode" in params["adv_settings"]:
            if params["adv_settings"]["auto_generate_synonyms_mode"] in auto_generate_synonym_modes.keys():
                auto_generate_synonyms_mode = params["adv_settings"]["auto_generate_synonyms_mode"]
            else:
                return "auto_generate_synonyms_mode is not valid"

        if "output_utterances_type" in params["adv_settings"]:
            if params["adv_settings"]["output_utterances_type"] in steps.keys():
                output_utterances_type = params["adv_settings"]["output_utterances_type"]
            else:
                return "output_utterances_type is not valid"

        if "remove_unimportant_word" in params["adv_settings"]:
            if isinstance(params["adv_settings"]["remove_unimportant_word"], list):
                remove_unimportant_word = params["adv_settings"]["remove_unimportant_word"]
            else:
                return "remove_unimportant_word must be an array"

        if "each_cluster_min_length" in params["adv_settings"]:
            if isinstance(params["adv_settings"]["each_cluster_min_length"], int):
                if params["adv_settings"]["each_cluster_min_length"] <= 1:
                    return "each_cluster_min_length must be >= 2"
                else:
                    each_cluster_min_length = params["adv_settings"]["each_cluster_min_length"]
            else:
                return "each_cluster_min_length must be an integer"

        if "max_utterances_similarity" in params["adv_settings"]:
            if isinstance(params["adv_settings"]["max_utterances_similarity"], float):
                if round(params["adv_settings"]["max_utterances_similarity"], 1) >= 0.2 and round(params["adv_settings"]["max_utterances_similarity"], 1) <= 1.0:
                    max_utterances_similarity = round(params["adv_settings"]["max_utterances_similarity"], 1)
                else:
                    return "0.2 >= max_utterances_similarity <= 1.0"
            else:
                return "max_utterances_similarity must be float"

        if "min_utterances_similarity" in params["adv_settings"]:
            if isinstance(params["adv_settings"]["min_utterances_similarity"], float):
                if round(params["adv_settings"]["min_utterances_similarity"], 1) < round(params["adv_settings"]["max_utterances_similarity"], 1):
                    if round(params["adv_settings"]["min_utterances_similarity"], 1) >= 0.1 and round(params["adv_settings"]["min_utterances_similarity"], 1) <= 0.9:
                        min_utterances_similarity = round(params["adv_settings"]["min_utterances_similarity"], 1)
                    else:
                        return "0.2 >= min_utterances_similarity <= 0.9"
                else:
                    return "min_utterances_similarity must be less than max_utterances_similarity"
            else:
                return "min_utterances_similarity must be float"

        if "lowest_similarity_limit" in params["adv_settings"]:
            if isinstance(params["adv_settings"]["lowest_similarity_limit"], int):
                if params["adv_settings"]["lowest_similarity_limit"] >= len(params["excel_data"]) and params["adv_settings"]["lowest_similarity_limit"] < params["adv_settings"]["each_cluster_min_length"]:
                    return "lowest_similarity_limit must be less than length of excel_data and greater than each_cluster_min_length"
                else:
                    lowest_similarity_limit = params["adv_settings"]["lowest_similarity_limit"]
            else:
                return "lowest_similarity_limit must be an integer"

    print(botname, "excel_data", synonyms_generating_type, custom_synonyms, auto_generate_synonyms_mode,
                     remove_unimportant_word, output_utterances_type, each_cluster_min_length,
                     max_utterances_similarity,
                     min_utterances_similarity, lowest_similarity_limit)
    return BotClusters(botname, excel_data, synonyms_generating_type, custom_synonyms, auto_generate_synonyms_mode,
                     remove_unimportant_word, output_utterances_type, each_cluster_min_length,
                     max_utterances_similarity,
                     min_utterances_similarity, lowest_similarity_limit)
