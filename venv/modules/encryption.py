import secrets

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes


# symmetric_encryption
def aes_encrypt_decrypt(message):
    """
    Demonstrates symmetric encryption using AES-GCM.
    Same key is used for both encryption and decryption.
    """
    # Generate a random 256-bit (32 byte) key for AES
    key = secrets.token_bytes(32)

    # Generate a 12-byte nonce (number used once) for GCM mode
    nonce = secrets.token_bytes(12)

    # Create AES-GCM cipher object with the key
    aes = AESGCM(key)

    # ENCRYPT: nonce + encrypted message
    # The nonce is prepended to the ciphertext for use in decryption
    ciphertext = nonce + aes.encrypt(nonce, message.encode(), None)

    # DECRYPT: Extract nonce (first 12 bytes) and decrypt the rest
    plaintext = aes.decrypt(ciphertext[:12], ciphertext[12:], None)

    # Return key, ciphertext (both in hex), and decrypted message
    return key.hex(), ciphertext.hex(), plaintext.decode()


# Asymmetric_encryption
def rsa_encrypt_decrypt(message):
    """
    Demonstrates asymmetric encryption using RSA.
    Different keys: public key encrypts, private key decrypts.
    """
    # Generate RSA key pair (private key contains both)
    private_key = rsa.generate_private_key(
        public_exponent=65537,  # Standard public exponent
        key_size=2048,  # Key size in bits
    )

    # Extract public key from private key
    public_key = private_key.public_key()

    # ENCRYPT using the PUBLIC key
    ciphertext = public_key.encrypt(
        message.encode(),
        padding.OAEP(  # Optimal Asymmetric Encryption Padding
            mgf=padding.MGF1(algorithm=hashes.SHA256()),  # Mask generation function
            algorithm=hashes.SHA256(),  # Hash algorithm
            label=None,  # Optional label
        ),
    )
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),  # Mask generation function
            algorithm=hashes.SHA256(),  # Hash algorithm
            label=None,  # Optional label
        ),
    )
    return ciphertext.hex(), plaintext.decode()


if __name__ == "__main__":
    print(aes_encrypt_decrypt("Hello, AES!"))
    print(rsa_encrypt_decrypt("Hello, RSA!"))
