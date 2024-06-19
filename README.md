<h6 align="center"><img src="eduroom-fe/image/logo2.png"></h6>

# EDUROOM

PROJEK AKHIR MATA KULIAH ANALISIS DESAIN SISTEM

P2 KELOMPOK 4

## Anggota:
|  | Nama  | NIM | Role |
| - | ------------- | ------------- | -
| 1 | Andika Risky Sururi  | G6401211046 | PM, Backend Developer |
| 2 | Althaf Nawadir Taqiyyah  | G6401211077  | System Analyst, DevOps |
| 3 | Nabila Elora Rasyda  | G6401211005 |  Front End Developer, UI Desaigner|
| 4 | Angela Prima Lie | G6401201096 | UI Designer, QA  |

## Deskripsi Singkat
EDUROOM merupakan sistem peminjaman ruangan yang dirancang untuk meningkatkan efisiensi dan akurasi proses peminjaman ruangan di universitas, khususnya di IPB. Sistem ini memungkinkan mahasiswa untuk melihat ketersediaan ruangan secara real-time, mengajukan permintaan peminjaman, dan menerima konfirmasi secara otomatis. Selain itu, sistem ini membantu universitas dalam mengumpulkan data penggunaan ruang untuk perencanaan dan manajemen fasilitas di masa depan.

## Fitur-Fitur Utama

1. **Mengajukan Peminjaman Ruangan**
   - Mahasiswa dapat mengajukan permintaan peminjaman ruangan untuk jadwal tertentu.

2. **Melihat Detail Ruangan**
   - Menyediakan deskripsi detail ruangan, termasuk kapasitas, lokasi, dan fasilitas yang tersedia.

3. **Mengelola Pengajuan Peminjaman**
   - Staf administrasi dapat menerima atau menolak permintaan peminjaman yang diajukan mahasiswa.

4. **History Peminjaman Ruangan**
   - Menyimpan dan menampilkan riwayat peminjaman ruangan yang pernah dilakukan.

## Kontainerisasi

Proyek ini menggunakan Docker untuk kontainerisasi, yang memungkinkan aplikasi berjalan secara konsisten di berbagai lingkungan dan mempermudah proses deployment. Berikut adalah langkah-langkah untuk menjalankan proyek ini menggunakan Docker:

### Requirements
- Docker

### Langkah-Langkah Menjalankan Proyek

1. **Clone repository:**
   ```sh
   git clone https://github.com/althaftaqiyyah/Eduroom.git
   cd Eduroom
2. **Build Docker image:**
   ```sh
   docker build -t eduroom-app .
3. **Jalankan Docker container:**
   ```sh
   docker run -d -p 8000:8000 eduroom-app
