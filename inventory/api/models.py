from pydantic import BaseModel
from bson.objectid import ObjectId

class Manufacturer(BaseModel):
    name: str
    id: ObjectId

class Model(BaseModel):
    name: str
    manufacturer: Manufacturer
    id: ObjectId

class Automobile(BaseModel):
    year: int
    model: Model
    color: str
    vin: str
    id: ObjectId