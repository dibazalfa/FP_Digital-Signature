from flask import Flask, jsonify, request
from flask_cors import CORS
# from flask.helpers import send_file
import os
import io
import json

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from Tanda_Tangan import *
from Pembangkitan_Kunci import *
from Baca_File import *
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

@app.route('/api/data', methods=['POST'])
def get_data():
    data = request.json
    # key = data['q']
    key = data.get('q')
    print(key)

    publickKey, privateKey = writeKey(key)
    message = {
        'key': key,
        'publicKey' : publickKey,
        'privateKey' : privateKey, 
        'message': 'Hello from Python server!'
    }
    return jsonify(message)

@app.route('/api/sign', methods=['POST'])
def sign_file():
    file = request.files['filename']
    privatekey = request.files['privatekey']

    if file.filename == "" or privatekey.filename == "":
        return jsonify({'error': 'File dan private key tidak boleh kosong!'})
    elif not file.filename.endswith(".pdf"):
        return jsonify({'error': 'File harus dalam format .pdf'})
    elif not privatekey.filename.endswith(".pri"):
        return jsonify({'error': 'Masukkan kunci private (dengan file .pri)'})

    signed_filename = secure_filename(file.filename)
    file.save(signed_filename)

    privatekey_filename = secure_filename(privatekey.filename)
    privatekey.save(privatekey_filename)

    signed_zip_filename = generateDigitalSigned(signed_filename, privatekey_filename)

    # Hapus file sementara setelah digunakan
    os.remove(signed_filename)
    os.remove(privatekey_filename)

    return jsonify({'message': 'File berhasil ditandatangani', 'signed_filename': signed_zip_filename})

# @app.route('/api/validation', methods=['POST'])
# def valid_sign():


if __name__ == '__main__':
    app.run()