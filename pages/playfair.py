import streamlit as st


def generate_playfair_matrix(key):
    key = key.replace("J", "I")
    key = "".join(sorted(set(key), key=key.index))
    matrix = [['' for _ in range(5)] for _ in range(5)]
    k = 0
    for i in range(5):
        for j in range(5):
            if k < len(key):
                matrix[i][j] = key[k]
                k += 1
            else:
                for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
                    if ch not in key:
                        matrix[i][j] = ch
                        break
    return matrix


def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return None


def encrypt(plain_text, matrix):
    plain_text = plain_text.replace("J", "I")
    pairs = [plain_text[i:i + 2] for i in range(0, len(plain_text), 2)]
    cipher_text = ""
    for pair in pairs:
        row1, col1 = find_position(matrix, pair[0])
        row2, col2 = find_position(matrix, pair[1])
        if row1 == row2:
            cipher_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            cipher_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            cipher_text += matrix[row1][col2] + matrix[row2][col1]
    return cipher_text


def decrypt(cipher_text, matrix):
    pairs = [cipher_text[i:i + 2] for i in range(0, len(cipher_text), 2)]
    plain_text = ""
    for pair in pairs:
        row1, col1 = find_position(matrix, pair[0])
        row2, col2 = find_position(matrix, pair[1])
        if row1 == row2:
            plain_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plain_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            plain_text += matrix[row1][col2] + matrix[row2][col1]
    return plain_text


def playfair_page():
    st.title("Playfair Cipher Encryption/Decryption")

    option = st.radio("Select an option:", ("Encrypt", "Decrypt"))

    key = st.text_input("Enter the key:")
    plain_text = st.text_input("Enter the plain text:")

    if key and plain_text:
        key = key.upper()
        matrix = generate_playfair_matrix(key)

        st.text("Playfair Matrix:")
        st.write(matrix)

        if option == "Encrypt":
            cipher_text = encrypt(plain_text.upper(), matrix)
            st.success(f"Encrypted Text: {cipher_text}")
        else:
            cipher_text = st.text_input("Enter the cipher text:")
            if cipher_text:
                plain_text = decrypt(cipher_text.upper(), matrix)
                st.success(f"Decrypted Text: {plain_text}")
