import streamlit as st

def generate_key_matrix(key):
    key = key.upper().replace("J", "I")
    key_matrix = [['' for _ in range(5)] for _ in range(5)]
    key_set = set()
    i, j = 0, 0
    for letter in key + 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
        if letter not in key_set:
            key_matrix[i][j] = letter
            key_set.add(letter)
            j += 1
            if j == 5:
                i += 1
                j = 0
    return key_matrix

def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

def playfair_encrypt(plain_text, key_matrix):
    plain_text = plain_text.upper().replace("J", "I")
    cipher_text = ""
    for i in range(0, len(plain_text), 2):
        pair1 = plain_text[i]
        pair2 = plain_text[i + 1] if i + 1 < len(plain_text) else 'X'
        row1, col1 = find_position(key_matrix, pair1)
        row2, col2 = find_position(key_matrix, pair2)
        if row1 == row2:
            cipher_text += key_matrix[row1][(col1 + 1) % 5] + key_matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            cipher_text += key_matrix[(row1 + 1) % 5][col1] + key_matrix[(row2 + 1) % 5][col2]
        else:
            cipher_text += key_matrix[row1][col2] + key_matrix[row2][col1]
    return cipher_text

def playfair_decrypt(cipher_text, key_matrix):
    plain_text = ""
    for i in range(0, len(cipher_text), 2):
        pair1 = cipher_text[i]
        pair2 = cipher_text[i + 1]
        row1, col1 = find_position(key_matrix, pair1)
        row2, col2 = find_position(key_matrix, pair2)
        if row1 == row2:
            plain_text += key_matrix[row1][(col1 - 1) % 5] + key_matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plain_text += key_matrix[(row1 - 1) % 5][col1] + key_matrix[(row2 - 1) % 5][col2]
        else:
            plain_text += key_matrix[row1][col2] + key_matrix[row2][col1]
    return plain_text

def main():
    st.title("Playfair Cipher Encryption/Decryption")

    key = st.text_input("Enter the key:")
    plain_text = st.text_input("Enter the plain text:")
    cipher_text = st.text_input("Enter the cipher text:")

    key_matrix = generate_key_matrix(key)

    st.text("Playfair Matrix:")
    for row in key_matrix:
        st.text(row)

    if st.button("Encrypt"):
        if plain_text:
            encrypted_text = playfair_encrypt(plain_text, key_matrix)
            st.success(f"Encrypted Text: {encrypted_text}")
        else:
            st.warning("Please enter plain text.")

    if st.button("Decrypt"):
        if cipher_text:
            decrypted_text = playfair_decrypt(cipher_text, key_matrix)
            st.success(f"Decrypted Text: {decrypted_text}")
        else:
            st.warning("Please enter cipher text.")
    key_matrix = generate_key_matrix(key)
    st.table(key_matrix)
if __name__ == "__main__":
    main()
