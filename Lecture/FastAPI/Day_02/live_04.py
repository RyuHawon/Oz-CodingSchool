from fastapi import FastAPI
from pydantic import BaseModel, computed_field, field_validator

app = FastAPI()


class Product(BaseModel):
    name: str
    price: float
    discount: float = 0

    @field_validator("discount")
    @classmethod
    def discount_validator(cls, v):
        if not (0 <= v <= 100):
            raise ValueError("Discount must be between 0 and 100")
        return v

    @computed_field
    @property
    def final_price(self) -> float:
        return round(self.price * (1 - self.discount / 100), 1)

@app.post("/products/")
def create_product(product: Product):
    return product
