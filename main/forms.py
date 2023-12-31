from django.forms import ModelForm
from main.models import Items

class ItemForm(ModelForm):
    class Meta:
        model = Items
        fields = ["name", "size", "color", "amount", "price", "description"] 