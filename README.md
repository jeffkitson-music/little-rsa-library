# 📚 Little RSA Library
A simple wrapper for the basic RSA functionality of [cryptography](https://cryptography.io/en/latest/).

## :lock: About
This script is designed for those who want to implement asymmetric RSA encryption in a project quickly and easily without struggling to figure out the often-overwhelming cryptography docs. 

:lock: Primary Uses:
- :lock: Create both public and private key files (PEM)
- :lock: Load both public and private key files
- :lock: Encrypt and decrypt with RSA encryption 

## :old_key: Dependencies 

- cryptography (pip install cryptography)

## :eyes: Example Uses
**Creating Key Files**

*Note: Not pip installable. Just copy this repo...*
```python
import litte_rsa_lib as rsa_lib

# Creating Key Files
# returns private key, but isn't necessary - uses default filenames
pk = rsa_lib.create_key_pair()

# or you can specify your own filenames
pk = rsa_lib.create_key_pair(private_filename="foo.pem",public_filename="bar.pem")
```
**Load Key Files**
```python

# Load a private key file
private_key = rsa_lib.load_private_key("my_private_key.pem")
public_key = private_key.public_key()

# Load a public key file
public_key = jrsa.load_public_key("my_public_key.pem")
```
**Encrypting and Decrypting**
```python
# Note: Remember in RSA, you encrypt with the public key and decrypt with the private key.

# Encrypt
cleartext = "Hello world!"
ciphertext = rsa_lib.encrypt(cleartext, public_key)
print(ciphertext.decode())

# Decrypt
plaintext = rsa_lib.decrypt(ciphertext, private_key)
print(plaintext.decode())

```

## :mega:  Shoutouts
- [Gabriel Falcão](https://github.com/gabrielfalcao) for [this gist](https://gist.github.com/gabrielfalcao/de82a468e62e73805c59af620904c124) that I read when I couldn't quite get things right, and quite literally gave me the gist. 

- [President James K. Polk](https://stackoverflow.com/users/238704/president-james-k-polk) in [this thread](https://stackoverflow.com/questions/45146504/python-cryptography-module-save-load-rsa-keys-to-from-file) on how to save the keys, as the cryptography docs aren't straightforward on this topic. 

- [cryptography](https://cryptography.io/en/latest/). You never cease to amaze me. 
