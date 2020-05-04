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
3. Go to handler.py file, as he execution start from there
4. Verify and update the parameters as per your need
5. Save and run the application using the command
```python handler.py```


###### Input Parameters in handler.py
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
    }
}
```

1. botname - Give any alphanumeric+underscore name without space
2. excel_data - Pass your excel file path which contains only utterances
3. synonyms_generating_type - These are the ways of generating the synonyms. Choose one as per your need.
    - custom_synonyms - If you already have synonyms
    - auto_generate_synonyms - Selecting this, the model looks for the pattern of words appearing 
in the utterances to find synonyms on its own
    - apply_global_synonyms - If you want to search for related synonyms and antonyms of words in the utterances
and identify them as slots
4. custom_synonyms - This is required if you have selected "custom_synonyms" in synonyms_generating_type
else leave it blank. This take the dictionary format of input as below
    ```
    {
    "action":["add", "remove", "register", "signup", "cancel", "delete", "updated"],
    "fruits":["orange","apple","pineapple"]
    }
    ```

5. auto_generate_synonyms_mode - It has 3 different modes based on which it looks at the utterances 
for similar words to create slots. Choose one among the below - 
    - strict
    - moderate
    - loose
6. remove_unimportant_word - If you have already know there are some unwanted words 
in the utterances and you do not want them in the process of clustering then, 
you can list here. It will definitely help the model to cluster in better way.
You can also list the words which are common in every utterences.
7. output_utterances_type - 
    - alphanumeric : If your clustered output to be in alphanumeric
    - extract_only_text : If you want to filter all unncessary things and 
    just want only plain text in the clustered output
8. each_cluster_min_length - What is the minimum count you expect in a cluster
9. max_utterances_similarity - (0.9 >= value =< 0.2) - what percentage of similarity of
utterances you want to cluster. Greater the number, more cluster and 
less count of each cluster
10. min_utterances_similarity - (max_utterances_similarity > value =< 0.1)