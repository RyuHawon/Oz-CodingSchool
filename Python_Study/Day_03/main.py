from Manager import Manager
from vender import VendingMachine

manager = Manager()

choice = input("자판기 선택: ")
vender = manager.get_vender(choice)

if vender:
    try:
        amount_input = int(input("투입할 금액 입력"))
        vender.serve(amount_input)
    except ValueError:
        print("숫자만 입력해주세요.")
else:
    print("존재하지 않는 자판기입니다.")