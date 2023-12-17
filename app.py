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

def find_position(matrix, char):
    # Find the position of a character in the Playfair matrix
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

def encrypt_playfair(plain_text, playfair_matrix):
    def handle_same_row(i, j, matrix):
        return matrix[i][(j + 1) % 5], matrix[i][(j + 1) % 5]

    def handle_same_column(i, j, matrix):
        return matrix[(i + 1) % 5][j], matrix[(i + 1) % 5][j]

    def handle_different_row_column(i1, j1, i2, j2, matrix):
        return matrix[i1][j2], matrix[i2][j1]

    def process_bigrams(bigrams, matrix, encrypt=True):
        result = []
        for bigram in bigrams:
            char1, char2 = bigram[0], bigram[1]
            i1, j1 = find_position(matrix, char1)
            i2, j2 = find_position(matrix, char2)

            if i1 == i2:
                result.extend(handle_same_row(i1, j1, matrix))
            elif j1 == j2:
                result.extend(handle_same_column(i1, j1, matrix))
            else:
                result.extend(handle_different_row_column(i1, j1, i2, j2, matrix))

        return result

    plain_text = plain_text.replace("J", "I")  # Replace 'J' with 'I'
    bigrams = [plain_text[i:i + 2] for i in range(0, len(plain_text), 2)]

    result = process_bigrams(bigrams, playfair_matrix)

    return "".join(result)

def decrypt_playfair(cipher_text, playfair_matrix):
    def process_bigrams(bigrams, matrix):
        result = []
        for bigram in bigrams:
            char1, char2 = bigram[0], bigram[1]
            i1, j1 = find_position(matrix, char1)
            i2, j2 = find_position(matrix, char2)

            if i1 == i2:
                result.extend(handle_same_row(i1, j1, matrix))
            elif j1 == j2:
                result.extend(handle_same_column(i1, j1, matrix))
            else:
                result.extend(handle_different_row_column(i1, j1, i2, j2, matrix))

        return result

    bigrams = [cipher_text[i:i + 2] for i in range(0, len(cipher_text), 2)]

    result = process_bigrams(bigrams, playfair_matrix)

    return "".join(result)

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
