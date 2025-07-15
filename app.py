from flask import Flask, request, send_file
import cv2
import numpy as np
import os
from PIL import Image
from io import BytesIO

app = Flask(_name_)

UPLOAD_FOLDER = "uploads"
PROCESSED_FOLDER = "processed"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

def remove_background(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, alpha = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)
    b, g, r = cv2.split(image)
    rgba = [b, g, r, alpha]
    result = cv2.merge(rgba)
    output_path = os.path.join(PROCESSED_FOLDER, os.path.basename(image_path))
    cv2.imwrite(output_path, result)
    return output_path

@app.route('/')
def index():
    return "✅ Background Remover API is Live!"

@app.route('/remove', methods=['POST'])
def remove():
    if 'file' not in request.files:
        return {"error": "No file part"}, 400

    file = request.files['file']
    if file.filename == '':
        return {"error": "No selected file"}, 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    output_path = remove_background(filepath)

    return send_file(output_path, mimetype='image/png')

if _name_ == '_main_':
    app.run(debug=True, host="0.0.0.0")