# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tucil-3-KriptoKoding.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from flask import Flask, jsonify, request, send_file
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

app = Flask(__name__)
CORS(app)

@app.route('/api/data', methods=['POST'])
def get_data():
    data = request.json
    # key = data['q']
    key = data.get('q')
    print(key)

    publickKey, privateKey = writeKey(key)

    # print("public:", publickKey)
    # print("private:", privateKey)

    # message = {'message': 'Hello from Python server!'}
    message = {
        'key': key,
        'publicKey' : publickKey,
        'privateKey' : privateKey, 
        'message': 'Hello from Python server!'
    }
    return jsonify(message)

if __name__ == '__main__':
    app.run()