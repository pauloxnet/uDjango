# 🧬 μDjango (micro Django)

A single file Django micro project created for demonstration purposes to be used in the same way as other Python frameworks.

## 💻 Set Up

### Python

We need a stable and supported version of Python 3 (tested with Python 3.10-3.13):

```console
$ python3 --version
```

<details><summary></summary><pre>Python 3.13.0</pre></details>

### ⚗️ Virtualenv

Creating and activating the virtual environment:

```console
$ python3 -m venv .venv
$ source .venv/bin/activate
```

### 🧩 Requirements

Installing the required python packages in the virtual environments:

```console
$ python -m pip install django uvicorn
```

<details><summary></summary><pre>Collecting django
  Using cached Django-5.1.2-py3-none-any.whl.metadata (4.2 kB)
Collecting uvicorn
  Using cached uvicorn-0.31.1-py3-none-any.whl.metadata (6.6 kB)
Collecting asgiref<4,>=3.8.1 (from django)
  Using cached asgiref-3.8.1-py3-none-any.whl.metadata (9.3 kB)
Collecting sqlparse>=0.3.1 (from django)
  Using cached sqlparse-0.5.1-py3-none-any.whl.metadata (3.9 kB)
Collecting click>=7.0 (from uvicorn)
  Using cached click-8.1.7-py3-none-any.whl.metadata (3.0 kB)
Collecting h11>=0.8 (from uvicorn)
  Using cached h11-0.14.0-py3-none-any.whl.metadata (8.2 kB)
Using cached Django-5.1.2-py3-none-any.whl (8.3 MB)
Using cached uvicorn-0.31.1-py3-none-any.whl (63 kB)
Using cached asgiref-3.8.1-py3-none-any.whl (23 kB)
Using cached click-8.1.7-py3-none-any.whl (97 kB)
Using cached h11-0.14.0-py3-none-any.whl (58 kB)
Using cached sqlparse-0.5.1-py3-none-any.whl (44 kB)
Installing collected packages: sqlparse, h11, click, asgiref, uvicorn, django
Successfully installed asgiref-3.8.1 click-8.1.7 django-5.1.2 h11-0.14.0 sqlparse-0.5.1 uvicorn-0.31.1</pre></details>

## 🧮 Code

Create a new file called `main.py` and update it as follows:

```python
from django import conf, http, urls
from django.core.handlers import asgi

conf.settings.configure(ALLOWED_HOSTS="*", ROOT_URLCONF=__name__)

app = asgi.ASGIHandler()


async def root(_request: http.HttpRequest) -> http.JsonResponse:
    return http.JsonResponse({"message": "Hello World"})


urlpatterns = [urls.path("", root)]
```

## 🏃 Run

Start the server with `uvicorn` command.

```console
$ uvicorn main:app --reload
```

<details><summary></summary><pre>INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [...] using StatReload
INFO:     Started server process [...]
INFO:     Waiting for application startup.
INFO:     ASGI 'lifespan' protocol appears unsupported.
INFO:     Application startup complete.</pre></details>

## 🔬 Check it

Open your browser at [http://127.0.0.1:8000](http://127.0.0.1:8000)

You will see the JSON response as:

```json
{ "message": "Hello World" }
```

## ⚠️ Disclaimer

This code is for demonstration purposes only and should not be used in production. However, the code is released without any guarantee from the author and no liability can be attributed. Use at your own risk.

## 🏛️ History

I created this code while working on an improvement to [Will Vincent](https://github.com/wsvincent)'s [Django Microframework](https://github.com/wsvincent/django-microframework) repository, which was itself inspired by a talk that [Carlton Gibson](https://github.com/carltongibson) gave at [DjangoCon US 2019](https://2019.djangocon.us/talks/using-django-as-a-micro-framework-on-the/): _"[Using Django as a Micro-Framework](https://www.youtube.com/watch?v=w9cYEovduWI)"_.

Starting from that demonstration code I thought of a `Django` micro application that could be used in the same way as a minimal application used in other `Python` frameworks such as `Flask` or `FastAPI`.

I presented this code during the [first sprint day](https://2023.djangocon.us/sprints/thursday/) of [DjangoCon US 2023](https://2023.djangocon.us), together with [Will Vincent](https://github.com/wsvincent) and seeing the appreciation I decided to publish it in this repository.

[![μDjango presentation during the DjangoCon US 2023 sprints in Durham, North Carolina (USA)](https://cdn.fosstodon.org/media_attachments/files/111/262/282/120/320/402/original/0b644dcffe2eeecf.jpg "© 2023 Paolo Melchiorre CC BY-NC-SA “μDjango presentation during the DjangoCon US 2023 sprints in Durham, North Carolina (USA)”"){loading=lazy}](https://fosstodon.org/@paulox/111262287902120294)

> μDjango presentation during the DjangoCon US 2023 sprints in Durham, North Carolina

## 💬 Sharing

Here's where the **μDjango** _(micro Django)_ project was shared online in case you want to re-share it.

### 🦣 Mastodon

- [https://fosstodon.org/@paulox/111262287902120294](https://fosstodon.org/@paulox/111262287902120294)

### 📣 Django forum

- [https://forum.djangoproject.com/t/django-micro-django/24681](https://forum.djangoproject.com/t/django-micro-django/24681)

## ⚖️ License

**μDjango** is licensed under the [BSD 3-Clause License](https://github.com/pauloxnet/uDjango/blob/main/LICENSE).

## 👥 Authors

### 👤 Paolo Melchiorre

- 🌍 Blog: [www.paulox.net](https://www.paulox.net)
- 🐙 Github: [github.com/pauloxnet](https://github.com/pauloxnet)
- 🦣 Mastodon: [fosstodon.org/@paulox](https://fosstodon.org/@paulox)
- 👔 LinkedIn: [linkedin.com/in/paolomelchiorre/](https://www.linkedin.com/in/paolomelchiorre/)
