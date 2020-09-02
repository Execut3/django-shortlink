from django.urls import re_path

from .views import map_link
from .settings import SHORTLINK_URL_BASE


urlpatterns = [
    re_path('^{}(?P<path>[a-zA-Z0-9 _-]+)$'.format(SHORTLINK_URL_BASE), map_link, name='map_link'),
]
