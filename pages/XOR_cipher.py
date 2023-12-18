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

st.title("XOR Cipher Decryption App")

uploaded_file = st.file_uploader("Upload an encrypted image", type=["jpg", "jpeg"])

if uploaded_file is not None:
    encrypted_data = uploaded_file.read()  # Corrected line

    st.subheader("Encryption Key")
    key = st.text_input("Enter the encryption key (6 letters):", "uithcm").encode()  # Corrected line

    # Correct the function call to decrypt
    decrypted_data = decrypt(encrypted_data, key)

    # Display the decrypted image
    st.image(BytesIO(decrypted_data), caption="Decrypted Image", use_column_width=True)

    # Provide option to download the decrypted image
    st.sidebar.markdown(
        f"**Download Decrypted Image:** [decrypted_image_{key.decode()}.jpg](data:application/octet-stream;base64,{base64.b64encode(decrypted_data).decode()})",
        unsafe_allow_html=True
    )
