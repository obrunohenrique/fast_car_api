from fastapi import FastAPI
from fast_car_api.routers import router as car_router

app = FastAPI( #add informações opcionais
    title='Fast car API',
    description = 'pycode modern car api',
    version = '0.1.0'
)


app.include_router(car_router)


@app.get('/') # usa a variavel app para anotar(@) uma função
def read_root():
    return {'status': 'ok'}


