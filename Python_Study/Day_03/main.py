from Manager import Manager

manager = Manager()
manager.show_list()

choice = input("이용하실 자판기를 입력해주세요: ")
choiced_vender = manager.get_vender(choice)
if not choiced_vender:
    print("존재하지 않는 자판기입니다.")
    exit()
else:
    choiced_vender.serve()