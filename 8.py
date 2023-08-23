def generate_cipher_sequence(keyword):
    keyword = keyword.upper()
    cipher_sequence = list(keyword)
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if letter not in cipher_sequence:
            cipher_sequence.append(letter)
    return cipher_sequence

def monoalphabetic_encrypt(plaintext, cipher_sequence):
    plaintext = plaintext.upper()
    encrypted_text = ""
    for char in plaintext:
        if char == ' ':
            encrypted_text += ' '
        else:
            index = ord(char) - ord('A')
            encrypted_text += cipher_sequence[index]
    return encrypted_text

def monoalphabetic_decrypt(ciphertext, cipher_sequence):
    ciphertext = ciphertext.upper()
    decrypted_text = ""
    for char in ciphertext:
        if char == ' ':
            decrypted_text += ' '
        else:
            index = cipher_sequence.index(char)
            decrypted_text += chr(index + ord('A'))
    return decrypted_text

def main():
    keyword = "CIPHER"
    cipher_sequence = generate_cipher_sequence(keyword)

    plaintext = input("Enter the plaintext: ")
    encrypted_text = monoalphabetic_encrypt(plaintext, cipher_sequence)
    print("Encrypted text:", encrypted_text)

    decrypted_text = monoalphabetic_decrypt(encrypted_text, cipher_sequence)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
