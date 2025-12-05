"""
Setup a singleton database connection that supports asyncio and transactions
"""

from typing import Callable, Coroutine, TypeVar
from prisma import Prisma


T = TypeVar("T")


class Database:
    """
    A singleton database connection
    """

    def __init__(self):
        self.__prisma = Prisma()

    async def connect(self) -> None:
        """
        Connect to the database
        """
        await self.__prisma.connect()

    async def disconnect(self) -> None:
        """
        Disconnect from the database
        """
        await self.__prisma.disconnect()

    async def transaction(
        self, callback: Callable[[Prisma], Coroutine[None, None, T]]
    ) -> T:
        """
        Execute a database transaction
        """
        async with self.__prisma.tx():
            return await callback(self.__prisma)

    def get_db(self) -> Prisma:
        """
        Get the database connection
        """
        return self.__prisma


db = Database()
