from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/reverse', methods=['POST'])
def reverse_string():
    string = request.json['string']
    reversed_string = string[::-1]
    return jsonify({'reversed_string': reversed_string})

