from flask import Flask, render_template, request

app = Flask(__name__)


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Analyzer Page
@app.route("/analyzer", methods=["GET", "POST"])
def analyzer():

    result = None

    if request.method == "POST":

        password = request.form.get("password")

        if password:

            length = len(password)

            if length >= 12:
                strength = "Strong 🔒"
            elif length >= 8:
                strength = "Medium ⚠️"
            else:
                strength = "Weak ❌"

            result = {
                "length": length,
                "strength": strength
            }

    return render_template(
        "analyzer.html",
        result=result
    )


# About Page
@app.route("/about")
def about():
    return render_template("about.html")


# Contact Page
@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)