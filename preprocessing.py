# preprocessing.py
import joblib
import pandas as pd


def preprocess_input(education_df):
    education_df = education_df.copy()

    # Muat fitur yang digunakan saat pelatihan
    features_expected = joblib.load("model/features_used.joblib")

    cat_cols = [
        'Gender', 'Displaced', 'Debtor',
        'Scholarship_holder', 'Tuition_fees_up_to_date', 'Daytime_evening_attendance'
    ]
    num_cols = [
        'Admission_grade', 'Previous_qualification_grade',
        'Curricular_units_1st_sem_approved', 'Curricular_units_1st_sem_grade',
        'Curricular_units_1st_sem_enrolled', 'Curricular_units_1st_sem_credited',
        'Curricular_units_2nd_sem_approved', 'Curricular_units_2nd_sem_grade',
        'Curricular_units_2nd_sem_enrolled', 'Curricular_units_2nd_sem_credited'
    ]

    # Encode kategori
    for col in cat_cols:
        encoder = joblib.load(f"model/encoder_{col}.joblib")
        education_df[col] = encoder.transform(education_df[col])

    # Scaling numerik
    for col in num_cols:
        scaler = joblib.load(f"model/scaler_{col}.joblib")
        education_df[col] = scaler.transform(education_df[[col]])

    # Filter dan urutkan kolom agar identik dengan saat training
    education_df = education_df[features_expected]

    return education_df

