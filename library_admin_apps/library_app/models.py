from django.db import models
from interfaces.models import BaseModel
from library_admin_apps.library_app.managers import BookManager
from constants.constants import BORROWED, DELETED, AVAILABLE


class Book(BaseModel):
    '''book model'''
    STATUSES = (
        (BORROWED, "BORROWED"),
        (DELETED, "DELETED"),
        (AVAILABLE, "AVAILABLE"),
    )
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    summary = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(choices=STATUSES, default=AVAILABLE)
    borrower = models.ForeignKey(to="users.User", on_delete=models.SET_NULL, null=True, blank=True)
    available_date = models.DateTimeField(null=True, blank=True, help_text="date the book would be available to be borrowed again")
    added_by = models.IntegerField(null=True, blank=True, help_text="id of the admin-user who added the book to the library")

    objects = BookManager()

    class Meta:
        db_table = "book"
        verbose_name = "book"
        verbose_name_plural = "books"

    def __str__(self):
        return f"{self.title}"
    