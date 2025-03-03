import streamlit as st
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import numpy as np
import os

# Tentukan kunci 16-byte untuk AES
AES_KEY = b'1234567890abcdef'  # Contoh kunci 16 karakter

# Fungsi untuk enkripsi dan dekripsi teks menggunakan Hill Cipher
def hill_encrypt(text, key_matrix):
    text_numbers = [ord(char) for char in text]
    encrypted_numbers = []
    for i in range(0, len(text_numbers), 3):
        block = text_numbers[i:i+3]
        if len(block) < 3:
            block += [0] * (3 - len(block))
        encrypted_block = np.dot(key_matrix, block) % 256
        encrypted_numbers.extend(encrypted_block)
    encrypted_text = ''.join(chr(num) for num in encrypted_numbers)
    return encrypted_text

def hill_decrypt(text, key_matrix_inv):
    text_numbers = [ord(char) for char in text]
    decrypted_numbers = []
    for i in range(0, len(text_numbers), 3):
        block = text_numbers[i:i+3]
        decrypted_block = np.dot(key_matrix_inv, block) % 256
        decrypted_numbers.extend(decrypted_block)
    decrypted_text = ''.join(chr(int(num)) for num in decrypted_numbers if int(num) != 0)
    return decrypted_text

# Fungsi untuk enkripsi file biner menggunakan AES
def aes_encrypt_file(input_file, key):
    cipher = AES.new(key, AES.MODE_EAX)
    with open(input_file, 'rb') as f:
        plaintext = f.read()
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    encrypted_file = input_file.replace('.', '_enkrip.')
    with open(encrypted_file, 'wb') as f:
        f.write(cipher.nonce)
        f.write(tag)
        f.write(ciphertext)
    return encrypted_file

# Fungsi untuk dekripsi file biner menggunakan AES
def aes_decrypt_file(input_file, key):
    decrypted_file = input_file.replace('_enkrip', '_dekrip')
    with open(input_file, 'rb') as f:
        nonce = f.read(16)
        tag = f.read(16)
        ciphertext = f.read()
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    with open(decrypted_file, 'wb') as f:
        f.write(plaintext)
    return decrypted_file

# Fungsi utama Streamlit
def main():
    st.title("Enkripsi Dan Dekripsi File")
    st.write("Encrypt and decrypt `.txt` files using Hill Cipher, and `.pdf`, `.docx`, `.rar` using AES.")

    # Pilihan mode
    mode = st.radio("Choose a mode:", ("Encrypt", "Decrypt"))

    # Upload file
    uploaded_file = st.file_uploader("Upload a file", type=['txt', 'pdf', 'docx', 'rar'])
    hill_key_matrix = np.array([[1, 1, 0], [1, 2, 1], [1, 3, 3]])
    hill_key_matrix_inv = np.linalg.inv(hill_key_matrix).astype(int) % 256

    if uploaded_file is not None:
        with open(uploaded_file.name, 'wb') as f:
            f.write(uploaded_file.getbuffer())

        # Mode Enkripsi
        if mode == "Encrypt":
            if uploaded_file.name.endswith('.txt'):
                with open(uploaded_file.name, 'r') as f:
                    plaintext = f.read()
                encrypted_text = hill_encrypt(plaintext, hill_key_matrix)
                encrypted_file_path = uploaded_file.name.replace('.', '_enkrip.')
                with open(encrypted_file_path, 'w') as f:
                    f.write(encrypted_text)
                st.success("Text file encrypted with Hill Cipher!")
                with open(encrypted_file_path, "rb") as f:
                    st.download_button("Download Encrypted File", f, file_name=os.path.basename(encrypted_file_path))
            else:
                encrypted_file_path = aes_encrypt_file(uploaded_file.name, AES_KEY)
                st.success("Binary file encrypted with AES!")
                with open(encrypted_file_path, "rb") as f:
                    st.download_button("Download Encrypted File", f, file_name=os.path.basename(encrypted_file_path))

        # Mode Dekripsi
        elif mode == "Decrypt":
            if uploaded_file.name.endswith('_enkrip.txt'):
                with open(uploaded_file.name, 'r') as f:
                    encrypted_text = f.read()
                decrypted_text = hill_decrypt(encrypted_text, hill_key_matrix_inv)
                decrypted_file_path = uploaded_file.name.replace('_enkrip', '_dekrip')
                with open(decrypted_file_path, 'w') as f:
                    f.write(decrypted_text)
                st.success("Text file decrypted with Hill Cipher!")
                
                # Verifikasi apakah file dekrip tersedia
                if os.path.exists(decrypted_file_path):
                    with open(decrypted_file_path, "rb") as f:
                        st.download_button("Download Decrypted File", f, file_name=os.path.basename(decrypted_file_path))
                else:
                    st.error("Decrypted file not found.")
                    
            elif uploaded_file.name.endswith('_enkrip'):
                decrypted_file_path = aes_decrypt_file(uploaded_file.name, AES_KEY)
                st.success("Binary file decrypted with AES!")
                
                # Verifikasi apakah file dekrip tersedia
                if os.path.exists(decrypted_file_path):
                    with open(decrypted_file_path, "rb") as f:
                        st.download_button("Download Decrypted File", f, file_name=os.path.basename(decrypted_file_path))
                else:
                    st.error("Decrypted file not found.")

        # Hapus file asli setelah proses
        os.remove(uploaded_file.name)

if __name__ == "__main__":
    main()
