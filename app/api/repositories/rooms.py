from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database.config import get_general_session


class RoomsRepository:
    def __init__(self,
                 session: AsyncSession = Depends(get_general_session)):
        self.session = session