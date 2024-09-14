from graphene_django import DjangoObjectType
from library_admin_apps.library_app.models import Book

class BookType(DjangoObjectType):
    '''serialization repr for the book model'''
    class Meta:
        model = Book
        fields = "__all__"