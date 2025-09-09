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