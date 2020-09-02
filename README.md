# django-shortlink

A simple Django App to hold short links mapped to long urls used in your projects.

### Requirements

To use this package following needed. if not provided will be installed automatically.
```
Django>=2.0
```

### Installation

**Note:** This package is well tested on `django>=2.0`. But if you are using older versions can be
used with minor changes in structure.

install using pip:
```
$ pip install django-shortlink
```

### Usage
Register app in `settings.py`

```
INSTALLED_APPS = [
    "django_shortlink",
]
```

update `urls.py` like below:

```
urlpatterns += [
    ...
    re_path(r'', include('shortlink.urls')),
    ...
```

Now set Setting variables, If not will use default values as below:

```python
SHORTEN_PATH_LENGTH = 8
SHORTLINK_URL_BASE = 's/'
HOST_ADDRESS = 'http://localhost:8000'
```

Now to create shortlink, pass your full_url like this:

```python
from shortlink.models import ShortLink
s = ShortLink.objects.create(full_url="https://test.com")
print(s.short_url)
```

`short_url` is the shorten url that you should give users.
If they click on it, methods in `views.py` will be triggered
and if short_url is valid, will redirect to `full_url`.