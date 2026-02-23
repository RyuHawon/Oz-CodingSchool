from typing import Annotated
from fastapi import FastAPI
from app.models.users import UserModel
from app.schemas.users import UserCreateRequest

app = FastAPI()
UserModel.create_dummy()


@app.post("/users/")
async def create_user(data: UserCreateRequest) -> int:
    user = UserModel.create(**data.model_dump())
    return user.id


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
