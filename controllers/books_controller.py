from flask import Flask, Blueprint, render_template, redirect, request

books_blueprint = Blueprint("books", __name__)

from repositories import book_repository, author_repository
from models.book import Book

# View all books
@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books = books)

# Delete a book
@books_blueprint.route("/books/<id>/delete", methods=['POST'])
def delete_book(id):
    book_repository.delete(id)
    return redirect('/books')

# Get new book
@books_blueprint.route("/books/new", methods=['GET'])
def new_book():
    authors = author_repository.select_all()
    return render_template("books/new.html", all_authors = authors)

# Create a new book
@books_blueprint.route("/books", methods=['POST'])
def create_book():
    title = request.form['title']
    genre = request.form['genre']
    publisher = request.form['publisher']
    author_id = request.form['author_id']
    author = author_repository.select(author_id)
    book = Book(title, genre, publisher, author)
    book_repository.save(book)
    return redirect('/books')

# Show a single book by clicking on its title
@books_blueprint.route("/books/<id>", methods=['GET'])
def show_book(id):
    book = book_repository.select(id)
    return render_template('books/show.html', book = book)