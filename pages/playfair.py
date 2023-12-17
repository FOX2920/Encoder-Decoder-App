import streamlit as st
import numpy as np

def generate_playfair_matrix(key):
    key = key.replace("J", "I")
    key_set = sorted(set(key), key=key.index)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    remaining_letters = [letter for letter in alphabet if letter not in key_set]

    playfair_matrix = np.array(list(key_set + remaining_letters))
    playfair_matrix = playfair_matrix.reshape(5, 5)

    return playfair_matrix

def find_coordinates(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i, j] == char:
                return i, j

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
    st.title("Playfair Cipher Tool")

    # Input key
    key = st.text_input("Enter the key:")
    key = key.upper().replace(" ", "")

    # Generate and display Playfair matrix
    matrix = generate_playfair_matrix(key)
    st.write("Playfair Matrix:")
    st.write(matrix)

    # Select operation
    operation = st.radio("Select operation:", ("Encrypt", "Decrypt"))

    # Input text
    if operation == "Encrypt":
        plaintext = st.text_area("Enter the plaintext:")
        ciphertext = encrypt_playfair(plaintext, key)
        st.write("Ciphertext:")
        st.write(ciphertext)
    elif operation == "Decrypt":
        ciphertext = st.text_area("Enter the ciphertext:")
        plaintext = decrypt(ciphertext, key)
        st.write("Decrypted Text:")
        st.write(plaintext)
