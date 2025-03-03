import requests

# URL endpoint dari web service
url = "https://example.com/api/users"

# XML data yang akan dikirim
xml_data = """<?xml version="1.0" encoding="UTF-8"?>
<NewUser>
    <Name>John Doe</Name>
    <Email>johndoe@example.com</Email>
    <Age>28</Age>
</NewUser>"""

# Header yang menunjukkan bahwa request menggunakan XML
headers = {
    "Content-Type": "application/xml"
}

# Mengirim request POST dengan data XML
response = requests.put(url, data=xml_data, headers=headers)

# Memeriksa hasil respons dari server
if response.status_code == 200:
    print("Request berhasil!")
    print("Respons dari server:", response.text)
else:
    print("Request gagal dengan status code:", response.status_code)
    print("Pesan error:", response.text)
