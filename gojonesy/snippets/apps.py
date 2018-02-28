from django.apps import AppConfig


class SnippetsConfig(AppConfig):
    name = 'snippets'
    verbose_name = 'Snippets'

    def ready(self):
        pass
