from flask import Flask, jsonify, request
import json

app = Flask(__name__)

languages = [{'name' : 'JavaScript'}, {'name': 'Python'}, {'name':'Ruby'}]


@app.route('/', methods=['GET'])
def index():
    return jsonify({'message':'It works'})


@app.route('/lang', methods = ['GET'])
def getAll():
    return jsonify({'languages' : languages})


@app.route('/lang/<string:name>' , methods = ['GET'])
def getOne(name):
    langs = [language for language in languages if language["name"] == name]
    return jsonify({'language' : langs[0]})


@app.route('/postlang', methods=['POST'])
def addOne():

    data = request.get_json()

    for d in data:
        name = d['name']
        languages.append({"name":name})

    return jsonify({"languages" : languages})

@app.route('/lang/<string:name>', methods = ['PUT'])
def editOne(name):
    langs = [language for language in languages if language["name"] == name]
    langs[0]['name'] = request.json['name']

    return jsonify({"language":langs[0]})

@app.route('/lang/<string:name>', methods =['DELETE'])
def removeOne(name):
    langs = [language for language in languages if language["name"] == name]
    languages.remove(langs[0])

    return jsonify({'languages':languages})


if __name__ == '__main__':
    app.run(debug=True)