from django.http import HttpResponse

from .models import Comment


def test(request):
    return HttpResponse("Hola mundo desde comentarios")


def create(request):
    # comment = Comment(
    #     name="Flatley",
    #     score=5,
    #     text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quibusdam.",
    # )
    # comment.save()
    comment = Comment.objects.create(
        name="Windler, Hegmann and Armstrong",
        score=3,
        text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quibusdam.",
    )

    return HttpResponse("Hola mundo desde create")


def delete(request):
    # comment = Comment.objects.get(id=1)
    # comment.delete()
    Comment.objects.filter(id=2).delete()

    return HttpResponse("Hola mundo desde delete")
