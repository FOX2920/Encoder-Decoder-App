import streamlit as st

def generate_playfair_matrix(key):
    # Create a 5x5 matrix with unique letters from the key
    key = key.upper().replace("J", "I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key += alphabet
    matrix = []

    for char in key:
        if char not in matrix:
            matrix.append(char)

    playfair_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
    return playfair_matrix

def find_position(matrix, char):
    # Find the position (row, col) of a character in the matrix
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

def encrypt_playfair(plaintext, key):
    matrix = generate_playfair_matrix(key)
    ciphertext = ""
    plaintext = plaintext.upper().replace("J", "I")

    for i in range(0, len(plaintext), 2):
        pair1 = plaintext[i]
        pair2 = plaintext[i + 1] if i + 1 < len(plaintext) else 'X'

        row1, col1 = find_position(matrix, pair1)
        row2, col2 = find_position(matrix, pair2)

        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5]
            ciphertext += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1]
            ciphertext += matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2]
            ciphertext += matrix[row2][col1]

    return ciphertext

def decrypt_playfair(ciphertext, key):
    matrix = generate_playfair_matrix(key)
    plaintext = ""

    for i in range(0, len(ciphertext), 2):
        pair1 = ciphertext[i]
        pair2 = ciphertext[i + 1]

        row1, col1 = find_position(matrix, pair1)
        row2, col2 = find_position(matrix, pair2)

        if row1 == row2:
            plaintext += matrix[row1][(col1 - 1) % 5]
            plaintext += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[(row1 - 1) % 5][col1]
            plaintext += matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += matrix[row1][col2]
            plaintext += matrix[row2][col1]

    return plaintext

def display_matrix(matrix):
    for row in matrix:
        print(" ".join(row))
    print()


# Streamlit web application
def main():
    st.title("Playfair Cipher Encryption/Decryption")

    # Input key
    key = st.text_input("Enter the key for Playfair cipher:")

    # Input plaintext or ciphertext
    plaintext_or_ciphertext = st.text_area("Enter the plaintext or ciphertext:")

    # Choose encryption or decryption
    operation = st.radio("Select operation:", ['Encryption', 'Decryption'])

    # Display the Playfair matrix
    playfair_matrix = generate_playfair_matrix(key)
    st.subheader("Playfair Matrix:")
    st.table(playfair_matrix)

    # Perform encryption or decryption based on user input
    if st.button("Submit"):
        if operation == 'Encryption':
            result = encrypt_playfair(plaintext_or_ciphertext, key)
            st.success(f"Encrypted text: {result}")
        elif operation == 'Decryption':
            result = decrypt_playfair(plaintext_or_ciphertext, key)
            st.success(f"Decrypted text: {result}")

if __name__ == "__main__":
    main()
