import graphene
from library_app.schema.types.library_object_types import BookType
from library_app.schema.types.library_input_types import BookInputType
from django.db.transaction import atomic
from utils.book_utils.books import BookUtils



class CreateBook(graphene.Mutation):
    message = graphene.String()
    book = graphene.Field(BookType)

    class Arguments:
        book_data = BookInputType(required=True)
    
    @atomic
    def mutate(self, info, book_data):
        '''adds a book to the library'''

        added_book = BookUtils.create_book(book_data)
        return CreateBook(
            message="book successfully added to the catalogue",
            book=added_book
        )



class Mutation(graphene.ObjectType):
    '''root mutation for the library app'''
    add_book = CreateBook.Field(description="admin adds book to the library")
