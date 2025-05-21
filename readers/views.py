from django.shortcuts import render


# Create your views here.
def readers_home(request):
    return render(request, 'readers/readers_home.html')