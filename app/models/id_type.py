from sqlalchemy import Column, Integer, String

from app.models.base import Base


class IdType(Base):
    __tablename__ = "id_type"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
