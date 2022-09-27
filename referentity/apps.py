from django.apps import AppConfig


class ReferentityConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'referentity'

    # def ready(self):
    #     import referentity.signals

