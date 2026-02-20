import re

from pydantic import BaseModel, model_validator
from fastapi import FastAPI

app = FastAPI()


class ContactInfo(BaseModel):
    email: str | None = None
    phone_number: str | None = None

    @model_validator(mode="before")
    @classmethod
    def email_process(cls, data):
        if isinstance(data, dict) and "email" in data:
            data["email"] = data["email"].lower()
        return data

    @model_validator(mode="after")
    def contact_process(self):
        if self.email is None and self.phone_number is None:
            raise ValueError("Either email or phone_number must be set")

        if self.email:
            EMAIL_REGEX = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
            if not re.match(EMAIL_REGEX, str(self.email)):
                raise ValueError("Invalid email address")

        return self
