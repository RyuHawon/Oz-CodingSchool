from fastapi import FastAPI
from pydantic import BaseModel, Field
from datetime import datetime
import uuid

app = FastAPI()


class User(BaseModel):
    user_id: str = Field(default_factory=lambda: str(uuid.uuid4))
    name: str
    role: str = "user"
    created_at: datetime = Field(default_factory=datetime.now)


@app.post("/users/")
def create_users(user: User):
    return user
