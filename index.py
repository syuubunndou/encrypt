from flask import Flask, request, jsonify
import hashlib
from cryptography.fernet import Fernet

app = Flask(__name__)

# 暗号化キーを生成 (実運用なら .env などで管理)
key = Fernet.generate_key()
cipher = Fernet(key)

@app.route('/', methods=['POST'])
def encrypt_data():
    try:
        data = request.get_json()
        key = data.get("key")

        
        if not uid or not create_at:
            return jsonify({"error": "Invalid data"}), 400
        
        # ハッシュ生成
        hashed = hashlib.sha256(key.encode()).hexdigest()
        
        # 暗号化
        encrypted_data = cipher.encrypt(hashed.encode()).decode()
        
        return jsonify({"encrypted_data": encrypted_data})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
