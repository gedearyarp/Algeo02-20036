from flask import Flask, request

app = Flask(__name__)
# venv\Scripts\activate
# python api.py
@app.route('/compress', methods=['POST', 'GET'])
def compressImage():
    # imageURL = request.get_json()
    # print(imageURL)
    return "imageURL"

if __name__ == '__main__':
    app.run(debug=True)