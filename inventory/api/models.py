from pydantic import BaseModel
from bson.objectid import ObjectId

class Manufacturer(BaseModel):
    name: str
    id: ObjectId

class VehicleModel(BaseModel):
    name: str
    manufacturer: Manufacturer
    id: ObjectId

class Automobile(BaseModel):
    year: int
    model: VehicleModel
    color: str
    vin: str
    id: ObjectId