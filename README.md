# 🎓 Attendance System Using Face-Recognition from API JS

Sistem presensi dan sistem poin otomatis untuk lingkungan sekolah, menggunakan teknologi pengenalan wajah berbasis web. Sistem ini menghitung jam masuk dan keluar siswa secara otomatis serta memberikan penilaian poin perilaku, terintegrasi dengan antarmuka web dan kamera.

## 📌 Fitur Utama

- 🔍 **Face Recognition** real-time menggunakan `face-api.js` (client-side) dan `face_recognition` (server-side).
- 📆 **Absensi Otomatis**: Deteksi masuk dan keluar berbasis waktu.
- 🎯 **Sistem Poin Siswa**: Pemberian dan pemantauan poin perilaku siswa.
- 🛡️ **Manajemen Pengguna**: Admin, guru, dan siswa dengan otorisasi berbeda.
- 📊 **Dashboard Real-time**: Statistik kehadiran dan performa siswa.
- 📁 **Penyimpanan Ganda**: Firebase Realtime Database + MongoDB untuk efisiensi dan integrasi.

## ⚙️ Teknologi yang Digunakan

### Backend:

- **Python** + **Flask**: Server utama dan REST API
- **face_recognition**: Library Python berbasis CNN untuk verifikasi wajah
- **MongoDB**: Menyimpan data siswa dan absensi
- **Firebase Realtime Database**: Sinkronisasi data secara langsung

### Frontend:

- **JavaScript** dengan **face-api.js**: Deteksi wajah langsung dari browser
- **Bootstrap**: Antarmuka pengguna yang responsif
- **Fetch API**: Pengiriman data kamera ke server Flask

## 🚀 Instalasi Lokal

1. **Clone repositori**

```bash
git clone https://github.com/username/attendance-face-recognition.git
cd attendance-face-recognition
```
