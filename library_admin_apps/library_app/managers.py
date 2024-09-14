from django.db.models import manager


class BookManager(manager.Manager):
    '''book manager'''
    def get_queryset(self):
        return super().get_queryset().exclude(status="DELETED")

