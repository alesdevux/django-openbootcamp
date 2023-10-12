from django.http import HttpResponse


# Create your views here.
def test(request):
    return HttpResponse("Hola mundo desde comentarios")
