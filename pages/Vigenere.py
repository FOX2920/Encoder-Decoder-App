import streamlit as st

def vigenere_encrypt(plain_text, key):
    encrypted_text = ""
    key = key.upper()
    key_index = 0

    for char in plain_text:
        if char.isalpha():
            key_char = key[key_index % len(key)]
            shift = ord(key_char) - ord('A')
            if char.isupper():
                encrypted_text += chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
            else:
                encrypted_text += chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
            key_index += 1
        else:
            encrypted_text += char

    return encrypted_text

def vigenere_decrypt(encrypted_text, key):
    decrypted_text = ""
    key = key.upper()
    key_index = 0

    for char in encrypted_text:
        if char.isalpha():
            key_char = key[key_index % len(key)]
            shift = ord(key_char) - ord('A')
            if char.isupper():
                decrypted_text += chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
            else:
                decrypted_text += chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
            key_index += 1
        else:
            decrypted_text += char

    return decrypted_text

# Streamlit UI
st.title("Vigenère Cipher Encryption and Decryption")

# Input text
text = st.text_area("Enter your message:")

# Input key
key = st.text_input("Enter the encryption/decryption key:")

# Radio box for choosing between encryption and decryption
operation = st.radio("Select Operation:", ["Encrypt", "Decrypt"])

if operation == "Encrypt":
    result = vigenere_encrypt(text, key)
    st.success(f"Encrypted Message: {result}")
elif operation == "Decrypt":
    result = vigenere_decrypt(text, key)
    st.success(f"Decrypted Message: {result}")

