# Flowchart Program Prediksi Harga Barang

Berikut adalah flowchart untuk program prediksi harga barang berdasarkan rata-rata selama 7 hari.

```mermaid
graph TD;
    A[Mulai] --> B[Input harga selama 7 hari]
    B --> C{Validasi input}
    C -- Salah --> B
    C -- Benar --> D[Hitung rata-rata harga]
    D --> E[Prediksi harga berdasarkan rata-rata]
    E --> F[Tampilkan hasil]
    F --> G[Selesai]
