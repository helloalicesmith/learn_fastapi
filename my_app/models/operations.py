from pydantic import BaseModel
from datetime import date

class OperationBase(BaseModel):
    date: date
    name: str

class Operation(OperationBase):
    id: int

    class Config:
        orm_mode = True

class OperationCreate(OperationBase):
    pass
