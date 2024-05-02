# Daftar barang beserta harganya
daftar_barang = {
    "buku": 90000,
    "majalah": 50000,
    "topi": 70000,
    "parfum": 90000,
    "ikat rambut": 10000,
}

# menampilkan daftar barang
print("Daftar barang: ") 
for barang, harga in daftar_barang.items():
    print(f"{barang}: Rp {harga}")

# Input jumlah barang yang dibeli
total_belanja = 0
jumlah_barang = int(input("\nMasukkan jumlah barang yang dibeli: "))

# Mengitung total belanjaan
for i in range(jumlah_barang):
    barang = input(f"Masukkan nama barang ke-{i+1}: ")
    if barang in daftar_barang:
        total_belanja += daftar_barang[barang]
    else:
        print(f"{barang} tidak ada dalam daftar barang.")

# Menampilkan total belanja
print(f"\nTotal belanjaan anda: Rp {total_belanja}")