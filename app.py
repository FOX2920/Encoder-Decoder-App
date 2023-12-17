import streamlit as st

def generate_playfair_matrix(key):
    key = key.upper().replace('J', 'I')  # Convert to uppercase and replace 'J' with 'I'
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key_set = set(key)
    remaining_letters = [l for l in alphabet if l not in key_set]

    matrix = [[0] * 5 for _ in range(5)]
    key += ''.join(remaining_letters)

    k = 0
    for i in range(5):
        for j in range(5):
            matrix[i][j] = key[k]
            k += 1

    return matrix

def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

def playfair_encrypt(plain_text, key):
    matrix = generate_playfair_matrix(key)
    encrypted_text = ""
    plain_text = plain_text.upper().replace('J', 'I')

    i = 0
    while i < len(plain_text):
        char1 = plain_text[i]
        char2 = plain_text[i + 1] if i + 1 < len(plain_text) else 'X'

        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        if row1 == row2:  # Same row
            encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Same column
            encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:  # Different row and column
            encrypted_text += matrix[row1][col2] + matrix[row2][col1]

        i += 2

    return encrypted_text

def playfair_decrypt(cipher_text, key):
    matrix = generate_playfair_matrix(key)
    decrypted_text = ""

    i = 0
    while i < len(cipher_text):
        char1 = cipher_text[i]
        char2 = cipher_text[i + 1]

        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        if row1 == row2:  # Same row
            decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:  # Same column
            decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:  # Different row and column
            decrypted_text += matrix[row1][col2] + matrix[row2][col1]

        i += 2

    return decrypted_text

def main():
    st.title("Playfair Cipher Tool")

    action = st.selectbox("Select Action", ["Encrypt", "Decrypt"])

    key = st.text_input("Enter Key:")
    text = st.text_area("Enter Text:")

    if key and text:
        key_matrix = generate_playfair_matrix(key)
        st.text("Playfair Matrix:")
        st.write(key_matrix)

        if action == "Encrypt":
            result = playfair_encrypt(text, key)
            st.success(f"Encrypted Text: {result}")
        elif action == "Decrypt":
            result = playfair_decrypt(text, key)
            st.success(f"Decrypted Text: {result}")

if __name__ == "__main__":
    main()
