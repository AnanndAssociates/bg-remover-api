from flask import Flask, request, send_file
from flask_cors import CORS
from rembg import remove
from rembg.session_factory import new_session
from PIL import Image
from io import BytesIO

app = Flask(__name__)
CORS(app)

# 🔧 Session configuration for rembg
session = new_session(
    model_name='u2net_cloth_seg',  # other options: 'u2net', 'u2netp', 'silueta', etc.
    optimize=True,
    providers=["CPUExecutionProvider"],  # Use CPU if no GPU
)

@app.route('/')
def index():
    return "✅ AI Background Remover API is Live with Session!"

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    file = request.files.get('image') or request.files.get('file')
    if not file:
        return "❌ No image provided", 400

    input_image = Image.open(file.stream).convert("RGBA")
    output_image = remove(input_image, session=session)

    # Return as downloadable image
    byte_io = BytesIO()
    output_image.save(byte_io, format='PNG')
    byte_io.seek(0)

    return send_file(byte_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
