from pydantic import BaseModel, Field, ConfigDict
from enum import Enum


class Gender(str, Enum):
    male = "male"
    female = "female"


class UserCreate(BaseModel):
    username: str
    gender: Gender
    age: int


class UserUpdate(BaseModel):
    username: str | None = None
    gender: Gender | None = None
    age: int | None = None


class UserSearchParams(BaseModel):
    username: str | None = None
    gender: Gender | None = None
    age: int | None = Field(None, gt=0)

    model_config = ConfigDict(extra="forbid")
