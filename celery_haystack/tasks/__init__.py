from celery import current_app  # noqa

from .base import BaseCeleryHaystackSignalHandler, BaseCeleryHaystackUpdateIndex


@current_app.register_task
class CeleryHaystackSignalHandler(BaseCeleryHaystackSignalHandler):
    pass

@current_app.register_task
class CeleryHaystackUpdateIndex(BaseCeleryHaystackUpdateIndex):
    pass