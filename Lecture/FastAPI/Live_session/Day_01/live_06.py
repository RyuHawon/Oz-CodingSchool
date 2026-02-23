from pydantic import BaseModel, Field
from fastapi import FastAPI

app = FastAPI()


class Product(BaseModel):
    name: str
    price: float = Field(ge=0, description="price must be greater than 0")
    description: str = "No description"


@app.post("/products/")
def create_product(product: Product):
    return {
        "name": product.name,
        "price": product.price,
        "description": product.description,
    }
