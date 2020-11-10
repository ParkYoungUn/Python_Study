students = [1, 2, 3, 4, 5]
print(students)

students = [i+100 for i in students]
print(students)

# 이름을 길이로 변환
students = ["Park", "Kim", "Hans"]
students = [len(i) for i in students]
print(students)

# 이름을 대문자로
students = ["Park", "Kim", "Hans"]
students = [i.upper() for i in students]
print(students)
