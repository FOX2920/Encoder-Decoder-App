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

def playfair_encrypt(plaintext, key):
    matrix = generate_playfair_matrix(key)

    # Preprocess the plaintext
    plaintext = plaintext.upper().replace("J", "I")
    plaintext_pairs = [plaintext[i:i + 2] for i in range(0, len(plaintext), 2)]

    # Encrypt pairs
    ciphertext = ""
    for pair in plaintext_pairs:
        x1, y1 = find_coordinates(matrix, pair[0])
        x2, y2 = find_coordinates(matrix, pair[1])

        if x1 == x2:
            ciphertext += matrix[x1, (y1 + 1) % 5] + matrix[x2, (y2 + 1) % 5]
        elif y1 == y2:
            ciphertext += matrix[(x1 + 1) % 5, y1] + matrix[(x2 + 1) % 5, y2]
        else:
            ciphertext += matrix[x1, y2] + matrix[x2, y1]

    return ciphertext

def playfair_decrypt(ciphertext, key):
    matrix = generate_playfair_matrix(key)

    # Preprocess the ciphertext
    ciphertext_pairs = [ciphertext[i:i + 2] for i in range(0, len(ciphertext), 2)]

    # Decrypt pairs
    plaintext = ""
    for pair in ciphertext_pairs:
        x1, y1 = find_coordinates(matrix, pair[0])
        x2, y2 = find_coordinates(matrix, pair[1])

        if x1 == x2:
            plaintext += matrix[x1, (y1 - 1) % 5] + matrix[x2, (y2 - 1) % 5]
        elif y1 == y2:
            plaintext += matrix[(x1 - 1) % 5, y1] + matrix[(x2 - 1) % 5, y2]
        else:
            plaintext += matrix[x1, y2] + matrix[x2, y1]

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
        ciphertext = playfair_encrypt(plaintext, key)
        st.write("Ciphertext:")
        st.write(ciphertext)
    elif operation == "Decrypt":
        ciphertext = st.text_area("Enter the ciphertext:")
        plaintext = playfair_decrypt(ciphertext, key)
        st.write("Decrypted Text:")
        st.write(plaintext)
