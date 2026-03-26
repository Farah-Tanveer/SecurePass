from flask import Flask, render_template, request
from modules import strength, entropy, hashing, common_check

app = Flask(__name__)

# Landing page
@app.route('/')
def home():
    return render_template('index.html')

# Analyzer page
@app.route('/analyzer', methods=['GET', 'POST'])
def analyzer():
    result = None   # important: not empty dict

    if request.method == 'POST':
        password = request.form['password']

        strength_val, feedback = strength.check_strength(password)

        result = {
            'strength': strength_val,
            'feedback': feedback,
            'entropy': entropy.calculate_entropy(password),
            'common': common_check.is_common(password),
            'md5': hashing.generate_hashes(password)[0],
            'sha256': hashing.generate_hashes(password)[1]
        }

    return render_template('analyzer.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)