Nama        : Aiza Derisyana
NPM         : 2206082436
Kelas       : PBP C
Adaptable   : https://zumartapp.adaptable.app

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   Cara saya mengimplementasikan chacklist tersebut adalah dengan cara:
   1) Membuat direktori baru bernama ZUMART
   2) Mengaktifkan virtual enviroment dengan perintah seperti python -m venv env dan source env/bin/activate
   3) Membuat berkas requirements.txt
   4) Membuat repositori bernama ZUMART-APP di github
   5) Membuat project django dengan django-admin startproject ZUMART .
   6) Menambahkan ALLOWED_HOSTS = ["*"] di settings.py 
   7) Mengunggah proyek ke repositori github dengan menambah berkas .gitignore dan melakukan add, coommit, push
   8) Membuat Aplikasi main dalam ZUMART dengan python manage.py startapp main 
   9) Mendaftarkan aplikasi main ke dalam proyek dengan cara menambah 'main' di INSTALLED_APPS pada berkas settings.py
   10) Membuat direktori baru yaitu templates dalam main
   11) Membuat berkas main.html dalam berkas templates dan isi sesuai ketentuan soal yaitu nama, kelas, deskripsi, nama aplikasi
   12) Buka dan isi berkas models.py sesuai ketentuan soal yaitu name, amount, description serta tambahannya
   13) Melakukan migrasi model untuk melacak perubahan pada model dengan python manage.py makemigrations untuk menciptakan berkas migrasi yang berisi perubahan model dan python manage.py migrate untuk mengaplikasikan perubahan model yang tercantum dalam berkas migrasi ke basis data
   14) Buka berkas views.py lalu tambahkan from django.shortcuts import render. Setelah itu tambahkan fungsi show_main dan ubah datanya sesuai dengan yang diinginkan soal
   15) Modifikasi berkas main.html dalam templates agar dapat menampilkan data yang telah diambil dari model
   16) Melakukan konfigurasi routing URL dalam main dengan menambah path('', show_main, name='show_main') untuk dapat mengimport rute URL dari berkas
   16) Melakukan konfigurasi routing URL ZUMART dengan menambah path('main/', include('main.urls')) untuk memungkinkan aplikasi dalam proyek Django untuk bersifat modular dan terpisah
   17) Cek django yang sudah berhasil dibuat dengan python manage.py runserver lalu membuka http://localhost:8000
   18) Mengunggah kembali ke github dengan add, commit push
   19) Deploy aplikasi ke Adaptable.io​ dengan membuat akun Adaptable.io​, lalu login dan hubungkan Adaptable.io dengan repository github. Setelah itu pilih Python App Template sebagai template deployment dan PostgreSQL sebagai tipe basis data yang akan digunakan. Selanjutnya sesuaikan versi Python menggunakan python --version dan  masukkan perintah python manage.py migrate && gunicorn ZUMART.wsgi pada bagian Start Command. Terakhir Masukkan nama aplikasi yang juga akan menjadi nama domain situs web, centang bagian HTTP Listener on PORT dan klik Deploy App.
  

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

  Client Request

       |
       V

    urls.py

       |
       V

    views.py 

       |
       V

    models.py 

       |
       V

   berkas HTML       

   Client Request yaitu pengguna yang biasanya melalui webnya mengirimkan permintaan HTTP ke URL tertentu dalam aplikasi Django.

   urls.py merupakan berkas yang memiliki tugas untuk mengarahkan permintaan dari pengguna ke fungsi yang sesuai dalam berkas views.py. Pada tahap ini, urls.py akan menganalisis URL yang diterima dari permintaan dan mencocokkannya dengan pola URL yang telah ditentukan sebelumnya. Jika ada kesesuaian, maka permintaan akan diarahkan dengan tepat ke tampilan yang sesuai.

   views.py memberikan tampilan-tampilan yang mengandung logika dari aplikasi dan persiapan data. Saat terjadi  Client Request, berkas views.py akan melakukan pemrosesan yang dibutuhkan, berinteraksi dengan models.py dan menyiapkan data yang akan ditampilkan dalam HTML.
   
   models.py memberikan definisi model-data yang digunakan dalam aplikasi. Berkas ini merincikan struktur dan skema basis data yang digunakan oleh aplikasi. Jika Client Request memerlukan akses atau pengubahan data, berkas views.py akan berinteraksi dengan models.py untuk mengambil atau mengubah data sesuai kebutuhan.

   HTML Template berfungsi untuk merender tampilan dari pengguna, views.py dan models.py yang akan dikirimkan kembali kepada pengguna.
               
3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
    Virtual environment adalah alat yang penting dalam pengembangan perangkat lunak. Ini memungkinkan kita untuk mengisolasi dan mengelola dependensi yang digunakan dalam proyek dengan efisien. Dengan menggunakan virtual environment, setiap proyek memiliki lingkungan terpisah untuk mengatur pustaka dan paket Python yang diperlukan, serta memungkinkan kita untuk memilih versi Python yang cocok.
    Secara teknis mungkin untuk mengembangkan aplikasi web berbasis Django tanpa menggunakan virtual environment, namun praktik ini lebih baik dihindari. Hal ini disebabkan karena penggunaan virtual environment sangat dianjurkan untuk menjaga keteraturan, kejelasan, serta keterpeliharaan yang optimal dalam pengembangan proyek Django. Dengan cara ini, kita dapat menghindari masalah rumit yang terkait dengan konflik dependensi dan membuat manajemen dependensi proyek menjadi lebih mudah. Oleh karena itu, penting untuk selalu menggunakan virtual environment saat mengembangkan proyek Django.

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
    MVC (Model-View-Controller):
    Model: Menyimpan data dan logika aplikasi.
    View: Menampilkan data dari model dan menghubungkannya dengan template.
    Controller: Menerima input, memprosesnya, dan mengatur Model dan View. 

    MVT (Model-View-Template):
    Model: Menyimpan data dan logika aplikasi.
    View: Menampilkan data dari model dan menghubungkannya dengan template.
    Template: Menentukan tampilan antarmuka pengguna.

    MVVM (Model-View-ViewModel):
    Model: Menyimpan data dan logika aplikasi.
    View: Menampilkan data dari model dan menghubungkannya dengan template.
    ViewModel: Memfasilitasi komunikasi antara Model dan View, mengelola tampilan data, dan berfungsi sebagai perantara. 

    Dalam MVT, peran Controller dalam MVC digantikan oleh Template, yang memiliki peran yang lebih terbatas dalam mengendalikan tampilan dibandingkan dengan Controller dalam MVC.

    Pada MVC, tanggung jawab utama Controller adalah mengatur alur logika aplikasi dan bertindak sebagai penghubung antara Model dan View.

    Pada MVVM, diperkenalkan ViewModel, yang tidak ada dalam MVC dan MVT. ViewModel berfungsi sebagai perantara antara Model dan View, dengan pemisahan tampilan dari logika bisnis yang jauh lebih ketat dibandingkan dengan MVC dan MVT.
