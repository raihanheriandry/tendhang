# Tendhang Football Store
Where Kickers Find Their Gear

### 🪁 Deployment
Check here: [Tendhang Football Shop](https://raihan-maulana41-tendhang.pbp.cs.ui.ac.id/)

### 📚 Archive Tugas
   - [Tugas 2 PBP 2025/2026](https://github.com/raihanheriandry/tendhang/wiki/Tugas-2-PBP)
   - [Tugas 3 PBP 2025/2026](https://github.com/raihanheriandry/tendhang/wiki/Tugas-3-PBP)
   - [Tugas 4 PBP 2025/2026](https://github.com/raihanheriandry/tendhang/wiki/Tugas-4-PBP)
   - [Tugas 5 PBP 2025/2026](https://github.com/raihanheriandry/tendhang/wiki/Tugas-5-PBP)

---

## Tugas Individu 5

### Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Jika ada beberapa CSS selector yang berlaku pada satu elemen HTML, browser akan menentukan prioritas (specificity). Urutannya:
   - Inline CSS (ditulis langsung di elemen)
   - ID Selector (#id) → lebih tinggi dibanding class.
   - Class, Attribute, dan Pseudo-class Selector
   - Element dan Pseudo-element Selector (div, h1, ::before, ::after).

Jika specificty sama, maka aturan yang muncul terakhir (paling bawah) dalam CSS yang akan dipakai (last rule wins).


### Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!

Jarena responsive design membuat tampilan web menyesuaikan berbagai ukuran layar (HP, tablet, desktop) agar tetap nyaman digunakan. Contoh aplikasi yang sudah responsive adalah YouTube, dan kebanyakan website sudah responsif, mungkin yang belum adalah web lama atau web football-news sebelum ditambah responsif. 

Hal ini penting karena banyak juga user yang mengakses web melalui HP atau tablet. Jika tidak di setting, maka UX nya akan jelek dan sulit dibaca atau berinteraksi dengan webnya

### Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

- Margin : Ruang di luar border yang mengosongkan area di sekitar border (transparan)
- Border : Garis tepian yang membungkus konten dan padding-nya
- Padding : Ruang yang mengosongkan area di sekitar konten (transparan)

Cara implementasinya, kita set saja css nya di bagian yang bersesuaian, contoh:
```
.box {
  margin: 20px;               /* jarak luar */
  border: 2px solid black;    /* garis di sekeliling box */
  padding: 15px;              /* jarak antara teks dan border */
}
```

### Jelaskan konsep flex box dan grid layout beserta kegunaannya!

Flexbox adalah sistem layout satu dimensi di CSS yang digunakan untuk mengatur elemen dalam satu arah, baik horizontal (baris) maupun vertikal (kolom). Flexbox sangat berguna untuk menyusun elemen secara fleksibel, seperti membuat menu navigasi, daftar kartu produk, atau tombol yang selalu sejajar meskipun ukurannya berbeda.

Grid Layout adalah sistem layout dua dimensi yang memungkinkan pengaturan elemen dalam baris dan kolom sekaligus. Grid lebih cocok untuk membuat struktur halaman yang kompleks, misalnya layout dashboard, halaman utama dengan sidebar, atau galeri gambar. 

Perbedaannya, flexbox lebih fokus pada distribusi dan alignment elemen dalam satu dimensi (row atau column), sedangkan grid digunakan ketika kita butuh kontrol penuh terhadap tata letak dalam dua dimensi (row dan column).

---

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

#### 1. Implementasikan fungsi untuk menghapus dan mengedit product.
```
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')
    context = {
        'form': form
    }
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse("main:show_main"))
```
Menambahkan fungsi diatas pada views.py dan menambahkan url dan menambahkan tombol di main.html. Fungsi edit diatas mengambil objek produk dan menampilkan form lagi untuk mengedit.

#### 2. Kustomisasi desain pada template HTML yang telah dibuat menggunakan Tailwind CSS:

Ubah file global.css untuk kustom pada form nya yang memiliki class form-style
Kemudian melakukan kustomisasi pada halaman login, register, tambah product, edit product, dan detail product
Kustomisasi halaman daftar product juga menjadi lebih menarik dan responsive
Menambahkan beberapa detail:
- Jika pada aplikasi belum ada product yang tersimpan, halaman daftar product akan menampilkan gambar dan pesan bahwa belum ada product yang terdaftar.
- Jika sudah ada product yang tersimpan, halaman daftar product akan menampilkan detail setiap product dengan menggunakan card
- Untuk setiap card product, ada juga dua buah button untuk mengedit dan menghapus product pada card tersebut tapi khusus sellernya
Membuat navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.

Detail kode nya bisa diakses pada file di folder templates

Kondisi navbar untuk versi mobile: 

![Mobile Nav Off](https://github.com/user-attachments/assets/ee1b45d9-3051-4454-8521-1e69fd9e4304)

Ketika tombol hamburger diklik: 

![Mobile Nav On](https://github.com/user-attachments/assets/0d8fddcc-2447-45d3-8bfa-aff4ce7472ae)

Kondisi navbar untuk versi desktop: 

![Dekstop](https://github.com/user-attachments/assets/c0ae3582-3ddc-42f6-a49e-cf6a96c66173)
