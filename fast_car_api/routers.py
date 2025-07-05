from fastapi import APIRouter

router = APIRouter( #informações interessantes de se adicionar
    prefix='/api/v1/cars',
    tags=['cars'],
)

@router.get('/') # "/" é o prefix
def list_cars():
    return {
        'cars': [
            {'id': 1, 'modelo': 'Marea 20v'},
            {'id': 2, 'modelo': 'Opala'},
            {'id': 3, 'modelo': 'Corsa Wind'}
        ]
    }