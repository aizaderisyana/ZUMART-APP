from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': ['Nike','Adidas', ],
        'amount': ['6', '4', '3'],
        'description': ['Air Jordan', 'Samba', '550'],
        'size': ['38', '39', '40'],
        'price': [2000000, 1200000, 1500000], 
    }

    return render(request, "main.html", {'context': context})