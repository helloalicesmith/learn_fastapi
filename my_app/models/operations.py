from pydantic import BaseModel
from datetime import date

class Operation(BaseModel):
    id: int
    date: date
    name: str

    class Config:
        orm_mode = True
