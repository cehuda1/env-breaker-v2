# env-breaker

Pendeteksi `.env` adalah alat sederhana untuk memindai dan mendeteksi file `.env` yang tidak diatur dengan benar pada situs-situs target. Alat ini dirancang untuk membantu mengidentifikasi kemungkinan kebocoran informasi sensitif yang terkait dengan file `.env` pada aplikasi web.

## Cara Kerja
Alat ini menggunakan skrip Ptyhon untuk melakukan pemindaian pada daftar situs target yang diberikan. Skrip ini mengirim permintaan HTTP ke setiap situs dan memeriksa keberadaan file `.env`. Jika file `.env` ditemukan dengan status respons 200 OK, alat ini memberikan laporan dan memberi tahu pengguna bahwa file `.env` telah ditemukan.

## Fitur Utama
- Pemindaian otomatis untuk mencari file `.env` pada situs-situs target.
- Pemberitahuan langsung ketika file `.env` ditemukan.
- Kemampuan untuk menyimpan informasi dari file `.env` yang ditemukan.
- Antarmuka baris perintah sederhana untuk penggunaan yang mudah.

## Penggunaan
1. Pastikan Anda memiliki python yang terinstal di sistem Anda.
2. Siapkan file "target.txt" yang berisi daftar situs target yang ingin Anda periksa.
3. Jalankan alat ini dengan perintah berikut:
   ```
   python3 env-breaker2.py -h
   ```
4. Alat akan memulai pemindaian dan menampilkan laporan saat file `.env` ditemukan.
5. Jika Anda ingin menyimpan informasi dari file `.env` yang ditemukan, Anda dapat menyetujui prompt yang ditampilkan oleh alat.

Pastikan untuk membaca dokumentasi lengkap dan panduan penggunaan di [link dokumentasi] untuk mempelajari lebih lanjut tentang cara menggunakan alat ini dan melindungi situs web Anda dari kemungkinan kebocoran informasi sensitif.

## Catatan
Alat ini hanya dimaksudkan untuk tujuan pengujian keamanan dan harus digunakan dengan izin pemilik situs target. Pengguna bertanggung jawab penuh atas penggunaan alat ini. Pengembang tidak bertanggung jawab atas penyalahgunaan atau kerusakan yang disebabkan oleh penggunaan alat ini.

## Kontribusi
Jika Anda menemukan masalah atau memiliki saran untuk perbaikan, silakan buka *issue* atau ajukan *pull request* di repositori ini. Kami menerima kontribusi dari komunitas dan berharap dapat meningkatkan alat ini bersama.

## Lisensi
Alat ini dilisensikan di bawah [MIT License](https://opensource.org/licenses/MIT). Silakan merujuk file LICENSE untuk informasi lebih lanjut.

---
Tambahkan bagian informasi kontak atau kredit jika Anda ingin memasukkannya dalam README.
