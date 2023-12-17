import streamlit as st

def generate_playfair_matrix(key):
    key = key.replace("J", "I")  # Treat I and J as the same letter
    key = key.upper()
    key = "".join(sorted(set(key), key=key.find))  # Remove duplicate letters and sort
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = [list(key[i:i + 5]) + list(filter(lambda c: c not in key, alphabet))[j:j + 5] for i, j in zip(range(0, 25, 5), range(0, 25, 5))]
    return matrix

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)

def playfair_encrypt(plain_text, key):
    matrix = generate_playfair_matrix(key)
    cipher_text = ""
    plain_text = plain_text.upper().replace("J", "I")
    pairs = [plain_text[i:i + 2] for i in range(0, len(plain_text), 2)]

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

def playfair_decrypt(cipher_text, key):
    matrix = generate_playfair_matrix(key)
    plain_text = ""
    pairs = [cipher_text[i:i + 2] for i in range(0, len(cipher_text), 2)]

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
    # Streamlit UI
    st.title("Playfair Cipher Encryption and Decryption")
    
    action = st.radio("Select Action", ["Encrypt", "Decrypt"])
    
    key = st.text_input("Enter Key:")
    text_input_label = "Enter Plain Text to Encrypt:" if action == "Encrypt" else "Enter Cipher Text to Decrypt:"
    text_input = st.text_area(text_input_label)
    
    if st.button(f"{action} Text"):
        if key and text_input:
            if action == "Encrypt":
                result = playfair_encrypt(text_input, key)
            else:
                result = playfair_decrypt(text_input, key)
    
            st.success(f"Result: {result}")
    
    # Display Playfair Matrix
    if key:
        matrix = generate_playfair_matrix(key)
        st.text("Playfair Matrix:")
        st.table(matrix)
