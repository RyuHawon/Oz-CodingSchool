from fastapi import status
from httpx import AsyncClient

from app.models.users import UserModel
from app.schemas.users import GenderEnum


async def test_api_create_user(client: AsyncClient) -> None:
    # given
    data = {"username": "testuser", "age": 20, "gender": GenderEnum.male}

    # when
    response = await client.post(url="/users/", json=data)

    # then
    assert response.status_code == status.HTTP_200_OK
    created_user_id = response.json()
    created_user = UserModel.filter(id=created_user_id)[0]
    assert created_user
    assert created_user.username == data["username"]
    assert created_user.age == data["age"]
    assert created_user.gender == data["gender"]


async def test_api_get_all_users_success(client: AsyncClient) -> None:
    # given
    UserModel.create_dummy()

    # when
    response = await client.get("/users/")

    # then
    assert response.status_code == status.HTTP_200_OK
    response_data = response.json()
    assert len(response_data) == len(UserModel._data)
    assert response_data[0]["id"] == UserModel._data[0].id
    assert response_data[0]["username"] == UserModel._data[0].username
    assert response_data[0]["age"] == UserModel._data[0].age
    assert response_data[0]["gender"] == UserModel._data[0].gender


async def test_api_get_all_users_not_found(client: AsyncClient) -> None:
    # given (비어있음)

    # when
    response = await client.get("/users/")

    # then
    assert response.status_code == status.HTTP_404_NOT_FOUND


async def test_api_get_user(client: AsyncClient) -> None:
    # given
    user = UserModel.create(username="testuser", age=20, gender=GenderEnum.male)
    user_id = user.id

    assert user

    # when
    response = await client.get(url=f"/users/{user_id}")

    # then
    assert response.status_code == status.HTTP_200_OK
    response_data = response.json()
    assert user.id == response_data["id"]
    assert user.username == response_data["username"]
    assert user.age == response_data["age"]
    assert user.gender == response_data["gender"]


async def test_api_get_user_when_user_not_found(client: AsyncClient) -> None:
    # when
    response = await client.get(url="/users/999999")

    # then
    assert response.status_code == status.HTTP_404_NOT_FOUND


async def test_api_update_user(client: AsyncClient) -> None:
    # given
    user = UserModel.create(username="testuser", age=20, gender=GenderEnum.male)
    user_id = user.id
    assert user

    update_data = {"username": "newtestuser", "age": 25}

    # when
    response = await client.patch(url=f"/users/{user_id}", json=update_data)

    # then
    assert response.status_code == status.HTTP_200_OK

    response_data = response.json()
    assert response_data["username"] == update_data["username"]
    assert response_data["age"] == update_data["age"]

    assert user.username == update_data["username"]
    assert user.age == update_data["age"]


async def test_api_update_user_when_user_not_found(client: AsyncClient) -> None:
    # when
    response = await client.patch(
        url="/users/12341234", json={"username": "updated_user"}
    )

    # then
    assert response.status_code == status.HTTP_404_NOT_FOUND


async def test_api_delete_user(client: AsyncClient) -> None:
    # given
    user = UserModel.create(username="deletethisuser", age=22, gender=GenderEnum.male)
    user_id = user.id

    assert user

    # when
    response = await client.delete(url=f"/users/{user_id}")

    # then
    assert response.status_code == status.HTTP_200_OK
    response_data = response.json()
    assert response_data["detail"] == f"User: {user_id}, Successfully Deleted."
    assert UserModel.get(id=user_id) is None


async def test_api_delete_user_when_user_not_found(client: AsyncClient) -> None:
    # when
    response = await client.delete(url="/users/999999")

    # then
    assert response.status_code == status.HTTP_404_NOT_FOUND


async def test_api_search_user(client: AsyncClient) -> None:
    # given
    UserModel.clear()
    UserModel.create_dummy()
    search_name = "dummy3"

    # when
    response = await client.get("/users/search", params={"username": search_name})

    # then
    assert response.status_code == status.HTTP_200_OK
    response_data = response.json()

    assert len(response_data) == 1
    assert response_data[0]["username"] == search_name


async def test_api_search_user_when_user_not_found(client: AsyncClient) -> None:
    # when
    response = await client.get(url="/users/search?username=whatever")

    # then
    assert response.status_code == status.HTTP_404_NOT_FOUND
