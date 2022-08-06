from fastapi import APIRouter, Depends, Response, status

from ..models.operations import Operation, OperationCreate
from ..services import operations

router = APIRouter(
    prefix='/operations',
)

@router.get('/', response_model=list[Operation])
def get_operations(
        kind: str | None = None,
        service: operations.OperationsService = Depends()
): # Depends -> говорит fastapi о внедрении зависимости
    return service.get_list(kind=kind)

@router.post('/create', response_model=Operation)
def create_operation(
        operation_date: OperationCreate,
        service: operations.OperationsService = Depends(),
):
    return service.create(operation_date)

@router.delete('/delete')
def delete_operation(
        operation_id: int,
        service: operations.OperationsService = Depends(),
):
    service.delete(operation_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
