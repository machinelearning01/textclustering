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
        "auto_generate_synonyms_mode": "loose",
        "remove_unimportant_word": [],
        "output_utterances_type": "alphanumeric",
        "each_cluster_min_length": 10,
        "max_utterances_similarity": 0.4,
        "min_utterances_similarity": 0.1
        # "lowest_similarity_limit": 1
    }
}

def _main(params, return_type):
    print("validating...")
    resp = validate(params)

    if type(resp) == str:
        print("alert:", resp)
        return {"status":"400", "message": resp, "data":""}
    else:
        print("initialised")
        print("executing...")
        response_data = resp.execute(return_type)
        print("process completed!")
        return {"status":"200", "message": "sucessfully completed the process", "data":response_data}

# print("validating...")
# resp = validate(params)
#
# if type(resp) == str:
#     print("alert:", resp)
# else:
#     print("initialised")
#     print("executing...")
#     response_data = resp.execute("slots")
#     print("process completed!", response_data)