from django.shortcuts import render


def simple(request):
    return render(request, "simple.html", {})


def dynamic(request, name):
    context = {"name": name}
    return render(request, "dynamic.html", context)
