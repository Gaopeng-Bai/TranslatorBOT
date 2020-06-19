import flask
from flask import request, jsonify

from translator import translator

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Integration possibilities
integrations = [
    {'api': 'MS'},
    {'api': 'Google'},
    {'api': 'DeepL'}
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Technidoo Translation BOT</h1>
<p>(. | .)</p>'''


@app.route('/api/v1/', methods=['GET'])
def api_integrations():
    return jsonify(integrations)


@app.route('/api/v1/translate', methods=['GET'])
def api_translate():

    if 'text' in request.args:
        text =  request.args['text']
    else:
        return "Error: No text field provided. Please specify a text to translate."

    # Here we call the translation service
    results = [] 
    t = translator()
    results.append(t.translate_text(text))

    return jsonify(results)


app.run()