import streamlit as st

def xor_decrypt(encrypted_data, key):
    decrypted_data = bytearray()
    key = key.encode()

    for i in range(len(encrypted_data)):
        decrypted_byte = encrypted_data[i] ^ key[i % len(key)]
        decrypted_data.append(decrypted_byte)

    return bytes(decrypted_data)

def main():
    st.title("XOR Cipher Decryption App")

    uploaded_file = st.file_uploader("Choose an encrypted image file", type=["jpg", "jpeg"])

    if uploaded_file is not None:
        key = st.text_input("Enter 6-letter key:")
        if len(key) != 6:
            st.warning("Please enter a 6-letter key.")
        else:
            with open(uploaded_file.name, "rb") as file:
                encrypted_data = file.read()

            decrypted_data = xor_decrypt(encrypted_data, key)

            st.image(decrypted_data, caption="Decrypted Image", use_column_width=True)

            st.success("Decryption successful! Check the image for the flag.")

if __name__ == "__main__":
    main()
