from fastapi import Depends
from sqlalchemy.orm import Session

from my_app.models.operations import OperationCreate

from ..database import get_session
from .. import tables

class OperationsService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_list(self, kind) -> list[tables.Operation]:
        operations = (
                self.session
                .query(tables.Operation)
                .all()
        )
        return operations

    def create(self, operation_date: OperationCreate) -> tables.Operation:
        operation = tables.Operation(**operation_date.dict())
        self.session.add(operation)
        self.session.commit()

        return operation
