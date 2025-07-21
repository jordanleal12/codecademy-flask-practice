"""Separate file to store models and import to app.py"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Book(db.Model):
    """Book class to create database table"""

    id = db.Column(
        db.Integer, primary_key=True
    )  # primary key column, automatically generated IDs
    title = db.Column(
        db.String(80), index=True, unique=True
    )  # Indexing takes up extra storage space but makes it faster to search by title
    author_name = db.Column(db.String(50), index=True)
    author_surname = db.Column(db.String(80), index=True)
    month = db.Column(db.String(20), index=True)
    year = db.Column(db.Integer, index=True)
    reviews = db.relationship(
        "Review",  # "review" declares the review table as the many in the one to many relationship.
        backref="book",  # backref="book" creates a property in reviews that lets you access the book related to the reviews (eg.review.book).
        lazy="dynamic",  # lazy = dynamic turns the output of book.reviews into an object you can use sql functions on like .all() or .filter_by()
    )

    def __repr__(self):
        """Automatically passes f string to python when printing a specific row from Book table"""
        return f"{self.title} in: {self.month},{self.year}"


class Reader(db.Model):
    """Reader class to create database table"""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True)
    surname = db.Column(db.String(80), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    reviews = db.relationship("Review", backref="reviewer", lazy="dynamic")

    def __repr__(self):
        return f"Reader {self.name} with email: {self.email}"


class Review(db.Model):
    """Review class to create junction table between reader and book"""

    id = db.Column(db.Integer, primary_key=True)
    stars = db.Column(db.Integer)
    text = db.Column(db.String(200))
    book_id = db.Column(
        db.Integer, db.ForeignKey("book.id")
    )  # Foreign key references id in book model
    reviewer_id = db.Column(db.Integer, db.ForeignKey("reader.id"))

    def __repr__(self):
        return f"Review: {self.text} stars: {self.stars}"
