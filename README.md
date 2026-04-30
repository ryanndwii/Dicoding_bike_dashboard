# 🚴 Bike Sharing Dashboard

Dashboard interaktif untuk menganalisis pola penyewaan sepeda berdasarkan waktu, cuaca, dan tipe pengguna menggunakan Streamlit.

---

## 📊 Fitur Dashboard

- Analisis jumlah penyewaan per jam (Peak Hour)
- Pengaruh cuaca terhadap jumlah penyewaan
- Segmentasi pengguna (Casual vs Registered)
- Perbandingan hari kerja vs hari libur
- KPI utama (Total, rata-rata harian & per jam)


---
## ⚙️ Setup Environment - Anaconda

    conda create --name main-ds python=3.9
    conda activate main-ds
    pip install -r requirements.txt

---

## 💻 Setup Environment - Shell/Terminal

    mkdir proyek_analisis_data
    cd proyek_analisis_data
    pip install pipenv
    pipenv install
    pipenv shell
    pip install -r requirements.txt

---

## 📁 Struktur Project

    ├── dashboard.py
    ├── day_clean.csv
    ├── hour_clean.csv
    ├── requirements.txt
    └── README.md

---

## ▶️ Run Streamlit App

    streamlit run dashboard.py

---

## 🌐 Deploy ke Streamlit Cloud

1. Push project ke GitHub  
2. Buka https://share.streamlit.io  
3. Login dengan GitHub  
4. Klik **New App**  
5. Pilih repository & file `dashboard.py`  
6. Klik **Deploy**

---

## 🔗 Demo Online

👉 https://dicodingbikedashboard-e6trgsewrxd7iddbxddyrm.streamlit.app/

---

## 🚀 Teknologi

- Streamlit  
- Pandas  
- Matplotlib 
- Seaborn 
