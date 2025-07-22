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
        # "review" declares the review table as the many in the one to many relationship.
        "Review",
        # Creates a property in reviews that lets you access the book related to the
        # reviews (eg.review.book).
        backref="book",
        # Turns the output of book.reviews into an object you can use sql functions on like
        # .all() or .filter_by()
        lazy="dynamic",
        # 'all, delete' deletes on cascade, 'delete-orphan' deletes when foreign key
        # association is removed (eg. when set NULL)
        cascade="all, delete, delete-orphan",
    )
    annotations = db.relationship(
        "Annotation",
        backref="book",
        lazy="dynamic",
        cascade="all, delete, delete-orphan",
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
    reviews = db.relationship(
        "Review",
        backref="reviewer",
        lazy="dynamic",
        cascade="all, delete, delete-orphan",
    )
    annotations = db.relationship(
        "Annotation",
        backref="author",
        lazy="dynamic",
        cascade="all, delete, delete-orphan",
    )

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


class Annotation(db.Model):
    """Annotations class as junction table between reviewer and book"""

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    reviewer_id = db.Column(db.Integer, db.ForeignKey("reader.id"))
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"))

    def __repr__(self):
        return f"<Annotation {self.reviewer_id}-{self.book_id}:{self.text}"
