from django.shortcuts import render
from .models import Product

def show_main(request):
    context = {
        'NAJ': {
            'Description': 'bagus',
            'Size': 38,
            'Amount': 12,
            'Price': 2300000, 
        },
        'AS': {
            'Description': 'cool',
            'Size': 40,
            'Amount': 14,
            'Price': 2500000, 
        },
        'NB550': {
            'Description': 'ini dia',
            'Size': 37,
            'Amount': 7,
            'Price': 1500000, 
        },
        'NDL': {
            'Description': 'edgy',
            'Size': 42,
            'Amount': 3,
            'Price': 2600000, 
        },
        'CCT': {
            'Description': 'classic',
            'Size': 36,
            'Amount': 17,
            'Price': 1000000, 
        },
    }
    return render(request, "main.html", context)
