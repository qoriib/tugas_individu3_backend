# Product Review Analyzer - Backend

## Deskripsi

Aplikasi **Product Review Analyzer** adalah aplikasi yang memungkinkan pengguna untuk mengirimkan ulasan produk untuk dianalisis. Sistem ini menggunakan model **Hugging Face** untuk melakukan analisis sentimen (positif, negatif, netral) pada setiap ulasan, dan **Gemini** untuk mengekstraksi poin penting dari teks ulasan. Hasil analisis ini kemudian disimpan dalam database **PostgreSQL**.

Backend ini dibangun menggunakan **Flask** sebagai web framework dan **SQLAlchemy** untuk integrasi dengan database PostgreSQL.

## Fitur Utama

- **Analisis Sentimen**: Menggunakan model **Hugging Face** untuk menganalisis sentimen dari teks ulasan.
- **Ekstraksi Poin Penting**: Menggunakan metode ekstraksi untuk mendapatkan poin-poin utama dari ulasan.
- **Database PostgreSQL**: Menyimpan hasil analisis ke dalam tabel `reviews`.
- **API Endpoints**:

  - `POST /api/analyze-review`: Untuk mengirimkan ulasan dan mendapatkan hasil analisis.
  - `GET /api/reviews`: Untuk mendapatkan semua ulasan yang sudah dianalisis.

## Struktur Proyek

```
/backend
  /app
    __init__.py          # Inisialisasi aplikasi Flask dan database
    models.py            # Model untuk tabel Review
    routes.py            # Mendefinisikan rute API
    analysis.py          # Fungsi analisis sentimen dan ekstraksi poin penting
  config.py              # Konfigurasi aplikasi
  run.py                 # Menjalankan aplikasi Flask
```
