import streamlit as st

# Define functions for Playfair cipher
def generate_matrix(key):
    """
    Generates the Playfair matrix based on a key.

    Args:
        key: The key string used to populate the matrix.

    Returns:
        A 5x5 matrix with letters from the key and remaining alphabets.
    """
    key = key.replace(" ", "").upper()
    matrix = []
    used_letters = set(key)
    for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if char not in used_letters:
            used_letters.add(char)
            matrix.append(char)
        if len(matrix) == 25:
            break
    matrix = [matrix[i:i + 5] for i in range(0, len(matrix), 5)]
    return matrix


def playfair_encrypt(plaintext, key):
    """
    Encrypts a plaintext message using Playfair cipher.

    Args:
        plaintext: The plaintext message to encrypt.
        key: The key string used for encryption.

    Returns:
        The encrypted ciphertext.
    """
    plaintext = plaintext.replace(" ", "").upper()
    matrix = generate_matrix(key)
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        pair1, pair2 = plaintext[i:i + 2], plaintext[i + 1:i + 3]
        if pair2 == "":
            pair2 = "X"
        row1, col1 = find_coordinates(pair1[0], matrix)
        row2, col2 = find_coordinates(pair2[0], matrix)
        if row1 == row2:
            new_col1 = (col1 + 1) % 5
            new_col2 = (col2 + 1) % 5
        elif col1 == col2:
            new_row1 = (row1 + 1) % 5
            new_row2 = (row2 + 1) % 5
        else:
            new_col1, new_col2 = col1, col2
        ciphertext += matrix[new_row1][new_col1] + matrix[new_row2][new_col2]
    return ciphertext


def playfair_decrypt(ciphertext, key):
    """
    Decrypts a ciphertext message using Playfair cipher.

    Args:
        ciphertext: The ciphertext message to decrypt.
        key: The key string used for decryption.

    Returns:
        The decrypted plaintext.
    """
    ciphertext = ciphertext.upper()
    matrix = generate_matrix(key)
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        pair1, pair2 = ciphertext[i:i + 2], ciphertext[i + 1:i + 3]
        row1, col1 = find_coordinates(pair1[0], matrix)
        row2, col2 = find_coordinates(pair2[0], matrix)
        if row1 == row2:
            new_col1 = (col1 - 1) % 5
            new_col2 = (col2 - 1) % 5
        elif col1 == col2:
            new_row1 = (row1 - 1) % 5
            new_row2 = (row2 - 1) % 5
        else:
            new_col1, new_col2 = col2, col1
        plaintext += matrix[new_row1][new_col1] + matrix[new_row2][new_col2]
    return plaintext


def find_coordinates(letter, matrix):
    """
    Finds the row and column of a letter in the Playfair matrix.

    Args:
        letter: The letter to find the coordinates for.
        matrix: The Playfair matrix.

    Returns:
        The row and column of the letter in the matrix.
    """
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col
    raise ValueError(f"Letter '{letter}' not found in Playfair matrix!")

# Streamlit app
st.title("Playfair Cipher")

st.subheader("Encryption / Decryption")

# Input key
key = st.text_input("Enter the key:")

# Input plaintext or ciphertext
input_text = st.text_area("Enter the plaintext or ciphertext:")

# Choose encryption or decryption
encryption_mode = st.radio("Choose mode:", ["Encrypt", "Decrypt"])

if st.button("Process"):
    if encryption_mode == "Encrypt":
        result = playfair_encrypt(input_text, key)
    else:
        result = playfair_decrypt(input_text, key)

    # Display Playfair matrix
    st.subheader("Playfair Matrix")
    matrix = generate_matrix(key)
    for row in matrix:
        st.write(row)

    # Display result
    st.subheader("Result")
    st.write(result)
