import graphene
from django.db.transaction import atomic
from library_admin_apps.library_app.schema.types.library_object_types import BookType
from library_admin_apps.library_app.schema.types.library_input_types import BookInputType
from library_admin_apps.library_app.models import Book
from utils.book_utils.books import BookUtils
from constants.constants import DELETED, BORROWED, AVAILABLE
from AMQPs.producer import Publisher
import logging

logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")





class CreateBook(graphene.Mutation):
    message = graphene.String()
    book = graphene.Field(BookType)

    class Arguments:
        book_data = BookInputType(required=True)
    
    @atomic
    def mutate(self, info, book_data):
        '''adds a book to the library'''

        added_book = BookUtils.create_book(book_data)
        book_info = (added_book and added_book.__dict__) or None
        # publish to remote api that admin has added a new book to the library
        # this can be improved by making it ran by another process or other form of asynchronuos operations, e.g celery
        try:
            result = Publisher().publish_to_remote_process(msg=book_info)
            logger.debug(f"publishing result: {result}")
        except Exception as e:
            logger.debug(f"an error occurred when publishing to the user library api. Error details: {e}")
        return CreateBook(
            message="book successfully added to the catalogue",
            book=added_book
        )

class DeleteBook(graphene.Mutation):
    message = graphene.String()

    class Arguments:
        book_id = graphene.ID(required=True)

    def mutate(self, book_id):
        '''soft deletes a book'''
        updated_count = Book.objects.filter(id=book_id).update(status=DELETED)
        if not updated_count:
            raise Exception("book not found")
        return DeleteBook(
            message="book successfully deleted from the catalogue"
        )



class Mutation(graphene.ObjectType):
    '''root mutation for the library app'''
    add_book = CreateBook.Field(description="admin adds a book to the library")
    remove_book = DeleteBook.Field(description="admin removes a book from the library")
