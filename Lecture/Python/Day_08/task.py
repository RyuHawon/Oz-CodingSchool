class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def return_balance(self):
        return self.__balance

    def deposit(self, amount_d):
        if amount_d <= 0:
            print('0 이하의 금액은 입금하실 수 없습니다.')
        else:
            self.__balance += amount_d
            print(f'{amount_d}원이 입금되었습니다.')
    
    def withdraw(self, amount_w):
        if amount_w <= 0:
            print('0 이하의 금액은 출금하실 수 없습니다.')
        elif amount_w > self.__balance:
            print(f'현재 잔액 {self.__balance}원 이상의 금액은 출금하실 수 없습니다.')
        else:
            self.__balance -= amount_w
            print(f'{amount_w}원이 출금되었습니다.')
    
    def finish(self):
        print(f'거래가 완료되었습니다. 현재 잔액은 {self.__balance}원 입니다. 감사합니다.')

def Atm(my_account:Account):
    Call = None
    while(True):
        if Call is None:
            Call = input('원하는 메뉴의 숫자를 입력해주세요.\n1: 입금, 2: 출금, 3: 취소')
        
        if Call == '3':
            print("거래를 취소합니다.")
            break
        
        if Call == '1':
            try:

                get_amount = input(
                    '입금하실 금액을 입력하세요.\n다시 선택하려면 0을 입력해주세요.'
                    )
                if get_amount == '0':
                    print('선택메뉴로 돌아갑니다.')
                    Call = None
                    continue

                get_amount = int(get_amount)
                my_account.deposit(get_amount)
                my_account.finish()
                Call = None
                continue

            except ValueError:
                print('금액은 정수로 입력해주세요.')
                Call = '1'
                continue

        if Call == '2':
            try:

                get_amount = input(
                    '출금하실 금액을 입력하세요.\n다시 선택하려면 0을 입력해주세요.'
                    )
                if get_amount == '0':
                    print('선택메뉴로 돌아갑니다.')
                    Call = None
                    continue

                get_amount = int(get_amount)
                my_account.withdraw(get_amount)
                my_account.finish()
                Call = None
                continue

            except ValueError:
                print('금액은 정수로 입력해주세요.')
                Call = '2'
                continue

        Call = None
        print("1, 2, 3 중에서 선택해주세요.")


my_account = Account("KimDoYeong", 50000)
Atm(my_account)


#피드백 전 코드
'''
#수정전코드
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def return_balance(self):
        return self.__balance
        # 잔액 내용을 보고싶을 때 사용할 매서드 미리 설정
    def deposit(self, amount_d):
        if amount_d <= 0:
            print('0 이하의 금액은 입금하실 수 없습니다.')
        else:
            self.__balance += amount_d
            print(f'{amount_d}원이 입금되었습니다.')
    
    def withdraw(self, amount_w):
        if amount_w <= 0:
            print('0 이하의 금액은 출금하실 수 없습니다.')
        elif amount_w > self.__balance:
            print(f'현재 잔액 {self.__balance}원 이상의 금액은 출금하실 수 없습니다.')
        else:
            self.__balance -= amount_w
            print(f'{amount_w}원이 출금되었습니다.')
    
    def finish(self):
        print(f'거래가 완료되었습니다. 현재 잔액은 {self.__balance}원 입니다. 감사합니다.')

my_account = Account("KimDoYeong", 50000)

def Atm():
    while(True):
        Call = input('원하는 메뉴의 숫자를 입력해주세요.\n1: 입금, 2: 출금, 3: 취소')
        if Call == '1':
            try:
                get_amount = input('입금하실 금액을 입력하세요.\n다시 선택하려면 0을 입력해주세요.')
                if get_amount == '0':
                    print('선택메뉴로 돌아갑니다.')
                    continue
                else:
                    get_amount = int(get_amount)
            except ValueError:
                print('금액은 정수로 입력해주세요.')
                continue
            my_account.deposit(get_amount)
            my_account.finish()
            while(True):
                con = input("거래를 계속 하시려면 1번, 종료하시려면 0번을 눌러주세요.")
                if con == '1':
                    break
                elif con == '0':
                    return
                else: print("다시 입력해주세요.")
            continue
        elif Call == '2' :
            try:
                get_amount = input('출금하실 금액을 입력하세요.\n다시 선택하려면 0을 입력해주세요.')
                if get_amount == '0' :
                    print('선택메뉴로 돌아갑니다.')
                    continue
                else:
                    get_amount = int(get_amount)
            except ValueError:
                print('금액은 정수로 입력해주세요.')
                continue
            my_account.withdraw(get_amount)
            my_account.finish()
            while(True):
                con = input("거래를 계속 하시려면 1번, 종료하시려면 0번을 눌러주세요.")
                if con == '1':
                    break
                elif con == '0':
                    return
                else : print("다시 입력해주세요.")
            continue
        elif Call == '3':
            print("거래를 취소합니다.")
            return
        else:
            print("숫자 1 또는 2, 3 을 입력해주세요.")

Atm()
'''