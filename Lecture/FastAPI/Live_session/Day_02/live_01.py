from pydantic import BaseModel, Field
from fastapi import FastAPI
from typing import List

app = FastAPI()


class Item(BaseModel):
    name: str
    quantity: int = Field(ge=1)


class Order(BaseModel):
    id: int
    items: List[Item]
    total_price: float = Field(ge=0)


@app.post("/orders/")
def create_order(order: Order):
    return {"order": order}
