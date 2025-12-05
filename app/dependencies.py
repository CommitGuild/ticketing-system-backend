"""
Setup dependencies for the app
"""

from prisma import Prisma
from app.database import db


def get_db() -> Prisma:
    """
    Get the database connection
    """
    return db.get_db()
