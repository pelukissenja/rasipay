# Flask Dashboard App

🚀 **Flask Dashboard App** adalah aplikasi berbasis web yang dibangun menggunakan **Python Flask** dengan arsitektur **MVC (Model-View-Controller)**. Aplikasi ini memiliki fitur **autentikasi pengguna**, **dashboard interaktif**, dan **UI profesional**.

---

## 📌 **Fitur yang Sudah Selesai**
### ✅ **1. Environment Setup**
- Instalasi Flask dan dependensi utama
- Struktur proyek berbasis **MVC**
- Penggunaan **Flask Blueprint** untuk modularisasi kode

### ✅ **2. Halaman Utama (Landing Page)**
- Tampilan landing page sederhana menggunakan HTML + CSS
- Terintegrasi dengan template base untuk kemudahan styling

### ✅ **3. Autentikasi Pengguna**
- **Login & Register** menggunakan Flask-WTF
- Hashing password dengan **Werkzeug**
- Redirect ke dashboard setelah login berhasil
- Logout untuk mengakhiri sesi pengguna

### ✅ **4. Dashboard UI Profesional**
- **Sidebar Navigation** dengan menu
- **Navbar** sebagai header
- **Card Informasi** (Total Pengguna, Total Transaksi, Total Produk)
- **Chart Data** menggunakan **Chart.js** untuk visualisasi statistik pengguna

---

## 📌 **Fitur yang Akan Dikerjakan**
### ⏳ **1. Manajemen Pengguna**
- CRUD pengguna (Tambah, Edit, Hapus)
- Role-based access control (Admin & User)

### ⏳ **2. Laporan & Statistik**
- Halaman laporan dengan data grafik
- Filter data berdasarkan waktu

### ⏳ **3. Pengaturan Sistem**
- Opsi untuk mengubah tema tampilan
- Konfigurasi akun dan preferensi pengguna

### ⏳ **4. API Endpoint**
- REST API untuk akses data pengguna dan transaksi
- Integrasi dengan frontend (Vue.js/React)

---

## 🛠 **Instalasi dan Menjalankan Aplikasi**

### **1. Clone Repository**
```sh
git clone https://github.com/username/flask-dashboard.git
cd flask-dashboard
```

### **2. Buat Virtual Environment & Install Dependencies**
```sh
python -m venv venv
source venv/bin/activate  # (Linux/Mac)
venv\Scripts\activate     # (Windows)
pip install -r requirements.txt
```

### **3. Jalankan Aplikasi**
```sh
python app.py
```

### **4. Akses di Browser**
```
http://127.0.0.1:5000/
```

---

## ⚙ **Struktur Proyek**
```
flask_app/
│── app.py  # Entry point aplikasi
│── config.py  # Konfigurasi aplikasi
│── models/  # Database models
│── views/  # Route & rendering templates
│── controllers/  # Business logic
│── templates/  # HTML templates
│   ├── layout.html  # Base template
│   ├── dashboard.html  # Dashboard UI
│── static/
│   ├── css/style.css  # Styling UI
│   ├── js/chart.js  # Chart logic
│── forms.py  # Flask-WTF Forms
│── database.db  # SQLite database
│── requirements.txt  # Dependencies
│── README.md  # Dokumentasi
```

---

## 🔥 **Kontributor**
- **pelukissenja | @kang_ghostin9** (Owner & Developer)

Jika Anda ingin berkontribusi, silakan buat **Pull Request** atau **Issue**.

---

## 📜 **Lisensi**
MIT License © 2025 pelukissenja | @kang_ghostin9

---

## 📩 **Kontak & Feedback**
Jika ada pertanyaan atau saran, hubungi saya di [email@example.com](mailto:email@example.com) atau buat **Issue** di repository ini.

🎯 **Selamat Membangun Aplikasi! 🚀**
