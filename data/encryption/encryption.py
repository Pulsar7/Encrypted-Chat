import base64,random,os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

#
passwords = []
#

def create_private_key():
    nummer = random.randint(9999,999999)
    random_string,random_string_2,random_string_3 = Fernet.generate_key(),Fernet.generate_key(),Fernet.generate_key()
    random_string,random_string_2,random_string_3 = random_string.decode(),random_string_2.decode(),random_string_3.decode()
    args_1,args_2,args_3 = random_string.split('='),random_string_2.split('='),random_string_3.split('=')
    random_string,random_string_2,random_string_3 = args_1[0],args_2[0],args_3[0]
    password = ("%s%s%s%s"%(random_string,random_string_2,random_string_3,nummer)).encode()
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
    return (private_key,private_f,password)

def encrypt(key,msg):
    f = Fernet(key)
    package = f.encrypt(msg.encode())
    return (package)

def decrypt(key,package):
    f = Fernet(key)
    response = f.decrypt(package).decode()
    return (response)
