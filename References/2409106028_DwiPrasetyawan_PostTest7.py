user_data = {}  # Untuk Akun User
admin_login = {"username": "adminkontak", "password": "admin1234"}  # Login Admin
default_contacts = [{"name": "Cek nomor", "number": "808"}, {"name": "Layanan Pencegahan Bunuh Diri", "number": "119"}]  # Kontak Publik
start = True # Untuk Pengulangan saat login berhasil

def add_user_contact():
    nama = input("Masukkan nama kontak : ")
    nomor = input("Masukkan nomor kontak : ")
    email = input("Tambahkan e-mail? [Y/N] ")
    if email == "Y" or email == "y":
        e_mail = input("Masukkan e-mail kontak : ")
    else:
        e_mail = "N/A"
    social = input("Tambahkan Akun Sosial? [Y/N] ")
    if social == "Y" or social == "y":
        social1 = input("Masukkan akun sosial (contoh : @JohnDoe (Instagram)) : ")
    else:
        social1 = "N/A"
    user_data[match_un]["contacts"].append({"name": nama, "number": nomor, "email": e_mail, "social": social1})
    print("Kontak Berhasil ditambahkan")

def check_user_contact():
    for contact in user_data[match_un]["contacts"]:
        print(f"Kontak ke-{user_data[match_un]['contacts'].index(contact)+1}\nNama : {contact['name']}\nNomor : {contact['number']}\nE-mail : {contact['email']}\nSocial : {contact['social']}\n")
    print("Kontak Lainnya :")
    for contact in default_contacts:
        print(f"Nama : {contact['name']}\nNomor : {contact['number']}\n")

def updating_user_contact(match_un,match_ch):
    new_name = input("Nama : ")
    new_num = input("Nomor : ")
    new_email = input("E-mail : ")
    new_social = input("Social : ")
    user_data[match_un]["contacts"][match_ch]["name"] = new_name
    user_data[match_un]["contacts"][match_ch]["number"] = new_num
    user_data[match_un]["contacts"][match_ch]["email"] = new_email
    user_data[match_un]["contacts"][match_ch]["social"] = new_social

def update_user_contact():
    show_user_contact()
    match_ch = int(input("Pilih kontak yang ingin diubah (hanya angka) : ")) - 1
    if match_ch >= 0 and match_ch <= len(user_data[match_un]["contacts"]):
        updating_user_contact(match_un,match_ch)
        print("Kontak berhasil diubah")
    else:
        print("Kontak tidak ditemukan")

def show_user_contact():
    for i, contact in enumerate(user_data[match_un]["contacts"]):
        print(f"Kontak ke-{i+1}\nNama : {contact['name']}, Nomor : {contact['number']}\n")

def delete_user_contact():
    show_user_contact()
    match_cdel = int(input("Pilih kontak yang ingin dihapus (hanya angka) : ")) - 1
    if match_cdel >= 0 and match_cdel <= len(user_data [match_un]["contacts"]):
        del user_data[match_un]["contacts"][match_cdel]
        print("Kontak Berhasil dihapus")
    else:
        print("Kontak tidak ditemukan")

def add_admin_contact():
    adm_name = input("Masukkan nama kontak : ")
    adm_num = int(input("Masukkan nomor kontak : "))
    default_contacts.append({"name": adm_name, "number": adm_num})
    
def check_admin_contact():
    for contact in user_data.values():
        for c in contact["contacts"]:
            print(f"Nama : {c['name']}\nNomor : {c['number']}\nE-mail : {c['email']}\nSocial : {c['social']}\n")
    print("Kontak lainnya :")
    for contact in default_contacts:
        print(f"Nama : {contact['name']}\nNomor : {contact['number']}\n")

def show_admin_contact():
    for i, contact in enumerate(default_contacts):
        print(f"Nama : {contact['name']}\nNomor : {contact['number']}\n")

def updating_admin_contact(match_adm_ch):
    new_adm_name = input("Nama : ")
    new_adm_num = input("Nomor : ")
    default_contacts[match_adm_ch]["name"] = new_adm_name
    default_contacts[match_adm_ch]["number"] = new_adm_num

def update_admin_contact():
    show_admin_contact()
    match_adm_ch = int(input("Pilih kontak yang ingin diubah (hanya angka) : ")) - 1
    if match_adm_ch >= 0 and match_adm_ch <= len(default_contacts):
        updating_admin_contact(match_adm_ch)
        print("Kontak berhasil diubah")
    else:
        print("Kontak tidak ada")

def create_account():
    print("Silahkan isi pertanyaan berikut :")
    add_un = input("Masukkan Username : ")
    add_pw = input("Masukkan Password : ")
    user_data[add_un] = {"password": add_pw, "contacts": []}
    print("Akun anda telah dibuat, silahkan pilih opsi login untuk masuk")

while True:
    try:
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
        log = int(input("Pilih Fitur [1-3] : "))
        if log == 1:
            i = 0
            # Login
            while i < 1:
                print("""
            ================
            |    LOGIN     |
            ================
    """)
                match_un = input("Masukkan Username : ")
                match_pw = input("Masukkan Password : ")
                if match_un in user_data and user_data[match_un]["password"] == match_pw:
                    print("Login Berhasil!")
                    i = 1
                    while start == True:
                        print("""
            ========================
            |   KONTAK INFORMASI   |
            ========================
            | [1] Tambah Kontak    |
            | [2] Lihat Kontak     |
            | [3] Ubah Kontak      |
            | [4] Hapus Kontak     |
            | [5] Log Out          |
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
    
                elif match_un == admin_login["username"] and match_pw == admin_login["password"]:
                    print("Login Berhasil!")
                    while start == True:
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
                        adm_choose = int(input("Pilih Fitur (1 - 4) : "))
                        match adm_choose:
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
        elif log == 2:
            create_account()
            
        elif log == 3:
            # Quit Program
            break
        else:
            print("Fitur tidak ada (pilih antara 1 dan 3)")
    except ValueError:
        print("Fitur tidak ada (pilih antara 1 dan 3)")