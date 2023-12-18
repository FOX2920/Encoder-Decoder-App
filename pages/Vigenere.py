import streamlit as st

def vigenere_cipher(text, key, encrypt=True):
    result = ''
    key_length = len(key)
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            key_char = key[i % key_length].upper()
            key_offset = ord(key_char) - ord('A')
            if encrypt:
                result += encrypt_char(char, key_offset)
            else:
                result += decrypt_char(char, key_offset)
        else:
            result += char
    return result

def encrypt_char(char, key_offset):
    base = ord('A') if char.isupper() else ord('a')
    return chr((ord(char) - base + key_offset) % 26 + base)

def decrypt_char(char, key_offset):
    base = ord('A') if char.isupper() else ord('a')
    return chr((ord(char) - base - key_offset) % 26 + base)

def main():
    st.title("Vigenère Cipher Encryption and Decryption")

    operation = st.radio("Select Operation", ["Encrypt", "Decrypt"])

    message = st.text_area("Enter Message:")

    key = st.text_input("Enter Key:")

    if st.button("Perform Operation"):
        if operation == "Encrypt":
            result = vigenere_cipher(message, key, encrypt=True)
        else:
            result = vigenere_cipher(message, key, encrypt=False)

        st.success(f"Result: {result}")

if __name__ == "__main__":
    main()
