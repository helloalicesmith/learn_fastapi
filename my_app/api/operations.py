from fastapi import APIRouter
from fastapi import Depends

from ..models.operations import Operation
from ..services import operations

router = APIRouter(
    prefix='/operations',
)

@router.get('/', response_model=list[Operation])
def get_operations(service: operations.OperationsService = Depends()): # Depends -> говорит fastapi о внедрении зависимости
    return service.get_list()
