from sqlalchemy.orm import DeclarativeBase

from app.database.connection import core_engine


class Base(DeclarativeBase):
    bind = core_engine
