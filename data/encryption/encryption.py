from cryptography.fernet import Fernet
import base64,random,os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def create_private_key():
    nummer = random.randint(9999,999999)
    random_string = Fernet.generate_key().decode()
    random_string_2 = Fernet.generate_key().decode()
    password = ("%s%s%s"%(random_string,random_string_2,nummer)).encode()
    salt = os.urandom(999999)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    private_key = base64.urlsafe_b64encode(kdf.derive(password))
    private_f = Fernet(private_key)
    return (private_key,private_f)

(private_key,private_f) = create_private_key()
print(len(private_key))
print(private_key)
