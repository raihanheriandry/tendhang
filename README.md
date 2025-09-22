# Tendhang Football Shop
Sebuah Web Football Shop untuk Orang yang Suka Menendang

### 🪁 Deployment
Check here: [Tendhang Football Shop](https://raihan-maulana41-tendhang.pbp.cs.ui.ac.id/)

### 📚 Archive Tugas
   - [Tugas 2 PBP 2025/2026](https://github.com/raihanheriandry/tendhang/wiki/Tugas-2-PBP)
   - [Tugas 3 PBP 2025/2026](https://github.com/raihanheriandry/tendhang/wiki/Tugas-3-PBP)
   - [Tugas 4 PBP 2025/2026](https://github.com/raihanheriandry/tendhang/wiki/Tugas-4-PBP)

---

## Tugas Individu 4

### Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
Django `AuthenticationForm` adalah sebuah class form dalam Django yang dirancang khusus untuk menangani proses login pengguna. Form ini menyediakan field untuk username dan password, serta menangani validasi dan autentikasi pengguna secara otomatis.

- Kelebihan:
   - Mudah digunakan dan cepat, sudah langsung jadi
   - Keamanan terjamin, sudah terintegrasi dengan sistem autentikasi Django yang aman.
   - Validasi bawaan
   - Masih bisa di custom secara fleksibel
- Kekurangan:
   - Hanya dirancang untuk login standar (username & password)
   - Hanya terbatas untuk beberapa form saja
   - Kurang fleksibel untuk tampilan frontend kompleks

### Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
- Autentikasi (Authentication): Proses verifikasi identitas pengguna, langkah pertama untuk memastikan pengguna siapa yang mengakses. Contohnya saat login dengan username dan password.

- Otorisasi (Authorization): Proses penentuan hak akses atau izin apa yang dimiliki pengguna setelah identitasnya diverifikasi, langkah kedua yang menentukan apa yang boleh pengguna tersebut lakukan. Contohnya apakah seorang admin bisa menghapus data atau apakah pengguna biasa bisa melihat suatu data.

Django mengimplementaskan menggunakan `django.contrib.auth`.
Contoh implementasi untuk autentikasi adalah saat login yang kemudian dipanggil `autenticate()` atau `login(request, user)` dan contoh implementasi otorisasi adalah decorator yang membatasi akses view berdasarkan izin usernya `@login_required(login_url='/login')`

### Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
- Session:
   - Kelebihan: 
      - Lebih aman karena data penting tidak disimpan di browser, dan hanya session ID. 
      - Bisa menyimpan data yang lebih besar dan kompleks. 
      - Server memiliki kontrol penuh atas data.
   - Kekurangan: 
      - Membebani server karena harus menyimpan state di server
      - Jika server down, sesi bisa hilang. 
      - Sulit diimplementasikan pada aplikasi yang besar dan terdistribusi (multi-server) karena state harus dibagi ke setiap server.
- Cookies: 
   - Kelebihan: 
      - Mengurangi beban server karena data disimpan di sisi klien
      - Ringan dan sederhana untuk menyimpan preferensi pengguna. 
      - Tidak memerlukan penyimpanan tambahan di server
      - Bisa diakses langsung dari JavaScript untuk kebutuhan client-side.
   - Kekurangan: 
      - Ukuran data terbatas (biasanya 4KB per cookie)
      - Rentan terhadap serangan XSS (Cross-Site Scripting) jika cookie tidak diamankan
      - Data sensitif tidak aman jika disimpan langsung di cookie (karena bisa dibaca/dimanipulasi oleh client).

### Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
Tidak selalu aman, jika tanpa pengamanan yang tepat, cookies rentan terhadap beberapa risiko, antara lain:

- Cross-Site Scripting (XSS): Penyerang bisa menyuntikkan skrip berbahaya ke halaman web untuk mencuri cookies pengguna.
- Cross-Site Request Forgery (CSRF): Penyerang bisa memaksa pengguna untuk melakukan tindakan yang tidak diinginkan dengan menggunakan cookie autentikasi yang sudah ada.
- Man-in-the-Middle Attack: Jika tidak dikirim melalui koneksi aman (HTTPS), cookies dapat dicuri atau diubah saat transit.

Django mengambil langkah-langkah keamanan untuk meminimalkan risiko tersebut:

- Session ID: Secara default, Django tidak menyimpan data sesi langsung di cookie. Sebaliknya, ia hanya menyimpan session ID yang unik. Data sesi yang sebenarnya disimpan di sisi server (database atau cache).
- Tanda Tangan Kriptografis (Cryptographic Signing): Walaupun cookies dapat berisi data (misalnya, untuk pesan flash message), Django menandatangani (sign) cookies tersebut. Ini memastikan bahwa jika cookie diubah di sisi klien, Django akan mendeteksinya sebagai tidak valid dan menolaknya.
- Proteksi CSRF: Django menyediakan CSRF middleware yang secara otomatis menambahkan token unik ke setiap formulir. Token ini harus ada saat permintaan diproses, mencegah serangan CSRF.
- HTTPOnly: Django menetapkan cookie sesi dengan flag HttpOnly secara default. Ini mencegah skrip JavaScript di sisi klien untuk mengakses atau mencuri cookie tersebut, memberikan perlindungan terhadap serangan XSS.
- Secure Flag: Django memungkinkan Anda untuk menetapkan SECURE_COOKIE menjadi True, yang memaksa browser hanya mengirim cookie melalui koneksi HTTPS. Ini mencegah pencurian cookie melalui koneksi yang tidak aman.

### Langkah Pengimplementasian

#### 1. Implementasi Fungsi Registrasi, Login, dan Logout   
   - Membuat fungsi `register`, `login_user`, `logout_user` pada `views.py` yang diimplementasikan dengan `UserCreationForm()`
      ```
      def register(request):
         form = UserCreationForm()

         if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                  form.save()
                  messages.success(request, 'Your account has been successfully created!')
                  return redirect('main:login')
         context = {'form':form}
         return render(request, 'register.html', context)
      
      def login_user(request):
         if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                  user = form.get_user()
                  login(request, user)
                  return redirect('main:show_main')
         else:
            form = AuthenticationForm(request)
         context = {'form': form}
         return render(request, 'login.html', context)

      def logout_user(request):
         logout(request)
         return redirect('main:login')
      ```
   - Implementasi juga untuk path di 'urls.py'

#### 2. Buat 2 akun pengguna dengan masing-masing tiga (3) dummy data menggunakan model yang telah dibuat sebelumnya untuk setiap akun di lokal.
   - Membuat dua akun dengan dua kali register dengan akun yang berbeda
   - Membuat tiga produk pada setiap akun yang telah dibuat

   Akun 1
   ![akun1](https://github.com/user-attachments/assets/d9e768d9-581e-4b31-841f-cf4669acce75)
   Akun 2
   ![akun2](https://github.com/user-attachments/assets/fd70a673-8ed5-483a-ac20-e4351e8b5897)

#### 3. Hubungkan model `Product` dengan `User`.
   - Mengimport User pada models.py
      `user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) `
   - Menghubungkan satu product satu user, sehingga tiap product dapat terasosiasi dengan seorang user (many-to-one relationship)
   - `null=True` memungkinkan news yang sudah ada sebelumnya tetap valid tanpa harus memiliki user
   - `on_delete=models.CASCADE` berarti jika user dihapus, semua news milik user tersebut juga akan ikut terhapus
   - Melakukan migrasi model

#### 4. Tampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last_login pada halaman utama aplikasi.
   - Menampilkan nama pengguna yang sedang login
      `'name': request.user.username,`
   - Menerapkan cookies last_login, Simpan cookie pada fungsi `login_user`
      ```
      if form.is_valid():
         user = form.get_user()
         login(request, user)
         response = HttpResponseRedirect(reverse("main:show_main"))
         response.set_cookie('last_login', str(datetime.datetime.now()))
         return response
      ```
   - Tambahkan `last_login` pada `context` di `show_main` dengan mengakses cookie yang terdaftar di `request`
   - Tambahkan juga `last_login` pada `main.html`
   - Hapus cookie setelah logout pada fungsi `logout_user`
      `response.delete_cookie('last_login')`