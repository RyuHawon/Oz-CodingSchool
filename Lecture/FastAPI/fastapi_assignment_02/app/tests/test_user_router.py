import httpx
from fastapi import status

from main import app
from app.models.users import UserModel
from app.schemas.users import GenderEnum


async def test_api_create_user() -> None:
    # given
    data = {"username": "testuser", "age": 20, "gender": GenderEnum.male}

    # when
    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app), base_url="http://test"
    ) as client:
        response = await client.post(url="/users/", json=data)

    # then
    assert response.status_code == status.HTTP_200_OK
    created_user_id = response.json()
    created_user = UserModel.filter(id=created_user_id)[0]
    assert created_user
    assert created_user.username == data["username"]
    assert created_user.age == data["age"]
    assert created_user.gender == data["gender"]
