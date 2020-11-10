# print("대기번호:1")
# print("대기번호:2")
# print("대기번호:3")
# print("대기번호:4")

# for waiting_no in [0, 1, 2, 3, 4]:
for waiting_no in range(1, 6):
    print("대기번호:{0}".format(waiting_no))

starbucks = ["박영운", "한윤정", "김보성"]
for customer in starbucks:
    print("{0}, 커피가 준비 되었습니다.".format(customer))


# while
customer = "박영운"
index = 5
while index >= 1:
    print("{}, 커피가 준비되었습니다. {} 번 남았어요".format(customer, index))
    index -= 1
    if index == 0:
        print("커피가 폐기처분 되었습니다.")

# 무한루프
# customer = "한윤정"
# index = 1
# while True:
#     print("{0}, 커피가 준비되었습니다. 호출 {1} 번".format(customer, index))
#     index += 1

customer = "김보성"
person = "Unknown"
while person != customer:
    print("{}, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?")
