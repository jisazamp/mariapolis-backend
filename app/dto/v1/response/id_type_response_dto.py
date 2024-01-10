from typing import List

from pydantic import BaseModel


class IdTypeResponseDTO(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
