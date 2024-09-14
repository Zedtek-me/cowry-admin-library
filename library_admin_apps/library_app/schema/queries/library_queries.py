import graphene
from library_admin_apps.library_app.schema.types.library_object_types import BookType
from library_admin_apps.library_app.models import Book
from utils.helpers.general import get_kwarg_values



class Query(graphene.ObjectType):
    book = graphene.Field(
        BookType,
        id=graphene.Int(),
        title=graphene.String()
    )

    def resolve_book(self, info, **kwargs):
        '''returns a single book'''
        [
            _id, title
        ] = get_kwarg_values(kwargs, ["id", "title"])

        _filter = {
            "_id": _id,
            "title": title
        }
        if not _id:
            _filter.pop("_id")
        if not title:
            _filter.pop("title")
        return Book.objects.get(**_filter)
