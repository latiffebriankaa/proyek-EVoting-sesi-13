daftar_pemilih = []

def tambah_pemilih():
    global daftar_pemilih
    idp = input("Masukkan ID pemilih: ")
    nama = input("Masukkan nama pemilih: ")
    jurusan = input("Masukkan jurusan pemilih: ")

    # Validasi ID unik
    for pemilih in daftar_pemilih:
        if pemilih["id"] == idp:
            print("ID pemilih sudah terdaftar.")
            return

    pemilih_baru = {
        "id": idp,
        "nama": nama,
        "jurusan": jurusan,
        "sudah_memilih": False
    }
    daftar_pemilih.append(pemilih_baru)
    print(f"Pemilih {nama} berhasil didaftarkan.")

def tampilkan_pemilih():
    global daftar_pemilih
    if not daftar_pemilih:
        print("Belum ada pemilih yang terdaftar.")
    else:
        print("Daftar pemilih:")
        for idx, pemilih in enumerate(daftar_pemilih, 1):
            status = "Sudah memilih" if pemilih["sudah_memilih"] else "Belum memilih"
            print(f"{idx}. ID: {pemilih['id']}, Nama: {pemilih['nama']}, Jurusan: {pemilih['jurusan']}, Status: {status}")