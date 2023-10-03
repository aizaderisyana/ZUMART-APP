Nama        : Aiza Derisyana
NPM         : 2206082436
Kelas       : PBP C
Adaptable   : https://zumartapp.adaptable.app



TUGAS 5

Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya. 
    Element Selector 
    Element Selector digunakan untuk mengubah properti pada semua elemen dengan tag HTML yang sama. Dengan menggunakan selector ini,  kita dapat dengan mudah mengubah gaya elemen-elemen dengan tag yang sama di seluruh halaman web. Element Selector cocok digunakan ketika ingin menerapkan gaya umum pada semua elemen dengan tipe tertentu di halaman web. Ini sering digunakan untuk mengatur gaya dasar seperti huruf tebal, ukuran font, atau jarak antar elemen.

    ID Selector 
    ID Selector digunakan untuk memilih elemen berdasarkan ID unik yang diberikan pada tag HTML. ID harus unik dalam satu halaman web, sehingga selector ini memungkinkan kita untuk secara khusus mengganti properti elemen dengan ID tertentu.

    Class Selector 
    Class Selector memungkinkan kita mengklasifikasikan item dengan kualitas terkait dan memodifikasi properti tersebut untuk kelompok komponen tertentu.
    Sebuah elemen mungkin termasuk dalam satu atau lebih kelas, dan banyak instance dari kelas yang sama dapat diberi gaya sekaligus.
    Class selector sangat berguna ketika ingin menerapkan gaya yang sama pada beberapa elemen dengan atribut class yang sama. Ini memungkinkan kita untuk mengelompokkan elemen dan menerapkan gaya dengan presisi.

Jelaskan HTML5 Tag yang kamu ketahui.
    Bentuk HTML terbaru, yaitu HTML5 digunakan untuk membuat halaman web. HTML5 Tag biasa digunakan sebagai:
    <header> = Menunjukkan bagian atas halaman atau awal bagian tertentu di dalamnya.
    <nav> = Menentukan bagian navigasi halaman.
    <section> = Mengelompokkan informasi di situs web yang relevan dengan subjek tertentu menjadi beberapa bagian.
    <Artikel> = Aalah contoh materi tersendiri yang dapat ditemukan di bagian halaman tertentu.
    <aside> = Segmen yang terkait dengan materi terdekat lainnya ditetapkan sebagai "sampingan" menggunakan sidebar atau kotak informasi sebagai contoh.
    <footer> = Menjelaskan bagian bawah halaman atau bagian tertentu.
    Ada beberapa tag HTML5 lain yang dapat digunakan untuk menambahkan media dan grafik ke halaman web, antara lain <video>, <audio>, <canvas>, dan <svg>. 

