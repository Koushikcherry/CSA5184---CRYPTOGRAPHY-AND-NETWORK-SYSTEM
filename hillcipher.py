import numpy as np

def matrix_mod_inverse(matrix, mod):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = pow(det, -1, mod)
    adj_matrix = np.round(det_inv * np.linalg.inv(matrix)).astype(int) % mod
    return adj_matrix

def hill_encrypt(plain_text, key_matrix):
    block_size = len(key_matrix)
    mod = 26  # Modulus for the alphabet size
    encrypted_text = ""

    while len(plain_text) % block_size != 0:
        plain_text += 'X'

    for i in range(0, len(plain_text), block_size):
        block = np.array([ord(char) - ord('A') for char in plain_text[i:i+block_size]])
        encrypted_block = np.dot(key_matrix, block) % mod
        encrypted_text += ''.join([chr(val + ord('A')) for val in encrypted_block])

    return encrypted_text

# Example usage
plaintext = input("Enter the text:")
key_matrix = np.array([[6, 24], [13, 16]])  # Example 2x2 key matrix
encrypted_text = hill_encrypt(plaintext, key_matrix)
print("Encrypted:", encrypted_text)
