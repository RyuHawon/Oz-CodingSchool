from abc import ABC, abstractmethod

class Pizza(ABC):
    def __init__(self):
        self.name = ""

    @abstractmethod
    def prepare(self):
        pass
    
    def bake(self):
        print(f"{self.name}을(를) 굽는 중입니다")
    
    def cut(self):
        print(f"{self.name}을(를) 자르는 중입니다")
    
    def box(self):
        print(f"{self.name}을(를) 박스에 담는 중입니다")

# 추상 팩토리 !!
class PizzaStore(ABC):
    @abstractmethod

    # 실제 존재하는 팩토리를 만드는 creat_pizza
    # 변함
    def creat_pizza(self, pizza_type: str) -> Pizza:
        pass

    # 여기서 한번만 해놓고 팩토리에서 다 가져다쓸것
    # 변하지 않음
    def order_pizza(self, pizza_type: str):
        pizza = self.creat_pizza(pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza
    
class NYstylePizza(PizzaStore):
    def creat_pizza(self, pizza_type: str) -> Pizza:
        if pizza_type 

class NYstyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "NYstyleCheesePizza"

    def prepare(self):
        print(f"{self.name}을(를) 준비합니다.")

        