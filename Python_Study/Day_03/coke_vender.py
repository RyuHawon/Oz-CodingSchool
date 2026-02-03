from vender import Vending_Machine

class coke_vender(Vending_Machine):
    def __init__(self):
        super().__init__("콜라", 1200)
    
    def prepare_product(self):
        print(f"콜라 위치 확인 중 ...")
        print(f"콜라 재고 확인 중 ...")