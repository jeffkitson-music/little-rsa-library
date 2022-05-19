# Alice and Bob: An RSA Example
A very simple example about how two parties could use RSA encyption to have a conversation.

## Step One: Generating Keys
Alice and Bob want to have a private conversation. In symmetrical encryption there is only one key, but 
in asymmetrical encryption, both Alice and Bob will each need their own public key and private key. 

Let's do that now... 

```python
import litte_rsa_library as rsa_lib

alice_private_key = rsa_lib.create_key_pair(private_filename="alice_private_key.pem",
                                            public_filename="alice_public_key.pem")

# Bob creates his keys
bob_private_key = rsa_lib.create_key_pair(private_filename="bob_private_key.pem", 
                                          public_filename="bob_public_key.pem")
```

## Step Two: Exchanging keys
Alice and Bob will keep their private keys private. If they fall into the wrong hands, all their messages can be read! However, Alice and Bob will exchange public keys with each other so they can share messages. 

## Step Three: Encrypting a message
In order to send a message to Bob, Alice must use Bob's public key. 
```python
bob_public_key = rsa_lib.load_public_key("bob_public_key.pem")
```
Alice writes her message to Bob
```python
message_to_bob = "Hi, Bob! How are you?"
```
Now, Alice will use RSA encryption to encrypt the message to Bob.
```python
secret_message = rsa_lib.encrypt(message_to_bob, bob_public_key)
print(secret_message)
# (will be different every time, but will decrypt correctly)
# output: O6iNd8HWA48-HoiIWXDZenb__-QRgHIoP2AcRuz7e67rptN4-s8wsYI6GcfVFmHU503TiD-qOcGA7u-pCDcSGKgWYT_fgviMtpQwRG2gZOSXhdFSR81oh35Rjp0ILaIa-OlF1W1msgaq4KPazaIgHnRjH0eCvP8NUFgtscUKPlNqxrhFUPZjMMdL4e5Uv-2wi3TjDvQFTgiDijgVJ51FmCkGtnVoOWtG7GA60y-pBsCqaXHdXBAjbSg5AuW1jOLkVHC_X2rs-bQzotCDoJ7j4X8F4FKrg6vh0UQyof031Xd7mVahSQXpP6eyhlfV3XXF0A68EmhXNKmZnUAAB9tdDQ==
```
Alice then sends the encrypted secret message to Bob. 

## Step Four: Decrypting a message
Bob received the secret message from Alice and wants to decrypt it. To do so, he needs his private key. 
```python
bob_private_key = rsa_lib.load_private_key("bob_private_key.pem")
```
With his key loaded, Bob can decrypt the message.
```python
#secret_message = "O6iNd8HWA48-HoiIWXDZenb__-QRgHIoP2AcRuz7e67rptN4-s8wsYI6GcfVFmHU503TiD-qOcGA7u-pCDcSGKgWYT_fgviMtpQwRG2gZOSXhdFSR81oh35Rjp0ILaIa-OlF1W1msgaq4KPazaIgHnRjH0eCvP8NUFgtscUKPlNqxrhFUPZjMMdL4e5Uv-2wi3TjDvQFTgiDijgVJ51FmCkGtnVoOWtG7GA60y-pBsCqaXHdXBAjbSg5AuW1jOLkVHC_X2rs-bQzotCDoJ7j4X8F4FKrg6vh0UQyof031Xd7mVahSQXpP6eyhlfV3XXF0A68EmhXNKmZnUAAB9tdDQ=="
plaintext = rsa_lib.decrypt(secret_message, bob_private_key)
print(plaintext)
# output: Hi, Bob! How are you?"
```

## Step Five: Going forward
Bob will respond to Alice's message by writing his own message and then using Alice's public key to encrypt, just like Alice used Bob's key to encrypt her message to him. 

## Want More?
[Here is a great video](https://www.youtube.com/watch?v=NmM9HA2MQGI) from Dr. Mike Pound and Computerphile on this topic! 
