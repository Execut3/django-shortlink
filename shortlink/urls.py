from django.urls import re_path

from .views import map_link


urlpatterns = [
    re_path('^(?P<link>[a-zA-Z0-9 _-]+)$', map_link, name='map_link'),

]
