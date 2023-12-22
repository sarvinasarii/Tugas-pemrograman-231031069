#peogram selisih waktu
waktu_awal = input("\nMasukkan waktu awal (HH.MM): ")
jam_awal, menit_awal = map(int, waktu_awal.split("."))

jam_kurang = int(input("Masukkan jumlah jam yang akan dikurangkan: "))
menit_kurang = int(input("Masukkan jumlah menit yang akan dikurangkan: "))

jam_hasil = jam_awal - jam_kurang
menit_hasil = menit_awal - menit_kurang

if menit_hasil < 0:
    menit_hasil += 60
    jam_hasil -= 1

if jam_hasil < 0:
    jam_hasil += 24

print(f"Waktu sekarang menunjukkan Pukul {jam_hasil:02d}:{menit_hasil:02d}")