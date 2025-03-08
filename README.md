# Bike Sharing Dashboard

## Overview

Dashboard ini dikembangkan untuk menganalisis tren peminjaman sepeda berdasarkan berbagai faktor seperti cuaca, musim, dan kecepatan angin. Visualisasi data membantu dalam memahami pola penggunaan sepeda sepanjang waktu.

## Features

- **Analisis Musiman**: Melihat tren peminjaman sepeda di berbagai musim.
- **Pengaruh Cuaca & Kecepatan Angin**: Menganalisis dampak kondisi cuaca terhadap jumlah peminjaman sepeda.
- **Visualisasi Data**: Menggunakan **Seaborn** dan **Matplotlib** untuk membuat grafik yang informatif.
- **Dashboard Interaktif**: Dibangun dengan **Streamlit** untuk pengalaman yang lebih dinamis.

## Installation

### Install Python

Pastikan kamu memiliki **Python 3.12** terinstal di sistem kamu. Jika belum, unduh dari [python.org](https://www.python.org/downloads/).

### Setup Environment

Jalankan perintah berikut di terminal atau shell untuk membuat lingkungan proyek:

```sh
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
```

### Install Dependencies

Setelah masuk ke dalam environment, instal dependensi yang diperlukan:

```sh
pip install pandas numpy streamlit seaborn matplotlib jupyter
```

## Run Dashboard

Untuk menjalankan dashboard, gunakan perintah berikut:

```sh
streamlit run dashboard/dashboard.py
```

## Folder Structure

```
proyek_analisis_data/
│-- dashboard/
│   │-- dashboard.py  # Main dashboard script
│   │-- all_data.csv # Dataset gabuungan dari day.csv dan hour.csv
│-- data/
│   │-- day.csv  # Dataset Peminjaman pada setiap harinya
|   |-- hour.csv # Dataset peminjaman berdasarkan jam setiap harinya
│-- notebook.ipynb  # Notebook untuk eksplorasi awal
│-- README.md  # Dokumentasi proyek
|-- requirements.txt # Library yang perlu diinstall dan digunakan
|-- url.txt # Berisi Link dashboard streamlit
```

## Data Source

Dataset yang digunakan berasal dari **[Bike Sharing Dataset](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset)** yang berisi informasi peminjaman sepeda harian dan per jam.

## License

Proyek ini menggunakan lisensi **MIT License**. Silakan gunakan dan modifikasi sesuai kebutuhan.

---

_Enjoy analyzing bike sharing data! 🚴‍♂️📊_
