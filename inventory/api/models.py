from pydantic import BaseModel

class Manufacturer(BaseModel):
    name: str

class Model(BaseModel):
    name: str
    manufacturer: Manufacturer

class Automobile(BaseModel):
    year: int
    model: Model
    color: str
    vin: str