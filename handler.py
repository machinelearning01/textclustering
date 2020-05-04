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
from file_mgmt import write_excel
from flask import Flask, request, jsonify
import pandas as pd
app = Flask(__name__)

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
        "min_utterances_similarity": 0.2
    },
    "export_results_to_csv": True
}

def start(parameters):
    msg =""
    print("validating...")
    resp = validate(parameters)

    if type(resp) == str:
        print("alert:", resp)
        msg = {"status":400, "body":resp}
    else:
        print("initialised")
        print("executing...")
        intents = resp.execute()
        if parameters["export_results_to_csv"]:
            output_csv_filename = 'csv_output.csv'
            write_excel(intents, output_csv_filename)
            msg = {"status": 200, "body": "results are saved to csv file - " + output_csv_filename}
        else:
            msg = {"status": 200, "body": "completed successfully"}
    return msg


@app.route('/upload_excel', methods=['POST'])
def upload_file():
    # I used form data type which means there is a
    # "Content-Type: application/x-www-form-urlencoded"
    # header in my request
    raw_data = request.files['myfile']
    data_xls = pd.read_excel(raw_data)
    arr_data = data_xls["utterances"].tolist()

    if len(arr_data) >=1:
        params["excel_data"] = arr_data
        response = start(params)
        print(response)
        return jsonify(response)
    else:
        return jsonify({"status":400, "body":"excel file is empty"})


@app.route('/', methods=['GET'])
def home():
    return "<h1>Automatic Utterances Clustering for Chatbots</h1>"


if __name__ == '__main__':
    app.run(debug=True)

