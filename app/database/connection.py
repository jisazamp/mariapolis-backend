import os
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_CORE_CONNECTION_URL = os.getenv(
    "DATABASE_CORE_CONNECTION_URL",
    "mysql+pymysql://root:root@localhost:3306/mariapolis",
)

core_engine = create_engine(DATABASE_CORE_CONNECTION_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=core_engine)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
