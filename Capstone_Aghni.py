# Data awal pengguna
# menggunakan feature login untuk menentukkan masuk ke menu admin atau menu user
users = [
    {"username": "admin", "password": "admin", "saldo": 0, "pesanan": []}, # (dapat dilihat di def menu utama) jika user login dengan nama admin maka masuk ke menu_admin()
    {"username": "aghni", "password": "aghni**12", "saldo": 250000, "pesanan": []},# lainnya menu_pelanggan()
    {"username": "lala", "password": "password", "saldo": 50000, "pesanan": []}, # lainnya menu_pelanggan()
    {"username": "kak richard", "password": "mantap", "saldo": 900000, "pesanan": []}, # lainnya menu_pelanggan()
]

def login(): # login sesuai akun yang sudah ada dengan username dan password
    username = input("Username: ") # input username
    password = input("Password: ")# input password
    # pengecekan 
    for user in users:
        if user["username"] == username and user["password"] == password: # jika password sesuai dengan yang ada pada database
            print("Login berhasil!") # di konfirmasi login berhasil
            return user # jika berhasil di return user dictionary
    print("Username atau Password salah") 
    return None # jika gagal login return None

# Data produk dengan kategori
data_snack = [
    {
        "kategori": "Snack Manis", # data dibagi menjadi kategori
        "produk": [
            {"nama": "Cookies", "stok": 50, "harga": 15000},
            {"nama": "Cereal bar", "stok": 60, "harga": 9000},
            {"nama": "Coklat batangan", "stok": 40, "harga": 10000},
            {"nama": "Energy bar", "stok": 30, "harga": 12000},
        ]
    },
    {
        "kategori": "Keripik", # data dibagi menjadi kategori
        "produk": [
            {"nama": "Keripik Udang", "stok": 30, "harga": 9000},
            {"nama": "Keripik Kentang", "stok": 70, "harga": 13000},
            {"nama": "Keripik Singkong", "stok": 50, "harga": 14000},
            {"nama": "Peyek", "stok": 50, "harga": 14000},
        ]
    },
    {
        "kategori": "Snack Tradisional", # data dibagi menjadi kategori
        "produk": [
            {"nama": "Risoles", "stok": 40, "harga": 5000},
            {"nama": "Onde-onde", "stok": 20, "harga": 3000},
            {"nama": "Arem-arem", "stok": 30, "harga": 4000},
            {"nama": "Bala-bala", "stok": 30, "harga": 3000},
        ]
    }
]

# Keranjang Belanja
keranjang = [] # dikosongkan untuk dimodifikasi 

# Fungsi untuk menampilkan saldo 
def tampilkan_saldo(saldo):
    return f"Rp {saldo:,.0f}".replace(",", ".") # menggunakan fungsi replace dimana mengganti koma menjadi titik pada formatting saldo

# Menampilkan Produk
def tampilkan_produk(): # membuat tabel secara manual
    print("\n=== Toko Snack Kusuma ===\n")
    print("-" * 91)
    # Header
    print(f"| {'Index':<5} | {'Nama':<20} | {'Kategori':<20} | {'Stok':<10} | {'Harga (per buah)':<20} |")
    print("-" * 91)

    # loop dalam kategori
    for kategori_produk in data_snack: # mengiterasi kategori produk di dalam data_snack
        kategori = kategori_produk.get("kategori", "N/A") # dengan default jika kategori tidak ada
        produk = kategori_produk.get("produk", []) # jika produk tidak ada, maka list kosong
        # menggunakan get() untuk mengambil nilai atau variabel dari list maupun dictionary
        print(f"Kategori: {kategori}")
        print("-" * 91)

        for i, produk in enumerate(produk): # mengiterasi kategori index dan produk
            nama = produk.get("nama", "N/A")
            stok = produk.get("stok", 0) 
            harga = produk.get("harga", 0)
            # menggunakan get() untuk mengambil nilai atau variabel dari list maupun dictionary
            # N/A dan 0 merupakan default jika variabel nama, stok, dan harga tidak ada

            print(f"| {i:<5} | {nama:<20} | {kategori:<20} | {stok:<10} | {tampilkan_saldo(harga):<20} |")
        print("-" * 91)

