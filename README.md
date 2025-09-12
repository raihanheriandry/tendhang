# Tugas Individu 2 

## Langkah Pengimplementasian

#### 1. Buat Proyek Django Baru
   - Menginstal dependensi yang ditulis di file `requirements.txt`
   - Buat proyek django baru menggunakan `django-admin startproject tendhang .`
   - Setelah proyek berhasil dibuat, akan ada direktori env dan tendhang beserta file lain 
   - Melakukan setup environment variable dan konfigurasi `settings.py`

#### 2. Buat Aplikasi Bernama `main`
   - Buat aplikasi dengan `python manage.py startapp main`
   - Akan ada direktori main

#### 3. Routing Pada Proyek Agar Bisa Menjalankan `main`
   - Menabmahkan rute URL di dalam list urlpatterns pada `urls.py` pada direktori proyek

#### 4. Buat Model Pada Aplikasi `main`
   - Membuat model pada `models.py` name, price, dll dengan tipe yang sesuai
   - Menambahkan kategori choices

#### 5. Buat Fungsi Pada `views.py` Untuk Dikembalikan ke Template 
   - Membuat fungsi `show_main()` yang akan merender kode HTML

#### 6. Routing Pada Aplikasi `main` 
   - Menambahkan rute URL pada list urlpattern yang memetakan ke fungsi yang dibuat tadi

#### 7. Deployment ke PWS
   - Melakukan commit dan push ke github dan pws juga

#### 8. Buat `README.md`
   - Membuat file `README.md` yang menjelaskan cara mengerjakan checkpoint diatas dan jawaban pertanyaan


## Bagan Alur Django

