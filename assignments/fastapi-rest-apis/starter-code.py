from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Book(BaseModel):
    # TODO: Add required title and author fields.
    pass


books = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"id": 2, "title": "A Wrinkle in Time", "author": "Madeleine L'Engle"},
]


@app.get("/books")
def get_books():
    # TODO: Return all books.
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # TODO: Find and return the book with this ID.
    # Raise an HTTP 404 error when the book does not exist.
    pass


@app.post("/books")
def create_book(book: Book):
    # TODO: Give the new book a unique ID, save it, and return it.
    pass


# Run from the terminal with:
# uvicorn starter-code:app --reload