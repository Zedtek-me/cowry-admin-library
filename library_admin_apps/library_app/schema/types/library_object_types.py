from graphene_django import DjangoObjectType
from library_admin_apps.library_app.models import Book
import graphene
from library_admin_apps.users.schema.types.user_types import UserType

class BookType(DjangoObjectType):
    '''serialization repr for the book model'''
    borrower = graphene.Field(UserType)
    class Meta:
        model = Book
        fields = "__all__"

    def resolve_borrower(self, info):
        return self.borrower
        