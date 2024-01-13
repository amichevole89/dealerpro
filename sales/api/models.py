from pydantic import BaseModel

class AutomobileVO(BaseModel):
    vin: str
    href: str

class Salesperson(BaseModel):
    name: str
    employee_number: str

class Customer(BaseModel):
    name: str
    address: str
    phone: str
    email: str

class Sale(BaseModel):
    automobile: AutomobileVO
    salesperson: Salesperson
    customer: Customer
    price: float
    date: str
    href: str