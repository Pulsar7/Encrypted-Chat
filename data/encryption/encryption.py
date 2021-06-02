from cryptography.fernet import Fernet

def create_key():
    key = Fernet.generate_key()
    print(key.decode())
    
