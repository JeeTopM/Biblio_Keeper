"""
from .models import Articles
from django.forms import ModelForm, TextInput, Textarea

class ArticlesForm(ModelForm):

    class Meta:
        model = Articles
        fields = ['reader','operation', 'book_list']

        widgets = {
            'reader': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер читателя или ФИО'
            }),
            'operation': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Операция'
            }),
            'book_list': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Штрихкоды книг'
            })
         }

"""

from django import forms
from .models import Articles


class ArticlesForm(forms.ModelForm):
    OPERATION_CHOICES = [
        ("Выдать", "Выдать"),
        ("Принять", "Принять"),
    ]

    operation = forms.ChoiceField(  # Исправлено: ChoiceField вместо ChoiceField
        label="Операция",
        choices=OPERATION_CHOICES,
        initial="Выдать",
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Articles
        fields = ["reader", "operation", "book_list"]
        widgets = {
            "reader": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Номер читателя или ФИО"}
            ),
            "book_list": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Штрихкоды книг"}
            ),
        }
