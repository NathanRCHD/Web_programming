from fastapi import APIRouter
from src.api.routes import books

api_router = APIRouter()
api_router.include_router(books.router, prefix="/books", tags=["Books"])
