from django.db import models

from .utils import generate_random_str


class ShortLink(models.Model):
    name = models.CharField(max_length=100)
    short_url = models.CharField(max_length=100)
    long_url = models.CharField(max_length=500)

    def __str__(self):
        return '{}-{}'.format(self.id, self.name)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.short_url:
            self.generate_short_link(False)
        super(ShortLink, self).save()

    def generate_short_link(self, commit=True):
        while True:
            url = generate_random_str(8)
            if not ShortLink.objects.filter(short_url=url).exists():
                break
        self.short_url = url
        if commit:
            self.save()

