import streamlit as st
import io
from PIL import Image

# XOR decryption function
def decrypt(ciphertext, key):
    decrypted = bytearray()
    key_len = len(key)
    for i, byte in enumerate(ciphertext):
        decrypted_byte = byte ^ key[i % key_len]
        decrypted.append(decrypted_byte)
    return bytes(decrypted)

# Streamlit app
def main():
    st.title("Image Decryption App")

    # Upload image
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)

        # Input decryption key
        decryption_key = st.text_input("Enter 6-letter decryption key:")

        if len(decryption_key) == 6:
            # Read image file
            image_bytes = io.BytesIO(uploaded_file.read())
            image = Image.open(image_bytes)

            # Decrypt image
            encrypted_data = image.tobytes()
            decrypted_data = decrypt(encrypted_data, decryption_key.encode())

            # Display decrypted image
            decrypted_image = Image.frombytes(image.mode, image.size, decrypted_data)
            st.image(decrypted_image, caption="Decrypted Image.", use_column_width=True)
        else:
            st.warning("Please enter a 6-letter decryption key.")

if __name__ == "__main__":
    main()
