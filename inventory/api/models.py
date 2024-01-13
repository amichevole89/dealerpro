from pydantic import BaseModel
from bson.objectid import ObjectId
from custom_validators import CustomValidators

class Manufacturer(BaseModel, CustomValidators):
    name: str
    id: ObjectId

class VehicleModel(BaseModel, CustomValidators):
    name: str
    manufacturer: Manufacturer
    id: ObjectId

class Automobile(BaseModel, CustomValidators):
    year: int
    model: VehicleModel
    color: str
    vin: str
    id: ObjectId