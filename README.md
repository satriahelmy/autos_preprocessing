# Autos Preprocessing

Autos Preprocessing adalah sebuah script yang digunakan untuk melakukan data preprocessing pada dataset ```autos.csv```. Yang dilakukan pada script ini adalah:
1. Pengecekan data
- membaca data dengan format .csv
- melakukan rename kolom
- melakukan konversi data menjadi date time untuk kolom yang seharusnya bertipe datetime

2. Feature Engineering
- Cleansing data pada kolom ```odometer``` dan ```price```
- drop column yang perbandingan data unik terlalu besar
- drop column yang tidak berisi informasi apapun
- drop column yang informasinya unik disetiap baris datanya dan kolom yang memiliki banyak kategori namun tidak balance
- hapus outliers yang memiliki nilai price sehingga hanya yang memiliki nilai 500 s.d 40000
- imputasi nilai NaN dengan mode pada kolom bertipe object
- imputasi nilai NaN dengan median pada kolom bertipe numeric
- normalization
- encoding

3. Save data menjadi .csv

# Lokasi dataset

Dataset yang digunakan bernama ```autos.csv``` yang berada pada folder ```data```

# Cara Menjalankan Program

Setelah pull, jalankan langkah berikut
1. Buka terminal dan install package yang dibutuhkan dengan cara ```python setup.py develop```
2. Jalankan script utamanya dengan cara ```python data_preprocessing.py```
3. Hasil preprocessing berada pada folder ```artifacts```
