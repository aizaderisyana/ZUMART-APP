from django.shortcuts import render
from .models import Product

def show_main(request):
    context = {
        'appName' : 'ZUMART',
        'name' : 'Aiza Derisyana',
        'kelas' : 'PBP C',
        'description' : 'Aplikasi Thrift Shop yang menjual produk sepatu',
    }
    return render(request, "main.html", context)
