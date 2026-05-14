# Dashboard Pemantauan Cuaca

Aplikasi pemantauan cuaca berbasis Flask yang melacak prakiraan cuaca 7 hari untuk wilayah Jakarta dan menyimpannya ke dalam database SQLite.

## Fitur Utama
- **Pemantauan Mingguan**: Mengambil data prakiraan cuaca 7 hari secara otomatis dari Open-Meteo API.
- **Integrasi SQLite**: Menyimpan data cuaca secara lokal untuk akses cepat.
- **Antarmuka Modern**: Desain premium dengan gaya glassmorphism dan mode gelap.
- **Responsif**: Dapat diakses dengan baik melalui perangkat desktop maupun mobile.

## Instruksi Pengaturan

1. **Buat dan aktifkan virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Instal dependensi**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Jalankan aplikasi**:
   ```bash
   python app.py
   ```

4. **Akses Dashboard**:
   Buka browser Anda dan buka `http://127.0.0.1:5001`.
   Klik tombol **Refresh Data** untuk mengambil data cuaca terbaru.

## Struktur Proyek
- `app.py`: Logika utama aplikasi dan rute (routes).
- `models.py`: Definisi skema database (ORM).
- `static/css/style.css`: Styling antarmuka.
- `templates/index.html`: Template dashboard.
- `instance/weather.db`: Database SQLite (dibuat otomatis).

## Alur Program

1. **Pengambilan Data**: Aplikasi mengambil data cuaca dari [Open-Meteo API](https://api.open-meteo.com/v1/forecast).
2. **Spesifikasi API**: Dokumentasi detail mengenai parameter lokasi dan fitur API lainnya dapat ditemukan di [Dokumentasi Open-Meteo](https://open-meteo.com/en/docs).
3. **Penyimpanan Database**: Data yang diambil disimpan dalam database SQLite dengan skema berikut:

   ```sql
   CREATE TABLE weather_forecast (
       id INTEGER NOT NULL PRIMARY KEY, 
       date DATE NOT NULL UNIQUE, 
       temp_min FLOAT NOT NULL, 
       temp_max FLOAT NOT NULL, 
       condition_code INTEGER NOT NULL, 
       precipitation FLOAT NOT NULL, 
       created_at DATETIME
   );
   ```

4. **Konfigurasi Lokasi Jakarta**: Untuk melacak Jakarta, parameter berikut digunakan:
   - **Latitude**: -6.2088
   - **Longitude**: 106.8456
   - **Data Harian**: `weathercode`, `temperature_2m_max`, `temperature_2m_min`, `precipitation_sum`
   - **Timezone**: `Asia/Bangkok`

5. **Antarmuka Web**: Dashboard ditampilkan menggunakan framework Flask pada Python.

---
*Dibuat untuk tugas mata kuliah Pemrograman Back-End.*
