# Aplikasi Konversi Nilai Angka Ke Nilai Huruf

print("APLIKASI KONVERSI NILAI ANGKA KE HURUF")
print("By : Irfan Kurniawan ")

# Inisialisasi Variabel
nilai = int(input("Masukkan Nilai Anda : "))

# Konversi Nilai
if nilai > 100 or nilai < 0 :
  print("Nilai Tidak Valid")
elif nilai >= 80 :
  print("Nilai Anda adalah " + str(nilai) + " Predikat nilai anda : A")
elif nilai >= 70 and nilai < 80 :
  print("Nilai Anda adalah " + str(nilai) + " Predikat nilai anda : B")
elif nilai >= 60 and nilai < 70 :
  print("Nilai Anda adalah " + str(nilai) + " Predikat nilai anda : C")
elif nilai >= 50 and nilai < 60 :
  print("Nilai Anda adalah " + str(nilai) + " Predikat nilai anda : D")
else :
  print("Nilai Anda adalah " + str(nilai) + " Predikat nilai anda : E")