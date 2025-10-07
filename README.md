# Tendhang Football Store
Where Kickers Find Their Gear

### 🪁 Deployment
Check here: [Tendhang Football Shop](https://raihan-maulana41-tendhang.pbp.cs.ui.ac.id/)

### 📚 Archive Tugas
   - [Tugas 2 PBP 2025/2026](https://github.com/raihanheriandry/tendhang/wiki/Tugas-2-PBP)
   - [Tugas 3 PBP 2025/2026](https://github.com/raihanheriandry/tendhang/wiki/Tugas-3-PBP)
   - [Tugas 4 PBP 2025/2026](https://github.com/raihanheriandry/tendhang/wiki/Tugas-4-PBP)
   - [Tugas 5 PBP 2025/2026](https://github.com/raihanheriandry/tendhang/wiki/Tugas-5-PBP)
   - [Tugas 6 PBP 2025/2026](https://github.com/raihanheriandry/tendhang/wiki/Tugas-6-PBP)

---

## Tugas Individu 6

### Mengubah fitur - fitur tugas sebelumnya menggunakan AJAX

#### Fitur CRUD (Create Read Update Delete) product menggunakan AJAX

Template `product_detail.html` masih menggunakan HTML dan Tailwind yang sama untuk menampilkan gambar, kategori, harga, stok, deskripsi, serta informasi penjual, namun elemen-elemennya diisi secara otomatis oleh JavaScript setelah mengambil data JSON dari endpoint Django (`show_json_by_id`). 

Pada Add Product dibuat juga dengan ajax, form penambahan produk dikirim menggunakan fetch() ke endpoint Django yang menerima data POST, Fitur Update menggunakan `modal_edit.html`, di mana data produk diambil berdasarkan ID (UUID), ditampilkan ke form, lalu dikirim kembali lewat fetch() POST ke endpoint `edit_product_ajax/<uuid:product_id>/` untuk menyimpan perubahan tanpa reload halaman. 

#### Mengubah Login dan Register menggunakan AJAX.

Pada versi sebelumnya, proses login dan register menggunakan form standar Django,  ketika pengguna menekan tombol “Login” atau “Register”, browser akan mengirimkan permintaan HTTP POST langsung ke server, lalu Django akan memproses form tersebut dan merender ulang halaman (misalnya `login.html` atau `register.html`). Kemudian ditambahkan javascript dibawahnya yang berfungsi untuk menangkap event submit form, mencegah reload bawaan browser (`event.preventDefault()`), lalu mengirim data form ke server menggunakan `fetch()` atau `XMLHttpRequest` secara asinkron (tanpa memuat ulang halaman). Server Django masih menggunakan fungsi autentikasi bawaan, seperti `authenticate()`, `login()`, dan `UserCreationForm`, namun view Django sekarang mengembalikan respons JSON seperti `{ "success": true }` jika berhasil, atau `{ "success": false, "errors": {...} }` jika gagal. JavaScript di sisi klien kemudian membaca hasil JSON tersebut dan menampilkan pesan sukses atau error langsung di halaman (tanpa berpindah) kemudian redirect manual menggunakan `window.location.href` ke halaman tujuan.

### Update tampilan

#### Membuat tombol yang akan menampilkan modal untuk create dan update product dalam bentuk form.

Membuat modal untuk menambahkan produk dan edit produk. Saya sambungkan ke add product yang utam, sehingga jika akan menambah produk hanya lewat modal yang muncul di halaman `main.html`. Selain `modal_add.html`, saya juga buat `modal_edit.html` yang untuk fitur update product tapi juga lewat modal, jadi tidak perlu pindah halaman.

#### Membuat modal konfirmasi saat pengguna ingin menghapus product

Pada modal_delete.html showConfirmModal() menampilkan modal, kemudian mengembalikan Promise yang akan di-resolve dengan nilai true jika pengguna mengklik "Yes, Delete" atau false jika mengklik "Cancel" atau di luar modal. Kemudian, fungsi deleteProduct() menggunakan sintaks await showConfirmModal() untuk menghentikan eksekusi hingga Promise tersebut selesai (modal ditutup), memungkinkan program melanjutkan proses penghapusan (mengirim request POST dengan CSRF Token) hanya jika pengguna mengkonfirmasi penghapusan (confirmed adalah true), dan menampilkan notifikasi toast Success atau Error berdasarkan respons server.

#### Saat melakukan aksi dari modal, product akan di-refresh tanpa perlu melakukan refresh halaman.
Menambahkan ini pada `main.html` 
```document.addEventListener('productAdded', function() {
    fetchProducts();
});

document.addEventListener('productUpdated', function() {
    fetchProducts();
});

document.addEventListener('productDeleted', function() {
    fetchProducts();    
});
```

#### Membuat tombol refresh yang akan menampilkan list product terbaru tanpa perlu refresh halaman

Ini ada pada main.html All Product maka akan menampikan list product terbaru tanpa refresh halaman

#### Membuat Loading, Empty, dan Error state melalui Javascript.

Pada main.html ditambahkan juga state untuk loading empty dan error. Yang mana bisa dikendalikan dengan js saat misal ada data yang error atau gagal dikirim dari server, sehingga tidak error semua halamannya.

#### Menampilkan Toast saat create, update, atau delete product dan saat login, logout, dan register

Membuat toast pada toast.html dan toast.js yang mana bisa dipanggil saat dibutuhkan, bisa dengan state succes (hijau), error(merah) atau tidak ada state (putih)

### Apa perbedaan antara synchronous request dan asynchronous request?

Perbedaan utama terletak pada cara klien (browser) menangani permintaan saat menunggu respons dari server. 
- Synchronous request bersifat blocking; artinya, klien akan terhenti dan tidak dapat menjalankan operasi atau interaksi lain hingga permintaan selesai dan respons diterima. Hal ini sering menyebabkan browser tampak "membeku" atau memerlukan refresh halaman total. 

- Asynchronous request (seperti yang digunakan dalam AJAX) bersifat non-blocking. Klien mengirim permintaan di latar belakang dan segera melanjutkan operasi normal. Ketika server selesai memproses, respons akan dikirim kembali, dan fungsi callback JavaScript akan menangani hasilnya, memungkinkan multitasking di sisi klien.

### Bagaimana AJAX bekerja di Django (alur request–response)?

Alur request-response AJAX di Django melibatkan interaksi antara browser (menggunakan JavaScript) dan server (aplikasi Django):

- Pemicu di Klien: Sebuah event (misalnya, klik tombol, pengiriman formulir) di halaman HTML memicu eksekusi kode JavaScript.

- Request AJAX: JavaScript (menggunakan objek XMLHttpRequest atau Fetch API/jQuery) membuat permintaan HTTP baru ke URL tertentu di server Django. Permintaan ini biasanya membawa data dalam format JSON atau form data.

- URL Mapping (Django): Permintaan HTTP mencapai Django, dan URLconf Django mencocokkan URL yang diminta ke fungsi View yang sesuai.

- View Processing (Django): Fungsi View Django menerima objek HttpRequest. Karena ini adalah request AJAX, View biasanya:
    - Memverifikasi bahwa itu adalah request AJAX (misalnya, memeriksa request.headers.get('x-requested-with') == 'XMLHttpRequest').
    - Mengambil data yang dikirim (misalnya, request.POST.get('data')).
    - Memproses data tersebut (misalnya, menyimpan ke database, otentikasi).
    - Tidak me-render template HTML lengkap.

- Response JSON (Django): Setelah pemrosesan, View membuat respons, biasanya dalam format JSON (menggunakan JsonResponse di Django) yang berisi hasil (misalnya, status berhasil, pesan kesalahan, data terbaru).

- Penerimaan Respons di Klien: JavaScript di browser menerima respons JSON dari server.

- Update DOM: Fungsi callback JavaScript menangani respons ini. Berdasarkan data yang diterima, JavaScript kemudian secara dinamis memodifikasi atau memperbarui hanya bagian yang relevan dari halaman web (Document Object Model atau DOM) tanpa refresh total.

### Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?

Keuntungan utama penggunaan AJAX adalah peningkatan besar pada User Experience (UX). Dengan AJAX, interaksi pengguna terasa lebih cepat dan lebih responsif karena menghilangkan kebutuhan untuk memuat ulang seluruh halaman (full page reload). Hal ini juga mengurangi beban bandwidth dan sumber daya server karena hanya data yang dibutuhkan (seperti JSON) yang dikirim, bukan seluruh template HTML, CSS, dan aset. Keuntungan ini memungkinkan implementasi fitur yang lebih dinamis, seperti pembaruan konten in-place dan real-time (misalnya live search atau notifikasi), yang membuat aplikasi web terasa lebih modern dan mulus.

### Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?

Keamanan pada fitur Login dan Register yang menggunakan AJAX harus fokus pada perlindungan di sisi server. 
- Langkah terpenting adalah menyertakan dan memverifikasi Token CSRF (Cross-Site Request Forgery) dalam setiap permintaan POST/PUT/DELETE AJAX, biasanya melalui header HTTP kustom (`X-CSRFToken`). 
- Selain itu, validasi data harus selalu dilakukan di sisi server (menggunakan Django Forms/Serializers) untuk mencegah malicious input, terlepas dari validasi sisi klien. 
- Wajib menggunakan HTTPS untuk mengenkripsi semua transmisi kredensial. 
- Untuk memitigasi serangan Brute Force, terapkan mekanisme Rate Limiting atau throttling pada endpoint login untuk membatasi jumlah upaya request yang diizinkan dalam periode waktu tertentu.

### Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?

AJAX memiliki pengaruh yang sangat positif terhadap UX. Karena AJAX memungkinkan pembaruan konten tanpa refresh halaman penuh, hal ini menciptakan aliran interaksi yang mulus dan tanpa gangguan, membuat pengguna merasa seolah-olah menggunakan aplikasi desktop. AJAX meningkatkan perceived speed (kecepatan yang dirasakan) dan responsivitas situs. Dengan kemampuan untuk memberikan feedback instan** (seperti pesan validasi form langsung atau indikator loading minimal) dan mengizinkan multitasking di browser saat data sedang diproses, AJAX secara signifikan mengurangi frustrasi pengguna yang ditimbulkan oleh waktu tunggu yang lama dan *page reload* yang mengganggu.

### Melakukan add-commit-push ke GitHub.