from sqlmodel import Field, SQLModel

# Field é como se fosse "column" e também é onde vc passa as configs


class Car(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    brand: str = Field()
    model: str = Field()
    color: str | None = Field(default=None)
    factory_year: int | None = Field()
    model_year: int | None = Field()
    description: str | None = Field()
