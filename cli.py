"""Separate file to store cli commands to be imported into app.py"""

import click
from flask.cli import with_appcontext
from models import db, Book, Reader, Review


@click.command("create")
@with_appcontext
def create_tables():
    """Creates tables in database from models"""

    db.create_all()
    click.echo("database tables created")


@click.command("drop")
@with_appcontext
def drop_tables():
    """Deletes all tables from database"""

    db.drop_all()
    click.echo("database tables dropped")


@click.command("seed")
@with_appcontext
def seed_data():
    """Seeds database table with provided objects"""

    b1 = Book(
        id=123,
        title="Demian",
        author_name="Hermann",
        author_surname="Hesse",
        month="February",
        year=2020,
    )
    r1 = Reader(id=342, name="Ann", surname="Adams", email="ann.adams@example.com")
    b2 = Book(
        id=533,
        title="The Stranger",
        author_name="Albert",
        author_surname="Camus",
        month="April",
        year=2019,
    )
    r2 = Reader(id=765, name="Sam", surname="Adams", email="sam.adams@example.com")

    rev1 = Review(
        id=435,
        text="This book is amazing...",
        stars=5,
        reviewer_id=r1.id,
        book_id=b1.id,
    )
    rev2 = Review(
        id=450,
        text="This book is difficult!",
        stars=2,
        reviewer_id=r2.id,
        book_id=b2.id,
    )
    # Create data variables
    db.session.add_all([b1, r1, b2, r2, rev1, rev2])  # Add data variables
    db.session.commit()
    click.echo("database tables created")
