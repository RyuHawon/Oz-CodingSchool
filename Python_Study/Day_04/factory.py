from abc import ABC, abstractmethod

class Pizza(ABC):
    def __init__(self):
        self.name = ""

    @abstractmethod
    def prepare(self):
        raise Exception("오버라이딩 해야합니다.")
    
    def bake(self):
        print(f"{self.name}을(를) 굽는 중입니다")
    
    def cut(self):
        print(f"{self.name}을(를) 자르는 중입니다")
    
    def box(self):
        print(f"{self.name}을(를) 박스에 담는 중입니다")

class PizzaStore(ABC):
    @abstractmethod
    def creat_pizza(self, pizza_type: str) -> Pizza:
        pass

class NYPizzaStore(PizzaStore
        pass