import streamlit as st

def generate_playfair_matrix(key):
    # Remove duplicate characters from the key
    key = "".join(sorted(set(key.upper()), key=key.find))

    # Fill the matrix with the key
    matrix = [list(key[i:i+5]) for i in range(0, len(key), 5)]

    # Fill the remaining cells with the remaining alphabet (excluding 'J')
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in alphabet:
        if char not in key:
            matrix.append(char)

    return matrix

def find_position(matrix, char):
    for row_idx, row in enumerate(matrix):
        if char in row:
            col_idx = row.index(char)
            return row_idx, col_idx

def encrypt_playfair(plaintext, key):
    matrix = generate_playfair_matrix(key)
    ciphertext = ""
    plaintext = plaintext.upper().replace("J", "I")

    for i in range(0, len(plaintext), 2):
        pair1 = plaintext[i]
        pair2 = plaintext[i + 1] if i + 1 < len(plaintext) else 'X'

        row1, col1 = find_position(matrix, pair1)
        row2, col2 = find_position(matrix, pair2)

        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5]
            ciphertext += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1]
            ciphertext += matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2]
            ciphertext += matrix[row2][col1]

    return ciphertext

def decrypt_playfair(ciphertext, key):
    matrix = generate_playfair_matrix(key)
    plaintext = ""

    for i in range(0, len(ciphertext), 2):
        pair1 = ciphertext[i]
        pair2 = ciphertext[i + 1]

        row1, col1 = find_position(matrix, pair1)
        row2, col2 = find_position(matrix, pair2)

        if row1 == row2:
            plaintext += matrix[row1][(col1 - 1) % 5]
            plaintext += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[(row1 - 1) % 5][col1]
            plaintext += matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += matrix[row1][col2]
            plaintext += matrix[row2][col1]
            
    return plaintext

    
def playfair_page():
    st.title("Playfair Cipher Encryption and Decryption")

    # Input key
    key = st.text_input("Enter the Playfair cipher key:")

    # Input plaintext or ciphertext
    text_input = st.text_area("Enter the plaintext or ciphertext:")

    # Select operation (encrypt or decrypt)
    operation = st.radio("Select operation:", ["Encrypt", "Decrypt"])

    if st.button("Perform Operation"):
        if operation == "Encrypt":
            result = encrypt_playfair(text_input, key)
        elif operation == "Decrypt":
            result = decrypt_playfair(text_input, key)
        else:
            result = "Invalid operation"

        # Display result
        st.subheader(f"Result ({operation}):")
        st.write(result)
