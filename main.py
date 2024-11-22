import json
import smtplib
import os

start = True # Untuk Pengulangan saat login berhasil

# Deklarasi Tempat json
json_s = str(os.path.dirname(os.path.abspath(__file__))) + "\\Contacts.json"
json_feedback = str(os.path.dirname(os.path.abspath(__file__))) + "\\feedback.json"

# Membaca Contacts.json  
def load_contacts():
    with open(json_s, 'r') as Contacts:
        return json.load(Contacts) 
data = load_contacts()

# Simpan Perubahan kedalam json
def save_contacts(data):
    with open(json_s, 'w') as dataContacts: 
        json.dump(data, dataContacts, indent=4)

def refresh():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

# Fitur Umpan Balik yang bisa langsung masuk kedalam email
def feedback(feedback_message,sender):
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "ebot3412@gmail.com"
    password = "fdlvihxcutptrrdl"
    receiver_email = "chrogam@gmail.com"
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.starttls()
        server.login(sender_email, password)
        message = f"""
Umpan balik baru dari {sender}

Pesan : {feedback_message}
"""
        server.sendmail(sender_email, receiver_email, message)
        server.quit()
    except Exception as e:
        print(e)

# Membaca feedback.json
def load_feedback():
    try:
        with open(json_feedback, 'r') as feedback_file:
            return json.load(feedback_file)
    except FileNotFoundError:
        return {"Feedback": []}
fb = load_feedback()

# Simpan Perubahan ke dalam feedback.json
def save_feedback (feedback_data):
    with open(json_feedback, 'w') as feedback_file:
        json.dump(feedback_data, feedback_file, indent=4)

# Fitur Umpan Balik yang menyimpan ke JSON
def feed_back():
    print("========== FEEDBACK ==========")
    feedback_message = input("Berikan Feedback Anda : ")
    if feedback_message != None:
        for kontak in data['User']:
            if pengguna_aktif == kontak['username']:
                sender = kontak['name']
        # Tambahkan umpan balik ke data JSON
        feedback(feedback_message,sender)
        fb["Feedback"].append({"username": pengguna_aktif,"name": sender,"pesan": feedback_message})
        save_feedback(fb)
        print("Feedback Anda tersimpan. Terima kasih!")
    else:
        print("Pesan kosong, feedback tidak tersimpan.")

# Fungsi untuk Admin melihat feedback yang terkirim pada program
def check_feedback():
    print("-----=====|| Daftar Feedback ||======-----")
    for num, feed in enumerate(fb['Feedback']):
        print(f"\nFeedback ke-{num + 1}\nUsername : {feed['username']}\nNama : {feed['name']}\nPesan : {feed['pesan']}")

# Tuple yang muncul saat berada di menu awal
def copyright():
    copyright = ("Manajemen Kontak Informasi","Ahnaf Aliyyu (2409106035)","Nabila Putri Karni (2409106041)","Dwi Prasetyawan (2409106028)")
    print("="*20)
    print(f"{copyright[0]}\n{copyright[1]}\n{copyright[2]}\n{copyright[3]}")
    print("="*20)

# Menambahkan Kontak Pengguna
def add_user_contact():
    nama = input("Masukkan nama kontak : ")
    while True:
        nomor = input("Masukkan nomor kontak : ")
        if not nomor.isnumeric() :
            print("nomor tidak terdiri dari angka, silahkan ulangi lagi")
        else:
            break
    while True:
        e_mail = input("Masukkan E-Mail (Tekan Enter jika tidak ada) : ").strip()
        if e_mail == "":
            e_mail = "N/A"
        elif "@" not in e_mail:
            print("E-mail tidak lengkap")
        else:
            break
    domisili = input("Masukkan Domisili (Tekan Enter jika tidak ada) : ")
    if domisili.strip() == "":
        domisili = "N/A"
    pekerjaan = input("Masukkan Pekerjaan (Tekan Enter jika tidak ada) : ")
    if pekerjaan.strip() == "":
        pekerjaan = "N/A"
    for kontak in data['User ']:
        if kontak['username'] == pengguna_aktif:
            kontak['kontak'].append({"nama": nama, "nomor": nomor, "email": e_mail, "domisili": domisili, "pekerjaan": pekerjaan})
            save_contacts(data)
    print("Kontak Berhasil ditambahkan")

