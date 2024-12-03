from django.apps import AppConfig


class LessonSignalsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lesson_signals'

    def ready(self):
        import lesson_signals.signals
