from flask import Flask
from flask import request
from flask import jsonify
from handler import _main

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_data():
    return "Utterances Clustering API is running..."


@app.route('/slots', methods=['POST'])
def get_slots():
    input_data = request.get_json()
    print(input_data)
    slots_data = _main(input_data, "slots")
    return jsonify(slots_data)


@app.route('/intents', methods=['POST'])
def get_intents():
    input_data = request.get_json()
    print(input_data)
    intent_data = _main(input_data, "intents")
    return jsonify(intent_data)


if __name__ == '__main__':
    app.run(debug=True)
