from flask import Flask, request, send_file
import cv2
import numpy as np
import os
from PIL import Image
from io import BytesIO

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
PROCESSED_FOLDER = "processed"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

def remove_background(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, alpha = cv2.threshold(gray, 248, 255, cv2.THRESH_BINARY_INV)
    b, g, r = cv2.split(image)
    rgba = [b, g, r, alpha]
    result = cv2.merge(rgba)

    output_path = os.path.join(PROCESSED_FOLDER, os.path.basename(image_path))
    cv2.imwrite(output_path, result)
    return output_path

@app.route('/')
def index():
    return "✅ Background Remover API is Live!"

@app.route('/remove_bg', methods=['POST'])
def remove():
    file = request.files['file']
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    output_path = remove_background(filepath)
    return send_file(output_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
