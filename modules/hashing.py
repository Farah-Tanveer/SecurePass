import hashlib

def generate_hashes(password):
    md5_hash = hashlib.md5(password.encode()).hexdigest()
    sha256_hash = hashlib.sha256(password.encode()).hexdigest()
    return md5_hash, sha256_hash