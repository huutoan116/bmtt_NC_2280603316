from flask import Flask, render_template, request, jsonify
from cipher.caesar import CaesarCipher 

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/api/caesar/encrypt", methods=['POST'])
def caesar_encrypt():
    data = request.get_json()
    text = data.get('plain_text', '')
    key = int(data.get('key', 0))
    caesar = CaesarCipher()
    encrypted_text = caesar.encrypt_text(text, key)
    return jsonify({"encrypted_message": encrypted_text})

@app.route("/api/caesar/decrypt", methods=['POST'])
def caesar_decrypt():
    data = request.get_json()
    text = data.get('cipher_text', '')
    key = int(data.get('key', 0))
    caesar = CaesarCipher()
    decrypted_text = caesar.decrypt_text(text, key)
    return jsonify({"decrypted_message": decrypted_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
