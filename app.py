from flask import Flask, request, send_file
from flask_cors import CORS
from rembg import remove
from PIL import Image
from io import BytesIO

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "✅ AI Background Remover is Live!"

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    file = request.files.get('image') or request.files.get('file')
    if not file:
        return "No file uploaded", 400

    input_image = Image.open(file.stream).convert("RGBA")
    output = remove(input_image)

    img_io = BytesIO()
    output.save(img_io, 'PNG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
