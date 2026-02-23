from pydantic import BaseModel
from enum import Enum
from typing import Optional


class Gender(str, Enum):
    male = "male"
    female = "female"


class UserCreate(BaseModel):
    username: str = ""
    gender: Gender
    age: int


class UserUpdate(BaseModel):
    username: str | None = None
    gender: Gender | None = None
    age: int | None = None