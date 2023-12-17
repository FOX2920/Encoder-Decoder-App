import streamlit as st


def extend_key(key, length):
    extended_key = key
    while len(extended_key) < length:
        extended_key += key
    return extended_key[:length]


def vigenere_encrypt(plain_text, key):
    encrypted_text = ""
    key = extend_key(key.upper(), len(plain_text))
    for i in range(len(plain_text)):
        if plain_text[i].isalpha():
            shift = ord(key[i]) - ord('A')
            if plain_text[i].islower():
                encrypted_text += chr((ord(plain_text[i]) + shift - ord('a')) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(plain_text[i]) + shift - ord('A')) % 26 + ord('A'))
        else:
            encrypted_text += plain_text[i]
    return encrypted_text


def vigenere_decrypt(encrypted_text, key):
    decrypted_text = ""
    key = extend_key(key.upper(), len(encrypted_text))
    for i in range(len(encrypted_text)):
        if encrypted_text[i].isalpha():
            shift = ord(key[i]) - ord('A')
            if encrypted_text[i].islower():
                decrypted_text += chr((ord(encrypted_text[i]) - shift - ord('a')) % 26 + ord('a'))
            else:
                decrypted_text += chr((ord(encrypted_text[i]) - shift - ord('A')) % 26 + ord('A'))
        else:
            decrypted_text += encrypted_text[i]
    return decrypted_text


def vigenere_page():
    st.title("Vigenère Cipher Encryption/Decryption")

    option = st.radio("Select an option:", ("Encrypt", "Decrypt"))

    key = st.text_input("Enter the key:")
    text = st.text_input("Enter the text:")

    if key and text:
        if option == "Encrypt":
            result = vigenere_encrypt(text, key)
            st.success(f"Encrypted Text: {result}")
        else:
            result = vigenere_decrypt(text, key)
            st.success(f"Decrypted Text: {result}")
