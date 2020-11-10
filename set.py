# 집합 (set)
# 중복 안됨, 순서 없음
my_set = {1, 2, 3, 3, 3, 2}
print(my_set)

java = {"박영운", "김보성", "한윤정"}
python = set(["박영운", "정도원"])

# 교집합 (java와 python을 모두 할 수있는 사람)
print(java & python)
print(java.intersection(python))

# 합집합 (java도 할 수 있거나 python 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합(java 할 수 있지만 python은 할 줄 모르는 개발자)
print(java-python)
print(java.difference(python))

#  python 을 할 줄 아는사람이 늘어남
python.add("김보성")
print(python)

# java를 까먹었어요
java.remove("한윤정")
print(java)
