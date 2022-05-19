import os
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes


def create_key_pair(**kwargs):
    if "private_filename" in kwargs.keys():
        private_filename = kwargs['private_filename']
    else:
        private_filename = "my_private_key.pem"
    print("Private Key filename is: " + private_filename)

    if "public_filename" in kwargs.keys():
        public_filename = kwargs['public_filename']
    else:
        public_filename = "my_public_key.pem"
    print("Public Key filename is: " + public_filename)

    if os.path.exists(private_filename):
        raise Exception("Private Key file already exists! Do you want to overwrite it?")

    if os.path.exists(public_filename):
        raise Exception("Public Key file already exists! Do you want to overwrite it?")

    private_key = create_private_key_file(private_filename)
    public_key = private_key.public_key()
    create_public_keyfile(public_key, public_filename)
    return private_key


def create_private_key_file(private_filename):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )

    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )

    with open(private_filename, 'wb') as keyfile:
        keyfile.write(pem)

    return private_key


def create_public_keyfile(public_key, public_filname):
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    with open(public_filname, 'wb') as f:
        f.write(public_pem)
    return


def load_private_key(filename):
    with open(filename, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
        )
    return private_key


def load_public_key(filename):
    with open(filename, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )
    return public_key


def encrypt(cleartext, public_key):
    message = cleartext.encode()
    length_okay = check_message_length(message)
    if length_okay:
        # URL SAFE FOR SAFETY! I am so fucking proud of myself right now!!!!!!!!
        ciphertext = base64.urlsafe_b64encode(public_key.encrypt(
            message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        ))
    else:
        raise Exception("Message is too long to encrypt! Must be shorter than 2048 bits (about 834 chars).")
    return ciphertext  # use base64, not hex


def decrypt(ciphertext, private_key):
    # Add try/except for url safe?
    try:
        # Defaults to decrypting url-safe base64
        plaintext = private_key.decrypt(
            base64.urlsafe_b64decode(ciphertext),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
    except Exception as e:
        # Falls back to plain base64 if the above fails.
        plaintext = private_key.decrypt(
            base64.b64decode(ciphertext),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
    return plaintext


def check_message_length(message):
    # Messages have to be less than the key length, which is 2048 bits
    bit_length = len(message) * 8
    if bit_length > 2048:
        return False
    else:
        return True
