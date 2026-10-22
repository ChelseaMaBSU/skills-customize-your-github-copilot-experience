# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI for managing a collection of books. Practice defining routes, accepting JSON request data, returning structured responses, and validating client input.

## 📝 Tasks

### 🛠️ Create API Routes

#### Description

Complete the starter code to create a FastAPI application that stores books in memory. Add routes that let a client view all books, view one book by its ID, and add a new book.

#### Requirements

Completed program should:

- Create a FastAPI application instance.
- Define `GET /books` to return the complete list of books.
- Define `GET /books/{book_id}` to return one book by its ID.
- Define `POST /books` to add a book from a JSON request body.
- Return JSON responses with the book's `id`, `title`, and `author` fields.

### 🛠️ Validate Requests and Handle Errors

#### Description

Improve the API by using a Pydantic model for incoming book data and by returning a clear error when a requested book does not exist.

#### Requirements

Completed program should:

- Define a request model that requires a non-empty `title` and `author`.
- Reject invalid book data with FastAPI's validation response.
- Return HTTP status `404` and a clear detail message when a book ID is not found.
- Return the newly created book from `POST /books` with a unique ID.
- Include instructions in the starter code comments for running the API with Uvicorn.