"""
Text Clustering: handler

Author: Jinraj K R <jinrajkr@gmail.com>
Created Date: 1-Apr-2020
Modified Date: 1-May-2020
===================================

Execution starts from here...
It takes the parameters as mentioned in the sample below and
returns the clusters and slots
if export_results_to_csv is set true, then save the results into excel file

"""

from validation import validate
from input_data import input_data


#Input parameters
params = {
    "botname": "pizza_bot",
    "excel_data": input_data(""),
    "adv_settings":{
        "synonyms_generating_type": "auto_generate_synonyms", # "auto_generate_synonyms" OR "custom_synonyms" OR "apply_global_synonyms"
        "custom_synonyms": {},
        "auto_generate_synonyms_mode": "moderate",
        "remove_unimportant_word": ["abcd","wxyz"],
        "output_utterances_type": "extract_only_text",
        "each_cluster_min_length": 2,
        "max_utterances_similarity": 0.4,
        "min_utterances_similarity": 0.2,
        "lowest_similarity_limit": 1
    },
    "export_results_to_csv": True
}

print("validating...")
resp = validate(params)

if type(resp) == str:
    print("alert:", resp)
else:
    print("initialised")
    print("executing...")
    intents = resp.execute()
    print("process completed!")
