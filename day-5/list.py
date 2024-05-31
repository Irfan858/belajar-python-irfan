# Mendefinisikan List
nama_buah = ["Apel", "Mangga", "Anggur", "Jeruk"]
# Tuple
nama_siswa = ("Irfan", "Yoga", "Lengga", "Elly", "Nabila")

# Menampilkan Isi Dari Lit dan Tuple
# List
print(nama_buah)

# Tuple
print(nama_siswa)

# Menampilkan satu Isi dari List
# List
print(nama_buah[1])
print(nama_siswa[1:3])

# Menampilkan Element list dan tupple dengan perulangan
# List
for buah in nama_buah :
  print(buah)
  
# Tupple
for siswa in nama_siswa :
  print(siswa)

# Memanipulasi List
# 1. Menghitung Jumlah Elemen dalam List
jumlah_elemen = len(nama_buah)
print(jumlah_elemen)

# 2. Mengurutkan Elemen dalam List
# ASCENDING
# Sebelum diurutkan
# print(nama_buah)
# Proses Pengurutan Data
# nama_buah.sort()
# Menampilkan hasil dari pengurutan
# print(nama_buah)

# DESCENDING
# Sebelum diurutkan
# print(nama_buah)
# Urutkan Elemen
# nama_buah.sort(reverse=True)
# Tampilkan Elemen setelah diurutkan
# print(nama_buah)

# 3. Menambahkan Element Baru
# Sebelum diurutkan
# print(nama_buah)
# Menambah Element Baru
# nama_buah.append("Pisang")
# Menampilkan Kembali List yang telah ditambahkan elemen baru
# print(nama_buah)

# Modifikasi Tuple
# nama_siswa.append("Rosa")

# 4. Menganti isi element pada List 
# Sebelum diubah
print(nama_buah)
# Mengubah isi Element
nama_buah[2] = "Melon"
# Setelah Di Ubah
print(nama_buah)

# 5. Menghapus Element pada List
# Sebelum dihapus
print(nama_buah)
# Menhapus isi Element
nama_buah.pop()
# Setelah Dihapus
print(nama_buah)
# Menghapus Element yang dipilih
nama_buah.remove("Apel")
# Setelah Dihapus
print(nama_buah)
