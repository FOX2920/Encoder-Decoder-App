import streamlit as st

def caesar_cipher(text, key, decrypt=False):
    result = ""
    for char in text:
        if char.isalpha():
            shift = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - shift + key * (1 if not decrypt else -1)) % 26 + shift)
        else:
            result += char
    return result

def brute_force(ciphertext, mapping=None):
    results = []
    for key in range(26):
        decrypted_text = caesar_cipher(ciphertext, key, decrypt=True)
        if mapping:
            decrypted_text = apply_mapping(decrypted_text, mapping)
        results.append(f"Key {key}: {decrypted_text}")
    return results

def apply_mapping(text, mapping):
    return ''.join(mapping.get(char, char) for char in text)

def main():
    st.title("Caesar Cipher Encryption/Decryption")

    operation = st.sidebar.radio("Choose Operation", ["Encrypt", "Decrypt", "Brute Force Decrypt", "Brute Force Encrypt"])

    key = st.sidebar.number_input("Enter Key", min_value=0, max_value=25, value=3)

    # Given mapping for decryption
    mapping = {
        '5': 'a', '2': 'b', '-': 'c', '†': 'd', '8': 'e', '1': 'f', '3': 'g', '4': 'h',
        '6': 'i', '0': 'j', '9': 'k', '*': 'l', '‡': 'm', '.': 'n', '$': 'o',
        '(': 'p', ')': 'q', ';': 'r', '?': 's', '¶': 't', ']': 'u', '¢': 'v', ':': 'w',
        '[': 'x', ':': 'y', '[': 'z'
    }

    if operation == "Brute Force Decrypt" or operation == "Brute Force Encrypt":
        ciphertext = st.text_area("Enter Ciphertext", "")
        if st.button(f"Brute Force {operation.split(' ')[-1]}"):
            results = brute_force(ciphertext, mapping if operation == "Brute Force Decrypt" else None)
            for result in results:
                st.write(result)
    else:
        text = st.text_area(f"Enter {'Plaintext' if operation=='Encrypt' else 'Ciphertext'}", "")
        result = caesar_cipher(text, key, decrypt=(operation == "Decrypt"))
        result_with_mapping = apply_mapping(result, mapping)

        st.write(f"Result: {result_with_mapping}")

if __name__ == "__main__":
    main()
