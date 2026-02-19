from fastapi import FastAPI

# FastAPI 애플리케이션 인스턴스 생성
app = FastAPI()


@app.get('/users/{user_id}')
def get_user(user_id: int, detailed: bool = False):
    if detailed:
        return {"user_id": user_id, 'info':'Detailed user information'}
    return {"user_id": user_id}