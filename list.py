subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["박영운", "김보성", "한윤정"]
print(subway)
print(subway.index("김보성"))

# 정도원 추가
subway.append("정도원")
print(subway)

# 1번째 자리에 박원진 추가
subway.insert(1, "박원진")
print(subway)

# 뒤에서 한명씩 꺼냄
print(subway.pop())
print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인하기
subway.append("박영운")
print(subway)
print(subway.count("박영운"))

# 정렬도 가능
num_list = [5, 2, 4, 3, 1]
print(num_list)
num_list.sort()
print(num_list)

# 거꾸로 정렬
num_list.reverse()
print(num_list)

# 비우기
num_list.clear()
print(num_list)

num_list = [5, 4, 3, 1, 2]
min_lsit = ["박영운", 20, True]
print(min_lsit)

# 리스트 확장
num_list.extend(min_lsit)
print(num_list)
