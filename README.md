# Proyek Akhir: Menyelesaikan Permasalahan institusi pendidikan (jaya jaya institut).

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Permasalahan Bisnis
Permasalahan yang dihadapi adalah tingginya jumlah mahasiswa yang dropout di jaya jaya institut. 


### Cakupan Proyek
Untuk menjawab permasalahan bisnis tersebut, kita akan mengidentifikasi berbagai faktor yang mempengaruhi tingginya angka dropout. Nah, pada proyek ini kita akan membuat bussiness dashboard untuk membantu memonitori berbagai faktor tersebut.Selain itu, kita akan menerapkan analisis klasifikasi untuk fitur dropout dengan metode machine learning. Algoritma machine learning yang digunakan adalah random forest. Kita juga akan melakukan sedikit proses Exploratory Data Analysis (EDA) untuk memperoleh gambaran terkait dataset yang akan kita gunakan. Pada prosesnya, kita juga akan coba melihat karakteristik dari setiap kelompok data (berdasarkan beberapa kolom kategoris) yang terdapat dalam dataset.

Berdasarkan cakupan proyek tersebut, kita membutuhkan beberapa resource dan tool, yaitu

1.data siswa di Jaya Jaya Institut (data.csv).
2.Tool yang digunakan untuk membuat bussiness dashboard adalah Looker Studio.
3.bahasa pemrograman Python sebagai tool utama kita dalam proyek ini.
4.berbagai library pendukung untuk pengolahan data dan pengembangan model machine learning.

### Persiapan

Sumber data: https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/refs/heads/main/students_performance/data.csv

Setup environment:

```
pip install numpy pandas matplotlib seaborn scikit-learn==1.2.2 joblib==1.4.2 streamlit==1.24.1
```

## Business Dashboard

Business dashboard proyek ini dibuat menggunakan Google Looker Studio dengan menambahkan fitur filter berdasarkan gender, status, debtor, scholarship, attendance, 
displaced, and tuition


Dashboard dibuat dengan menggunakan Google Looker Studio. Dashboard dapat diakses pada link berikut ini:
```
https://lookerstudio.google.com/reporting/e7dee503-a8e1-4e15-a03b-3b37c3edc792

```

Prediksi untuk model machine learning dibuat dengan menggunakan Streamlit. Prediksi dapat diakses pada link berikut ini:
```
https://jaya-jaya-institut-iipqyfahiv3fmgtwfyjue3.streamlit.app/

```


## Conclusion

- Komposisi siswa terdiri dari 65.6% Laki-laki dan 34.4% Perempuan.
- Tingkat kelulusan siswa (Graduation Rate) sebesar 60.9%% sedangkan tingkat ketidaklulusan (Dropout Rate) sebesar 39,1% dari 3.630 siswa
- Penerima beasiswa terdapat (26,7%) dan siswa yang bukan penerima (73,3%)
- Dari 1.421 siswa yang dropout terdapat 1.214 siswa (85.43%) yang mengikuti kelas pagi dan 207 siswa (14.57%) yang mengikuti kelas malam
- Selain itu, faktor curricular units dan tuition fees juga cukup berpengaruh pada tingkat kelulusan siswa.

### Rekomendasi Action Items

- Memberikan bimbingan dan dukungan tambahan kepada siswa penerima beasiswa untuk membantu mereka mengatasi tantangan akademik dan non-akademik.
- Menyediakan tutor atau mentor, kelas remedial, bimbingan akademik, dan dukungan psikologis bagi siswa yang membutuhkannya.
