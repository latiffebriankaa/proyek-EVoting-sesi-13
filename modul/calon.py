daftar_calon = []

def tambah_calon():
    global daftar_calon
    idc = input("Masukkan ID calon: ")
    nama = input("Masukkan nama calon ketua: ")
    visi = input("Masukkan visi misi calon: ")

    # Cek apakah ID atau nama sudah terdaftar
    for calon in daftar_calon:
        if calon["id"] == idc or calon["nama"].lower() == nama.lower():
            print("Calon dengan ID atau nama tersebut sudah terdaftar.")
            return

    calon_baru = {
        "id": idc,
        "nama": nama,
        "visi": visi,
        "jumlah_suara": 0
    }
    daftar_calon.append(calon_baru)
    print(f"Calon {nama} berhasil didaftarkan.")

def tampilkan_calon():
    global daftar_calon
    if not daftar_calon:
        print("Belum ada calon yang terdaftar.")
    else:
        print("Daftar calon ketua:")
        for idx, calon in enumerate(daftar_calon, 1):
            print(f"{idx}. ID: {calon['id']}, Nama: {calon['nama']}, Visi: {calon['visi']}, Jumlah Suara: {calon['jumlah_suara']}")