# Melihat Daftar Kontak Pengguna
def check_user_contact():
    for kontak in data['User ']:
        if pengguna_aktif == kontak['username']:
            for num, contact in enumerate(kontak['kontak']):
                print(f"Kontak ke-{num + 1}\nNama : {contact['nama']}\nNomor : {contact['nomor']}\nE-mail : {contact['email']}\nDomisili : {contact['domisili']}\nPekerjaan : {contact['pekerjaan']}\n")
    print("Kontak Lainnya")
    for kontakk in data['Admin']:
        for num, contact in enumerate(kontakk['kontak_K']):
            print(f"Nama : {contact['nama']}\nNomor : {contact['nomor']}\n")

# Proses Mengubah Data Kontak
def updating_user_contact(pengguna_aktif, pilihan_kontak):
    nama_baru = input("Nama : ")
    while True:
        nomor_baru = input("Nomor : ").strip()
        if not nomor_baru.isnumeric():
            print("nomor baru tidak terdiri dari angka, silahkan ulangi lagi")
        else:
            break
    while True:
        email_baru = input("E-mail : ")
        if email_baru.strip() == "":
            email_baru = "N/A"
        elif "@" not in email_baru:
            print("E-mail tidak lengkap")
        else:
            break
    dom_baru = input("Domisili : ")
    if dom_baru.strip() == "":
        dom_baru = "N/A"
    job_baru = input("Pekerjaan : ")
    if job_baru.strip() == "":
        job_baru = "N/A"
    for kontak in data['User ']:
        if kontak['username'] == pengguna_aktif:
            up = kontak['kontak'][pilihan_kontak]
            up['nama'] = nama_baru
            up['nomor'] = nomor_baru
            up['email'] = email_baru
            up['domisili'] = dom_baru
            up['pekerjaan'] = job_baru

# Fungsi Mengubah Data Kontak Pengguna Tertentu
def update_user_contact():
    show_user_contact()
    try:
        pilihan_kontak = int(input("Pilih kontak yang ingin diubah (hanya angka) : ")) - 1
        for kontak in data['User ']:
            if pengguna_aktif == kontak["username"]:
                if 0 <= pilihan_kontak < len(kontak['kontak']):
                    updating_user_contact(pengguna_aktif, pilihan_kontak)
                    save_contacts(data)
                    print("Kontak berhasil diubah")
                else:
                    print("Kontak tidak ditemukan")
                break
    except ValueError:
        print("Input tidak valid, silakan masukkan angka.")

# Menampilkan Kontak Pengguna
def show_user_contact():
    for kontak in data['User ']:
        if pengguna_aktif == kontak['username']:
            for num, contact in enumerate(kontak['kontak']):
                print(f"Kontak ke-{num + 1}\nNama : {contact['nama']}\nNomor : {contact['nomor']}\nE-mail : {contact['email']}\nDomisili : {contact['domisili']}\nPekerjaan : {contact['pekerjaan']}\n")

# Menghapus Kontak Pengguna
def delete_user_contact():
    show_user_contact()
    try:
        indeks_hapus = int(input("Pilih kontak yang ingin dihapus (hanya angka) : ")) - 1
        for kontak in data['User ']:
            if pengguna_aktif == kontak['username ']:
                if 0 <= indeks_hapus < len(kontak['kontak']):
                    kontak_lama = kontak['kontak'].pop(indeks_hapus)
                    save_contacts(data)
                    print(f"Kontak [{kontak_lama['nama']}] Berhasil dihapus")
                else:
                    print("Kontak tidak ditemukan")
                break
    except ValueError:
        print("Input tidak valid, silakan masukkan angka.")

