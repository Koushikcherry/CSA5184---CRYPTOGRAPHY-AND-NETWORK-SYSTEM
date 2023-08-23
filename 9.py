def generate_playfair_matrix(keyword):
    keyword = keyword.upper().replace('J', 'I')
    keyword_set = set(keyword)
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    matrix = []
    
    for char in keyword_set:
        if char not in matrix:
            matrix.append(char)
    
    for char in alphabet:
        if char not in matrix:
            matrix.append(char)
    
    playfair_matrix = [matrix[i:i+5] for i in range(0, len(matrix), 5)]
    return playfair_matrix

def find_position(matrix, char):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == char:
                return row, col

def playfair_decrypt(ciphertext, keyword):
    matrix = generate_playfair_matrix(keyword)
    plaintext = ""
    pairs = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
    
    for pair in pairs:
        row1, col1 = find_position(matrix, pair[0])
        row2, col2 = find_position(matrix, pair[1])
        
        if row1 == row2:
            plaintext += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += matrix[row1][col2] + matrix[row2][col1]
    
    return plaintext

def main():
    keyword = "PT109"
    ciphertext = "KXJEY UREBE ZWEHE WRYTU HEYFS KREHE GOYFI WTTTU OLKSY CAJPO BOTEI ZONTX BYBNT GONEY CUZWR GDSON SXBOU YWRHE BAAHY USEDQ"
    
    cleaned_ciphertext = ciphertext.replace(' ', '').upper()
    decrypted_text = playfair_decrypt(cleaned_ciphertext, keyword)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
