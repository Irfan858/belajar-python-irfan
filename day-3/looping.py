# Looping
# Contoh kasus
# menampilakn bilangan 1 - 10
# for i = 0; i < 5; i++ {
#   print(i)
# }

# menampilkan bilangan 1 - 10
for i in range(1,11) :
  print(i)
  
# Menampilkan Data Dari Array
list_siswa = ["Irfan", "Yoga", "Lengga", "Ely", "Nabila"]

for siswa in list_siswa :
  print(siswa)

# Menampilkan Kalimat Secara Berulang dengan Range
kalimat = "Saya Berjanji Tidak Mengulangi Lagi"

for i in range(1,2) :
  print(kalimat)
  
# Menampilkan Bilangan Ganjil
for i in range(1, 30, 2) :
  print((i), end=" ")

print("\n")
# Menampilkan Bilangan Genap
for i in range(1, 30, 2) :
  print((i)+1, end=" ")
  
print("\n")
# Menampilkan Angka Kelipatan
for i in range(4,44,4) :
  print((i), end=" ")

