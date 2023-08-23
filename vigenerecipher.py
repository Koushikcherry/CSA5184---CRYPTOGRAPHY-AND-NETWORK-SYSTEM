def vigenere_encrypt(plain_text, key):
    encrypted_text = ""
    key = key.upper()  # Convert the key to uppercase for consistency
    key_length = len(key)
    key_indices = [ord(char) - ord('A') for char in key]

    for i, char in enumerate(plain_text):
        if char.isalpha():
            shift = key_indices[i % key_length]
            if char.islower():
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    return encrypted_text

# Example usage
plaintext = input("Enter the text:")
key = input("Enter the key:")
encrypted_text = vigenere_encrypt(plaintext, key)
print("Encrypted:", encrypted_text)
