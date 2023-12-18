import streamlit as st
from PIL import Image
import io

def xor_decrypt(image_path, key):
    try:
        image = Image.open(image_path)
        pixels = image.load()
        width, height = image.size

        decrypted_data = bytearray()
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                decrypted_data.append(r ^ key[x % len(key)])

        decrypted_text = decrypted_data.decode('utf-8')
        return decrypted_text
    except Exception as e:
        return f"Error: {str(e)}"


def brute_force_decrypt(image_path):
    results = {}
    for key in range(256):  # Assuming key values are between 0 and 255
        try:
            decrypted_text = xor_decrypt(image_path, bytes([key] * 6))
            results[key] = decrypted_text
        except:
            pass
    return results


def main():
    st.title("Image Decryption with XOR Cipher")

    task_description = """
    Upload an encrypted image (crypto01.jpg) and find the flag.
    The image was encrypted with an XOR cipher using a 6-letter key.
    """
    st.markdown(task_description)

    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg"])

    if uploaded_file is not None:
        key = st.text_input("Enter the 6-letter key:")
        if len(key) != 6:
            st.warning("Please enter a 6-letter key.")
        else:
            if st.button("Decrypt Image"):
                try:
                    image_bytes = uploaded_file.read()
                    image_path = io.BytesIO(image_bytes)
                    decrypted_text = xor_decrypt(image_path, key.encode('utf-8'))
                    st.text(f"Decrypted Flag: {decrypted_text}")
                except Exception as e:
                    st.error(f"Error decrypting image: {str(e)}")

            if st.button("Brute-Force Decrypt"):
                try:
                    image_bytes = uploaded_file.read()
                    image_path = io.BytesIO(image_bytes)
                    brute_force_results = brute_force_decrypt(image_path)
                    st.text("Brute-Force Decryption Results:")
                    for possible_key, possible_flag in brute_force_results.items():
                        st.text(f"Key: {possible_key}, Flag: {possible_flag}")
                except Exception as e:
                    st.error(f"Error during brute-force decryption: {str(e)}")

if __name__ == "__main__":
    main()
