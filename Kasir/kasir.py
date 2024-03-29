print("============ Raddt Coffee ============")
nama = input("Nama Kasir: ")

menu = {
    1: {"item": "Espresso", "harga": 22000},
    2: {"item": "AMERICANO", "harga": 18000},
    3: {"item": "CAPPUCINO", "harga": 22000},
    4: {"item": "Matcha", "harga": 20000},
    5: {"item": "Taro", "harga": 20000},
}

# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print("========== Daftar Menu ==========")
    for num, value in menu.items():
        print(f"{num}. {value['item']} \t: Rp {value['harga']}\t|")
    print("=================================")

# Fungsi untuk menghitung total pembelian
def hitung_total(pesanan):
    total = 0
    for pilihan, jumlah in pesanan.items():
        total += menu[pilihan]["harga"] * jumlah
    return total


# Fungsi utama
def main():
    pesanan = {}
    while True:
        tampilkan_menu()
        try:
            pilihan = int(input("Pilih menu (1-5), 0 untuk mengakhiri pesanan: "))
            if pilihan == 0:
                break
            elif pilihan not in menu:
                print("Pilihan tidak valid. Silakan masukkan nomor yang benar")
            else:
                jumlah = int(input(f"Masukkan jumlah yang ingin dibeli\t\t: "))
                if pilihan in pesanan:
                    pesanan[pilihan] += jumlah
                else:
                    pesanan[pilihan] = jumlah
        except ValueError:
            print("Masukkan nomor atau jumlah yang valid.")

    if not pesanan:
        print("Anda belum memesan apapun.")
    else:
        total_harga = hitung_total(pesanan)

        # Meminta input jumlah uang yang diberikan oleh pelanggan
        Bayar_input = input("Bayar\t: ")
        if Bayar_input.isdigit():
            Tunai = int(Bayar_input)
        else:
            print("Masukkan jumlah uang yang valid.")

        # Menghitung kembalian
        kembalian = Tunai - total_harga

        # Menampilkan struk pembelian
        print("\n============ Struk Pembelian ============")
        for pilihan, jumlah in pesanan.items():
            print(f"{menu[pilihan]['item']} Sejumlah {jumlah} \t= Rp {menu[pilihan]['harga'] * jumlah}\t|")
        print("=========================================")
        print(f"Total Harga \t\t= Rp {total_harga}\t|")
        print(f"Tunai \t\t\t= Rp {Tunai}\t|")
        print(f"Kembalian \t\t= Rp {kembalian}\t|")
        print("=========================================")

        return total_harga, Tunai, kembalian

if __name__ == "__main__":
    total_harga, tunai, kembalian = main()
