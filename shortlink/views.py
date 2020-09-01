from django.http import (HttpResponseRedirect, Http404)

from .models import ShortLink


def map_link(request, **kwargs):
    link = kwargs.get('link', '')
    s = ShortLink.objects.filter(short_url=link).first()
    if s:
        return HttpResponseRedirect(s.long_url)
    raise Http404
