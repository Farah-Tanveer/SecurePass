def check_strength(password):
    if len(password) < 6:
        return 'Weak'
    elif any(c.isdigit() for c in password) and any(c.isupper() for c in password):
        return 'Strong'
    else:
        return 'Medium'