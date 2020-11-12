def open_acount():
    print("새로운 계좌가 생성되었습니다.")


open_acount()

# 전달값과 반환 값


def deposit(balance, money):  # 입금
    print("입금이 완료되었습니다. 잔액은 {}원 입니다.".format(balance+money))
    return balance+money


def withdraw(balance, money):  # 출금
    if balance > money:  # 잔액이 출금액보다 많으면 출금 가능
        print("출금이 완료되었습니다. 잔액은 {}원 입니다.".format(balance - money))
        return balance-money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {}원 입니다.".format(balance))
        return balance


def withdraw_night(balance, money):  # 저녁에 출금 (수수료 부과)
    comission = 100  # 수수료 100원
    return comission, balance - money - comission  # ,를 통해 여러개의 값을 한번에 출력 가능


balance = 0  # 잔액
balance = deposit(balance, 1000)

balance = withdraw(balance, 500)

comission, balance = withdraw_night(balance, 500)
print("수수료는 {}원이며, 잔액은 {}원 입니다.".format(comission, balance))
