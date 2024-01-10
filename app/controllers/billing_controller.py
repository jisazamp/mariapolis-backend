from functools import lru_cache
from http import HTTPStatus
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud.billing_crud import BillingCrud
from app.database.connection import get_db
from app.dto.v1.response.generic_response import Response
from app.dto.v1.response.id_type_response_dto import IdTypeResponseDTO

router = APIRouter()


@lru_cache()
def get_crud(db: Session = Depends(get_db)) -> BillingCrud:
    return BillingCrud(db)


@router.get("/id_types", response_model=Response[List[IdTypeResponseDTO]])
async def list(
    crud: BillingCrud = Depends(get_crud),
):
    id_types = crud.list_id_types()
    return Response[List[IdTypeResponseDTO]](
        data=id_types,
        error=None,
        message="Lista de tipos de identificación retornados",
        status_code=HTTPStatus.OK.value,
    )
