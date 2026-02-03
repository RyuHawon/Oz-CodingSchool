from vender import VendingMachine
from CoffeeVender import CoffeeVender
from CokeVender import CokeVender
from RamenVender import RamenVender

class Manager:
    def __init__(self):
        self.venders = {
            "커피": CoffeeVender(),
            "콜라": CokeVender(),
            "라면": RamenVender()
        }

    def get_vender(self, name) -> VendingMachine:
        return self.venders.get(name)
    
    def plus_vender(self, vender: VendingMachine):
        self.venders[vender.name] = vender
        print(f"{vender.name} 자판기가 추가되었습니다.")