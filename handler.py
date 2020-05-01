from validation import validate
from input_data import input_data

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
    }
}

print("validating...")
resp = validate(params)

if type(resp) == str:
    print("alert:", resp)
else:
    print("initialised")
    print("executing...")
    resp.execute()
    print("completed")


