from vender import Vending_Machine

class coffee_vender(Vending_Machine):
    def __init__(self):
        super().__init__("커피", 800)

    def prepare_product(self):
        print(f"원두 추출 중 ...")
        print(f"컵에 따르는 중 ...")