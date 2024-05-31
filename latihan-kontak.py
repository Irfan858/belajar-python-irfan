import os

# Inisialiasasi List
list_kontak = []

os.system('cls')

# Main Screen
def main_screen():
  print("Selamat Datang Di Aplikasi Kontak Sederhana")
  print("By : Irfan Kurniawan")
  print("\n")
  print("1. Lihat Kontak")
  print("2. Tambah Kontak Baru")
  print("3. Ubah Nama Kontak")
  print("4. Hapus Kontak")
  print("0. Keluar")
  pilihan  = int(input("Masukkan Pilihan Anda : "))
  
  if pilihan == 1:
    lihat_kontak()
  elif pilihan == 2:
    tambah_kontak()
  elif pilihan == 3:
    edit_kontak()
  elif pilihan == 4:
    hapus_kontak()
  elif pilihan == 0:
    quit()

# Exit Option
def exit():
  print("\n")
  pilihan = input(("Apakah anda akan Melanjutkan (y/n) : "))
  
  if pilihan == "y" :
    os.system('cls')
    main_screen()
  elif pilihan == "n" :
    quit()

# Function Melihat Isi Kontak
def lihat_kontak():
  os.system('cls')
  print("Lihat Kontak Anda")
  print("================================================")
  if list_kontak == [] :
    print("Kontak Anda Kosong")
  else :
    for kontak in list_kontak:
      print(str(list_kontak.index(kontak)) + ". " + kontak)
  exit()

# Function Untuk Menambah Kontak Baru
def tambah_kontak():
  os.system('cls')
  print("Tambah Kontak Baru")
  print("================================================")
  
  nama_kontak = ""
  print("Masukkan Nama Kontak : ")
  nama_kontak = input()
  
  if nama_kontak == "" :
    print("Nama Kontak Tidak Boleh Kosong")
    input()
    tambah_kontak()
  else :
    list_kontak.append(nama_kontak)
    print("Berhasil Menambahkan Nama Kontak")
    exit()

# Function Untuk Mengedit Isi Kontak
def edit_kontak():
  os.system('cls')
  print("Ubah Nama Kontak")
  print("================================================")
  
  if list_kontak == [] :
    print("Kontak Anda Kosong")
  else :
    for kontak in list_kontak:
      print(str(list_kontak.index(kontak)) + ". " + kontak)
  
  print("\n")
  pilihan = int(input("Masukkan Pilihan Anda: "))
  nama_kontak = input("Masukkan Nama Kontak Baru : ")
  
  if nama_kontak == "" :
    print("Nama Kontak Tidak Boleh Kosong")
    input()
    edit_kontak()
  else :
    list_kontak[pilihan] = nama_kontak
    print("Berhasil Mengubah Nama Kontak")
    exit()

# Function Untuk Menghapus Isi Kontak
def hapus_kontak():
  os.system('cls')
  print("Ubah Nama Kontak")
  print("================================================")
  
  if list_kontak == [] :
    print("Kontak Anda Kosong")
  else :
    for kontak in list_kontak:
      print(str(list_kontak.index(kontak)) + ". " + kontak)
  
  print("\n")
  nama_kontak = input("Masukkan Nama Kontak Yang Akan Di Hapus: ")
  pilihan = input("Apakah Yakin Anda Akan Menghapus Kontak (y/n) : ")
  
  if pilihan == "y" :
    list_kontak.remove(nama_kontak)
    print("Berhasil Menghapus Kontak")
    exit()
  elif pilihan == "n":
    hapus_kontak()

# Menjalankan Main Screen
main_screen()