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
