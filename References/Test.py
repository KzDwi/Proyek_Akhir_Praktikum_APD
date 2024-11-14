import json
import csv
import smtplib, ssl
import os

data_pengguna = {}  # Untuk Akun Pengguna
admin_login = {"username": "adminkontak", "password": "admin123"}  # Login Admin
kontak_publik = [{"nama": "Cek nomor", "nomor": "808"}, {"nama": "Layanan Pencegahan Bunuh Diri", "nomor": "119"}]  # Daftar Kontak Publik
start = True # Untuk Pengulangan saat login berhasil


smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "ebot3142@gmail.com"
password = "TugasPraktikum99"
receiver_email = "chrogam@gmail.com"
context = ssl.create_default_context()

# Membaca dataContacts.csv  
with open("dataContacts.csv", "r") as file:
    reader = csv.reader(file)
    dataContacts = list(reader)
    for i, data in enumerate(dataContacts):
        namaLayanan, nomorLayanan = data
        print(f"Kontak ke-{i+1}\nNama : {namaLayanan}\nNomor : {nomorLayanan}\n")

# Membaca User_Contacts.json  
json_s = "User_Contacts.json"
def load_contacts():
    with open(json_s, 'r') as dataContacts:
        return json.load(dataContacts) 
#       return data

# Simpan Perubahan kedalam json
def save_contacts(data):
    with open(json_s, 'w') as dataContacts: 
        json.dump(data, dataContacts, indent=4)

#Fitur Umpan Balik yang bisa langsung masuk kedalam email
def feedback():
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        message = input("Berikan Feedback kalian :")
        server.sendmail(sender_email, receiver_email, message)
    except Exception as e:
        print(e)
    finally:
        server.quit()

# Fungsi untuk Pengumuman pada kontak
def pengumuman():
    with open("changelog.csv", "r") as pengumuman:
        reader = csv.reader(pengumuman)
        changelog = list(reader)
        for data in enumerate(changelog):
            version, perubahan = data
            print(f"Versi : {version}\n")
            for i in enumerate(perubahan):
                print(f"{i}")


def copyright():
    copyright = ["Manajemen Kontak Informasi","Ahnaf Aliyyu (2409106035)","Nabila Putri Karni (24091060)","Dwi Prasetyawan (2409106028)"]
    print("="*20)
    print(f"{copyright[0]}\n{copyright[1]}\n{copyright[2]}\n{copyright[3]}")
    print("="*20)

#  Menambahkan Kontak Pengguna
def add_user_contact():
    nama = input("Masukkan nama kontak : ")
    nomor = input("Masukkan nomor kontak : ")
    email = input("Tambahkan e-mail? [Y/N] ")
    if email == "Y" or email == "y":
        e_mail = input("Masukkan e-mail kontak : ")
    else:
        e_mail = "N/A" #(jika pengguna tidak menambahkan email maka outputnya "N/A")
    for kontak in data['User']:
        kontak['kontak'].append({"nama":nama,"nomor":nomor,"email":e_mail})
        save_contacts(data)
    print("Kontak Berhasil ditambahkan")

# Melihat Daftar Kontak Pengguna
def check_user_contact():
    for kontak in data['User']:
        if pengguna_aktif == kontak['username']:
            for num, contact in enumerate(kontak['kontak']):
                print(f"Kontak ke-{num+1}\nNama : {contact['nama']}\nNomor : {contact['nomor']}\nE-mail : {contact['email']}\n")
    print("Kontak Lainnya")
    for kontakk in data['Admin']:
        for contact in enumerate(kontakk['kontak_K']):
            print(f"Nama : {contact['nama']}\nNomor : {contact['nomor']}\n")


# Proses Mengubah Data Kontak
def updating_user_contact(pengguna_aktif,pilihan_kontak):
    nama_baru = input("Nama : ")
    nomor_baru = input("Nomor : ")
    email_baru = input("E-mail : ")
    for kontak in data['User']:
        up = kontak['kontak'][pilihan_kontak]
        up['nama'] = nama_baru
        up['nomor'] = nomor_baru
        up['email'] = email_baru

# Fungsi Mengubah Data Kontak Pengguna Tertentu
def update_user_contact():
    show_user_contact()
    pilihan_kontak = int(input("Pilih kontak yang ingin diubah (hanya angka) : ")) - 1
    if pilihan_kontak >= 0 and pilihan_kontak <= len(data['User']['kontak']):
        updating_user_contact(pengguna_aktif,pilihan_kontak)
        save_contacts(data)
        print("Kontak berhasil diubah")
    else:
        print("Kontak tidak ditemukan")

# Menampilkan Kontak Pengguna
def show_user_contact():
    for kontak in data['User']:
        if pengguna_aktif == kontak['username']:
            for num, contact in enumerate(kontak['kontak']):
                print(f"Kontak ke-{num+1}\nNama : {contact['nama']}\nNomor : {contact['nomor']}\nE-mail : {contact['email']}\n")

# Menghapus Kontak Pengguna
def delete_user_contact():
    show_user_contact()
    indeks_hapus = int(input("Pilih kontak yang ingin dihapus (hanya angka) : ")) - 1
    if indeks_hapus >= 0 and indeks_hapus <= len(data['User']["kontak"]):
        kontak_lama = data['User']["kontak"].pop(indeks_hapus)
        save_contacts(data)
        print(f"Kontak {kontak_lama['nama']} Berhasil dihapus")
    else:
        print("Kontak tidak ditemukan")

# Menambah kontak baru sbg admin
def add_admin_contact():
    nama_adm = input("Masukkan nama kontak : ")
    nomor_adm = int(input("Masukkan nomor kontak : "))
    kontak_publik.append({"nama": nama_adm, "nomor": nomor_adm})
    for kontak in data['Admin']:
        kontak['kontak_K'].append({"nama":nama_adm,"nomor":nomor_adm})
    save_contacts(data)
    
