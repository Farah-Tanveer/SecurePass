import re
from modules import entropy

common_patterns = ['1234', 'abcd', 'password', 'qwerty', '1111']

def check_strength(password):
    score = 0
    feedback = []

    # Length checks
    if len(password) < 8:
        feedback.append("Password too short, use at least 8 characters.")
    else:
        score += 1
    if len(password) >= 16:
        score += 1

    # Character variety
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters for complexity.")
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters for complexity.")
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Add numbers for complexity.")
    if re.search(r'[^a-zA-Z0-9]', password):
        score += 1
    else:
        feedback.append("Add symbols (!@#$ etc.) for complexity.")

    # Common patterns penalty
    for pattern in common_patterns:
        if pattern in password.lower():
            score -= 2
            feedback.append(f"Avoid common patterns like '{pattern}'.")

    # Final classification
    if score <= 2:
        classification = 'Weak'
        feedback.append("Your password is weak.")
    elif score <= 4:
        classification = 'Medium'
        feedback.append("Your password is medium, can be stronger.")
    else:
        classification = 'Strong'
        feedback.append("Good! Your password is strong.")

    # Entropy calculation
    password_entropy = entropy.calculate_entropy(password)
    feedback.append(f"Entropy: {password_entropy} bits")

    return classification, feedback