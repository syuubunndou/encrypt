from flask import Flask, request, jsonify
import hashlib
from cryptography.fernet import Fernet
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # CORSを有効化

# 暗号化キーを生成 (実運用なら .env などで管理)
key = Fernet.generate_key()
cipher = Fernet(key)

@app.route('/encrypt', methods=['POST'])
def encrypt_data():
    try:
        data = request.get_json()
        uid = data.get("UID");
        createAt = data.get("FIREBASE_CREATE_AT"); 

        
        if not uid or not createAt:
            return jsonify({"error": "Invalid data"}), 400
        
        # ハッシュ生成
        combined = f"{uid}{createAt}";
        hashed = hashlib.sha256(combined.encode()).hexdigest()
        
        # 暗号化
        encrypted_data = cipher.encrypt(hashed.encode()).decode()
        
        return jsonify({"encrypted_data": encrypted_data})
    
    except Exception as e:
        print(f"エラー発生: {e}")  # エラーメッセージを表示
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