def menu_admin():# menu ini akan keluar jika saat login pengguna masuk sebagai admin dengan username admin
    while True: # membuat loop, sampai break di logout
        print("\n--- Menu Admin ---")
        print("1. Tambah Produk") #create
        print("2. Hapus Produk") # delete
        print("3. Perbarui Produk") # update
        print("4. Lihat Produk") # read
        print("5. Logout") # Exit dengan logout disini, keluar ke main_menu terlebih dahulu dan klik "3" untuk Keluar dari main_menu
        
        pilihan = input("Pilihan Anda: ").strip() # pilih input

        # Pilihan Menu
        if pilihan == "1":
            tambah_produk()
        elif pilihan == "2":
            hapus_produk()
        elif pilihan == "3":
            perbarui_produk()
        elif pilihan == "4":
            tampilkan_produk()
        elif pilihan == "5":
            print("Keluar...")
            break # exit menu admin dalam loop
        else:
            print("Pilihan tidak valid.")

def menu_pengguna(pengguna): # menu ini akan keluar jika saat login memasukan username dan password selain admin
    while True:
        print("\n--- Menu Pengguna ---")
        print("1. Lihat Produk") # recall tampilan produk
        print("2. Tambah ke Keranjang") # create
        print("3. Lihat Keranjang") # read
        print("4. Hapus dari Keranjang") # delete
        print("5. Perbarui Keranjang") # update
        print("6. Selesaikan Pembelian") 
        print("7. Tambah Saldo")
        print("8. Logout") # logout disini, keluar ke main_menu terlebih dahulu dan klik "3" untuk Keluar dari main_menu
        
        pilihan = input("Pilihan Anda: ").strip() # pilih input
        
        if pilihan == "1":
            tampilkan_produk()
        elif pilihan == "2":
            tambah_ke_keranjang(pengguna)
        elif pilihan == "3":
            lihat_keranjang()
        elif pilihan == "4":
            hapus_dari_keranjang()
        elif pilihan == "5":
            perbarui_keranjang()
        elif pilihan == "6":
            selesaikan_pesanan(pengguna)
        elif pilihan == "7":
            tambah_saldo(pengguna)
        elif pilihan == "8": # logout disini, keluar ke main_menu terlebih dahulu dan klik "3" untuk Keluar seluruhnya dari main_menu
            print("Keluar...")
            break # exit menu pengguna dalam loop
        else:
            print("Pilihan tidak valid.")


