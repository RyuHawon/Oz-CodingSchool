from vender import VendingMachine

class RamenVender(VendingMachine):
    def __init__(self):
        super().__init__("라면", 1000)
        
    def prepare_product(self):
        print(f"뜨거운 물 주입 중 ...")
        print(f"면이 익을 때 까지 기다리는 중...")