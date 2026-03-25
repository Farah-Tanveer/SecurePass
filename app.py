from flask import Flask, render_template, request
from modules import strength, entropy, hashing, common_check

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = {}
    if request.method == 'POST':
        password = request.form['password']
        
        # Evaluate strength
        result['strength'] = strength.check_strength(password)
        
        # Calculate entropy
        result['entropy'] = entropy.calculate_entropy(password)
        
        # Check common passwords
        result['common'] = common_check.is_common(password)
        
        # Generate hashes
        result['md5'], result['sha256'] = hashing.generate_hashes(password)
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)