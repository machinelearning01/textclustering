from validation import validate
from input_data import input_data

params = {
    "botname": "pizza_bot",
    "excel_data": input_data(""),
    "adv_settings":{
        "synonyms_generating_type": "custom_synonyms", # "upload_synonyms" OR "apply_global_synonyms"
        "custom_synonyms": {"system": ["windows", "mac", "ntid", "machine", "system"]},
        "auto_generate_synonyms_mode": "moderate",
        "remove_unimportant_word": ["abcd","wxyz"],
        "output_utterances_type": "alphanumeric",
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


