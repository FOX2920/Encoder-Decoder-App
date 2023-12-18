import streamlit as st

def caesar_cipher(text, key, decrypt=False):
    result = ""
    for char in text:
        if char.isalpha():
            shift = key % 26
            if char.isupper():
                result += chr((ord(char) - shift - 65) % 26 + 65) if decrypt else chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) - shift - 97) % 26 + 97) if decrypt else chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def brute_force_decrypt(ciphertext):
    results = {}
    for key in range(26):
        decrypted_text = caesar_cipher(ciphertext, key, decrypt=True)
        results[key] = decrypted_text
    return results

def main():
    st.title("Caesar Cipher Encryption and Decryption")

    operation = st.radio("Select Operation:", ["Encryption", "Decryption", "Brute-Force Attack"])

    if operation in ["Encryption", "Decryption"]:
        key = st.number_input("Enter Key:", min_value=0, max_value=25, step=1, value=3)
        input_text = st.text_area(f"Enter {'Plaintext' if operation == 'Encryption' else 'Ciphertext'}:")
        if st.button(f"Perform {operation}"):
            result = caesar_cipher(input_text, key) if operation == "Encryption" else caesar_cipher(input_text, key, decrypt=True)
            st.text(f"{operation} Result: {result}")

    elif operation == "Brute-Force Attack":
        ciphertext = st.text_area("Enter Ciphertext:")
        if st.button("Perform Brute-Force Attack"):
            results = brute_force_decrypt(ciphertext)
            st.text("Brute-Force Attack Results:")
            for key, decrypted_text in results.items():
                st.text(f"Key {key}: {decrypted_text}")

if __name__ == "__main__":
    main()
