from fastapi import APIRouter, HTTPException, status
from sqlmodel import select

from fast_car_api.database import SessionDep
from fast_car_api.models import Car
from fast_car_api.schemas import (
    CarList,
    CarPartialUpdate,
    CarPubllic,
    CarSchema,
)

router = APIRouter(  # informações interessantes de se adicionar
    prefix='/api/v1/cars',
    tags=['cars'],
)


@router.post(
    '/', response_model=CarPubllic, status_code=status.HTTP_201_CREATED
)
def create_car(car: CarSchema, session: SessionDep):
    car = Car(**car.model_dump())
    session.add(car)
    session.commit()
    session.refresh(car)
    return car


@router.get('/', response_model=CarList, status_code=status.HTTP_200_OK)
def list_cars(session: SessionDep, offset: int = 0, limit: int = 100):
    query = session.scalars(select(Car).offset(offset).limit(limit))
    cars = query.all()
    return {'cars': cars}


@router.get(
    '/{car_id}', response_model=CarPubllic, status_code=status.HTTP_200_OK
)
def get_car(car_id: int, session: SessionDep):
    car = session.get(Car, car_id)
    if not car:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='car not found'
        )
    return car


# put vai alterar o objeto inteiro
@router.put(
    '/{car_id}', response_model=CarPubllic, status_code=status.HTTP_201_CREATED
)
def update_car(car_id: int, car: CarSchema, session: SessionDep):
    dbcar = session.get(Car, car_id)
    if not dbcar:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='car not found'
        )
    for field, value in car.model_dump().items():
        setattr(dbcar, field, value)
    session.commit()
    session.refresh(dbcar)
    return dbcar


# não muda todos os campos de uma vez
@router.patch(
    '/{car_id}', response_model=CarPubllic, status_code=status.HTTP_201_CREATED
)
def patch_car(car_id: int, car: CarPartialUpdate, session: SessionDep):
    dbcar = session.get(Car, car_id)
    if not dbcar:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='car not found'
        )
    update_data = {k: v for k, v in car.model_dump(exclude_unset=True).items()}
    for field, value in update_data.items():
        setattr(dbcar, field, value)
    session.commit()
    session.refresh(dbcar)
    return dbcar


@router.delete(path='/{id_car}', status_code=status.HTTP_204_NO_CONTENT)
def delete_car(car_id: int, session: SessionDep):
    car = session.get(Car, car_id)
    if not car:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='car not found'
        )
    session.delete(car)
    session.commit()
