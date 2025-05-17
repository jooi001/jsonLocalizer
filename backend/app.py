from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from extractor import translate_source_file

app = Flask(__name__)
CORS(app)  # Enable CORS for Angular connection

@app.route('/translate', methods=['POST'])

def translate_endpoint():
    # Check if file was uploaded
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    
    file = request.files['file']
    
    # Check if file is JSON
    if not file.filename.endswith('.json'):
        return jsonify({"error": "Only JSON files are supported"}), 400
    
    # Save the uploaded file temporarily
    input_path = os.path.join('source', 'en.json')
    file.save(input_path)
    
    try:
        # Process the translation
        output_path = os.path.join('source', 'translations', 'translated.json')
        translate_json_file(input_path, output_path)
        
        # Return the translated file
        return send_file(output_path, as_attachment=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    os.makedirs(os.path.join('source', 'translations'), exist_ok=True)
    app.run(debug=True, host='0.0.0.0', port=5000)