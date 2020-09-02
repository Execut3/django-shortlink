from django.db import models

from .settings import *
from .utils import generate_random_str


class ShortLink(models.Model):
    name = models.CharField(
        max_length=100,
        null=True, blank=True,
        verbose_name='Presentation name for url'
    )   # If not set, will be set to full_url
    short_path = models.CharField(
        db_index=True,
        max_length=100,
        verbose_name='Shorten Path ID',
    )   # Should be db_index ed.
    full_url = models.CharField(
        max_length=500,
        verbose_name='Real URL to be shorten'
    )

    def __str__(self):
        return '{}-{}'.format(self.id, self.name)

    class Meta:
        db_table = 'shortlink'
        verbose_name = 'Shortlink'

    @property
    def short_url(self):
        """ Complete short url
        Pattern:
            short_url = HOST_ADDRESS + '/' +  SHORTLINK_URL_BASE + shorten_path
        """
        return '{}/{}{}'.format(
            HOST_ADDRESS,
            SHORTLINK_URL_BASE,
            self.short_path
        )

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.short_path:
            self.generate_short_path(commit=False)
            # Don't save cause will call save() later.

        if not self.name:
            self.name = self.full_url
        super(ShortLink, self).save()

    def generate_short_path(self, commit=True):
        # Loop until a not used path found!
        while True:
            path = generate_random_str(SHORTEN_PATH_LENGTH)
            if not ShortLink.objects.filter(short_path=path).exists():
                break
        self.short_path = path
        if commit:
            self.save()
