# Dictionary중복 X
cabinet = {3: "박영운", 100: "김보성"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5]) # 할당되지 않은 키 에러
print(cabinet.get(5))
print(cabinet.get(5, "사용 가능"))

print(3 in cabinet)  # key in 변수
print(5 in cabinet)

cabinet = {"A-3": "박영운", "B-100": "김보성"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "정도원"
cabinet["C-20"] = "한윤정"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())
# 값들만 출력
print(cabinet.values())
# key , value 쌍으로 출력
print(cabinet.items())

# 폐점
cabinet.clear()
print(cabinet)
