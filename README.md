# Project UAS
## Bahasa Pemrograman
```
   Nama : Raditra Ikhwanul Arifin
   Nim  : 312310487
   Kela : TI.23.A5
```

Berikut Link Dokumentasi di Youtube : https://youtu.be/6okEMKisK7U

```pyhton
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
```
* Mari kita mulai dari baris pertama, kode ini berfungsi untuk mencetak pilihan menu yang ada di Raddt Coffee.

```pyhton
# Fungsi untuk menghitung total pembelian
def hitung_total(pesanan):
    total = 0
    for pilihan, jumlah in pesanan.items():
        total += menu[pilihan]["harga"] * jumlah
    return total
```
* Pada baris ini kode berfungsi untuk menampilkan total pembelian di Raddt Coffee.

```pyhton
# Fungsi utama
def main():
    pesanan = {}
    while True:
        tampilkan_menu()
        try:
            pilihan = int(input("Pilih menu (1-5), 0 untuk mengakhiri pesanan, atau -1 untuk pembatalan/pengurangan pesanan: "))
            if pilihan == 0:
                break
            elif pilihan not in menu:
                print("Pilihan tidak valid. Silakan masukkan nomor yang benar ")
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
```
* Pada baris ini kode berfungsi untuk menginput pesanan yang dipesan oleh pembeli.
* Pada kode ini pembeli bisa menambahkan pesanan lebih dari 2 pesanan.
* JIka ada pesanan tidak ada atau salah input maka tidak akan muncul pada kolom pesanan.

```pyhton
# Meminta input jumlah uang yang diberikan oleh pelanggan
        Bayar_input = input("Bayar\t: ")
        if Bayar_input.isdigit():
            Tunai = int(Bayar_input)
        else:
            print("Masukkan jumlah uang yang valid.")
```
* Pada baris ini kode berfungsi untuk meminta input jumlah uang diberikan oleh pelanggan.

```pyhton
# Menghitung kembalian
        kembalian = Tunai - total_harga
```
* Pada baris ini kode berfungsi untuk menghitung kembalian dari jumlah uang yang dibayarkan oleh pembeli.

```pyhton
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
```
* Pada baris ini kode berfungsi untuk mencetak struk pembelian yang dipesan oleh pembeli.
* Pada kode ini ditampilkan total harga, jumlah uang yang dibayarkan dan jumlah kembali yang diterima oleh pembeli.

```pyhton
if __name__ == "__main__":
    total_harga, tunai, kembalian = main()
```
* if __name__ == "__main__":: Baris ini memeriksa apakah skrip sedang dijalankan sebagai program utama (bukan diimpor sebagai modul).

* Total_harga, tunai, kembalian = main(): Jika skrip adalah program utama, maka fungsi main() dipanggil dan nilainya diatribusikan ke variabel total_harga, tunai, dan kembalian.

