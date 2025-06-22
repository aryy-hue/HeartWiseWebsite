# Import library yang diperlukan
from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
import numpy as np

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Muat model dan label encoder yang sudah disimpan
try:
    model = joblib.load('heart_risk_model_dt.pkl')
    label_encoder = joblib.load('label_encoder.pkl')
    print("Model dan Label Encoder berhasil dimuat.")
except FileNotFoundError:
    print("Error: Pastikan file 'heart_risk_model_dt.pkl' dan 'label_encoder.pkl' ada di direktori yang sama.")
    model = None
    label_encoder = None

# Definisikan fitur yang diharapkan oleh model (sesuai urutan saat training)
MODEL_FEATURES = [
    'Age', 'Gender', 'Heart rate', 'Systolic blood pressure',
    'Diastolic blood pressure', 'Blood sugar', 'CK-MB', 'Troponin', 'Result'
]

# Definisikan rekomendasi
RECOMMENDATIONS = {
    'Pasien dengan Penyakit Jantung': 'Segera rujuk untuk penanganan medis intensif dan konsultasi dengan spesialis jantung.',
    'Pasien Sehat / Normal': 'Anjurkan untuk menjaga pola hidup sehat dan lakukan pemeriksaan rutin secara berkala.'
}

# [MODIFIKASI] Definisikan rentang nilai yang valid untuk setiap fitur
# CATATAN: Rentang ini adalah contoh dan dapat disesuaikan oleh ahli medis.
VALID_RANGES = {
    'Age': (18, 120),
    'Heart rate': (30, 220),
    'Systolic blood pressure': (70, 250),
    'Diastolic blood pressure': (40, 150),
    'Blood sugar': (2, 30),        # dalam mmol/L
    'CK-MB': (0, 50),              # dalam ng/mL
    'Troponin': (0, 10)            # dalam ng/mL
}

# Membuat route untuk halaman utama ('/')
@app.route('/')
def home():
    # Fungsi ini akan menampilkan file 'index.html' dari folder 'templates'
    return render_template('index.html')


# Membuat route untuk prediksi ('/predict')
# Route ini akan menerima data dari form HTML dengan metode POST
@app.route('/predict', methods=['POST'])
def predict():
    if not model or not label_encoder:
        return jsonify({'error': 'Model tidak berhasil dimuat, periksa log server.'}), 500

    try:
        # 1. Ambil semua data dari form HTML
        data_input = request.form.to_dict()

        # 2. Konversi nilai input ke tipe data yang benar (float)
        data_float = {key: float(value) for key, value in data_input.items()}

        # [MODIFIKASI BARU] Logika untuk validasi anomali
        anomalies = []
        for feature, value in data_float.items():
            # Periksa apakah fitur ada dalam daftar aturan validasi kita
            if feature in VALID_RANGES:
                min_val, max_val = VALID_RANGES[feature]
                if not (min_val <= value <= max_val):
                    anomalies.append(f"Nilai '{feature.title()}' ({value}) di luar rentang wajar ({min_val} - {max_val}).")

        # Validasi khusus: Tekanan sistolik harus lebih tinggi dari diastolik
        systolic = data_float.get('Systolic blood pressure')
        diastolic = data_float.get('Diastolic blood pressure')
        if systolic and diastolic and systolic <= diastolic:
            anomalies.append("Tekanan Darah Sistolik harus lebih besar dari Diastolik.")

        # Jika ditemukan anomali, hentikan proses dan kirim pesan error
        if anomalies:
            # Mengirim status HTTP 400 (Bad Request) bersamaan dengan pesan anomali
            return jsonify({'anomalies': anomalies}), 400

        # Jika tidak ada anomali, lanjutkan proses prediksi
        # 3. Buat DataFrame dari data input dengan urutan kolom yang benar
        input_df = pd.DataFrame([data_float], columns=MODEL_FEATURES)
        print("Data input diterima:", input_df.to_dict())

        # 4. Lakukan prediksi menggunakan model
        prediction_encoded = model.predict(input_df)

        # 5. Ubah hasil prediksi menjadi label teks
        prediction_label = label_encoder.inverse_transform(prediction_encoded)[0]
        
        # 6. Dapatkan rekomendasi
        recommendation_text = RECOMMENDATIONS.get(prediction_label, "Tidak ada rekomendasi spesifik.")

        # 7. Kirim hasil dalam format JSON
        return jsonify({
            'risk_level': prediction_label,
            'recommendation': recommendation_text
        })

    except ValueError:
        # [MODIFIKASI] Tangani jika input tidak bisa diubah ke angka
        return jsonify({'anomalies': ['Pastikan semua input diisi dengan angka yang valid.']}), 400
    except Exception as e:
        # Tangani error umum lainnya
        print(f"Terjadi error: {e}")
        return jsonify({'error': f'Terjadi kesalahan pada server: {e}'}), 500


# Menjalankan aplikasi
if __name__ == '__main__':
    # debug=True agar server otomatis restart jika ada perubahan kode
    app.run(debug=True)