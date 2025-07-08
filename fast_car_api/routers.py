from fastapi import APIRouter, status
from fast_car_api.database import SessionDep
from fast_car_api.models import Car
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
def create_car(car: CarSchema, session: SessionDep):
    car = Car(**car.model_dump())
    session.add(car)
    session.commit()
    session.refresh(car)
    return car 