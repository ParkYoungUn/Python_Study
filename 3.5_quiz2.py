from random import *
date = randint(4, 28)
print("오프라인 스터디 날짜는 매월 "+str(date)+"일로 선정되었습니다.")

python = "Python is Amazing"
print(python)
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))

index = python.index("n")
print(index)
index = python.index("n", index+1)
print(index)
print(python.find("java"))
# print(python.index("java")) # 에러

print(python.count("n"))

print("Red Apple\rPine")
