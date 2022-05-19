import little_rsa_library as rsa_lib

## STEP ONE: KEYS
# Alice creates her keys
alice_private_key = rsa_lib.create_key_pair(private_filename="alice_private_key.pem",
                                           public_filename="alice_public_key.pem")

# Bob creates his keys
bob_private_key = rsa_lib.create_key_pair(private_filename="bob_private_key.pem",
                                          public_filename="bob_public_key.pem")

## STEP TWO: EXCHANGING KEYS
# Alice and Bob exchange public keys and keep their private keys private.

# STEP THREE: ENCRYPTING A MESSAGE
# Alice loads Bob's public key
bob_public_key = rsa_lib.load_public_key("bob_public_key.pem")

# Alice writes her message to Bob
message_to_bob = "Hi, Bob! How are you?"

# Alice encrypts her message to Bob using his public key.
secret_message = rsa_lib.encrypt(message_to_bob, bob_public_key)
print(secret_message)

# Alice sends the encrypted message to Bob

# STEP FOUR: DECRYPTING A MESSAGE
# Bob loads his private key
bob_private_key = rsa_lib.load_private_key("bob_private_key.pem")

#secret_message = "O6iNd8HWA48-HoiIWXDZenb__-QRgHIoP2AcRuz7e67rptN4-s8wsYI6GcfVFmHU503TiD-qOcGA7u-pCDcSGKgWYT_fgviMtpQwRG2gZOSXhdFSR81oh35Rjp0ILaIa-OlF1W1msgaq4KPazaIgHnRjH0eCvP8NUFgtscUKPlNqxrhFUPZjMMdL4e5Uv-2wi3TjDvQFTgiDijgVJ51FmCkGtnVoOWtG7GA60y-pBsCqaXHdXBAjbSg5AuW1jOLkVHC_X2rs-bQzotCDoJ7j4X8F4FKrg6vh0UQyof031Xd7mVahSQXpP6eyhlfV3XXF0A68EmhXNKmZnUAAB9tdDQ=="
# secret message is different every time, so for this script to work, variable is kept from above.
plaintext = rsa_lib.decrypt(secret_message, bob_private_key)
print(plaintext)
