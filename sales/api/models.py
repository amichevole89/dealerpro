from pydantic import BaseModel
from bson.objectid import ObjectId
class AutomobileVO(BaseModel):
    id: ObjectId
    vin: str
    href: str

class Salesperson(BaseModel):
    name: str
    employee_number: str
    id: ObjectId

class Customer(BaseModel):
    name: str
    address: str
    phone: str
    email: str
    id: ObjectId
class Sale(BaseModel):
    automobile: AutomobileVO
    salesperson: Salesperson
    customer: Customer
    price: float
    date: str
    href: str
    id: ObjectId