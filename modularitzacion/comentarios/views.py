from django.http import HttpResponse

from .models import Comment


def test(request):
    return HttpResponse("Hola mundo desde comentarios")


def create(request):
    comment = Comment(
        name="Flatley",
        score=5,
        text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quibusdam.",
    )
    comment.save()

    return HttpResponse("Hola mundo desde create")
