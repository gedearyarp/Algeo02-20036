from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# venv\Scripts\activate
# python api.py
@app.route('/compress', methods=['POST', 'GET'])
def compressImage():
    imageURL = request.get_json()
    imageBase64 = imageURL["data"]
    compressionRates = imageURL["rates"]
    return imageURL

if __name__ == '__main__':
    app.run(debug=True)
