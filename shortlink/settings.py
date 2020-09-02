from django.conf import settings


# Lenght of shortlinked path
SHORTEN_PATH_LENGTH = getattr(settings, 'SHORTEN_PATH_LENGTH', 8)

# Will indicate that all path starting with s/ is redirected to this app.
SHORTLINK_URL_BASE = getattr(settings, 'SHORTLINK_URL_BASE', 's/')

# This variable is used for generate short_link and send for users usages.
# For example a shortlink with identifier /abcd is created, now we want to
# get the full short-link-url and send it to client.
# So short_link = HOST_ADDRESS + '/' +  SHORTLINK_URL_BASE + shorten_path
HOST_ADDRESS = getattr(settings, 'HOST_ADDRESS', 'http://localhost:8000')
