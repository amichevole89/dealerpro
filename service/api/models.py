from datetime import date, time
from pydantic import BaseModel


class AutomobileVO(BaseModel):
    href: str
    vin: str

class Technician(BaseModel):
    name: str
    employee_number: str

class Appointment(BaseModel):
    automobile: AutomobileVO
    technician: Technician
    customer_name: str
    date: date
    time: time
    vin: str
    href: str
    purpose: str
    completed: bool
