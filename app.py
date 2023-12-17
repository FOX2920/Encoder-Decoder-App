import streamlit as st

def generate_playfair_matrix(key):
    # Implementation of Playfair matrix generation based on the key
    # (You can replace this with a more sophisticated algorithm)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # excluding 'J'
    key = key.upper().replace("J", "I")
    key_set = set(key)
    remaining_chars = [char for char in alphabet if char not in key_set]

    playfair_matrix = [[0] * 5 for _ in range(5)]
    key += "".join(remaining_chars)
    key_index = 0

    for i in range(5):
        for j in range(5):
            playfair_matrix[i][j] = key[key_index]
            key_index += 1

    return playfair_matrix

def encrypt_playfair(plain_text, playfair_matrix):
    # Implementation of Playfair encryption
    # (You can replace this with a more sophisticated algorithm)
    pass  # Your implementation here

def decrypt_playfair(cipher_text, playfair_matrix):
    # Implementation of Playfair decryption
    # (You can replace this with a more sophisticated algorithm)
    pass  # Your implementation here

def main():
    st.title("Playfair Cipher Encryptor/Decryptor")

    action = st.radio("Choose Action", ("Encrypt", "Decrypt"))

    key = st.text_input("Enter Key (e.g., PLAYFAIR)", max_chars=25).upper()
    input_text = st.text_area("Enter Text")

    if key and input_text:
        playfair_matrix = generate_playfair_matrix(key)

        st.subheader("Playfair Matrix:")
        st.table(playfair_matrix)

        if action == "Encrypt":
            cipher_text = encrypt_playfair(input_text.upper(), playfair_matrix)
            st.subheader("Encrypted Text:")
            st.text(cipher_text)
        elif action == "Decrypt":
            plain_text = decrypt_playfair(input_text.upper(), playfair_matrix)
            st.subheader("Decrypted Text:")
            st.text(plain_text)

if __name__ == "__main__":
    main()
