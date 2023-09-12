Nama    : Aiza Derisyana
NPM     : 2206082436
Kelas   : PBP C

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   Cara saya mengimplementasikan chacklist tersebut adalah dengan cara:
   1) Membuat direktori baru bernama ZUMART
   2) Mengaktifkan virtual enviroment dengan perintah seperti python -m venv env dan source env/bin/activate
   3) Membuat berkas requirements.txt
   4) Membuat project django dengan django-admin startproject ZUMART
   5) Menambahkan * pada ALLOWED_HOSTS di settings.py 
   6) Membuat Aplikasi main dalam ZUMART
   7) Membuat direktori baru yaitu templates dalam main
   8) Buka dan isi berkas models.py sesuai ketentuan soal yaitu name, amount, description serta tambahannya
   9) Buka berkas views.py lalu ubah datanya sesuai dengan yang diinginkan pada templates
   10) Modifikasi berkas templates agar dapat menampilkan data yang telah diambil dari model
   11) Melakukan konfigurasi routing URL dalam main dengan menambah path('', show_main, name='show_main') untuk dapat mengimport rute URL dari berkas
   12) Melakukan konfigurasi routing URL ZUMART dengan menambah path('main/', include('main.urls')) untuk memungkinkan aplikasi dalam proyek Django untuk bersifat modular dan terpisah
   13) Melakukan migrasi model untuk melacak perubahan pada model
   14) Cek django yang sudah berhasil dibuat dengan python manage.py runserver lalu membuka http://localhost:8000
   15) Jika sudah dilanjutkan dengan mengunggah proyek ke repositori github dengan menambah berkas .gitignore dan melakukan add, coommit, push

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

    Client Request
    Seorang pengguna, biasanya melalui peramban webnya, mengirimkan permintaan HTTP ke URL tertentu dalam aplikasi Django.

    urls.py:
    Berkas yang dikenal dengan sebutan urls.py memiliki tugas penting, yaitu mengarahkan permintaan dari pengguna ke fungsi yang sesuai dalam berkas views.py. Ini menjelaskan bagaimana URL yang diterima akan diarahkan ke tampilan yang benar.
    Pada tahap ini, urls.py akan menganalisis URL yang diterima dari permintaan dan mencocokkannya dengan pola URL yang telah ditentukan sebelumnya. Jika ada kesesuaian, maka permintaan akan diarahkan dengan tepat ke tampilan yang sesuai.

    views.py:
    Dalam berkas yang disebut views.py ini, terdapat tampilan-tampilan (views) yang mengandung logika bisnis dari aplikasi dan persiapan data.
    Saat permintaan dari pengguna masuk, berkas views.py akan melakukan pemrosesan yang dibutuhkan, berinteraksi dengan Model (jika diperlukan), dan menyiapkan data yang akan ditampilkan dalam tampilan HTML.
    
    models.py:
    Berkas dengan nama models.py berperan penting dalam mendefinisikan model-data yang digunakan dalam aplikasi. Berkas ini merincikan struktur dan skema basis data yang digunakan oleh aplikasi.
    Apabila permintaan dari pengguna memerlukan akses atau pengubahan data, berkas views.py akan berinteraksi dengan Model untuk mengambil atau mengubah data sesuai kebutuhan.

    HTML Template:
    BBerkas HTML Template berfungsi untuk merender tampilan yang akan dikirimkan kembali kepada pengguna.
                

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
    Virtual environment adalah alat penting dalam pengembangan perangkat lunak yang memungkinkan isolasi serta manajemen yang efisien terhadap dependensi yang digunakan dalam suatu proyek. Virtual environment memastikan bahwa setiap proyek memiliki wadah terpisah yang disebut environment untuk mengelola pustaka-pustaka dan paket-paket Python yang dibutuhkan, serta memungkinkan pemilihan versi Python yang sesuai.
    
    Secara teknis mungkin untuk mengembangkan aplikasi web berbasis Django tanpa menggunakan virtual environment, namun praktik ini lebih baik dihindari. Hal ini disebabkan karena penggunaan virtual environment sangat dianjurkan untuk menjaga keteraturan, kejelasan, serta keterpeliharaan yang optimal dalam pengembangan proyek Django. Dengan cara ini, masalah konflik dependensi yang rumit dapat dihindari dan manajemen dependensi proyek menjadi lebih sederhana. Oleh karena itu, diperlukan penggunaan virtual environment untuk pengembangan Django  dalam setiap proyek.


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