from flask import Flask, request, jsonify
import hashlib
from cryptography.fernet import Fernet
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/encrypt": {"origins": "*"}})  # 必要に応じてオリジンを指定

@app.route('/get_message', methods=['GET'])
def get_message():
    return jsonify({"message": "foo"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
