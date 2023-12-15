import streamlit as st
import re
from collections import Counter

def caesar_cipher(text, key, decrypt=False):
    result = ""
    for char in text:
        if char.isalpha():
            shift = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - shift + key * (1 if not decrypt else -1)) % 26 + shift)
        else:
            result += char
    return result

def brute_force_decrypt(ciphertext):
    for key in range(26):
        decrypted_text = caesar_cipher(ciphertext, key, decrypt=True)
        st.write(f"Key {key}: {decrypted_text}")

def analyze_frequency(ciphertext):
    ciphertext = re.sub(r'[^a-zA-Z]', '', ciphertext)
    frequencies = Counter(ciphertext)
    sorted_frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
    return sorted_frequencies

def decrypt_ciphertext(ciphertext, mapping):
    decrypted_text = ''.join(mapping.get(char, char) for char in ciphertext)
    return decrypted_text

def main():
    st.title("Cipher Decryption with Streamlit")

    operation = st.sidebar.radio("Choose Operation", ["Caesar Cipher", "Brute Force Decrypt"])

    if operation == "Caesar Cipher":
        key = st.sidebar.number_input("Enter Key", min_value=0, max_value=25, value=3)
        text = st.text_area(f"Enter {'Plaintext' if key > 0 else 'Ciphertext'}", "")
        result = caesar_cipher(text, key, decrypt=(key > 0))
        st.write(f"Result: {result}")

    elif operation == "Brute Force Decrypt":
        ciphertext = st.text_area("Enter Ciphertext", "")
        if st.button("Brute Force Decrypt"):
            brute_force_decrypt(ciphertext)

            # Perform frequency analysis
            st.write("Frequency Analysis:")
            symbol_frequencies = analyze_frequency(ciphertext)
            st.write(symbol_frequencies)

            # English letter frequencies for reference
            english_frequencies = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

            # Initial mapping (replace this with your guesses)
            mapping = dict(zip([sym for sym, _ in symbol_frequencies], english_frequencies))

            # Decrypt the text
            decrypted_text = decrypt_ciphertext(ciphertext, mapping)

            st.write("\nDecrypted Text:")
            st.write(decrypted_text)

if __name__ == "__main__":
    main()
