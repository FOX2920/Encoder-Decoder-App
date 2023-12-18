import streamlit as st
import base64
from io import BytesIO

def decrypt(ciphertext, key):
    decrypted = bytearray()
    key_len = len(key)
    for i, byte in enumerate(ciphertext):
        decrypted_byte = byte ^ key[i % key_len]
        decrypted.append(decrypted_byte)
    return bytes(decrypted)

def main():
    st.title("XOR Cipher Decryptor")

    encryption_key = st.text_input("Enter a 6-letter key:")

    if st.button("Decrypt"):
        if len(encryption_key) == 6:
            # Use the global variable 'encrypted_data' from your existing code
            global encrypted_data

            # Decrypt the image with the provided key
            decrypted_image = decrypt(encrypted_data, encryption_key.encode())

            # Display the decrypted image
            st.image(decrypted_image, caption="Decrypted Image", use_column_width=True)
        else:
            st.warning("Please enter a 6-letter key.")

if __name__ == "__main__":
    # Load encrypted data from the file
    with open("crypto01.jpg", "rb") as file:
        encrypted_data = file.read()

    main()
