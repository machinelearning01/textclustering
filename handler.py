from validation import validate

params = {
    "botname": "pizza_bot",
    "excel_data":['queen IS Always referred to a godess visit@gmail.com',
               'queen is looking 20 year old like a godess',
               'reset my windows password __ test20thousand',
             'reset my mac password',
               'queen was once a queen young girl queen',
               'reset my windows password',
             'reset my mac password',
               'a stronger person can become king in any kingdom',
             'reset my system password',
             'reset my ntid',
               'a weeker person cannot become a king because he can be killed anytime',
             'reset my password',
             'reset my machine',
                'king can be killed anytime so we need make him strong',
               'our prince is as strong as rock'],
    "adv_settings":{
        "synonyms_generating_type": "auto_generate_synonyms", # "upload_synonyms" OR "apply_global_synonyms"
        "custom_synonyms": {},
        "auto_generate_synonyms_mode": "moderate",
        "remove_unimportant_word": ["abcd","wxyz"],
        "output_utterances_type": "alphanumeric",
        "each_cluster_min_length": 2,
        "max_utterances_similarity": 0.7,
        "min_utterances_similarity": 0.2,
        "lowest_similarity_limit": 0
    }
}

resp = validate(params)

if type(resp) == str:
    print("alert:", resp)
else:
    print("initialised")
    resp.execute()


# # Input data
# excel_file_path=""
# # or
# # excel_file_path="./only_utterances.xlsx"
# corpusx = input_data(excel_file_path)


# print(corpusx)