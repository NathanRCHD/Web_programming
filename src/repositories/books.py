from sqlalchemy.orm import Session
from typing import List

from src.repositories.base import BaseRepository
from src.models.books import Book as BookModel
from src.api.schemas.books import BookCreate, BookUpdate  # <-- correction ici

class BookRepository(BaseRepository[BookModel, BookCreate, BookUpdate]):
    def get_by_isbn(self, db: Session, *, isbn: str) -> BookModel:
        """
        Récupère un livre par son ISBN.
        """
        return db.query(BookModel).filter(BookModel.isbn == isbn).first()

    def get_by_title(self, db: Session, *, title: str) -> List[BookModel]:
        """
        Récupère des livres par leur titre (recherche partielle).
        """
        return db.query(BookModel).filter(BookModel.title.ilike(f"%{title}%")).all()

    def get_by_author(self, db: Session, *, author: str) -> List[BookModel]:
        """
        Récupère des livres par leur auteur (recherche partielle).
        """
        return db.query(BookModel).filter(BookModel.author.ilike(f"%{author}%")).all()
