from pydantic import BaseModel
from bson.objectid import ObjectId

class Role(BaseModel):
    id: ObjectId
    title: str
    description: str
class Admin(BaseModel):
    id: ObjectId
    email: str
    password: str
    name: str | None
    role: Role

class Manager(BaseModel):
    id: ObjectId
    email: str
    password: str
    name: str | None
    role: Role

class User(BaseModel):
    id: ObjectId
    email: str
    password: str
    name: str | None
    role: Role