Jelaskan perbedaan antara margin dan padding.
    Margin dan padding adalah properti CSS yang digunakan untuk mengatur ruang di sekitar dan di dalam elemen HTML, yang digunakan dalam desain dan tata letak web untuk menentukan ruang antara elemen dan komponen di sekitarnya serta ruang antara konten elemen dan batasnya.
    Perbedaan keduanya adalah margin, yang memiliki nilai default 0, dapat diberikan hingga empat kali untuk setiap elemen, menentukan jarak dari tepi elemen dan menyisakan ruang di sekitarnya tanpa mengubah ukurannya. Di sisi lain, padding hanya dapat diberikan hingga empat kali untuk setiap elemen dan menentukan jarak dari dalam elemen, memberikan ruang di dalam elemen, dan dapat membuat elemen lebih besar atau lebih kecil. Padding memiliki nilai default 0. 

Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan 
    sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
    Perbedaan antara framework CSS Tailwind dan Bootstrap adalah Tailwind membangun tampilan dengan menggabungkan kelas-kelas utilitas yang telah didefinisikan sebelumnya, memiliki file CSS yang lebih kecil, memberikan fleksibilitas dan adaptabilitas tinggi terhadap proyek, tetapi memerlukan pembelajaran yang lebih curam. Sementara itu, Bootstrap menggunakan gaya dan komponen yang telah didefinisikan, memiliki file CSS yang lebih besar, sering menghasilkan tampilan yang konsisten di seluruh proyek, dan memiliki pembelajaran yang lebih cepat untuk pemula karena dapat mulai dengan komponen yang telah didefinisikan.
    Bootstrap dapat menjadi pilihan yang tepat jika ingin membuat situs web lengkap dengan banyak komponen siap pakai dan gaya yang lebih kontemporer. Hal ini karena bootstrap memiliki semua karakteristik tersebut. Namun, ukuran file yang dimiliki Bootstrap lebih tinggi.
    Di sisi lain, Tailwind bisa menjadi pilihan yang baik jika ingin membuat komponen secara modular, memiliki kontrol lebih besar terhadap desain, dan memberikan tampilan yang lebih minimalis. Tailwind dapat memberikan transmisi yang lebih besar dalam hal desain dan memiliki ukuran file yang lebih kecil.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
    Tambahkan Bootstrap, CSS, JS ke aplikasi melalu templates/base.html seperti berikut
    <meta name="viewport" content="width=device-width, initial-scale=1">
        {% endblock meta %}
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha384-KyZXEAg3QhqLMpG8r+J4jsl5c9zdLKaUk5Ae5f5b1bw6AUn5f5v8FZJoMxm6f5cH1" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js" integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+" crossorigin="anonymous"></script>
    </head>
    Menambahkan navigation bar di main.html
    Menambah fitur edit_item dalam main/views.py seperti berikut
    def edit_item(request, id):
        product = Items.objects.get(pk = id)
        form = ItemForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    context = {'form': form}
    return render(request, "edit_item.html", context)
    Mebuat berkas baru yaitu edit_item.html dalam main/templates seperti berikut

    </style>
    <div class="content-container">
    <h1>Edit Item</h1>
    <form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Edit Item"/>
            </td>
        </tr>
    </table>
    </form>

    {% endblock %}
    Lalu menambahkan selectronya 
    Membuka main/urls.py lalu menambah ‘’’from main.views import edit_item’’’
    Tambahkan ‘’’path('edit-item/<int:id>', edit_item, name='edit_item'),’’’ dalam urlspatterns
    Dalam main.html di main/templates, tambahkan kode berikut
    <td>
        <a href="{% url 'main:edit_item' item.pk %}">
            <button>Edit</button>
        </a>
    Menambah fitur delete_item dalam main/views.py seperti berikut
    def delete_item(request, id):
    item = Items.objects.get(pk = id)
    item.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

    Membuka main/urls.py lalu menambah ‘’’from main.views import delete_item’’’
    Tambahkan ‘’’path('delete/<int:id>', delete_item, name='delete_item'), ‘’’dalam urlspatterns
    Dalam main.html di main/templates, tambahkan kode berikut
    </a>
        <a href="{% url 'main:delete_item' item.pk %}">
            <button>Delete</button>
        </a>
    Jalankan aplikasi dengan ‘’’python manage.py runserver’’’ dan buka http://localhost:8000  

===========================================================================================================================================================
===========================================================================================================================================================

