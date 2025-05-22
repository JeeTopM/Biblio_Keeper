from .models import Articles
from django.forms import ModelForm, TextInput, Textarea


class ArticlesForm(ModelForm):

    class Meta:
        model = Articles
        fields = ["reader", "need_book"]

        widgets = {
            "reader": TextInput(
                attrs={"class": "form-control", "placeholder": "Номер читателя или ФИО"}
            ),
            "need_book": TextInput(
                attrs={"class": "form-control", "placeholder": "Нужная книга"}
            ),
        }
