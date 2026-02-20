from typing import Annotated
from fastapi import FastAPI, HTTPException, status, Path
from app.models.users import UserModel
from app.schemas.users import UserCreate

app = FastAPI()

UserModel.create_dummy()

@app.post("/users/")
def create_users(user: UserCreate):
    new_user = UserModel.create(**user.model_dump())
    return new_user.id


@app.get("/users/")
def get_all_users():
    result = UserModel.all()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return result


@app.get("/users/{user_id}/")
def get_user(user_id: int = Path(gt=0)):
    user = UserModel.get(id=user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return user


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
