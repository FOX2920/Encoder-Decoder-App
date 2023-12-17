# app.py
import streamlit as st
from pages.Vigenere import vigenere_page
from pages.playfair import playfair_page

def main():
    st.sidebar.title("Choose a Cipher")
    selected_cipher = st.sidebar.radio("", ("Vigenère Cipher", "Playfair Cipher"))

    if selected_cipher == "Vigenère Cipher":
        vigenere_page()
    elif selected_cipher == "Playfair Cipher":
        playfair_page()

if __name__ == "__main__":
    main()
