# Library
import os
import math

# Membersihkan Layar
os.system('cls')


# SCREEN
# Main Screen
def main_screen() :
  print("Selamat Datang Di Aplikasi Menghitung Luas Dan Keliling Bangun Datar")
  print("By : Irfan Kurniawan")
  print("Pilihan Bangun Datar")
  print("1. Persegi")
  print("2. Persegi Panjang")
  print("3. Segitiga")
  print("4. Lingkaran")
  print("5. Belah Ketupat")
  print("0. Keluar")
  print("\n")
  pilihan = int(input("Masukkan Pilihan :"))
  
  if pilihan == 1 :
    persegi()
  elif pilihan == 2 :
    persegi_panjang()
  elif pilihan == 3 :
    segitiga()
  elif pilihan == 4 :
    lingkaran()
  elif pilihan == 5 :
    belah_ketupat()
  elif pilihan == 0 :
    quit()
    
# Opsi Pilihan Lanjut atau Keluar
def exit() :
  pilihan = input("Apakah Akan Melanjutkan y/n : ")
  
  if pilihan == "y" :
    os.system('cls')
    main_screen()
  elif pilihan == "n" :
    quit()

# Function Bangun Datar

# Persegi
def persegi() :
  os.system('cls')
  sisi = int(input(("Masukkan Sisi : ")))
  
  keliling = 4 * sisi
  luas = sisi * sisi
  
  print("Luas Dan Keliling Persegi")
  print("Sisi : " + str(sisi) + " cm")
  print("Luas : " + str(luas) + " cm^2")
  print("Keliling : " + str(keliling) + " cm")
  print("\n")
  exit()

# Persegi Panjang
def persegi_panjang() :
  os.system('cls')
  panjang = int(input(("Masukkan Panjang : ")))
  lebar = int(input(("Masukkan Lebar : ")))
    
  keliling = (2 * panjang) + (2 * lebar)
  luas = panjang * lebar
  
  print("Luas Dan Keliling Persegi")
  print("Panjang : " + str(panjang) + " cm")
  print("Lebar : " + str(lebar) + " cm") 
  print("Luas : " + str(luas) + " cm^2")
  print("Keliling : " + str(keliling) + " cm")
  print("\n")
  exit()

# Segitiga
def segitiga() :
  os.system('cls')
  alas = int(input(("Masukkan Alas : ")))
  tinggi = int(input(("Masukkan Tinggi : ")))
  sisi_miring = math.sqrt((alas * alas) +(tinggi * tinggi))
  
  keliling = alas + tinggi + sisi_miring
  luas = (alas * tinggi) / 2
  
  print("Luas Dan Keliling Persegi")
  print("Alas : " + str(alas) + " cm")
  print("Tinggi : " + str(tinggi) + " cm") 
  print("Sisi Miring : " + str(sisi_miring) + " cm") 
  print("Luas : " + str(luas) + " cm^2")
  print("Keliling : " + str(keliling) + " cm")
  print("\n")
  exit()

# Lingkaran
def lingkaran() :
  os.system('cls')
  jari = int(input(("Masukkan Panjang Jari-Jari Lingkaran : ")))
  phi = 3.14
  
  keliling = 2 * phi * jari
  luas = phi * jari * jari
  
  print("Luas Dan Keliling Persegi")
  print("Panjang Jari-Jari Lingkaran : " + str(jari) + " cm")
  print("Luas : " + str(luas) + " cm^2")
  print("Keliling : " + str(keliling) + " cm")
  print("\n")
  exit()

# Belah Ketupat
def belah_ketupat() :
  os.system('cls')
  sisi = int(input(("Masukkan Sisi : ")))
  diagonal_1 = int(input(("Masukkan Diagonal 1 : ")))
  diagonal_2 = int(input(("Masukkan Diagonal 2 : ")))
  
  
  keliling = 4 * sisi
  luas = (diagonal_1 * diagonal_2) / 2
  
  print("Luas Dan Keliling Belah Ketupat")
  print("Sisi : " + str(sisi) + " cm")
  print("Diagonal 1 : " + str(diagonal_1) + " cm")
  print("Diagonal 2 : " + str(diagonal_2) + " cm")
  print("Luas : " + str(luas) + " cm^2")
  print("Keliling : " + str(keliling) + " cm")
  print("\n")
  exit()

# Menampilkan Function Main Screen
main_screen()