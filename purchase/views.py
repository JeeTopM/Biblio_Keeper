from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


# Create your views here.
def purchase_home(request):
    purchase = Articles.objects.all()
    return render(request, "purchase/purchase_home.html", {"purchase": purchase})


class PurchaseDetailView(DetailView):
    model = Articles
    template_name = "purchase/details_create_purchase.html"
    context_object_name = "article"


class PurchaseUpdateView(UpdateView):
    model = Articles
    template_name = "purchase/create_purchase.html"
    form_class = ArticlesForm


class PurchaseDeleteView(DeleteView):
    model = Articles
    success_url = "/purchase/"
    template_name = "purchase/purchase_delete.html"


def create_purchase(request):
    error = ""
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            error = "Форма была неверной"

    form = ArticlesForm()
    data = {"form": form, "error": error}
    return render(request, "purchase/create_purchase.html", data)
