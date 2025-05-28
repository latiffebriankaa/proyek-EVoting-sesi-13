import json
import os
from modul import utils

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'calon.json')

def load_calon():
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, 'r') as f:
            return json.load(f)
    return []

def save_calon(daftar_calon):
    with open(DATA_PATH, 'w') as f:
        json.dump(daftar_calon, f, indent=4)

daftar_calon = load_calon()

def tambah_calon():
    global daftar_calon
    idc = utils.input_non_kosong("Masukkan ID calon: ")
    nama = utils.input_non_kosong("Masukkan nama calon ketua: ")
    visi = utils.input_non_kosong("Masukkan visi misi calon: ")

    # Validasi ID atau nama sudah terdaftar
    for calon in daftar_calon:
        if calon["id"] == idc:
            print("ID calon sudah terdaftar.")
            return
        if calon["nama"].lower() == nama.lower():
            print("Nama calon sudah terdaftar.")
            return

    calon_baru = {
        "id": idc,
        "nama": nama,
        "visi": visi,
        "jumlah_suara": 0
    }
    daftar_calon.append(calon_baru)
    save_calon(daftar_calon)
    print(f"Calon {nama} berhasil didaftarkan.")

def tampilkan_calon():
    global daftar_calon
    if not daftar_calon:
        print("Belum ada calon yang terdaftar.")
    else:
        print("Daftar calon ketua:")
        for idx, calon in enumerate(daftar_calon, 1):
            print(f"{idx}. ID: {calon['id']}, Nama: {calon['nama']}, Visi: {calon['visi']}, Jumlah Suara: {calon['jumlah_suara']}")