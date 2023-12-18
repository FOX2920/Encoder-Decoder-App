import streamlit as st
from pages import Caesar, Playfair, Vigenere, XOR_cipher, Capture_the_flag
# Chọn ứng dụng
selected_app = st.sidebar.selectbox("Chọn ứng dụng", ["Caesar", "Playfair", "Vigenere", "XOR_cipher", "Capture_the_flag"])

# Hiển thị ứng dụng được chọn
if selected_app == "Caesar":
    Caesar.main()
elif selected_app == "Playfair":
    Playfair.main()
elif selected_app == "Vigenere":
    Vigenere.main()
elif selected_app == "Capture_the_flag":
    Capture_the_flag.main()
else:
    Caesar.main()
  
