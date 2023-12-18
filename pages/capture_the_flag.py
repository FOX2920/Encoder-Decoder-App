import streamlit as st

def ascii_to_text(ascii_text):
    try:
        text = ''.join(chr(int(code)) for code in ascii_text.split())
        return text
    except ValueError:
        return "Invalid ASCII codes"

def text_to_ascii(text):
    return ' '.join(str(ord(char)) for char in text)

def main():
    st.title("Capture The Flag")

    operation = st.radio("Select Operation:", ["ASCII to Text", "Text to ASCII"])

    if operation == "Decode ASCII to Text":
        ascii_input = st.text_area("Enter ASCII Codes:")
        if st.button("Decode"):
            decoded_text = ascii_to_text(ascii_input)
            st.text(f"Decoded Text: {decoded_text}")

    elif operation == "Encode Text to ASCII":
        text_input = st.text_area("Enter Text:")
        if st.button("Encode"):
            encoded_ascii = text_to_ascii(text_input)
            st.text(f"Encoded ASCII Codes: {encoded_ascii}")

if __name__ == "__main__":
    main()
