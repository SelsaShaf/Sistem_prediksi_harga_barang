# Program Prediksi Harga Barang dengan Rata-rata

def input_harga():
    """Fungsi untuk meminta input harga barang selama 7 hari dari pengguna"""
    harga_mingguan = []
    for i in range(7):
        while True:
            try:
                harga = float(input(f"Masukkan harga barang hari ke-{i+1}: "))
                harga_mingguan.append(harga)
                break
            except ValueError:
                print("Input tidak valid! Harap masukkan angka.")
    return harga_mingguan


def hitung_rata_rata(harga_mingguan):
    """Fungsi untuk menghitung rata-rata harga barang"""
    return sum(harga_mingguan) / len(harga_mingguan)


def prediksi_harga(rata_rata):
    """Fungsi untuk memprediksi harga berdasarkan rata-rata"""
    return rata_rata  # Dalam kasus ini, prediksi harga keesokan hari sama dengan rata-rata


def main():
    print("Sistem Prediksi Harga Barang dengan Rata-rata")
    harga_mingguan = input_harga()
    rata_rata = hitung_rata_rata(harga_mingguan)
    harga_prediksi = prediksi_harga(rata_rata)
    
    print("\nRingkasan Prediksi:")
    print(f"Harga rata-ratrra selama 7 hari: Rp{rata_rata:.2f}")
    print(f"Prediksi harga barang keesokan hari: Rp{harga_prediksi:.2f}")

if __name__ == "__main__":
    main()