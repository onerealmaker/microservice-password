from flask import Flask, request, jsonify
import string, random, os

app = Flask(__name__)

# --- Configuration: set a safe max length via env var or default ---
MAX_LENGTH = int(os.environ.get("MAX_PASSWORD_LENGTH", "64"))
MIN_LENGTH = 4

@app.route("/password", methods=["GET"])
def password():
    try:
        length = int(request.args.get("length", 12))
    except:
        return jsonify({"error":"invalid length"}), 400

    if length < MIN_LENGTH or length > MAX_LENGTH:
        return jsonify({"error": f"length must be between {MIN_LENGTH} and {MAX_LENGTH}"}), 400

    chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{};:,.<>/?"
    pwd = ''.join(random.SystemRandom().choice(chars) for _ in range(length))
    return jsonify({"password": pwd, "length": length})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
