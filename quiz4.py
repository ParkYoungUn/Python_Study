from random import *
# lst = [1, 2, 3, 4, 5]
# print(lst)
# shuffle(lst)
# print(lst)

users = range(1, 21)  # 1부터 20까지 숫자 생성
print(type(users))
users = list(users)
print(type(users))

print(users)
shuffle(users)
print(users)

winners = sample(users, 4)
print("-- 당첨자 발표 --")
print("치킨 당첨자: {}".format(winners[0]))
print("커피 당첨자: {}".format(winners[1:]))
print("-- 축하힙니다. --")
