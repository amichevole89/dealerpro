from datetime import date, time
from pydantic import BaseModel
from bson.objectid import ObjectId

class AutomobileVO(BaseModel):
    id: ObjectId
    href: str
    vin: str

class Technician(BaseModel):
    id: ObjectId
    name: str
    employee_number: str

class Appointment(BaseModel):
    id: ObjectId
    automobile: AutomobileVO
    technician: Technician
    customer_name: str
    date: date
    time: time
    vin: str
    href: str
    purpose: str
    completed: bool
