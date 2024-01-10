from sqlalchemy.orm import Session

from app.models.id_type import IdType


class BillingCrud:
    def __init__(self, db: Session) -> None:
        self.__session = db

    def list_id_types(self):
        id_types = self.__session.query(IdType).all()

        id_types_list = [
            {"id": id_type.id, "name": id_type.name} for id_type in id_types
        ]

        return id_types_list
