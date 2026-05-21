from flask import Flask, render_template, request
import joblib
import re

app = Flask(__name__)

# Load model
model = joblib.load("phishing_model.pkl")


# Clean text
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return text


@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":

        email = request.form["email"]

        cleaned_email = clean_text(email)

        prediction = model.predict([cleaned_email])[0]

        if prediction == 1:
            result = "🚨 Phishing Email"
        else:
            result = "✅ Safe Email"

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)