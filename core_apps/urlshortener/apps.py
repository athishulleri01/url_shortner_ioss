from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class UrlshortenerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.urlshortener"
    verbose_name = _("Urlshortener")