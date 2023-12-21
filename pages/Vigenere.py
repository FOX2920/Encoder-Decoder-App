import streamlit as st
import numpy as np

def generate_vigenere_table():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    vigenere_table = np.zeros((26, 26), dtype='str')

    for i in range(26):
        for j in range(26):
            vigenere_table[i, j] = alphabet[(i + j) % 26]

    return vigenere_table

def vigenere_encrypt(plaintext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    vigenere_table = generate_vigenere_table()
    ciphertext = ""

    key = key.upper()
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            row = alphabet.index(key[key_index])
            col = alphabet.index(char.upper())

            ciphertext += vigenere_table[row, col]

            key_index = (key_index + 1) % len(key)
        else:
            ciphertext += char

    return ciphertext

def vigenere_decrypt(ciphertext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    vigenere_table = generate_vigenere_table()
    plaintext = ""

    key = key.upper()
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            row = alphabet.index(key[key_index])
            col = np.where(vigenere_table[row, :] == char.upper())[0][0]

            plaintext += alphabet[col]

            key_index = (key_index + 1) % len(key)
        else:
            plaintext += char

    return plaintext

def main():
    st.title("Vigenère Cipher Encryption and Decryption")

    operation = st.radio("Select Operation", ["Encrypt", "Decrypt"])

    message = st.text_area("Enter Message:")

    key = st.text_input("Enter Key:")

    if st.button("Perform Operation"):
        if operation == "Encrypt":
            result = vigenere_encrypt(message, key)
        else:
            result = vigenere_decrypt(message, key)

        st.success(f"Result: {result}")

if __name__ == "__main__":
    main()
