#jawaban nomor1

# Langkah a: Input bilangan A
bilangan = int(input("Masukkan bilangan: "))

# Langkah b: Cek apakah bilangan adalah kelipatan tiga
if bilangan % 3 == 0:
    # Langkah c: Cetak pesan jika bilangan adalah kelipatan tiga
    print(f"{bilangan} adalah bilangan Kelipatan 3")
else:
    # Langkah c: Cetak pesan jika bilangan bukan kelipatan tiga
    print(f"{bilangan} adalah bilangan Bukan Kelipatan 3")

# Langkah d: Selesai


# Meminta pengguna untuk memasukkan waktu awal dalam format HH:MM
waktu_awal = input("Masukkan waktu awal (HH:MM): ")

# Meminta pengguna untuk memasukkan jumlah jam dan menit yang akan ditambahkan
jam_tambahan = int(input("Jumlah jam yang akan ditambahkan: "))
menit_tambahan = int(input("Jumlah menit yang akan ditambahkan: "))

# Membagi waktu_awal menjadi jam dan menit
waktu_awal_split = waktu_awal.split(':')
jam_awal = int(waktu_awal_split[0])
menit_awal = int(waktu_awal_split[1])

# Menambahkan jam dan menit tambahan
jam_hasil = (jam_awal + jam_tambahan + (menit_awal + menit_tambahan) // 60) % 24
menit_hasil = (menit_awal + menit_tambahan) % 60

# Mengecek apakah perlu menambahkan "0" di depan jam dan menit jika nilainya kurang dari 10
jam_hasil_str = str(jam_hasil).zfill(2)
menit_hasil_str = str(menit_hasil).zfill(2)

# Mencetak hasil
print("Waktu sekarang menunjukkan Pukul {}:{}.".format(jam_hasil_str, menit_hasil_str))
# Meminta pengguna untuk memasukkan waktu awal dalam format HH.MM
waktu_awal = input("Masukkan waktu awal (HH.MM): ")

# Meminta pengguna untuk memasukkan jumlah jam dan menit yang akan dikurangkan
jam_selisih = int(input("Jumlah jam yang akan dikurangkan: "))
menit_selisih = int(input("Jumlah menit yang akan dikurangkan: "))

# Membagi waktu_awal menjadi jam dan menit
waktu_awal_split = waktu_awal.split('.')
jam_awal = int(waktu_awal_split[0])
menit_awal = int(waktu_awal_split[1])

# Menghitung waktu sebelumnya
jam_hasil = (jam_awal - jam_selisih - ((menit_awal - menit_selisih) // 60)) % 24
menit_hasil = (menit_awal - menit_selisih) % 60

# Mengecek apakah perlu menambahkan "0" di depan jam dan menit jika nilainya kurang dari 10
jam_hasil_str = str(jam_hasil).zfill(2)
menit_hasil_str = str(menit_hasil).zfill(2)

# Mencetak hasil
print("Waktu sekarang menunjukkan Pukul {}:{}.".format(jam_hasil_str, menit_hasil_str))
