from modul import pemilih, calon

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

    id_calon = input("Masukkan ID calon yang Anda pilih: ")
    c = next((x for x in calon.daftar_calon if x["id"] == id_calon), None)
    if not c:
        print("ID calon tidak terdaftar.")
        return

    c["jumlah_suara"] += 1
    p["sudah_memilih"] = True
    print(f"Terima kasih, suara Anda untuk {c['nama']} telah tercatat.")