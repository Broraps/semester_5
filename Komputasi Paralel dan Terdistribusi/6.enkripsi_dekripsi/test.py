import streamlit as st
from cryptography.fernet import Fernet
from io import BytesIO

# Key generation and loading
KEY_FILE = "filekey.key"

# Load or create a Fernet key
def load_key():
    try:
        # Membaca key yang sudah ada
        with open(KEY_FILE, "rb") as filekey:
            key = filekey.read()
    except FileNotFoundError:
        # Membuat key baru jika belum ada
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as filekey:
            filekey.write(key)
    return key

# Fungsi untuk mengenkripsi file
def encrypt_file(file_data, fernet):
    return fernet.encrypt(file_data)

# Fungsi untuk mendekripsi file
def decrypt_file(file_data, fernet):
    return fernet.decrypt(file_data)

# Inisialisasi Streamlit
st.title("Enkripsi dan Dekripsi File")
st.write("Upload file untuk dienkripsi atau didekripsi.")

# Load key and initialize Fernet
key = load_key()
fernet = Fernet(key)

# File uploader
uploaded_file = st.file_uploader("Upload file", type=["csv", "txt", "pdf", "docx", "rar"])
action = st.selectbox("Pilih Aksi", ["Enkripsi", "Dekripsi"])

if uploaded_file is not None:
    file_data = uploaded_file.read()  # Membaca konten file
    file_name = uploaded_file.name
    
    if action == "Enkripsi":
        # Proses enkripsi
        encrypted_data = encrypt_file(file_data, fernet)
        encrypted_file = BytesIO(encrypted_data)
        st.download_button(
            label="Download File Terenkripsi",
            data=encrypted_file,
            file_name=f"{file_name}.encrypted"
        )
    elif action == "Dekripsi":
        try:
            # Proses dekripsi
            decrypted_data = decrypt_file(file_data, fernet)
            decrypted_file = BytesIO(decrypted_data)
            st.download_button(
                label="Download File Didekripsi",
                data=decrypted_file,
                file_name=file_name.replace(".encrypted", "")  # Hapus ekstensi tambahan
            )
        except Exception as e:
            st.error("Gagal mendekripsi file. Pastikan file dan kunci cocok.")