![bagan](https://github.com/user-attachments/assets/d2d87dd5-f68a-4a17-81d5-48907f10173e)

Saat ada request dari pengguna, akan dipetakan oleh `urls.py` ke fungsi di `views.py`. `views.py` akan mengambil data dari `models.py` apabila dibutuhkan, kemudian diproses di `views.py` kembali. Output akan ditampilkan dengan cara dikirim ke Templates dan hasilnya di kembalikan ke pengguna sebagai response

## Peran `settings.py`

`settings.py` mengatur seluruh konfigurasi project Django, seperti
- Mengatur konfigurasi proyek dan mode development
- Mengatur keamanan seperti allowed host
- Mengatur aplikasi di installed apps
- Mengatur database
- Mengatur template, static url, dan media url
- Mengatur middleware

## Cara Kerja Migrasi Django

Migrasi adalah untuk membuat atau memperbarui struktur database berdasarkan perubahan pada file models.py. Kemudian perlu membuat file migrasi yang berisi instruksi perubahan database menggunakan `python manage.py makemigrations`. Kemudian baru mengeksekusi migrasi ke database dengan `python manage.py migrate`

## Alasan Django Menjadi Awal Pembelajaran Software Dev

Karena fiturnya cukup lengkap dan dokumentasi di web resminya sangat lengkap juga. Saat menggunakan django sudah sepaket terinstall library yang dibutuhkan juga dari keamanan, pengelolaan database, hingga pemetaan url dan template engine untuk render HTML. Struktur proyek juga menerapkan MVT, jadi untuk pemula bisa paham alur datanya dari request sampai response nya. 

## Feedback Asisten

Asdos saya sudah sangat baik, sangat mendalami bidangnya, jadi untuk saat ini belum ada feedback yang bagaimana. Terimakasih tim asdos.

link web: [tendhang](https://raihan-maulana41-tendhang.pbp.cs.ui.ac.id/)

---

# Tugas Individu 3

## Langkah Pengimplementasian

#### 1. Menambahkan 4 Fungsi Untuk Melihat Objek   
   Buat 4 fungsi baru untuk melihat objek yang akan me-return HTTP response, yaitu:
   - `show_xml` : melihat semua data dalam xml, parameter sebuah request
   - `show_json` : melihat semua data dalam json, parameter sebuah request
   - `show_xml_by_id` : melihat suatu objek data dalam xml berdasarkan id-nya, parameter sebuah request dan id
   - `show_json_by_id` : melihat suatu objek data dalam json berdasarkan id-nya, parameter sebuah request dan id

#### 2. Buat Routing URL untuk Masing-Masing `views` yang Ditambahkan
   Menambahkan 4 path sesuai fungsi yang sudah dibuat tadi pada `urls.py` di direktori `main` agar bisa diakses di browser

#### 3. Buat Halaman yang Menampilkan Data Objek dengan Tombol "Add" dan "Detail" 
   - Membuat struktur form dulu pada main dengan nama file forms.py 
   - Isi forms.py dengan field name, price, description, category, thumbnail, is_featured, stock, size
   - Tambahkan fungsi pada views.py untuk menambahkan data (add_product) dan melihat data (product_detail) yang akan diteruskan ke templates

#### 4. Buat Halaman Form untuk Menambahkan Data.
   - Membuat base.html dulu sebagai template konten selanjutnya
   - Mengupdate main.html di template di direktori main agar ada tombol Add dan Detail
   - Membuat halaman add_product.html, masukkan sebagai tujuan fungsi add_product di views.py, dan menambahkan path ke urls.py

#### 5. Buat Halaman untuk Melihat Detail dari Tiap Objek Data.
   - Membuat halaman product_detail.html, masukkan sebagai tujuan fungsi product_detail di views.py, dan menambahkan path ke urls.py


## Mengapa Kita Memerlukan Data Delivery dalam Pengimplementasian Sebuah Platform?

Agar tiap komponen pada platform tersebut bisa bertukar data dengan baik, tidak ada yang hilang dan bocor. Data Delivery juga memungkinkan untuk platform bisa diintegrasikan dengan pihak ketiga. Jadi Data Delivery memastikan data bisa mengalir dengan aman, cepat, akurat, dan terukur dari satu titik ke titik lain, sehingga platform bisa berjalan lancar, terintegrasi, dan memberikan pengalaman terbaik ke pengguna.

## Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Menurut saya, JSON lebih baik dibanding XML, karena sintaksnya yang lebih mudah dipahami meskipun orang awam, yang berupa seperti dictionary pada python. Saat ini juga JSON lebih populer dibanding XML dalam pengiriman data aplikasi maupun web. Hal itu bisa terjadi karena struktur JSON yang cenderung lebih sederhana dan mudah dipahami dibanding XML, juga terintegrasi pada ekosistem modern di hampir semua bahasa pemrograman. Selain itu JSON juga lebih cepat dan lebih mudah diimplementasi di web, karena terintegrasi langsung pada Javascript

## Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

Fungsi dari method is_valid() adalah untuk memvalidasi data apakah data dari user yang di input di form aman dan sesuai untuk diproses. Method ini mengecek apakah data form valid sesuai aturan field dan tipe datanya dan mencegah error pada pemrosesan data di proses lanjut.

## Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

Saat membuat form kita perlu membuat csrf_token untuk melindungi aplikasi web dari CSRF (Cross-Site Request Forgery) attack. CSRF attack terjadi ketika penyerang menipu user agar tanpa sadar mengirim request berbahaya ke server dalam kondisi user sudah login. Django perlu memastikan bahwa setiap request POST berasal dari form yang benar-benar dibuat oleh aplikasi kita, bukan dari situs luar. Tanpa token ini, server tidak dapat memverifikasi apakah request berasal dari sumber yang sah atau tidak, sehingga memungkinkan penyerang untuk melakukan tindakan yang tidak diinginkan atas nama pengguna tersebut, seperti mengubah data. Penyerang bisa memaksa browser user yang sudah login untuk mengirim request berbahaya.

## Feedback Asdos

Asdos saya sudah sangat baik, cukup membantu dan mendalami bidangnya, jadi untuk saat ini belum ada feedback yang bagaimana. Terimakasih tim asdos.

## Screenshot Hasil Akses URL pada Postman

