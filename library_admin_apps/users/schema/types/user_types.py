from graphene_django import DjangoObjectType
from library_admin_apps.users.models import User


class UserType(DjangoObjectType):
    '''serialization repr for the user model'''
    class Meta:
        model = User
        fields = "__all__"