from flask import Flask, request, jsonify, render_template
from langchain_logic import get_bot_response

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_query = data.get("message", "")
        print("🔍 Received:", user_query)
        response = get_bot_response(user_query)
        print("✅ Responding with:", response)
        return jsonify({"Response": response})
    except Exception as e:
        print("❌ Error:", e)
        return jsonify({"Response": "Server error"}), 500

if __name__ == "__main__":
    app.run(debug=True)
