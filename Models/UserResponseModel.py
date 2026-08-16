from typing import List
from pydantic import BaseModel

class Address(BaseModel):
    address: str
    city: str
    state: str
    postalCode: str
    country: str


class User(BaseModel):
    id: int
    firstName: str
    lastName: str
    maidenName: str
    age: int
    gender: str
    email: str
    phone: str
    username: str
    image: str
    address: Address

class UsersResponse(BaseModel):
    users: List[User]
    total: int
    skip: int
    limit: int