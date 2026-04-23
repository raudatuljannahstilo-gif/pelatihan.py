from collections import deque

class SistemRestoran:
    def __init__(self):
        self.antrean = deque()
        self.history = []

    def tambah_pesanan(self):
        nama = input("Masukkan nama pelanggan: ")
        print("Kategori: 1. Biasa | 2. VIP")
        pilihan = input("Pilih kategori (1/2): ")
        
        if pilihan == "2":
            self.antrean.appendleft(nama)
            print(f"★ [VIP] {nama} berhasil ditambahkan ke depan.")
        else:
            self.antrean.append(nama)
            print(f"[Biasa] {nama} berhasil ditambahkan.")
        
        self.history.append(nama)

    def undo_pesanan(self):
        if not self.history:
            print("❌ Tidak ada riwayat pesanan.")
            return
        
        nama_batal = self.history.pop()
        if nama_batal in self.antrean:
            self.antrean.remove(nama_batal)
            print(f"↩ Undo Berhasil: Pesanan {nama_batal} dibatalkan.")
        else:
            print(f"⚠️ {nama_batal} sudah mulai dimasak, tidak bisa dibatalkan.")

    def proses_dapur(self):
        if not self.antrean:
            print("📭 Antrean kosong, dapur istirahat.")
            return
        
        diproses = self.antrean.popleft()
        print(f"👨‍🍳 Dapur sedang memasak: {diproses}")

    def tampilkan_antrean(self):
        print("\n=== DAFTAR ANTREAN SAAT INI ===")
        if not self.antrean:
            print("Antrean Kosong")
        else:
            for i, nama in enumerate(self.antrean, 1):
                print(f"{i}. {nama}")
        print("===============================\n")

# --- MAIN PROGRAM ---
resto = SistemRestoran()

while True:
    print("\n--- MENU SISTEM RESTORAN ---")
    print("1. Tambah Pesanan")
    print("2. Proses Dapur (Layani)")
    print("3. Batalkan Pesanan Terakhir (Undo)")
    print("4. Lihat Antrean")
    print("5. Keluar")
    
    pilihan_menu = input("Pilih menu (1-5): ")

    if pilihan_menu == "1":
        resto.tambah_pesanan()
    elif pilihan_menu == "2":
        resto.proses_dapur()
    elif pilihan_menu == "3":
        resto.undo_pesanan()
    elif pilihan_menu == "4":
        resto.tampilkan_antrean()
    elif pilihan_menu == "5":
        print("Selesai. Program ditutup.")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")