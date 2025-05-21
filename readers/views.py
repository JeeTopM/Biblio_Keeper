from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm


# Create your views here.
def readers_home(request):
    readers = Articles.objects.all()  # добавить срез [:5]
    return render(request, "readers/readers_home.html", {"readers": readers})


def create_readers(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = ArticlesForm()
    data = {"form": form, 'error': error}
    return render(request, "readers/create_readers.html", data)