# Menambah kontak baru sbg admin
def add_admin_contact():
    tried = 0
    nama_adm = input("Masukkan nama kontak : ")
    while tried < 3:
        nomor_adm = input("Masukkan nomor kontak : ").strip()
        if not nomor_adm.isnumeric() or nomor_adm == "*" or "#":
            print("Nomor tidak valid")
            tried += 1
        else:
            break
    if any(kontakk['nama'] == nama_adm for kontakk in data['Admin']['kontak_K']):
        print("Nama kontak telah terdaftar, silahkan masukkan kontak lain")
    else:
        if any(kontakk['nomor'] == nomor_adm for kontakk in data['Admin']['kontak_K']):
            print("Nomor kontak telah terdaftar, silahkan masukkan kontak lain")
        else:
            for kontak in data['Admin']:
                kontak['kontak_K'].append({"nama": nama_adm, "nomor": nomor_adm})
            save_contacts(data)
            print("Kontak admin berhasil ditambahkan.")

#  Melihat Semua Daftar Kontak sbg admin
def check_admin_contact():
    for user in data['User']:
        print(f"\nPengguna: {user['name']} ({user['username']})")
        for num, contact in enumerate(user['kontak']):
            print(f"Kontak ke-{num+1}\nNama : {contact['nama']}\nNomor : {contact['nomor']}\nE-mail : {contact['email']}\nDomisili : {contact['domisili']}\nPekerjaan : {contact['pekerjaan']}\n")

    print("\nDaftar Kontak Khusus:")
    for admin in data['Admin']:
        for num, contact in enumerate(admin['kontak_K']):
            print(f"Nama : {contact['nama']}\nNomor : {contact['nomor']}\n")

# Menampilkan Daftar Kontak Admin
def show_admin_contact():
    for kontakk in data['Admin']:
        for num, contact in enumerate(kontakk['kontak_K']):
            print(f"Nama : {contact['nama']}\nNomor : {contact['nomor']}\n")

# Proses Mengubah Kontak Admin
def updating_admin_contact(pilihan_kontak_adm):
    tried = 0
    nama_adm_baru = input("Nama : ")
    while tried < 3:
        nomor_adm_baru = input("Nomor : ").strip()
        if not nomor_adm_baru.isnumeric() or nomor_adm_baru == "*" or "#":
            print("Nomor tidak valid")
            tried += 1
        else:
            break
        if any(kontakk['nama'] == nama_adm_baru for kontakk in data['Admin']['kontak_K']):
            print("Nama kontak telah terdaftar, silahkan masukkan kontak lain")
        else:
            if any(kontakk['nomor'] == nomor_adm_baru for kontakk in data['Admin']['kontak_K']):
                print("Nomor kontak telah terdaftar, silahkan masukkan kontak lain")
        for kontak in data['Admin']:
            up = kontak['kontak_K'][pilihan_kontak_adm]
            up['nama'] = nama_adm_baru
            up['nomor'] = nomor_adm_baru
        save_contacts(data)
        print("Kontak berhasil diubah")

# Mengubah Kontak Admin
def update_admin_contact():
    show_admin_contact()
    try:
        pilihan_kontak_adm = int(input("Pilih kontak yang ingin diubah (hanya angka) : ")) - 1
        for kontakk in data['Admin']:
            if pilihan_kontak_adm >= 0 and pilihan_kontak_adm <= len(kontakk['kontak_K']):
                updating_admin_contact(pilihan_kontak_adm)
            else:
                print("Kontak tidak ada")
    except ValueError:
        print("Kontak tidak ditemukan")

def delete_admin_contact():
    show_admin_contact()
    try:
        atmin_hapus = int(input("Pilih kontak yang ingin dihapus (hanya angka) : ")) - 1
        atmin = data['Admin']
        if atmin_hapus >= 0 and atmin_hapus <= len(atmin["kontak_K"]):
            kontak_lama = atmin["kontak_K"].pop(atmin_hapus)
            save_contacts(data)
            print(f"Kontak [{kontak_lama['nama']}] Berhasil dihapus")
        else:
            print("Kontak tidak ditemukan")
    except ValueError:
        print("Kontak tidak ditemukan")

