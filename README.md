# Tendhang Football Shop

### Deployment
Check here: [Tendhang Football Shop](https://raihan-maulana41-tendhang.pbp.cs.ui.ac.id/)

### Archive Tugas
   - [Tugas 2 PBP 2025/2026](https://github.com/raihanheriandry/tendhang/wiki/Tugas-2-PBP)

---

## Tugas Individu 3

### Langkah Pengimplementasian

#### 1. Menambahkan 4 Fungsi Untuk Melihat Objek   
   Buat 4 fungsi baru untuk melihat objek yang akan me-return HTTP response, yaitu:
   - `show_xml` : melihat semua data dalam xml, parameter sebuah request
   - `show_json` : melihat semua data dalam json, parameter sebuah request
   - `show_xml_by_id` : melihat suatu objek data dalam xml berdasarkan id-nya, parameter sebuah request dan id
   - `show_json_by_id` : melihat suatu objek data dalam json berdasarkan id-nya, parameter sebuah request dan id

#### 2. Buat Routing URL untuk Masing-Masing `views` yang Ditambahkan
   Menambahkan 4 path sesuai fungsi yang sudah dibuat tadi pada `urls.py` di direktori `main` agar bisa diakses di browser

#### 3. Buat Halaman yang Menampilkan Data Objek dengan Tombol "Add" dan "Detail" 
   - Membuat struktur form dulu pada main dengan nama file `forms.py` 
   - Isi `forms.py` dengan `field name`, `price`, `description`, `category`, `thumbnail`, `is_featured`, `stock`, `size`
   - Tambahkan fungsi pada `views.py` untuk menambahkan data (`add_product`) dan melihat data (`product_detail`) yang akan diteruskan ke templates

#### 4. Buat Halaman Form untuk Menambahkan Data.
   - Membuat `base.html` dulu sebagai template konten selanjutnya
   - Mengupdate `main.html` di template di direktori `main` agar ada tombol Add dan Detail
   - Membuat halaman `add_product.html`, masukkan sebagai tujuan fungsi `add_product` di `views.py`, dan menambahkan path ke `urls.py`

#### 5. Buat Halaman untuk Melihat Detail dari Tiap Objek Data.
   - Membuat halaman `product_detail.html`, masukkan sebagai tujuan fungsi `product_detail` di `views.py`, dan menambahkan path ke `urls.py`


### Mengapa Kita Memerlukan Data Delivery dalam Pengimplementasian Sebuah Platform?

Agar tiap komponen pada platform tersebut bisa bertukar data dengan baik, tidak ada yang hilang dan bocor. Data Delivery juga memungkinkan untuk platform bisa diintegrasikan dengan pihak ketiga. Jadi Data Delivery memastikan data bisa mengalir dengan aman, cepat, akurat, dan terukur dari satu titik ke titik lain, sehingga platform bisa berjalan lancar, terintegrasi, dan memberikan pengalaman terbaik ke pengguna.

### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Menurut saya, JSON lebih baik dibanding XML, karena sintaksnya yang lebih mudah dipahami meskipun orang awam, yang berupa seperti dictionary pada python. Saat ini juga JSON lebih populer dibanding XML dalam pengiriman data aplikasi maupun web. Hal itu bisa terjadi karena struktur JSON yang cenderung lebih sederhana dan mudah dipahami dibanding XML, juga terintegrasi pada ekosistem modern di hampir semua bahasa pemrograman. Selain itu JSON juga lebih cepat dan lebih mudah diimplementasi di web, karena terintegrasi langsung pada Javascript

### Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?

Fungsi dari method `is_valid()` adalah untuk memvalidasi data apakah data dari user yang di input di form aman dan sesuai untuk diproses. Method ini mengecek apakah data form valid sesuai aturan field dan tipe datanya dan mencegah error pada pemrosesan data di proses lanjut.

### Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

Saat membuat form kita perlu membuat `csrf_token` untuk melindungi aplikasi web dari CSRF (Cross-Site Request Forgery) attack. CSRF attack terjadi ketika penyerang menipu user agar tanpa sadar mengirim request berbahaya ke server dalam kondisi user sudah login. Django perlu memastikan bahwa setiap request POST berasal dari form yang benar-benar dibuat oleh aplikasi kita, bukan dari situs luar. Tanpa token ini, server tidak dapat memverifikasi apakah request berasal dari sumber yang sah atau tidak, sehingga memungkinkan penyerang untuk melakukan tindakan yang tidak diinginkan atas nama pengguna tersebut, seperti mengubah data. Penyerang bisa memaksa browser user yang sudah login untuk mengirim request berbahaya.

### Feedback Asdos

Asdos saya sudah sangat baik, cukup membantu dan mendalami bidangnya, jadi untuk saat ini belum ada feedback yang bagaimana. Terimakasih tim asdos.

### Screenshot Hasil Akses URL pada Postman

JSON
![json all](https://github.com/user-attachments/assets/c55695f4-2bb7-4e65-b673-d31c537e3c16)

XML
![xml all](https://github.com/user-attachments/assets/8d984e90-9b31-44e3-94d4-305391122073)

JSON by id
![json by id](https://github.com/user-attachments/assets/6af287b4-a50d-4ac2-8fb6-f03632a4bd2e)

XML by id
![xml by id](https://github.com/user-attachments/assets/63b9ea1f-233e-4d2e-8009-6a4ad46826e6)