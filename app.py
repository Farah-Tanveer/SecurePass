from flask import Flask, render_template, request
from modules.strength import check_strength
from modules.common_check import is_common
from modules.entropy import calculate_entropy
from modules.hashing import generate_hashes

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
            # Use imported modules - avoid redundancy
            classification, feedback = check_strength(password)
            is_common_pwd = is_common(password)
            entropy_score = calculate_entropy(password)
            md5_hash, sha256_hash = generate_hashes(password)

            result = {
                "password_length": len(password),
                "strength": classification,
                "feedback": feedback,
                "is_common": is_common_pwd,
                "entropy": entropy_score,
                "md5": md5_hash,
                "sha256": sha256_hash
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