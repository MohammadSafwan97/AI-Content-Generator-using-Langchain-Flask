from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    user_text = data.get("text", "")

    print("Received from user:", user_text)   # shows in terminal

    # send response back to browser
    return jsonify({"output": user_text})

if __name__ == "__main__":
    app.run(debug=True)
