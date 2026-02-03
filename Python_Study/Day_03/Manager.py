from vender import VendingMachine
from vender_list import vender_list


class Manager:
    def __init__(self):
        self.venders = {v.name: v for v in vender_list}

    def add_vender(self, vender: VendingMachine):
        self.venders[vender.name] = vender
        print(f"{vender.name} 자판기를 추가했습니다.")

    def rm_vender(self, name: str):
        if name not in self.venders:
            print(f"{name} 자판기는 존재하지 않습니다.")
            return
        del self.venders[name]
        print(f"{name} 자판기를 삭제했습니다.")

    def show_list(self):
            print("\n====== 이용 가능 자판기 ======")
            for name in self.venders.keys():
                print(f"- {name}")
            print("==============================")

    def get_vender(self, name) -> VendingMachine:
        return self.venders.get(name)