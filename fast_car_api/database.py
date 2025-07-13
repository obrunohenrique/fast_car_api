# onde ficam as sessões do bd e as conecções do bd(cofigs)

from typing import Annotated

from fastapi import Depends
from sqlmodel import Session, create_engine

SQLLITE_FILE_NAME = 'database.db'
DATABASE_URL = 'sqlite:///cars.db'

connect_args = {
    'check_same_thread': False
}  # isso permite que o fast api use o mesmo bd para diferentes threads
engine = create_engine(
    DATABASE_URL
)  # engine é a biblioteca que fala diretamente com o bd


# criando sessão
def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[
    Session, Depends(get_session)
]  # isso garante que usemos uma sessão por requisição
