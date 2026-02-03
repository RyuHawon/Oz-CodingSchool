from abc import ABC, abstractmethod


class Vending_Machine(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # 템플릿 메서드, 형식과 진행순서 모두 못박아둠
    def serve(self, amount):
        self.cost(amount)
        self.cost_check(amount)
        self.prepare_product()
        self.serve_product()
        self.return_charge(amount)

    # serve 를 통해 실행될 함수들 만들어주면 됨
    def cost(self, amount):
        print(f"{self.name}을(를) 원하시면 {amount}원을 투입해주세요.")

    def cost_check(self, amount):
        if amount < self.price:
            print("잔액이 모자랍니다.")
        else:
            print(f"금액이 확인되었습니다. {self.name}을 준비합니다.")

    # 준비함수는 각자 다를테니 꼭 각자 만들라고 인터페이스만 만들어둠
    @abstractmethod
    def prepare_product(self):
        pass

    def serve_product(self):
        print(f"{self.name}을(를) 배출합니다.")

    def return_charge(self, amount):
        print(f"거스름돈 {self.price - amount}원을 반환합니다.")


# 여기부터 각 자식클래스들

class coffee_vender(Vending_Machine):
    def __init__(self):
        super().__init__("커피", 800)

    def prepare_product(self):
        print(f"원두 추출 중 ...")
        print(f"컵에 따르는 중 ...")

class coke_vender(Vending_Machine):
    def __init__(self):
        super().__init__("콜라", 1200)
    
    def prepare_product(self):
        print(f"콜라 위치 확인 중 ...")
        print(f"콜라 재고 확인 중 ...")

class ramen_vender(Vending_Machine):
    def __init__(self):
        super().__init__("라면", 1000)
        
    def prepare_product(self):
        print(f"뜨거운 물 주입 중 ...")
        print(f"면이 익을 때 까지 기다리는 중...")