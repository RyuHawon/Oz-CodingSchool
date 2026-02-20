from pydantic import BaseModel
from enum import Enum


class Gender(str, Enum):
    male = "male"
    female = "female"


class UserCreate(BaseModel):
    username: str = ""
    gender: Gender
    age: int
