from flask import Flask, render_template, request, jsonify
import numpy as np
import os
from model import image_pre, predict

app = Flask(__name__)
UPLOAD_FOLDER = '/app/uploads'
ALLOWED_EXTENSIONS = set(['png'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file1' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file1 = request.files['file1']
    if file1.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file1 and allowed_file(file1.filename):
        filename = 'input.png'  # Always save as input.png
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file1.save(path)
        try:
            data = image_pre(path)
            prediction = predict(data)
            result = 'COVID not detected' if prediction == 0 else 'COVID detected'
            return jsonify({'result': result}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'File type not allowed. Only PNG files are accepted.'}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
