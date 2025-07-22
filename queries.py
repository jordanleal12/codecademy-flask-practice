from models import db, Book, Reader, Review, Annotation
from app import app

with app.app_context():
    books = Book.query.all()
    print(books)
    for book in books:
        print(book.reviews.all())
