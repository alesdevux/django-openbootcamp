from django.shortcuts import render


def simple(request):
    return render(request, "simple.html", {})


def dynamic(request, name):
    categories = [
        "JavaScript",
        "Python",
        "Django",
        "HTML",
        "CSS",
    ]
    context = {"name": name, "categories": categories}
    return render(request, "dynamic.html", context)
