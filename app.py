import streamlit as st

# Define alphabet and remove invalid characters
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Function to create Playfair matrix
def create_matrix(key):
  matrix = [[None for _ in range(5)] for _ in range(5)]
  key = key.upper().replace("J", "I")
  used_letters = set()
  for letter in key:
    if letter not in used_letters:
      used_letters.add(letter)
      for i in range(5):
        for j in range(5):
          if matrix[i][j] is None:
            matrix[i][j] = letter
            break
  for letter in ALPHABET:
    if letter not in used_letters:
      for i in range(5):
        for j in range(5):
          if matrix[i][j] is None:
            matrix[i][j] = letter
            break
  return matrix

# Function to process text into pairs
def process_text(text):
  processed_text = text.upper().replace(" ", "").replace("J", "I")
  if len(processed_text) % 2 != 0:
    processed_text += "X"
  return [processed_text[i:i+2] for i in range(0, len(processed_text), 2)]

# Function to encrypt a message
def encrypt(text, matrix):
  pairs = process_text(text)
  ciphertext = ""
  for pair in pairs:
    i1, j1, i2, j2 = get_coordinates(pair[0], pair[1], matrix)
    if i1 == i2:
      ciphertext += matrix[(i1 + 1) % 5][j1] + matrix[(i2 + 1) % 5][j2]
    elif j1 == j2:
      ciphertext += matrix[i1][(j1 + 1) % 5] + matrix[i2][(j2 + 1) % 5]
    else:
      ciphertext += matrix[i1][j2] + matrix[i2][j1]
  return ciphertext

# Function to decrypt a message
def decrypt(ciphertext, matrix):
  pairs = process_text(ciphertext)
  plaintext = ""
  for pair in pairs:
    i1, j1, i2, j2 = get_coordinates(pair[0], pair[1], matrix)
    if i1 == i2:
      plaintext += matrix[(i1 - 1) % 5][j1] + matrix[(i2 - 1) % 5][j2]
    elif j1 == j2:
      plaintext += matrix[i1][(j1 - 1) % 5] + matrix[i2][(j2 - 1) % 5]
    else:
      plaintext += matrix[i1][j2] + matrix[i2][j1]
  return plaintext

# Function to get coordinates of a letter in the matrix
def get_coordinates(letter, matrix):
  for i in range(5):
    for j in range(5):
      if matrix[i][j] == letter:
        return i, j, i, j

# Streamlit app
st.title("Playfair Cipher")

# Input fields for key and text
key_input = st.text_input("Key", max_chars=25)
text_input = st.text_input("Text", max_chars=250)
mode_select = st.radio("Mode", ["Encrypt", "Decrypt"])

# Button to execute encryption or decryption
if st.button("Submit"):
  if mode_select == "Encrypt":
    matrix = create_matrix(key_input)
    st.write("Playfair Matrix:")
    st.write(matrix)
    ciphertext = encrypt(text_input, matrix)
    st.write("Ciphertext:", ciphertext)
  elif mode_select == "Decrypt":
    matrix = create_matrix(key_input)
    st.write("Playfair Matrix:")
    st.write(matrix)
    plaintext = decrypt(text_input, matrix)
    st.write("Plaintext:", plaintext)
