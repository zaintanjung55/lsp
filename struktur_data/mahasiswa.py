# Struktur Data Mahasiswa dengan CRUD
class Mahasiswa:
    def __init__(self, npm, nama, tempat_lahir, tanggal_lahir, prodi):
        self.npm = npm
        self.nama = nama
        self.tempat_lahir = tempat_lahir
        self.tanggal_lahir = tanggal_lahir
        self.prodi = prodi

# List untuk menyimpan data mahasiswa
data_mahasiswa = []

# Fungsi Tambah Data Mahasiswa
def tambah_mahasiswa():
    print("\n--- Tambah Data Mahasiswa ---")
    npm = input("Masukkan NPM: ")
    nama = input("Masukkan Nama: ")
    tempat_lahir = input("Masukkan Tempat Lahir: ")
    tanggal_lahir = input("Masukkan Tanggal Lahir (DD/MM/YYYY): ")
    prodi = input("Masukkan Program Studi: ")

    mahasiswa = Mahasiswa(npm, nama, tempat_lahir, tanggal_lahir, prodi)
    data_mahasiswa.append(mahasiswa)
    print("Data mahasiswa berhasil ditambahkan!\n")

# Fungsi Menampilkan Semua Data Mahasiswa
def tampilkan_mahasiswa():
    print("\n--- Data Mahasiswa ---")
    if not data_mahasiswa:
        print("Tidak ada data mahasiswa.\n")
        return
    for i, mhs in enumerate(data_mahasiswa, start=1):
        print(f"Mahasiswa ke-{i}")
        print(f"NPM           : {mhs.npm}")
        print(f"Nama          : {mhs.nama}")
        print(f"Tempat Lahir  : {mhs.tempat_lahir}")
        print(f"Tanggal Lahir : {mhs.tanggal_lahir}")
        print(f"Program Studi : {mhs.prodi}")
        print("-" * 30)
    print()

# Fungsi Hapus Data Mahasiswa Berdasarkan NPM
def hapus_mahasiswa():
    print("\n--- Hapus Data Mahasiswa ---")
    npm = input("Masukkan NPM mahasiswa yang ingin dihapus: ")
    for i, mhs in enumerate(data_mahasiswa):
        if mhs.npm == npm:
            del data_mahasiswa[i]
            print(f"Data mahasiswa dengan NPM {npm} berhasil dihapus.\n")
            return
    print(f"Data mahasiswa dengan NPM {npm} tidak ditemukan.\n")

# Fungsi Menu Utama
def menu():
    while True:
        print("=== SISTEM DATA MAHASISWA ===")
        print("1. Tambah Data Mahasiswa")
        print("2. Tampilkan Data Mahasiswa")
        print("3. Hapus Data Mahasiswa")
        print("4. Keluar")
        pilihan = input("Pilih menu (1/2/3/4): ")

        if pilihan == "1":
            tambah_mahasiswa()
        elif pilihan == "2":
            tampilkan_mahasiswa()
        elif pilihan == "3":
            hapus_mahasiswa()
        elif pilihan == "4":
            print("Keluar dari program. Terima kasih!\n")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")

# Eksekusi Program
if __name__ == "__main__":
    menu()
