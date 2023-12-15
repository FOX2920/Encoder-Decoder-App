import streamlit as st

def caesar_cipher(text, key, decrypt=False):
    result = ""
    for char in text:
        if char.isalpha():
            shift = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - shift + key * (1 if not decrypt else -1)) % 26 + shift)
        else:
            result += char
    return result

def brute_force_decrypt(ciphertext):
    for key in range(26):
        decrypted_text = caesar_cipher(ciphertext, key, decrypt=True)
        st.write(f"Key {key}: {decrypted_text}")

def brute_force_encrypt(ciphertext):
    for key in range(26):
        decrypted_text = caesar_cipher(ciphertext, key, decrypt=False)
        st.write(f"Key {key}: {decrypted_text}")


def main():
    st.title("Caesar Cipher Encryption/Decryption")

    operation = st.sidebar.radio("Choose Operation", ["Encrypt", "Decrypt", "Brute Force Decrypt", "Brute Force Encrypt"])

    key = st.sidebar.number_input("Enter Key", min_value=0, max_value=25, value=3)

    if operation == "Brute Force Decrypt":
        ciphertext = st.text_area("Enter Ciphertext", "")
        if st.button("Brute Force Decrypt"):
            brute_force_decrypt(ciphertext)
    elif operation == "Brute Force Decrypt":
        ciphertext = st.text_area("Enter Ciphertext", "")
        if st.button("Brute Force Encrypt"):
            brute_force_encrypt(ciphertext)
    elif operation == "Decrypt":
        ciphertext = st.text_area("Enter Ciphertext", "")
        decrypted_text = caesar_cipher(ciphertext, key, decrypt=True)
        st.write(f"Decrypted Text: {decrypted_text}")
    else:
        text = st.text_area(f"Enter {'Plaintext' if operation=='Encrypt' else 'Ciphertext'}", "")
        result = caesar_cipher(text, key, decrypt=(operation == "Decrypt"))
        st.write(f"Result: {result}")

if __name__ == "__main__":
    main()
