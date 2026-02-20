from pydantic import BaseModel, field_validator
from fastapi import FastAPI
from datetime import datetime

app = FastAPI()


class Reservation(BaseModel):
    name: str
    email: str
    date: datetime
    special_request: str = ""

    @field_validator("name")
    @classmethod
    def validate_name(cls, v):
        if len(v) > 50:
            raise ValueError("Name length must be between 1 and 50")
        return v

    @field_validator("date")
    @classmethod
    def validate_date(cls, v):
        if v < datetime.now():
            raise ValueError("Date must be in the future")
        return v


@app.post("/reservations/")
def reservations(reservation: Reservation):
    return {"reservation": reservation}
