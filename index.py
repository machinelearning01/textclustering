from preprocessing import perform, remove_unimportant_words
from synonyms import synonyms_n_antonyms

synonyms = {"milewise": ["drivewise", "milewise", "drive-wise", "mile-wise", "dw", "mw"]}
unimportant_words = ["drivewise", "milewise", "policy"]

utterance = "what are the steps to moved a drivewise to a new vehicle from an old one?"

steps=[
    "lowercase", # Lowercase
    "remove_url", # Remove urls
    "remove_email", # Remove email address
    "extract_only_text", # Extract only text (remove numbers and special characters)
    "remove_stopwords", # Remove stopwords
    "remove_unimportant_words", # Remove common words which may not help in clustering Ex: "policy" word is common in insurance or hr related utterances
    "lemmatize" # Identify and replace the base or dictionary form of a word
]

print("input utterance -", utterance)
for step in steps:
    print("performing step -", step)
    if step == "remove_unimportant_words":
        utterance = remove_unimportant_words(utterance, unimportant_words)
    else:
        utterance = perform(step, utterance)
print("output utterance -", utterance)

# 7. Create slots - collect synonyms and antonyms together.
# 8. Replace every word in the utterance by it's slot name

# rs=[synonyms_n_antonyms(word) for word in utterance.split()]
# print(rs)
