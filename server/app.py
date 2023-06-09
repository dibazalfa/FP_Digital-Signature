from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "hello world"

@app.route('/nama')
def nama():
    return "<h1>Nama</h1>" "<br>halaman nama"

@app.route('/nama/<string:nama>')
def getnama(nama):
    return "nama anda adalah {}".format(nama)

if __name__ == '__main__':
    app.run(debug=True)
