"""
Common password detection module.
Checks passwords against a list of commonly used weak passwords.
"""

# Expanded list of common passwords (top 100+ weak passwords)
common_passwords = [
    '123456', 'password', 'qwerty', 'abc123', '111111',
    '123123', '1234567', '12345678', '123456789', '1234567890',
    'password123', 'admin', 'letmein', 'welcome', 'monkey',
    '1q2w3e4r', 'dragon', 'master', 'sunshine', 'princess',
    'shadow', 'michael', 'superman', 'batman', 'trustno1',
    'login', 'qwert', '000000', '666666', '888888',
    'iloveyou', 'starwars', 'passpass', 'pass123', 'admin123',
    'root', 'toor', 'pass', 'pass1234', 'password1',
]


def is_common(password):
    """
    Check if password is in the list of common weak passwords.
    
    Args:
        password (str): The password to check
        
    Returns:
        bool: True if password is common, False otherwise
    """
    return password.lower() in [p.lower() for p in common_passwords]


def get_common_password_count():
    """Get the number of monitored common passwords."""
    return len(common_passwords)