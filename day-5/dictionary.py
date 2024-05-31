# Mendefinisikan Dictionary
biodata = {"nama": "Irfan Kurniawan", "umur": 23, "alamat": "Dharmasraya"}

# Memanggil Dictionary
print(biodata)

# Memanggil Element Pada Dictionary
print(biodata["nama"])

# Menambah Element Baru
biodata["jurusan"] = "S2 Teknik Informatika"
# Menampilkan Dictionary Sesudah Menambahkan Element Baru
print(biodata)

# Merubah Isi Dari Element
biodata["alamat"] = "Padang"
# Menampilkan Dictionary Sesudah Merubah Isi Element
print(biodata)

# Menghapus Isi Element
del biodata["jurusan"]
# Menampilkan Dictionary Sesudah Merubah Isi Element
print(biodata)
