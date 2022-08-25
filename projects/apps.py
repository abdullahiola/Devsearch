from django.apps import AppConfig



class ProjectsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'projects'

    def ready(self) -> None:
        import projects.signals
        return super().ready()
