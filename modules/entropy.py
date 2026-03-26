import math
import string
import re

common_patterns = ['1234', 'abcd', 'password', 'qwerty', '1111']

def calculate_entropy(password):
    # Character sets
    charset = 0
    if re.search(r'[a-z]', password):
        charset += 26
    if re.search(r'[A-Z]', password):
        charset += 26
    if re.search(r'[0-9]', password):
        charset += 10
    if re.search(r'[^a-zA-Z0-9]', password):
        charset += 32  # Approximation for symbols

    # Empty password case
    if charset == 0 or len(password) == 0:
        return 0

    # Shannon entropy formula
    entropy = len(password) * math.log2(charset)

    # Optional: penalize common patterns to lower effective entropy
    for pattern in common_patterns:
        if pattern in password.lower():
            entropy *= 0.8  # Reduce by 20% if common pattern found

    return round(entropy, 2)