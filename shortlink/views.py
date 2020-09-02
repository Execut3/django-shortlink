from django.http import (HttpResponseRedirect, Http404)

from .models import ShortLink


def map_link(request, **kwargs):
    path = kwargs.get('path', '')
    s = ShortLink.objects.filter(short_path=path).first()
    if s:
        return HttpResponseRedirect(s.full_url)
    raise Http404
