from prisma import Prisma
from app.db.prisma import db


def get_db() -> Prisma:
    """
    Get the database connection
    """
    return db.get_db()
