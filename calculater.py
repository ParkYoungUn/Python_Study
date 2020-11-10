from random import *
from math import *
print(1+1)
print(2**3)  # 2^3=8
print(5 % 3)  # 나머지 구하기
print(5//3)  # 몫

print((3 > 0) and (3 < 5))
print((3 > 0) & (3 < 5))

print((3 > 0) or (3 < 5))
print((3 > 0) | (3 < 5))
print("-----------------")

number = 2+3
print(number)
number += 2
print(number)

print(abs(-5))  # 절대값
print(pow(4, 2))  # 4^2
print(max(1, 2, 3))
print(round(4.99))  # 반올림
print(floor(4.3))

print("-----------------")

print(random())  # 0.0~1.0 미만의 임의의 값
print(random()*10)
print(int(random()*10)+1)  # 1부터 10 이하의 랜덤값

print(randrange(1, 46))  # 1~ 16 미만의 임의의 값 생성
print(randint(1, 45))  # 1~45 이하의 값을 생성
