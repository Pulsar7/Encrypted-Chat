from cryptography.fernet import Fernet
import base64,random,os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

#
passwords = []
#

def create_private_key():
    nummer = random.randint(9999,999999)
    random_string,random_string_2 = Fernet.generate_key(),Fernet.generate_key()
    random_string,random_string_2 = random_string.decode(),random_string_2.decode()
    password = ("%s%s%s"%(random_string,random_string_2,nummer)).encode()
    passwords.append(password.decode())
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
