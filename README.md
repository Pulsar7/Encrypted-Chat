# Encrypted-Chat

# Encryption

With the Python-Modules cryptography and base64 the script is creating a private key:

    from cryptography.fernet import Fernet
    import base64,random,os
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

The Algorithm = hashes.SHA256
Here is an example Private-Key: 
        
        lFxFsS00nrSv9PsW-_0tbWkh9LaHL-gVa4NHKNTxPKY=
