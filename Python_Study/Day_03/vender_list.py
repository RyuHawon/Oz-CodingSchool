from vender import VendingMachine

class CoffeeVender(VendingMachine):
    def __init__(self):
        super().__init__("커피", 800)

    def prepare_product(self):
        print(f"원두 추출 중 ...")
        print(f"컵에 따르는 중 ...")

class CokeVender(VendingMachine):
    def __init__(self):
        super().__init__("콜라", 1200)
    
    def prepare_product(self):
        print(f"콜라 위치 확인 중 ...")
        print(f"콜라 재고 확인 중 ...")

class RamenVender(VendingMachine):
    def __init__(self):
        super().__init__("라면", 1000)
        
    def prepare_product(self):
        print(f"뜨거운 물 주입 중 ...")
        print(f"면이 익을 때 까지 기다리는 중...")

vender_list = [CoffeeVender(), CokeVender(), RamenVender()]