from abc import ABC, abstractmethod

class VendingMachine(ABC):
    def __init__(self, name, price: int):
        self.name = name
        self.price = price

    # 템플릿 메서드, 형식과 진행순서 모두 못박아둠
    def serve(self, amount):
        self.cost(amount)
        if not self.cost_check(amount):
            return
        self.prepare_product()
        self.serve_product()
        self.return_charge(amount)

    # serve 를 통해 실행될 함수들 만들어주면 됨
    def cost(self, amount):
        print(f"{self.name}을(를) 원하시면 {amount}원을 투입해주세요.")

    def cost_check(self, amount):
        if amount < self.price:
            print("잔액이 모자랍니다.")
            return False
        print(f"금액이 확인되었습니다. {self.name}을 준비합니다.")
        return True

    # 준비함수는 각자 다를테니 꼭 각자 만들라고 인터페이스만 만들어둠
    @abstractmethod
    def prepare_product(self):
        raise Exception("오버라이딩 해야합니다.")

    def serve_product(self):
        print(f"{self.name}을(를) 배출합니다.")

    def return_charge(self, amount):
        print(f"거스름돈 {amount - self.price}원을 반환합니다.")