def hitung_biaya(jenis_kamar, lama_menginap):
    if jenis_kamar.lower() == "standard":
        tarif = 200000
    elif jenis_kamar.lower() == "deluxe":
        tarif = 350000
    else:
        print("Jenis kamar tidak tersedia.")
        return 0

    total = tarif * lama_menginap
    return total

## bagian ini dipake buat hitung biaya total berdasarkan jenis kamar dan lama menginap.

def pesan_hotel():
    print("--- PEMESANAN HOTEL ---")

    jenis_kamar = input("Masukkan jenis kamar (Standard/Deluxe): ")
    tanggal_checkin = input("Tanggal check-in: ")
    tanggal_checkout = input("Tanggal check-out: ")
    lama_menginap = int(input("Lama menginap (malam): "))

    total = hitung_biaya(jenis_kamar, lama_menginap)

    if total == 0:
        return

## kalau ini buat memasukkan data pemesanan dan tanggal check-in, check-out, dan lama menginap. Lalu dihitung total biaya berdasarkan jenis kamar dan lama menginap.

    print("--- DETAIL PEMESANAN ---")
    print("Jenis kamar       :", jenis_kamar)
    print("Tanggal check-in  :", tanggal_checkin)
    print("Tanggal check-out :", tanggal_checkout)
    print("Lama menginap     :", lama_menginap, "malam")
    print("Total biaya       : Rp", total)

## untuk menampilkan detail pemesanan termasuk jenis kamar, tanggal check-in, tanggal check-out, lama menginap, dan total biaya.


while True:
    print("--- MENU HOTEL ---")
    print("1. Pesan kamar")
    print("2. Keluar")

    pilihan = input("Pilih menu (1-2): ")

    if pilihan == "1":
        pesan_hotel()

    elif pilihan == "2":
        print("Terima kasih!")
        break

    else:
        print("Pilihan tidak valid.")

## ini menu utama untuk pemesanan hotel, dengan opsi untuk memesan kamar atau keluar dari program.