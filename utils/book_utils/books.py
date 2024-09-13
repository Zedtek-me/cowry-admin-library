from library_app.models import Book

class BookUtils:
    '''all utilities related to the book model'''

    @classmethod
    def create_book(cls, book_data:dict):
        '''creates a book'''
        return Book.objects.create(**book_data)
        