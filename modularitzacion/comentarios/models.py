from django.db import models


class Comment(models.Model):
    name = models.CharField(max_length=50, null=False)
    score = models.IntegerField(default=4)
    text = models.TextField(max_length=1000, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return super().__str__()
