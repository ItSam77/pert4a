# 🏢 Employee Attrition Prediction

## 📋 Deskripsi

Aplikasi **Employee Attrition Prediction** ini adalah sebuah web app yang dibangun menggunakan **Streamlit** untuk memprediksi apakah seorang karyawan akan keluar dari perusahaan atau tidak. Aplikasi ini menggunakan algoritma machine learning yang telah dilatih dengan data historis karyawan untuk memberikan prediksi yang akurat.


## 📊 Dataset

**Sumber Dataset:** [Kaggle - Employee Attrition Rate](https://www.kaggle.com/datasets/prachi13/employeeattritionrate)


## 🚀 Cara Instalasi & Menjalankan

### 📋 Persyaratan Sistem
- **Python**: Versi 3.9, 3.10, atau 3.11 *(disarankan 3.10)*
- **Git**: Untuk clone repository
- **Internet**: Untuk download dependencies

### 🔧 Langkah-langkah Instalasi

#### 1️⃣ **Clone Repository**
```bash
git clone https://github.com/ItSam77/pert5a.git
cd pert5a
```

#### 2️⃣ **Buat Virtual Environment**

**Di bawah ini menggunakan Python 3.10, jika Anda menggunakan versi lain silakan sesuaikan dengan versi Python yang Anda gunakan.**
**Misalkan Anda menggunakan Python 3.9 maka ganti py -3.10 dengan py -3.9**

**Untuk Windows:**
```bash
py -3.10 -m venv venv
venv\Scripts\activate
```

**Untuk macOS/Linux:**
```bash
python3.10 -m venv venv
source venv/bin/activate
```

**Untuk Semua OS:**
```bash
cd pert5a
```

#### 3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

#### 4️⃣ **Jalankan Aplikasi**
```bash
streamlit run main.py
```

#### 5️⃣ **Buka Browser**
Aplikasi akan berjalan di: **http://localhost:8501**

---

## 💻 Cara Penggunaan

### 📝 Input Data Karyawan
1. **Age (Umur)**: Masukkan umur karyawan (18-60 tahun)
2. **Monthly Income**: Masukkan gaji bulanan
3. **Marital Status**: Pilih status pernikahan (Single/Married/Divorced)
4. **Years at Company**: Masukkan lama bekerja di perusahaan
5. **Job Satisfaction**: Pilih tingkat kepuasan kerja (Level 0-4)

### 🔍 Interpretasi Hasil
- 🟢 **Low Risk**: Karyawan kemungkinan akan tetap di perusahaan
- 🔴 **High Risk**: Karyawan kemungkinan akan keluar dari perusahaan
- **Percentage**: Menunjukkan tingkat kepercayaan prediksi

---

## 📁 Struktur Project

```
pert5a/
├── 📄 main.py                          # Aplikasi utama Streamlit
├── 🤖 attrition_prediction_model.pkl   # Model ML yang sudah dilatih
├── 📊 data.csv                         # Dataset training
├── 📓 notebook.ipynb                   # Notebook pengembangan model
├── 📋 requirements.txt                 # Daftar dependencies
├── 📖 README.md                        # Dokumentasi project
└── 📁 venv/                            # Virtual environment
```

---

## 🌐 Demo Online

Untuk mengakses aplikasi Streamlit yang telah di-deploy, silakan klik [di sini](https://pert5a-eme4yx37v3pvptbz2fnb7g.streamlit.app/) 
(**Tidak Lifetime, yang berarti jika tidak digunakan maka app akan masuk ke mode sleep**)