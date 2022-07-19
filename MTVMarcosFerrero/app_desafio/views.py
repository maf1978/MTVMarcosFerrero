from django.shortcuts import render

# Create your views here.
def listar_familiares(request):
    context = {}
    context["familiares"] = Familiar.objects.all()
    return render(request, "app_desafio/familia.html", context)