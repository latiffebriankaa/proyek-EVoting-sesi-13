from modul import pemilih, calon

def tampilkan_statistik():
    total_pemilih = len(pemilih.daftar_pemilih)
    sudah_memilih = sum(1 for p in pemilih.daftar_pemilih if p["sudah_memilih"])
    persentase = (sudah_memilih / total_pemilih * 100) if total_pemilih > 0 else 0

    # Cari calon dengan suara terbanyak
    if calon.daftar_calon:
        max_suara = max(c["jumlah_suara"] for c in calon.daftar_calon)
        calon_terbanyak = [c for c in calon.daftar_calon if c["jumlah_suara"] == max_suara and max_suara > 0]
    else:
        calon_terbanyak = []

    print("=== Statistik Pemilu ===")
    print(f"Total pemilih           : {total_pemilih}")
    print(f"Jumlah yang sudah memilih: {sudah_memilih}")
    print(f"Persentase partisipasi  : {persentase:.2f}%")
    if calon_terbanyak:
        print("Calon dengan suara terbanyak:")
        for c in calon_terbanyak:
            print(f"- {c['nama']} ({c['jumlah_suara']} suara)")
    else:
        print("Belum ada suara masuk untuk calon.")