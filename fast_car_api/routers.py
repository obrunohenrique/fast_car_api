from fastapi import APIRouter, status
from fast_car_api.schemas import (
    CarPubllic,
    CarSchema
    )

router = APIRouter(  # informações interessantes de se adicionar
    prefix='/api/v1/cars',
    tags=['cars'],
)


@router.post(
        '/',
        response_model=CarPubllic,
        status_code=status.HTTP_201_CREATED
)
def create_car(car: CarSchema):
    return car