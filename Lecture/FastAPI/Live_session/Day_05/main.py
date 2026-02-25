"""
메인 엔트리 (Main Entry)
- FastAPI 앱 생성 및 라우터 등록
- 앱 시작 시 DB 테이블 생성 및 시세 생성기 실행
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from jose import jwt
import asyncio

import models, auth, database
from routers import market, trade


@asynccontextmanager
async def lifespan(_: FastAPI):
    # 앱 시작 시 실행되는 로직
    async with database.engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

    task = asyncio.create_task(market.price_generator())
    # 서버가 켜져있는 동안 백그라운드에서 계속 실행 시작

    yield # 앱 실행

    task.cancel()

app = FastAPI(lifespan=lifespan)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# market과 trade 라우터 등록
app.include_router(market.router)
app.include_router(trade.router)


@app.post("/register")
async def register(
    username: str, password: str, db: AsyncSession = Depends(database.get_db)
):
    """회원가입"""
    # 중복 아이디를 확인하고, 새로운 유저를 생성하여 DB에 저장하세요
    result = await db.execute(select(models.User).where(models.User.username == username))
    existing_user = result.scalar().one_or_none()

    if existing_user:
        raise HTTPException(status_code=400, detail='이미 존재하는 아이디 입니다.')

    hashed_password = auth.pwd_context.hash(password)
    # auth.py 에서 만든 해시화 메서드

    new_user = models.User(
        username=username,
        password=hashed_password,
        balance=3000000.0
    )


"""로그인"""
# 유저 정보를 확인하고, 비밀번호 검증 후 JWT 토큰을 발급하세요
# 토큰 만료 시간은 현재시간 + 15분 입니다.
@app.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(database.get_db),
):
    # form_data 담겨있는 정보로 유저 확인
    result = await db.execute(select(models.User).where(models.User.username == form_data.username))
    user = result.scalar_one_or_none()

    if user is None:
        raise HTTPException(status_code=401, detail='존재하지 않는 유저입니다.')

    password_check = auth.pwd_context.verify(form_data.password, user.password)
    user = result.scalar_one_or_none()

    # 토큰 수여식



