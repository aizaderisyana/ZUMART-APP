Nama        : Aiza Derisyana
NPM         : 2206082436
Kelas       : PBP C
Adaptable   : https://zumartapp.adaptable.app

TUGAS 3

Apa perbedaan antara form POST dan form GET dalam Django?
    Form POST digunakan ketika pengguna ingin mengirim data dari elemen form ke server web. Salah satu keunggulan utama dari form POST adalah bahwa data yang dikirim tidak akan terlihat dalam URL, membuatnya lebih aman untuk mengirimkan data yang bersifat sensitif atau ketika pengguna perlu mengirimkan banyak informasi, seperti saat membuat, mengedit, atau menghapus entitas. 

    Form GET digunakan untuk mengambil data dari server tanpa melakukan perubahan pada entitas tersebut. Meskipun form GET cocok untuk pengambilan data, data yang dikirimkan dengan metode GET akan terlihat dalam URL, yang membuatnya kurang aman untuk data yang sensitif. Selain itu, data yang dikirim melalui form GET juga dapat disimpan di dalam cache, yang dapat mengakibatkan masalah dalam privasi dan keamanan.

Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
    XML merupakan format yang digunakan untuk menyimpan dan mengangkut data secara struktural dari satu aplikasi ke aplikasi lain melalui Internet. XML biasanya digunakan untuk merepresentasikan data dengan cara yang dapat dibaca oleh mesin dan sering digunakan sebagai format pertukaran data pada aplikasi web.

    JSON merupakan format pertukaran data terbuka yang dapat dibaca baik oleh manusia maupun mesin. JSON bersifat independen dari setiap bahasa pemrograman dan umum digunakan dalam berbagai aplikasi sebagai output API. JSON digunakan untuk menyimpan dan mengirimkan data dengan cara yang data diuraikan dan dikirimkan melalui Internet.

    HTML merupakan bahasa yang digunakan untuk membuat tampilan berisi  informasi pada browser web dan mendefinisikan tampilan halaman web. HTML tidak digunakan untuk pertukaran data antar aplikasi.

Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
    JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena terdapat beberapa alasan, seperti JSON memiliki format yang ringan dan mudah dipahami oleh manusia. Dibandingkan dengan format lain seperti XML, JSON lebih ringkas dan lebih mudah dibaca oleh manusia. Selain itu, JSON juga lebih efisien dalam pemrosesan oleh mesin dibandingkan dengan XML. Hal ini menjadikan JSON sebagai pilihan yang efisien dalam hal pengiriman dan pengolahan data. JSON biasanya digunakan dalam layanan web untuk mentransfer data ke aplikasi klien atau perangkat lunak lainnya. Kemampuan JSON untuk dengan mudah mengatur pertukaran data yang efisien dan mudah dipahami antara berbagai komponen dan layanan, membuat JSON menjadi sangat relevan dalam penggunaan pengembangan web yang semakin kompleks.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    Dengan melanjutkan aplikasi ZUMART kita aktifkan virtual environment terlebih dahulu dengan source env/bin/activate. Selanjutnya buka urls.py yang ada pada folder ZUMART dan ubahlah pathmain/ menjadi '' seperti berikut path('', include('main.urls')). Lalu buat folder templates pada root folder dan buatlah sebuah berkas HTML baru bernama base.html yang berisi kode berikut:

    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8" />
            <meta
                name="viewport"
                content="width=device-width, initial-scale=1.0"
            />
            {% block meta %}
            {% endblock meta %}
        </head>

        <body>
            {% block content %}
            {% endblock content %}
        </body>
    </html>

    Lalu buka settings.py dan cari baris yang mengandung templates dan tambahkan 'DIRS': [BASE_DIR / 'templates']. Pada templates di dalam direktori main, ubah kode main.html menjadi:
    {% extends 'base.html' %}
    {% block content %}
    <h1 style="background-color: #2a5bd1;">ZUMART</h1>
    <p>ZUMART merupakan Thrift Shop yang menjual berbagai jenis sepatu keren dan ramah di kantong.<p>
    <p>By Aiza Derisyana from PBP C.<p>
    {% endblock content %}

    > Pembuatan Form Input Data dan Menampilkan Data Produk Pada HTML
    Buat berkas dalam direktori main bernama forms.py lalu tambahkan kode berikut:

    from django.forms import ModelForm
    from main.models import Items
    class ItemForm(ModelForm):
    class Meta:
        model = Items
        fields = ["name", "size", "color", "amount", "price", "description"]

    Selanjutnya buka views.py lalu tambahkan:

    from django.http import HttpResponseRedirect
    from main.forms import ProductForm
    from django.urls import reverse

    Dan buat fungsi baru yang menerima parameter request seperti:

    def create_product(request):
        form = ProductForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            form.save()
            return HttpResponseRedirect(reverse('main:show_main'))

        context = {'form': form}
        return render(request, "create_product.html", context)

    Selanjutnya ubah kode show_main menjadi:

    def show_main(request):
    items = Items.objects.all()
    item_count = items.count()
    context = {
        'name' : 'Aiza Derisyana',
        'kelas' : 'PBP C',
        'items' : items,
        'item_count': item_count
    }
    return render(request, "main.html", context)

    Lalu Buka urls.py yang ada pada folder main dan import fungsi create_product seperti from main.views import show_main, create_product dan tambahkan path url ke dalam urlpatterns pada urls.py di main seperti path('create-product', create_product, name='create_product'), untuk mengakses fungsi yang sudah di-import sebelumnya.
    Selanjutnya buat berkas HTML baru bernama create_product.html dalam direktori main dan templates dan tambahkan kode berikut:

    {% extends 'base.html' %} 

    {% block content %}
    <h1>Add New Product</h1>

    <form method="POST">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td>
                    <input type="submit" value="Add Product"/>
                </td>
            </tr>
        </table>
    </form>

    {% endblock %}

    Lalu tambahkan juga kode berikut dalam main.html:

    <p>Kamu menyimpan {{ item_count }} item pada aplikasi ini.</p>
    <table>
        <tr>
            <th>Name</th>
            <th>Size</th>
            <th>Color</th>
            <th>Amount</th>
            <th>Price</th>
            <th>Description</th>
        </tr>
    
        {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}
    
        {% for item in items %}
            <tr>
                <td>{{item.name}}</td>
                <td>{{item.size}}</td>
                <td>{{item.color}}</td>
                <td>{{item.amount}}</td>
                <td>{{item.price}}</td>
                <td>{{item.description}}</td>
            </tr>
        {% endfor %}
    </table>
    
    <br/>
    
    <a href="{% url 'main:create_product' %}">
        <button>
            Add New Item
        </button>
    </a>
    <p>By Aiza Derisyana from PBP C.<p>
    {% endblock content %}

    > Mengembalikan data dalam bentuk XML
    Pertama buka views,py dalam direktori main dan lakukan:

    from django.http import HttpResponse
    from django.core import serializers

    Lalu buat fungsi show_xml seperti dan tambahkan return function berupa HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi XML dan parameter seperti:
    def show_xml(request):
    data = Items.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    Setelah itu buka urls.py dalam main dan tambahkan  from main.views import show_main, create_product, show_xml dan path('xml/', show_xml, name='show_xml'), dalam urlpatterns.

    > Mengembalikan data dalam bentuk JSON
    Pertama buka views,py dalam direktori main lalu buat fungsi show_json dengan return function berupa HttpResponse yang berisi parameter data hasil query yang sudah di serialisasi menjadi JSON dan parameter seperti:
    def show_json(request):
    data = Items.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    Setelah itu buka urls.py dalam main dan tambahkan from main.views import show_main, create_product, show_xml, show_json dan path('json/', show_json, name='show_json'),
    Dalam urlpatterns.

    > Mengembalikan Data Berdasarkan ID dalam Bentuk XML dan JSON
    Buka views,py dalam direktori main lalu buat fungsi show_xml_by_id dan show_json_by_id, seperti:
    def show_xml_by_id(request, id):
    data = Items.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


    def show_json_by_id(request, id):
    data = Items.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    Setelah itu buka urls.py dalam main dan tambahkan from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id  dan path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    Dalam urlpatterns

    > Penggunaan postman
    Pastikan server sudah berjalan dengan perintah python manage.py runserver.
    Buka postman dan tambahkan http://localhost:8000/xml atau http://localhost:8000/json dalam request GET. Lalu klik Send. Response dapat dilihat di bagian bawah postman.


======================================================================================================
======================================================================================================


TUGAS 2
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
<img width="894" alt="fc pbpb" src="https://github.com/aizaderisyana/ZUMART-APP/assets/82081149/a9982139-f38e-4a67-b284-c41632a4fefc">


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


