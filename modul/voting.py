from modul import pemilih, calon
from modul import utils

def lakukan_voting():
    id_pemilih = input("Masukkan ID pemilih: ")
    # Cari pemilih
    p = next((x for x in pemilih.daftar_pemilih if x["id"] == id_pemilih), None)
    if not p:
        print("ID pemilih tidak terdaftar.")
        return
    if p["sudah_memilih"]:
        print("Anda sudah melakukan voting.")
        return

    # Tampilkan daftar calon sebelum voting
    utils.garis_pemisah()
    print("Daftar Calon Ketua:")
    for idx, c in enumerate(calon.daftar_calon, 1):
        print(f"{idx}. ID: {c['id']}, Nama: {c['nama']}, Visi: {c['visi']}")
    utils.garis_pemisah()

    id_calon = input("Masukkan ID calon yang Anda pilih: ")
    c = next((x for x in calon.daftar_calon if x["id"] == id_calon), None)
    if not c:
        print("ID calon tidak terdaftar.")
        return

    c["jumlah_suara"] += 1
    p["sudah_memilih"] = True
    # Simpan perubahan ke file
    calon.save_calon(calon.daftar_calon)
    pemilih.save_pemilih(pemilih.daftar_pemilih)
    print(f"Terima kasih, suara Anda untuk {c['nama']} telah tercatat.")

def tampilkan_hasil():
    calon.tampilkan_calon()