Tugas 4

Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
UserCreationForm dalam Django adalah formulir bawaan yang sangat berguna untuk membuat formulir pendaftaran pengguna dalam aplikasi web dengan cepat. Kelebihannya dari UserCreationForm yaitu kemudahan penggunaan, validasi otomatis untuk memastikan bahwa input yang dimasukkan oleh pengguna valid dan sesuai dengan kebutuhan aplikasi dan integrasi yang baik dengan sistem keamanan Django. Kekurangannya adalah keterbatasan fitur untuk pendaftaran karena hanya menyediakan field untuk username, password, dan email. Serta Tampilan default yang mungkin tidak sesuai dengan desain aplikasi yang dibuat, sehingga perlu dilakukan penyesuaian tampilan.

Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
    Autentikasi adalah proses verifikasi identitas pengguna dengan memeriksa apakah username dan password yang dimasukkan oleh pengguna cocok dengan data yang tersimpan di database. Autentikasi adalah langkah pertama dalam menjaga keamanan aplikasi dan mencegah akses oleh pengguna yang tidak sah. Autentikasi penting untuk memastikan bahwa hanya pengguna yang identitasnya terverifikasi memiliki hak akses ke aplikasi atau sumber daya tertentu.
    Otorisasi adalah proses penentuan hak akses pengguna setelah identitasnya terverifikasi dengan memeriksa apakah pengguna memiliki hak akses untuk melakukan tindakan tertentu, seperti mengedit atau menghapus data. Otorisasi membantu melindungi data sensitif dan menghindari penyalahgunaan sumber daya aplikasi. Otorisasi penting untuk mengendalikan tingkat akses dan hak pengguna dalam aplikasi.
    Kedua hal ini penting karena keduanya bekerja sama untuk memastikan bahwa hanya pengguna yang sah yang dapat mengakses aplikasi dan melakukan tindakan tertentu, dengan begitu autentikasi dan otorisasi dapat membantu melindungi data sensitif dari akses yang tidak sah.

Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
    Cookies adalah file kecil yang disimpan di komputer pengguna oleh aplikasi web, memainkan peran penting dalam menyimpan informasi seputar pengguna dan interaksi mereka dengan situs web. Ini termasuk menyimpan preferensi pengguna, data sesi, dan sejarah penggunaan. Dalam kerangka kerja web Python Django, cookies digunakan untuk mengelola data sesi pengguna. Ketika pengguna masuk ke dalam aplikasi Django, sistem akan membuat sebuah cookie yang berisi ID sesi pengguna. ID ini digunakan untuk mengidentifikasi pengguna dan menyimpan data sesi mereka, seperti preferensi pengguna, konten dalam keranjang belanja, dan catatan riwayat penggunaan. Django juga memberikan kemampuan untuk mengatur waktu kedaluwarsa cookie, sehingga data sesi pengguna dapat dihapus secara otomatis setelah periode waktu tertentu.
    Penggunaan cookies sangat penting dalam pengembangan aplikasi web modern karena memungkinkan pengembang untuk dengan aman menyimpan informasi pengguna dan menyediakan pengalaman yang lebih personal serta interaktif. Dengan dukungan dari cookies, aplikasi web dapat mengingat preferensi pengguna, mengelola status masuk, serta menyimpan data yang esensial untuk meningkatkan keseluruhan pengalaman pengguna.

Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
    Penggunaan cookies dalam pengembangan web bisa aman atau berpotensi berisiko tergantung pada cara penggunaannya. Keamanan cookies dapat ditingkatkan dengan menggunakan HTTPS, mengatur "HttpOnly" dan "Secure" pada cookies, dan menghindari menyimpan data sensitif di dalamnya. Potensi risiko termasuk penyadapan data jika tidak ada enkripsi HTTPS, penyalahgunaan cookies yang dapat menyebabkan akses ilegal, pelacakan pengguna, dan pencurian cookies. Dalam pengembangan web dengan Django, cookies digunakan untuk mengelola sesi pengguna, dan waktu kadaluarsa cookies dapat diatur. Penting bagi pengembang untuk memahami risiko potensial ini dan menjalankan praktik keamanan yang tepat.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Fungsi Registrasi
    
	1. Pertama jalankan terlebih dahulu virtual enviroment dengan ‘source env/bin/activate’

    2. Buka main/views.py dan tambahkan import 
    from django.shortcuts import redirect
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib import messages  

    3. Buat fungsi register seperti berikut;
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

    4. Buat berkas baru yaitu register.html dalam main/templates dan isi dengan;
        {% extends 'base.html' %}
        {% block meta %}
        <title>Register</title>
        {% endblock meta %}

        {% block content %} 

        <div class = "login">
        
        <h1>Register</h1> 

            <form method="POST" > 
                {% csrf_token %} 
                <table> 
                    {{ form.as_table }} 
                    <tr> 
                        <td></td>
                        <td><input type="submit" name="submit" value="Daftar"/></td> 
                    </tr> 
                </table> 
            </form>

        {% if messages %} 
            <ul>  
                {% for message in messages %} 
                    <li>{{ message }}</li> 
                    {% endfor %} 
            </ul>  
        {% endif %}

        </div> 

        {% endblock content %}
        
    5. Buka main/urls.py lalu import 'from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id show_json_by_id, register'

    6. Tambahkan  dalam urlpatterns 'path('register/', register, name='register'),'


