from flask import Flask, request, jsonify, render_template
from ai_engine import generate_content   # import AI logic from separate file

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    """
    API endpoint called by the frontend.
    Takes user input -> sends to AI engine -> returns AI response.
    """

    data = request.get_json()
    user_text = data.get("text", "")

    print("User sent:", user_text)

    # AI content generation (clean + modular)
    ai_output = generate_content(user_text)

    return jsonify({"output": ai_output})


if __name__ == "__main__":
    app.run(debug=True)
