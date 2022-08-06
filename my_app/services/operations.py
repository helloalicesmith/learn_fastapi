from fastapi import Depends, status
from fastapi.exceptions import HTTPException
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

        if not tables.Operation:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return operations

    def create(self, operation_date: OperationCreate) -> tables.Operation:
        operation = tables.Operation(**operation_date.dict())
        self.session.add(operation)
        self.session.commit()

        return operation

    def delete(self, operation_id: int) -> int:
        operation = (
                self.session
                .query(tables.Operation)
                .filter_by(id=operation_id)
                .first()
        )
        self.session.delete(operation)
        self.session.commit()

        return operation_id

