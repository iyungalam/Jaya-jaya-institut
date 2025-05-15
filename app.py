# app.py
import streamlit as st
import pandas as pd
import joblib
import numpy as np
import time
from PIL import Image
from preprocessing import preprocess_input
from predict import make_prediction

# Konfigurasi halaman
st.set_page_config(page_title="🎓 Prediksi Kinerja Mahasiswa", layout="wide")

# Header Visual
col1, col2 = st.columns([1, 8])
with col1:
    st.image("logo.png", width=100)
with col2:
    st.markdown("<h1 style='color:#2980B9;'>🎓 Prediksi Dropout Mahasiswa</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:18px;'>Aplikasi ini memprediksi apakah mahasiswa akan <b style='color:#27AE60;'>LULUS</b> atau <b style='color:#E74C3C;'>DROPOUT</b> berdasarkan data akademik dan demografis.</p>", unsafe_allow_html=True)

st.markdown("---")

# Sidebar Identitas
with st.sidebar:
    st.markdown("## 👩‍💼 Informasi Developer")
    st.info("""
    **Nama:** Nurul Alam  
    **Email:** iyungalam5@gmail.com  
    **ID Dicoding:** -
    """)
    st.markdown("---")
    st.markdown("## 📝 Masukkan Data Mahasiswa")

    gender = st.selectbox("Jenis Kelamin", ["Male", "Female"])
    displaced = st.selectbox("Pengungsi", ["Yes", "No"])
    debtor = st.selectbox("Memiliki Hutang", ["Yes", "No"])
    scholarship = st.selectbox("Penerima Beasiswa", ["Yes", "No"])
    tuition_fees = st.selectbox("SPP Tepat Waktu", ["Yes", "No"])
    attendance = st.selectbox("Kehadiran", ["Daytime", "Evening"])

# Input Numerik
st.markdown("## 🎯 Data Akademik Mahasiswa")

col1, col2 = st.columns(2)
with col1:
    admission_grade = st.slider("🎓 Nilai Masuk", 0.0, 200.0, 100.0)
    prev_qual_grade = st.slider("📜 Nilai Kualifikasi Sebelumnya", 0.0, 200.0, 100.0)
    c1_approved = st.slider("✅ Disetujui Semester 1", 0, 30, 10)
    c1_grade = st.slider("📘 Nilai Semester 1", 0.0, 20.0, 10.0)
    c1_enrolled = st.slider("🧾 Terdaftar Semester 1", 0, 30, 10)

with col2:
    c1_credited = st.slider("📗 Kredit Semester 1", 0, 30, 10)
    c2_approved = st.slider("✅ Disetujui Semester 2", 0, 30, 10)
    c2_grade = st.slider("📘 Nilai Semester 2", 0.0, 20.0, 10.0)
    c2_enrolled = st.slider("🧾 Terdaftar Semester 2", 0, 30, 10)
    c2_credited = st.slider("📗 Kredit Semester 2", 0, 30, 10)

# Buat DataFrame
input_data = pd.DataFrame({
    'Gender': [gender],
    'Displaced': [displaced],
    'Debtor': [debtor],
    'Scholarship_holder': [scholarship],
    'Tuition_fees_up_to_date': [tuition_fees],
    'Daytime_evening_attendance': [attendance],
    'Admission_grade': [admission_grade],
    'Previous_qualification_grade': [prev_qual_grade],
    'Curricular_units_1st_sem_approved': [c1_approved],
    'Curricular_units_1st_sem_grade': [c1_grade],
    'Curricular_units_1st_sem_enrolled': [c1_enrolled],
    'Curricular_units_1st_sem_credited': [c1_credited],
    'Curricular_units_2nd_sem_approved': [c2_approved],
    'Curricular_units_2nd_sem_grade': [c2_grade],
    'Curricular_units_2nd_sem_enrolled': [c2_enrolled],
    'Curricular_units_2nd_sem_credited': [c2_credited],
})

with st.expander("📋 Tinjau Data Input"):
    st.dataframe(input_data)

# Prediksi
st.markdown("## 🔍 Hasil Prediksi")

if st.button("🚀 Prediksi Sekarang"):
    with st.spinner("🔄 Memproses prediksi..."):
        time.sleep(2)
        data_processed = preprocess_input(input_data)
        prediction = make_prediction(data_processed)

        if prediction == "Graduate":
            st.success("🎉 Mahasiswa diprediksi akan **LULUS**.")
        else:
            st.error("⚠️ Mahasiswa diprediksi akan **DROPOUT**.")

        st.markdown("#### 🔧 Data yang digunakan:")
        st.dataframe(data_processed)

st.snow()
