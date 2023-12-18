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

def playfair_encrypt(plain_text, key):
    key_matrix = generate_key_matrix(key)
    encrypted_text = ''

    # Preprocess plaintext
    plain_text = plain_text.upper().replace("J", "I")
    plain_text = [char for char in plain_text if char.isalpha()]

    # Add a placeholder letter between consecutive identical letters
    for i in range(1, len(plain_text), 2):
        if plain_text[i] == plain_text[i - 1]:
            plain_text.insert(i, 'X')

    if len(plain_text) % 2 != 0:
        plain_text.append('X')

    # Encrypt pairs of letters
    for i in range(0, len(plain_text), 2):
        char1, char2 = plain_text[i], plain_text[i + 1]
        row1, col1 = find_position(key_matrix, char1)
        row2, col2 = find_position(key_matrix, char2)

        if row1 == row2:
            encrypted_text += key_matrix[row1][(col1 + 1) % 5] + key_matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            encrypted_text += key_matrix[(row1 + 1) % 5][col1] + key_matrix[(row2 + 1) % 5][col2]
        else:
            encrypted_text += key_matrix[row1][col2] + key_matrix[row2][col1]

    return encrypted_text

def playfair_decrypt(encrypted_text, key):
    key_matrix = generate_key_matrix(key)
    decrypted_text = ''

    # Decrypt pairs of letters
    for i in range(0, len(encrypted_text), 2):
        char1, char2 = encrypted_text[i], encrypted_text[i + 1]
        row1, col1 = find_position(key_matrix, char1)
        row2, col2 = find_position(key_matrix, char2)

        if row1 == row2:
            decrypted_text += key_matrix[row1][(col1 - 1) % 5] + key_matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            decrypted_text += key_matrix[(row1 - 1) % 5][col1] + key_matrix[(row2 - 1) % 5][col2]
        else:
            decrypted_text += key_matrix[row1][col2] + key_matrix[row2][col1]

    return decrypted_text

def main():
    # Streamlit app
    st.title("Playfair Cipher Encryption and Decryption")
    
    # Input
    action = st.radio("Select Action", ["Encrypt", "Decrypt"])
    
    if action == "Encrypt":
        plaintext = st.text_input("Enter the plain text:")
        key = st.text_input("Enter the key:")
        if st.button("Encrypt"):
            encrypted_text = playfair_encrypt(plaintext, key)
            st.success(f"Encrypted Text: {encrypted_text}")
    
    elif action == "Decrypt":
        ciphertext = st.text_input("Enter the cipher text:")
        key = st.text_input("Enter the key:")
        if st.button("Decrypt"):
            decrypted_text = playfair_decrypt(ciphertext, key)
            st.success(f"Decrypted Text: {decrypted_text}")
    
    # Display Playfair matrix table
    key_matrix = generate_key_matrix(key)
    st.table(key_matrix)
if __name__ == "__main__":
    main()
