I have done CRUD opetration with fastapi and SQLite.
SQLite database is set up with a books table to store book information.
CRUD operations (create_book and get_book) are implemented to interact with the database.
FastAPI endpoints /books/ and /books/{book_id} are defined to add and retrieve books respectively.
Pydantic validation errors are handled automatically by FastAPI.
Database-related errors are handled by raising HTTPException with appropriate status codes and error messages.
