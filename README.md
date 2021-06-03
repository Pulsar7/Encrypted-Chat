# Encrypted-Chat

A multithreading Chat, with 2 randomly generated private keys and one public key.
The Client-GUI Application runs a module called *tkinter*

# Encryption

With the Python-Modules cryptography and base64 the script is creating a private key:

    from cryptography.fernet import Fernet
    import base64,random,os
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

Algorithm => hashes.SHA256

Private-Key example: 

    lFxFsS00nrSv9PsW-_0tbWkh9LaHL-gVa4NHKNTxPKY=
    
Generated password example:

    dJG8TnMzJTZ6jxbZfaA9doXSsDI4Kz0TjBbpdthcv4YAUk0TCFJmJIzlT-tvYDkUdiVGHeuz8Mujc0KibFr6So6H1evISh2D68S9PjYGvwPVGdu3qA4Zx2aOZF4-Lu7Ns999465