#  Melihat Semua Daftar Kontak sbg admin
def check_admin_contact():
    for kontak in data['User'].values(): # Menampilkan kontak Pengguna
        for c in kontak["kontak"]:
            print(f"Nama : {c['nama']}\nNomor : {c['nomor']}\nE-mail : {c['email']}\n")
    print("Kontak lainnya :")
    for kontakk in data['Admin']: # Untuk menampilkan kontak publik
        for contact in enumerate(kontakk['kontak_K']):
            print(f"Nama : {contact['nama']}\nNomor : {contact['nomor']}\n")

# Menampilkan Daftar Kontak Admin
def show_admin_contact():
    for kontakk in data['Admin']:
        for contact in enumerate(kontakk['kontak_K']):
            print(f"Nama : {contact['nama']}\nNomor : {contact['nomor']}\n")

# Proses Mengubah Kontak Admin
def updating_admin_contact(pilihan_kontak_adm):
    nama_adm_baru = input("Nama : ")
    nomor_adm_baru = input("Nomor : ")
    for kontak in data['User']:
        up = kontak['kontak'][pilihan_kontak_adm]
        up['nama'] = nama_adm_baru
        up['nomor'] = nomor_adm_baru

# Mengubah Kontak Admin
def update_admin_contact():
    show_admin_contact()
    pilihan_kontak_adm = int(input("Pilih kontak yang ingin diubah (hanya angka) : ")) - 1
    if pilihan_kontak_adm >= 0 and pilihan_kontak_adm <= len(kontak_publik):
        updating_admin_contact(pilihan_kontak_adm)
        save_contacts(data)
        print("Kontak berhasil diubah")
    else:
        print("Kontak tidak ada")

# Membuat Akun Pengguna Baru
def create_account(data):
    print("Silahkan isi pertanyaan berikut :")
    username = input("Masukkan Username : ")
    if username in data:
        print("Username telah terdaftar, silahkan masukkan username lain atau masuk melalui Login")
        return data
    password = input("Masukkan Password : ")
    for akun in data['User']:
        akun.append({"username":username,"password":password,"kontak":[]})
    save_contacts(data)
    print("Akun anda telah dibuat, silahkan pilih opsi login untuk masuk")

# Program yang dijalankan dalam pengulangan sampai pengguna memilih keluar
while True:
    try:
        # menu utama
        print("""
        =============================
        |     MANAJEMEN KONTAK      |
        =============================
        |                           |
        | [1] Login                 |
        | [2] Buat Akun             |
        | [3] Keluar Program        |
        |                           |
        =============================
    """)
        pilihan = int(input("Pilih Fitur [1-3] : "))
        if pilihan == 1:
            i = 0
            # Login
            while i < 1:
                print("""
            ================
            |    LOGIN     |
            ================
    """)
                pengguna_aktif = input("Masukkan Username : ")
                kata_sandi = input("Masukkan Password : ")
                if pengguna_aktif in data_pengguna and data_pengguna[pengguna_aktif]["password"] == kata_sandi:
                    print("Login Berhasil!")
                    i = 1
                    while start == True:
                        # Menu Pengguna
                        print("""
            ========================
            |   KONTAK INFORMASI   |
            ========================
            | [1] Tambah Kontak    |
            | [2] Lihat Kontak     |
            | [3] Ubah Kontak      |
            | [4] Hapus Kontak     |
            | [5] Feedback         |
            | [6] Log Out          |
            ========================
    """)
                        ans = int(input("Pilih Fitur [1-5] : "))
                        match ans:
                            case 1:
                                add_user_contact()
    
                            case 2:
                                check_user_contact()
    
                            case 3:
                                update_user_contact()
    
                            case 4:
                                delete_user_contact()
    
                            case 5:
                                i = 1
                                break
    
                            case _:
                                print("Perintah tidak diketahui (Pilih opsi antara 1 sampai 5)")
    
                elif pengguna_aktif == admin_login["username"] and kata_sandi == admin_login["password"]:
                    print("Login Berhasil!")
                    while start == True:
                        # Menu Admin
                        print("""
            ==================================
            |          KONTAK ADMIN          |
            ==================================
            |                                |
            | [1] Tambahkan Kontak Khusus    |
            | [2] Lihat Semua Daftar Kontak  |
            | [3] Ubah Kontak Khusus         |
            | [4] Log Out                    |
            |                                |
            ==================================
    """)
                        pilihan_adm = int(input("Pilih Fitur (1 - 4) : "))
                        match pilihan_adm:
                            case 1:
                                add_admin_contact()
    
                            case 2:
                                check_admin_contact()
    
                            case 3:
                                update_admin_contact()
    
                            case 4:
                                # Log out
                                print("Keluar dari mode Admin. . .")
                                start = False
                                i = 1
    
                            case _:
                                print("Perintah Tidak Diketahui (Pilih Antara 1 sampai 4)")
                else:
                    print("Login Gagal")
                    while True:
                        ul1 = input("Coba lagi? [Y/N] :")
                        if ul1 == "Y" or ul1 == "y":
                            break
                        elif ul1 == "N" or ul1 == "n":
                            i = 1
                            break
                        else:
                            print("Perintah tidak ditemukan (Hanya Y/N) ")
        elif pilihan == 2:
            create_account()
            
        elif pilihan == 3:
            # Keluar Program
            break
        else:
            print("Fitur tidak ada (pilih antara 1 dan 3)")
    except ValueError:
        print("Fitur tidak ada (pilih antara 1 dan 3)")