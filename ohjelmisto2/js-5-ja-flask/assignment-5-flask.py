from flask import Flask
import json

app = Flask(__name__)

@app.route("/translate/<word>")
def translate(word):
    with open("./js-5-ja-flask/dictionary.json", "r") as file:
        read_data = json.load(file)
        try:
            response = (f"Englanti: {word} Suomi: {read_data[word]}" )
            return response
        except KeyError:
           response = {"error": "Word not found"}
           return response


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, use_reloader=True)
