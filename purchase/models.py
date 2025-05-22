from django.db import models

# Create your models here.
class Articles(models.Model):
    reader = models.CharField('Номер читателя или ФИО', max_length=50)
    need_book = models.CharField('Полное название книги', max_length=50)
    date = models.DateTimeField("Дата операции", auto_now_add=True)

    def __str__(self):
        return self.reader