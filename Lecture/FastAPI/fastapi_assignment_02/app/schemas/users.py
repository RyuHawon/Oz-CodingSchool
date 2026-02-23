from enum import Enum

from pydantic import BaseModel, Field


class GenderEnum(str, Enum):
    male = "male"
    female = "female"


class UserCreateRequest(BaseModel):
    username: str
    age: int
    gender: GenderEnum


class UserResponse(BaseModel):
    id: int
    username: str
    age: int
    gender: GenderEnum


class UserUpdateRequest(BaseModel):
    username: str | None = None
    age: int | None = None


class UserSearchParams(BaseModel):
    model_config = {"extra": "forbid"}

    username: str | None = None
    age: int | None = Field(default=None, gt=0)
    gender: GenderEnum | None = None
