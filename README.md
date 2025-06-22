Analisis Risiko Penyakit Jantung (Heart Risk Analysis)

Aplikasi web sederhana untuk memprediksi risiko penyakit jantung pada pasien berdasarkan beberapa parameter medis. Aplikasi ini dibangun menggunakan model klasifikasi Decision Tree dan disajikan dengan antarmuka web yang interaktif menggunakan Flask.

    Catatan: Ganti link https://i.ibb.co/L5rK5Q5/image.png di atas dengan link screenshot aplikasi Anda. Ambil screenshot halaman utama aplikasi Anda dan unggah ke layanan seperti ImgBB atau langsung ke repositori GitHub Anda.

📜 Tentang Proyek

Proyek ini merupakan implementasi dari model machine learning ke dalam sebuah produk yang dapat digunakan secara nyata. Prosesnya mencakup analisis data, pelatihan model, hingga deployment menjadi aplikasi web yang fungsional. Tujuannya adalah untuk memberikan prediksi awal tingkat risiko penyakit jantung yang dapat digunakan sebagai alat bantu bagi tenaga medis.
✨ Fitur Utama

    Prediksi Real-time: Memberikan hasil prediksi risiko ("Pasien Sehat / Normal" atau "Pasien dengan Penyakit Jantung") secara langsung setelah data diinput.
    Antarmuka Modern & Responsif: UI yang bersih, profesional, dan dapat diakses dengan baik di perangkat desktop maupun mobile.
    Deteksi Anomali Input: Sistem secara otomatis memvalidasi data yang dimasukkan untuk mencegah nilai yang tidak wajar atau tidak mungkin secara medis.
    Rekomendasi Tindakan: Memberikan rekomendasi singkat berdasarkan hasil prediksi.
    Unduh Laporan PDF: Pengguna dapat mengunduh hasil analisis dalam format PDF yang rapi, berfungsi sebagai surat rujukan atau laporan.

🛠️ Dibangun Dengan

Berikut adalah teknologi dan library utama yang digunakan dalam proyek ini:

    Backend:
        Flask: Framework web micro untuk Python.
        Pandas: Untuk manipulasi dan analisis data.
        Scikit-learn: Untuk membangun dan menggunakan model machine learning.
        Joblib: Untuk memuat model yang telah disimpan.
        FPDF2 (pyfpdf): Untuk men-generate laporan PDF.
    Frontend:
        HTML5
        CSS3
        JavaScript

🚀 Memulai

Untuk menjalankan proyek ini di lingkungan lokal Anda, ikuti langkah-langkah sederhana berikut.
Prasyarat

Pastikan Anda telah menginstal Python 3.x dan pip di sistem Anda.
Instalasi

    Clone repositori ini
    Bash

git clone https://github.com/username_anda/nama_repositori_anda.git

    Ganti username_anda dan nama_repositori_anda dengan URL repositori GitHub Anda.

Masuk ke direktori proyek
Bash

cd nama_repositori_anda

Buat dan aktifkan virtual environment (direkomendasikan)
Bash

# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate

Install semua library yang dibutuhkan
Bash

    pip install -r requirements.txt

        Penting: Pastikan Anda memiliki file requirements.txt. Anda bisa membuatnya dengan menjalankan perintah pip freeze > requirements.txt di terminal setelah menginstal semua library (flask, pandas, scikit-learn, joblib, numpy, fpdf2).

Penggunaan

    Jalankan server Flask
    Bash

python app.py

Buka browser Anda dan akses alamat lokal anda:

Isi formulir dengan data pasien, klik tombol "Analisis Sekarang", dan lihat hasilnya. Jika analisis berhasil, tombol untuk mengunduh PDF akan muncul.
