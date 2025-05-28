from modul import utils
import json
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'pemilih.json')

def load_pemilih():
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, 'r') as f:
            return json.load(f)
    return []

def save_pemilih(daftar_pemilih):
    with open(DATA_PATH, 'w') as f:
        json.dump(daftar_pemilih, f, indent=4)

daftar_pemilih = load_pemilih()

def tambah_pemilih():
    global daftar_pemilih
    idp = utils.input_non_kosong("Masukkan ID pemilih: ")
    # Cek apakah ID sudah ada
    for pemilih in daftar_pemilih:
        if pemilih["id"] == idp:
            if pemilih["sudah_memilih"]:
                print("Pemilih ini sudah pernah memilih dan tidak bisa didaftarkan lagi.")
            else:
                print("ID pemilih sudah terdaftar.")
            return

    nama = utils.input_non_kosong("Masukkan nama pemilih: ")
    jurusan = utils.input_non_kosong("Masukkan jurusan pemilih: ")

    pemilih_baru = {
        "id": idp,
        "nama": nama,
        "jurusan": jurusan,
        "sudah_memilih": False
    }
    daftar_pemilih.append(pemilih_baru)
    save_pemilih(daftar_pemilih)
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