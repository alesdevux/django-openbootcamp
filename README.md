# Django
## Començar amb Django

_Curs per OpenBootcamp_

### Instal·lació

Python ➡️ pip ➡️ PATH ➡️ Django

```
pip install django
```

### Crear projecte

```
django-admin startproject mysite
```

## Esquema de fitxers

```
mysite/
  manage.py
  mysite/
    __init__.py
    settings.py
    urls.py
    asgi.py
    wsgi.py
```

La carpeta `mysite` a nivell superior és el directori del projecte. Els fitxers dins d'aquest directori són:

- `manage.py`: Un script de línia de comandes que permet interactuar amb el projecte de diverses maneres.
- El directori `mysite/`: El paquet Python per al projecte. El seu nom és el nom que s'utilitzarà per importar els seus mòduls Python.
Si hem utilitzat simplement `django-admin startproject mysite` es dirà igual que el directori pare. Si volem que tinguin un nom diferent, es pot especificar com a argument: `django-admin startproject mysite [nom del directori pare o .]`.

Dins del paquet del projecte hi ha els següents fitxers:

- `__init__.py`: Un fitxer buit que indica que el directori és un paquet Python.
- `settings.py`: La configuració del projecte.
- `urls.py`: Les definicions d'URL del projecte.
- `asgi.py`: Un punt d'entrada per al servidor web ASGI.
- `wsgi.py`: Un punt d'entrada per al servidor web WSGI compatible.

### Settings

---
### Crear aplicació

```
python manage.py startapp polls
```

I afegir-la a `INSTALLED_APPS` a `settings.py` de la carpeta del projecte.

```python
INSTALLED_APPS = [
    ...
    'polls',
]
```

Per comprovat que tot està correcte:

```
python manage.py check polls
```

## Models

Una vegada creem un Model, li hem d'indicar a Django que faci les migracions dels models a format SQL.

```
python manage.py makemigrations
```

Acte seguit hem d'aplicar les migracions:

```
python manage.py migrate
```

A partir d'aquí, si tornem a fer canvis al model, hem de tornar a fer els dos passos anteriors.
Els canvis que es fan a les migracions es guarden a la carpeta `migrations` de cada aplicació. A partir de la primera migració `0001_initial.py` es creen fitxers amb els canvis que s'han fet a cada migració.

Si creem un camp que pot ser nul quan ja tenim dades, estem comprometent la integritat de les dades, ja que tindríem camps buits d'un camp que no ho pot ser.
Django ho detecta, ens avisa i ens indica dues opcions:
1. Crear un valor per defecte per a les dades que ja tenim.
2. Tancar la migració i fer els canvis manualment.

## Delegació de URLs

Per poder reutilitzar les rutes quan volguem reutilitzar una app a un altre projecte, hem de fer que les rutes estiguin delegades a la app.
És a dir, dins del directori de l'app, al seu `urls.py` configurarem les noves rutes, i al arxiu `urls.py` del projecte, inclourem aquestes.

```python
# urls.py de l'app
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index_app'),
]
```

```python
# urls.py del projecte
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('name_path/', include('name_app.urls')),
]
```

## Creació i eliminació de dades

Per crear dades, hem de crear una instància del model i guardar-la a la base de dades.

```python
# Creació
from .models import Comment

def create(request):
    # Opció 1 -> Crear instància i guardar-la amb el mètode save a través del model directament
    comment = Comment(
        name="Flatley",
        score=5,
        text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quibusdam.",
    )
    comment.save()
    # Opció 2 -> Crear instància i guardar-la amb el mètode create del model a través de l'objecte
    comment = Comment.objects.create(
        name="Windler, Hegmann and Armstrong",
        score=3,
        text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quibusdam.",
    )

    return HttpResponse("Hola mundo desde create")

# Eliminació
def delete(request):
    # Opció 1 -> Eliminar instància amb el mètode delete a través del model directament
    comment = Comment.objects.get(id=1)
    comment.delete()
    # Opció 2 -> Eliminar instància amb filter i delete a través del model directament
    Comment.objects.filter(id=2).delete()

    return HttpResponse("Hola mundo desde delete")
```

## ForeignKey

Per crear una relació entre models, hem de crear un camp de tipus `ForeignKey` al model que volem que tingui la relació, i indicar-li el model amb el que volem que tingui la relació.

```python
from datetime import date
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    public_date = models.DateField(default=date.today)

    def __str__(self):
        return self.headline
```