# Membuat Akun Pengguna Baru
def create_account(data):
    print("Silahkan isi pertanyaan berikut :")
    while True:
        username = input("Masukkan Username : ").strip()
        if not username.isalnum() or username == ".":
            print("Username hanya boleh menggunakan huruf, angka, serta titik(.)")
        break
    if any(akun['username'] == username for akun in data['User']):
        print("Username telah terdaftar, silahkan masukkan username lain atau masuk melalui Login")
        return data
    password = input("Masukkan Password : ").strip()
    Nama = input("Masukkan Nama Kamu :")
    data['User'].append({"username":username,"name":Nama,"password":password,"kontak":[]})
    save_contacts(data)
    print("Akun anda telah dibuat, silahkan pilih opsi login untuk masuk")

# Program yang dijalankan dalam pengulangan sampai pengguna memilih keluar
while True:
    try:
        # menu utama
        refresh()
        copyright()
        print("""
        
        ========================================
        |      MANAJEMEN KONTAK INFORMASI      |
        ========================================
        |                                      |
        | [1] Login                            |
        | [2] Buat Akun                        |
        | [3] Keluar Program                   |
        |                                      |
        ========================================
    """)
        pilihan = int(input("Pilih Fitur [1/2/3] : "))
        if pilihan == 1:
            refresh()
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
                akses = 0
                for akun in data['User']:
                    if pengguna_aktif == akun["username"] and akun["password"] == kata_sandi:
                        akses = 1
                for admin in data['Admin']:
                    if pengguna_aktif == admin['username'] and admin['password'] == kata_sandi:
                        akses = 2
                    else:
                        continue
                if akses == 1:
                    aktif = None
                    for akun in data['User']:
                        global nama_akun
                        nama_akun = akun['name']
                        if akun['username'] == pengguna_aktif:
                            aktif = akun
                            break
                    refresh()
                    print("Login Berhasil!")
                    start = True
                    print(f"Selamat Datang, {nama_akun}!")
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
                        ans = input("Pilih Fitur [1/2/3/4/5/6] : ")
                        match ans:
                            case "1":
                                add_user_contact()

                            case "2":
                                check_user_contact()

                            case "3":
                                update_user_contact()

                            case "4":
                                delete_user_contact()
                            
                            case "5":
                                feed_back()
                            case "6":
                                i = 1
                                break

                            case _:
                                print("Perintah tidak diketahui (Pilih opsi antara 1 sampai 6)")

                elif akses == 2:
                    refresh()
                    start = True
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
            | [4] Hapus Kontak Khusus        |
            | [5] Lihat Feedback             |
            | [6] Log Out                    |
            |                                |
            ==================================
    """)
                        pilihan_adm = input("Pilih Fitur [1/2/3/4/5/6] : ")
                        match pilihan_adm:
                            case "1":
                                add_admin_contact()

                            case "2":
                                check_admin_contact()

                            case "3":
                                update_admin_contact()
                            
                            case "4":
                                delete_admin_contact()
                            
                            case "5":
                                check_feedback()

                            case "6":
                                # Log out
                                print("Keluar dari mode Admin. . .")
                                start = False
                                pengguna_aktif = None
                                i = 1

                            case _:
                                print("Perintah Tidak Diketahui (Pilih Antara 1 sampai 6)")
                else:
                    print("Login Gagal")
                    while True:
                        ul1 = input("Coba lagi? [Y/N] :").lower()
                        if ul1 == "y":
                            break
                        elif ul1 == "n":
                            i = 1
                            break
                        else:
                            print("Perintah tidak ditemukan (Hanya Y/N) ")
        elif pilihan == 2:
            refresh()
            create_account(data)
        
        elif pilihan == 3:
            # Keluar Program
            break
        else:
            print("Fitur tidak ada (pilih antara 1 dan 3)")
    except ValueError:
        print("Fitur tidak ada (pilih antara 1 dan 3)")