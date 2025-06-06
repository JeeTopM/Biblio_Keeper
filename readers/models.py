from django.db import models

# Create your models here.
"""class Articles(models.Model):
    reader = models.CharField('Номер читателя или ФИО', max_length=50)
    operation = models.CharField('Сдать / взять', max_length=5)
    book_list = models.TextField('Штрихкоды книг')
    date = models.DateTimeField('Дата операции', auto_now_add=True)
"""


class Articles(models.Model):
    OPERATION_CHOICES = [
        ("Выдать", "Выдать"),
        ("Принять", "Принять"),
    ]
    reader = models.CharField("Номер читателя или ФИО", max_length=50)
    operation = models.CharField(
        "Операция",
        max_length=10,
        choices=OPERATION_CHOICES,
        default="Выдать",
    )
    book_list = models.TextField("Штрихкоды книг")
    date = models.DateTimeField("Дата операции", auto_now_add=True)

    def __str__(self):
        return self.reader

    def get_absolute_url(self):
        return f'/readers/{self.id}'

    class Meta:
        verbose_name = "изменение книговыдачи"
        verbose_name_plural = "изменения книговыдачи"
