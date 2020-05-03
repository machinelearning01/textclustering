# Automatic Utterances Clustering for Chatbots

*A python model which automatically clean up the utterances, 
generate the possible slots and clusters. Later, 
it will be easy to look and merge the clusters together 
to form as many intents as you need.*

Assuming you have 10,000 utterances and to perform below operations 
would definitely takes a lot of time 
- **Cleaning up the utterances** - This includes removing unwanted utterances, email ids, numerics and special characters
- **Create Intents** - Analyse the utterances and start clustering the related utterances together to form intents
- **Identify Possible Slots** - Identify related words in the utterances to form slots/entities

So just run this algorithm to ease your work 
(there will be certain amount of effort you need
to put from your end to finish your work).

### So, how to use/run this code?
1. Download or clone the master branch
2. ```$ pip install -r requirements.txt -t . ```
(This installs all the python package 
dependencies required to run this code)
3. Run the application using the below command


###### Input Parameters
```JSON format
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
        "min_utterances_similarity": 0.2
    },
    "export_results_to_csv": False
}
```