## MENU PENGGUNA
def tambah_ke_keranjang(pengguna):
    tampilkan_produk() # recall def
    try:
        # Pilih input kategori
        indeks_kategori = int(input("Pilih kategori produk (0: Snack Manis, 1: Keripik, 2: Snack Tradisional): ").strip())
        
        #validasi indeks kategori
        if 0 <= indeks_kategori < len(data_snack):
            produk = data_snack[indeks_kategori]['produk']

            # pilih produk
            indeks_produk = int(input("Pilih nomor produk: ").strip())

            #validasi index produk
            if 0 <= indeks_produk < len(produk):
                produk_dipilih = produk[indeks_produk]

                # jumlah kuantitas
                jumlah = int(input(f"Masukkan jumlah {produk_dipilih['nama']} yang ingin dibeli: "))

                #validasi kuantitas
                if jumlah <= 0:
                    print("Jumlah harus lebih dari 0.")
                    return
                if jumlah > produk_dipilih["stok"]:
                    print("Stok tidak mencukupi.")
                    return 
                
                # stok di update dan ditambahkan ke keranjang
                produk_dipilih["stok"] -= jumlah
                keranjang.append({ # fungsi append digunakan untuk menambahkan ke keranjang
                    "nama": produk_dipilih["nama"],
                    "jumlah": jumlah,
                    "harga": produk_dipilih["harga"],
                    "subtotal": produk_dipilih["harga"] * jumlah
                })
                print(f"{produk_dipilih['nama']} (x{jumlah}) telah ditambahkan ke keranjang.")
            else:
                print("Nomor produk tidak valid.")
        else:
            print("Kategori tidak valid.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

def hapus_dari_keranjang():
    if not keranjang: # cek jika keranjang kosong
        print("Keranjang kosong.")
        return # bisa gunakan continue atau return untuk mengembalikan loop
    
    lihat_keranjang() # recall def
    nama_produk = input("Masukkan nama produk yang ingin dihapus: ").strip()
    
    # temukan dan hapus item dalam keranjang
    for item in keranjang:
        if item["nama"].lower() == nama_produk.lower():
            # Kembalikan stok ke produk asli
            for kategori in data_snack:
                for produk in kategori["produk"]:
                    if produk["nama"].lower() == nama_produk.lower():
                        produk["stok"] += item["jumlah"]
                        break

            # Hapus dari keranjang
            keranjang.remove(item)
            print(f"Produk '{nama_produk}' berhasil dihapus dari keranjang.")
            return
    # jika produk tidak ditemukan
    print(f"Produk '{nama_produk}' tidak ditemukan di keranjang.")

def perbarui_keranjang():
    if not keranjang:
        print("Keranjang kosong.")
        return
    
    lihat_keranjang()
    nama_produk = input("Masukkan nama produk yang ingin diperbarui: ").strip().lower()
    
    # Cari item di keranjang
    item_keranjang = None
    for item in keranjang:
        if item["nama"].lower() == nama_produk.lower():
            item_keranjang = item
            break
    
    if not item_keranjang:
        print("Produk tidak ditemukan di keranjang.")
        return
    
    # Cari produk di data utama
    produk_data = None
    for kategori in data_snack:
        produk_data = next((p for p in kategori["produk"] if p["nama"].lower() == nama_produk), None)
        if produk_data:
            break
    
    if not produk_data:
        print("Produk tidak ditemukan di data produk.")
        return
    
    try:
        # cek stok yang tersedia
        stok_tersedia = produk_data["stok"] + item_keranjang["jumlah"]
        
        while True:
            jumlah_baru = int(input(f"Masukkan jumlah baru untuk {item_keranjang['nama']} (maksimal {stok_tersedia}): "))
            
            if jumlah_baru <= 0:
                print("Jumlah harus lebih dari 0.")
            elif jumlah_baru > stok_tersedia:
                print(f"Jumlah melebihi stok tersedia ({stok_tersedia})")
            else:
                # Kembalikan stok lama dan kurangi stok baru
                produk_data["stok"] += item_keranjang["jumlah"]
                produk_data["stok"] -= jumlah_baru # jumlah baru 
                
                # Update keranjang
                item_keranjang["jumlah"] = jumlah_baru
                item_keranjang["subtotal"] = item_keranjang["harga"] * jumlah_baru
                print(f"Jumlah {item_keranjang['nama']} berhasil diperbarui.")
                break
    except ValueError:
        print("Input harus berupa angka.")

def lihat_keranjang():
    if not keranjang:
        print("Keranjang kosong.")
    else:
        total = 0
        print("\n=== Daftar Produk dalam Keranjang ===")
        print("-" * 80)
        print(f"| {'Produk':<20} | {'Jumlah':<15} | {'Harga':<16} | {'Subtotal':<16} |")
        print("-" * 80)
        # tampilkan tiap item dalam keranjang
        for item in keranjang:
            print(f"| {item['nama']:<20} | {item['jumlah']:<15} | {tampilkan_saldo(item['harga']):<16} | {tampilkan_saldo(item['subtotal']):<16} |")
            total += item["subtotal"]
        # total
        print("-" * 80)
        print(f"| {'Total':<57} | {tampilkan_saldo(total):<16} |")
        print("-" * 80)

def selesaikan_pesanan(pengguna):
    if not keranjang:
        print("Keranjang kosong.")
        return

    total = sum(item['subtotal'] for item in keranjang)
    print(f"Total Belanja: {tampilkan_saldo(total)}")

    # cek saldo apakah cukup untuk transaksi
    if pengguna["saldo"] >= total:
        pengguna["saldo"] -= total
        pengguna["pesanan"].append(keranjang.copy())
        keranjang.clear()
        print(f"Pesanan berhasil! Sisa saldo: {tampilkan_saldo(pengguna['saldo'])}")
    else:
        print(f"Saldo tidak mencukupi. Saldo Anda: {tampilkan_saldo(pengguna['saldo'])}")
        print("Silakan kurangi barang di keranjang atau topup saldo.")

def tambah_saldo(pengguna): # jika saldo tidak cukup, pengguna bisa topup terlebih dahulu
    try:
        jumlah = float(input("Jumlah yang akan ditambahkan (Rp): "))
        if jumlah <= 0:
            print("Jumlah harus positif.")
            return
        pengguna["saldo"] += jumlah
        print(f"Saldo baru: {tampilkan_saldo(pengguna['saldo'])}")
    except ValueError:
        print("Jumlah tidak valid. Harap masukkan angka.")

## MENU ADMIN
def tambah_produk():
    tampilkan_produk()
    print("\n--- Tambah Produk ---")
    print("Kategori:")

    # Tampilan kategori
    for i, kategori in enumerate(data_snack):
        print(f"{i}. {kategori['kategori']}")
    
    try:
        # pilih kategori
        pilihan_kategori = int(input("Pilih kategori (0: Snack Manis, 1: Keripik, 2: Snack Tradisional): "))

        # validasi kategori
        if 0 <= pilihan_kategori < len(data_snack):
            nama = input("Masukkan nama produk: ").strip()

            # validasi nama
            if not nama:
                print("Nama produk tidak boleh kosong.")
                return
            
            # cek apakah ada duplikat 
            for produk in data_snack[pilihan_kategori]["produk"]:
                if produk["nama"].lower() == nama.lower():
                    print("Produk dengan nama tersebut sudah ada.")
                    return
                
            # harga 
            harga = float(input("Masukkan harga produk (Rp): "))
            if harga < 0:
                print("Harga tidak boleh negatif.")
                return

            # stok
            stok = int(input("Masukkan stok produk: "))
            if stok < 0:
                print("Stok tidak boleh negatif.")
                return

            # tambahan produk baru
            data_snack[pilihan_kategori]["produk"].append({"nama": nama, "harga": harga, "stok": stok}) # fungsi append untuk menambahkan
            print(f"Produk '{nama}' berhasil ditambahkan!")
        else:
            print("Pilihan kategori tidak valid.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

def hapus_produk():
    tampilkan_produk() # recall def
    print("\n--- Hapus Produk ---")

    # menampilkan kategori
    print("Kategori:")
    for i, kategori in enumerate(data_snack):
        print(f"{i}. {kategori['kategori']}")
    
    try:
        # pilih kategori
        pilihan_kategori = int(input("Pilih kategori (0: Snack Manis, 1: Keripik, 2: Snack Tradisional): "))

        # validasi kategori
        if 0 <= pilihan_kategori < len(data_snack):
            nama_produk = input("Masukkan nama produk yang akan dihapus: ").strip()

            # cari dan remove produk
            for produk in data_snack[pilihan_kategori]["produk"]:
                if produk["nama"].lower() == nama_produk.lower():
                    data_snack[pilihan_kategori]["produk"].remove(produk) # remove() digunakan untuk menghapus produk
                    print(f"Produk '{nama_produk}' berhasil dihapus!")
                    return
            print("Produk tidak ditemukan di kategori ini.")
        else:
            print("Pilihan kategori tidak valid.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

def perbarui_produk():
    tampilkan_produk() # recall def
    print("\n--- Perbarui Produk ---")

    # Menampilkan Kategori
    print("Kategori:")
    for i, kategori in enumerate(data_snack):
        print(f"{i}. {kategori['kategori']}")
    
    try:
        # Pilih Kategori
        pilihan_kategori = int(input("Pilih kategori (0: Snack Manis, 1: Keripik, 2: Snack Tradisional): "))

        # validasi kategori
        if 0 <= pilihan_kategori < len(data_snack):
            nama_produk = input("Masukkan nama produk yang akan diperbarui: ").strip()

            # cari produk di database
            for produk in data_snack[pilihan_kategori]["produk"]:
                if produk["nama"].lower() == nama_produk.lower():
                    print(f"Memperbarui produk: {produk['nama']}")

                    # jika nama diganti
                    nama_baru = input("Masukkan nama baru (kosongkan jika tidak ingin mengubah): ").strip()
                    if nama_baru:
                        produk["nama"] = nama_baru

                    # jika harga diganti
                    harga_baru = input("Masukkan harga baru (Rp) (kosongkan jika tidak ingin mengubah): ").strip()
                    if harga_baru:
                        produk["harga"] = float(harga_baru)

                    # jika stok diganti
                    stok_baru = input("Masukkan stok baru (kosongkan jika tidak ingin mengubah): ").strip()
                    if stok_baru:
                        produk["stok"] = int(stok_baru)

                    print(f"Produk '{produk['nama']}' berhasil diperbarui!")
                    return
            print("Produk tidak ditemukan di kategori ini.")
        else:
            print("Pilihan kategori tidak valid.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

def menu_utama():
    pengguna_aktif = None # pengguna di awal 
    while True: # membuat loop sampai ada perintah
        if pengguna_aktif:
            if pengguna_aktif["username"] == "admin": # jika user login dengan nama admin maka masuk ke menu_admin()
                menu_admin()
            else:
                menu_pengguna(pengguna_aktif) # yang lainnya masuk kategori user
            pengguna_aktif = None  # Reset setelah logout
        else:
            print("\n=== Menu Utama ===")
            print("1. Login (menu pengguna atau menu admin)")
            print("2. Lihat Daftar Produk")
            print("3. Keluar") # setelah logout, users ke menu ini dulu dan untuk mengeluarkan loop pilih 3 dalam input menu

            pilihan = input("Pilih menu (1-3): ").strip()

            # pilihan menu
            if pilihan == "1":
                pengguna_aktif = login()
            elif pilihan == "2":
                tampilkan_produk()
            elif pilihan == "3":
                print("Terima kasih telah berbelanja di Toko Snack Kusuma!")
                break
            else:
                print("Input tidak valid. Pilih 1-3.")

def main():
    print("=== WELCOME TO KUSUMA'S SNACK SHOP ===")
    menu_utama() # mulai program

main()