Fungsi Login

    1. Buka main/views dan tambahkan import 'from django.contrib.auth import authenticate, login'

    2. Buat fungsi login_user seperti berikut; 
    def login_user(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:show_main')
            else:
                messages.info(request, 'Sorry, incorrect username or password. Please try again.')
        context = {}
        return render(request, 'login.html', context)

    3. Buat berkas baru yaitu login.html dalam main/templates dan isi dengan;
        {% extends 'base.html' %}

        {% block meta %}
        <title>Login</title>
        {% endblock meta %}

        {% block content %}

        <div class = "login">

        <h1>Login</h1>

        <form method="POST" action="">
            {% csrf_token %}
            <table>
                <tr>
                    <td>Username: </td>
                    <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
                </tr>
                        
                <tr>
                    <td>Password: </td>
                    <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
                </tr>


                <tr>
                    <td></td>
                    <td><input class="btn login_btn" type="submit" value="Login"></td>
                </tr>
            </table>
        </form>

        {% if messages %}
            <ul>
                {% for message in messages %}
                    <li>{{ message }}</li>
                {% endfor %}
            </ul>
        {% endif %}    
            
        Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

        </div>

        {% endblock content %}

    4. Buka main/urls.py lalu import 'from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user'

    5. Tambahkan  dalam urlpatterns 'path('login/', login_user, name='login'),'


Fungsi Logout

    1. Buka main/views dan tambahkan import 'from django.contrib.auth import logout'

    2. Buat fungsi logout_user seperti berikut ; 
        def logout_user(request):
            logout(request)
            return redirect('main:login')

    3. Buka berkas main.html dalam main/templates dan Tambahkan potongan kode di bawah ini setelah hyperlink tag 
        <a href="{% url 'main:logout' %}">
            <button>
                Logout
            </button>
        </a>

    4. Buka main/urls.py lalu import 'from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user'

    5. Tambahkan  dalam urlpatterns 'path('logout/', logout_user, name='logout'),'


Menerapkan Cookies
    
    1.  Buka main/views.py lalu lakukan 'import datetime'

    2. Update fungsi login_user dengan kode berikut sehingga login_user menjadi;
        def login_user(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                response = HttpResponseRedirect(reverse("main:show_main"))
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
            else:
                messages.info(request, 'Sorry, incorrect username or password. Please try again.')
        context = {}
        return render(request, 'login.html', context)

    3. Tambah last_login dalam showmain seperti berikut;
        def show_main(request):
        items = Items.objects.filter(user=request.user)
        item_count = items.count()
        context = {
            'name': request.user.username,
            'kelas' : 'PBP C',
            'items' : items,
            'item_count': item_count,
            'last_login': request.COOKIES['last_login'],
        }
        return render(request, "main.html", context)

    4. Update fungsi logout_user menjadi ;
        def logout_user(request):
            logout(request)
            response = HttpResponseRedirect(reverse('main:login'))
            response.delete_cookie('last_login')
            return response
    
    5. Buka templates/main.html dan tambahkan kode '<h5>Sesi terakhir login: {{ last_login }}</h5>' diantara tabel dan tombol logout 

 
Hubungkan model Items dengan User

    1. Buka main/models.py lalu lakukan impor 'from django.contrib.auth.models import User'

    2. Pada model Items tambahkan ;
        class Items(models.Model):
            user = models.ForeignKey(User, on_delete=models.CASCADE)

    3. Buka main/views.py lalu tambahkan kode berikut dalam fungsi create_products;
        form = ItemForm(request.POST or None)
        if form.is_valid() and request.method == "POST":
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return HttpResponseRedirect(reverse('main:show_main'))

    4. Update fungsi show_main sehingga;
        def show_main(request):
            items = Items.objects.filter(user=request.user)
            item_count = items.count()
            context = {
                'name': request.user.username,

    5. Lakukan ‘python manage.py makemigrations’ dan ‘python manage.py migrate’ di terminal folder

    6. Jalankan aplikasi dengan ‘python manage.py runserver’ 








======================================================================================================
======================================================================================================

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
<img width="1440" alt="Screenshot 2023-09-16 at 22 47 12" src="https://github.com/aizaderisyana/ZUMART-APP/assets/82081149/19251792-0440-4e8c-b478-52212156c65e">
<img width="1440" alt="Screenshot 2023-09-16 at 22 47 22" src="https://github.com/aizaderisyana/ZUMART-APP/assets/82081149/92676079-81ba-45ae-a78f-bf0909f77b85">
<img width="1440" alt="Screenshot 2023-09-16 at 22 47 41" src="https://github.com/aizaderisyana/ZUMART-APP/assets/82081149/b91b29fe-89b3-47da-b77c-e9f7fced22b8">


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


