from django.shortcuts import render
from .models import Articles


# Create your views here.
def readers_home(request):
    readers = Articles.objects.all() # можно сделать срез, чтобы было не больше скольких то записей на странице, например 5: [:5]
    return render(request, 'readers/readers_home.html', {'readers': readers})