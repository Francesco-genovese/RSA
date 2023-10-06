# RSA
In order to make it work, you need to install "pycryptodome" using the following command:

```bash
pip install pycryptodome
```


This command will install the "pycryptodome" package, which is necessary for the functionality you mentioned.


RSA (Rivest-Shamir-Adleman) is a widely used asymmetric encryption algorithm in the field of cryptography. It was first introduced by Ron Rivest, Adi Shamir, and Leonard Adleman in 1977. RSA encryption relies on the mathematical properties of large prime numbers and is known for its security and versatility. Here's a brief description of the RSA encryption algorithm in English:

RSA Encryption Algorithm:

1. Key Generation:
   - Choose two large prime numbers, p and q.
   - Calculate their product, n = p * q, which becomes the modulus for both the public and private keys.
   - Compute Euler's totient function, φ(n) = (p - 1) * (q - 1).
   - Choose an integer e (the public exponent) such that 1 < e < φ(n) and gcd(e, φ(n)) = 1. Common choices for e include 3 or 65537.
   - Calculate the private exponent d, which is the modular multiplicative inverse of e modulo φ(n), i.e., d ≡ e^(-1) (mod φ(n)).

2. Public Key (e, n):
   - The public key consists of two components: the public exponent (e) and the modulus (n). This key is used for encryption.

3. Private Key (d, n):
   - The private key consists of two components: the private exponent (d) and the modulus (n). This key is used for decryption.

4. Encryption:
   - To encrypt a message M, the sender obtains the recipient's public key (e, n).
   - The sender converts the message into a numerical value, typically using a padding scheme.
   - The sender computes the ciphertext C as C ≡ M^e (mod n).

5. Decryption:
   - To decrypt the ciphertext C, the recipient uses their private key (d, n).
   - The recipient computes the original message M as M ≡ C^d (mod n).

RSA is secure because the difficulty of factoring the product of two large prime numbers (n) makes it computationally infeasible for an attacker to determine the private key from the public key. It is widely used in secure communication, digital signatures, and various cryptographic applications, making it a cornerstone of modern cryptography.
