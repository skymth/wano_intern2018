# -*- coding: utf-8 -*-
from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
import os
import werkzeug
import base64
from datetime import datetime

app = Flask(__name__)
CORS(app)

MAX_JSON_CONTENT_LENGTH = 10
UPLOAD_DIR = os.getenv('./')

@app.route('/data/json/upload', methods=['POST'])
def upload_rest_json():
    print(request.headers)
    print(request.data)
    jsonData = request.json
    print(format(jsonData))
    jsonData = request.get_json(force=True)
    print(jsonData['flask_id'])
    fileName = jsonData.get("fileName")
    contentType = jsonData.get("content-Type")
    contentDataAscii = jsonData.get("contentData")

    contentData = base64.b64decode(contentDataAscii)

    contentDataSize = len(contentData)
    if MAX_JSON_CONTENT_LENGTH > 0:
        if MAX_JSON_CONTENT_LENGTH < contentDataSize:
            raise werkzeug.exceptions.RequestEntityTooLarge( \
                "json content length over : {0}".format(contentDataSize))

    saveFileName = datetime.now().strftime("%Y%m%d_%H%M%S_") \
        + werkzeug.utils.secure_filename(fileName)
    with open(os.path.join(UPLOAD_DIR, saveFileName), 'wb') as saveFile:
        saveFile.write(contentData)
    return make_response(jsonify({'result':'upload json OK.'}))

@app.errorhandler(werkzeug.exceptions.RequestEntityTooLarge)
def handle_over_max_file_size(error):
    print("werkzeug.exceptions.RequestEntityTooLarge")
    return 'result : file size is overed.'

# main
if __name__ == "__main__":
    print(app.url_map)
    app.run(host='127.0.0.1', port=3000)
