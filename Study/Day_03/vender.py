from abc import ABC, abstractmethod



class Vending_Machine(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def serve(self, amount):
        self.cost(amount)
        self.prepare_product()
        self.serve_product()
        self.return_charge(amount)

    def cost(self, amount):
        print(f"{self.name}을 원하시면 {amount}원을 투입해주세요.")

    def cost_check(self, amount):
        if amount < self.price:
            print("잔액이 모자랍니다.")
        else:
            print(f"금액이 확인되었습니다. {self.name}을 준비합니다.")

    @abstractmethod
    def prepare_product(self):
        pass

    def serve_product(self):
        print(f"{self.name}이 제공됩니다.")

    def return_charge(self, amount):
        print(f"거스름돈 {self.price - amount}원을 반환합니다.")



class coffee_vender(Vending_Machine):
    def __init__(self):
        super().__init__("커피", 800)

    def prepare_product(self):
        print(f"원두 추출 중 ...")
        print(f"컵에 따르는 중 ...")
