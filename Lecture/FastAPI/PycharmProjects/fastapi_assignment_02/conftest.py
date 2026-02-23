from typing import AsyncGenerator

import pytest
from httpx import ASGITransport, AsyncClient

from app.models.users import UserModel
from main import app

TEST_BASE_URL = "http://test"


@pytest.fixture(scope="function", autouse=True)
def user_model_clear() -> None:
    UserModel.clear()


@pytest.fixture
async def client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url=TEST_BASE_URL
    ) as ac:
        yield ac
