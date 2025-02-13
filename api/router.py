from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel

api_router = APIRouter()

class Book(BaseModel):
    id: int
    title: str
    author: str
    publication_year: int
    genre: str

# Sample book data
books = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien", "publication_year": 1937, "genre": "Fantasy"},
    {"id": 2, "title": "Book 2", "author": "Author 2", "publication_year": 2000, "genre": "Fiction"},
]

# Get all books
@api_router.get("/books/")
def get_all_books():
    return books

# Get single book
@api_router.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

# Create a new book
@api_router.post("/books/", status_code=201)
def create_book(book: Book):
    books.append(book.dict())
    return book

# Update a book
@api_router.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    for idx, existing_book in enumerate(books):
        if existing_book["id"] == book_id:
            books[idx] = book.dict()
            return book
    raise HTTPException(status_code=404, detail="Book not found")

# Delete a book
@api_router.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
    global books
    books = [book for book in books if book["id"] != book_id]
    return
