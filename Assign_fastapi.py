from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel
from typing import List, Optional
import sqlite3

# Initialize FastAPI app
app = FastAPI()

# Database connection
conn = sqlite3.connect('book_review.db')
c = conn.cursor()

# Create tables if not exist
c.execute('''CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                publication_year INTEGER NOT NULL
             )''')
c.execute('''CREATE TABLE IF NOT EXISTS reviews (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                book_id INTEGER,
                text_review TEXT NOT NULL,
                rating INTEGER NOT NULL,
                FOREIGN KEY (book_id) REFERENCES books(id)
             )''')
conn.commit()


# Pydantic models
class Book(BaseModel):
    title: str
    author: str
    publication_year: int


class Review(BaseModel):
    text_review: str
    rating: int


# API Endpoints
@app.post("/books/", response_model=Book)
async def add_book(book: Book):
    c.execute("INSERT INTO books (title, author, publication_year) VALUES (?, ?, ?)",
              (book.title, book.author, book.publication_year))
    conn.commit()
    return book


@app.post("/books/{book_id}/reviews/", response_model=Review)
async def submit_review(book_id: int, review: Review, background_tasks: BackgroundTasks):
    c.execute("SELECT id FROM books WHERE id=?", (book_id,))
    book = c.fetchone()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    c.execute("INSERT INTO reviews (book_id, text_review, rating) VALUES (?, ?, ?)",
              (book_id, review.text_review, review.rating))
    conn.commit()
    background_tasks.add_task(send_confirmation_email, book_id, review.text_review)
    return review


@app.get("/books/", response_model=List[Book])
async def get_books(author: Optional[str] = None, publication_year: Optional[int] = None):
    query = "SELECT * FROM books"
    if author:
        query += f" WHERE author='{author}'"
    if publication_year:
        if author:
            query += f" AND publication_year={publication_year}"
        else:
            query += f" WHERE publication_year={publication_year}"
    c.execute(query)
    books = c.fetchall()
    return books


@app.get("/books/{book_id}/reviews/", response_model=List[Review])
async def get_reviews(book_id: int):
    c.execute("SELECT * FROM reviews WHERE book_id=?", (book_id,))
    reviews = c.fetchall()
    return reviews


# Background task
def send_confirmation_email(book_id: int, text_review: str):
    # Simulated email sending process
    print(f"Sending confirmation email for book {book_id} with review: {text_review}")


# Close database connection
@app.on_event("shutdown")
def close_connection():
    conn.close()


# Run the FastAPI application using Uvicorn if this script is the main program
if __name__ == "__main__":
    import uvicorn
    # Run the FastAPI application on the specified host and port
    uvicorn.run(app, host="127.0.0.1", port=8000)
