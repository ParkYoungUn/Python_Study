import sys

print("Python", "Java", "JavaScript", sep=" vs ", end="?")
print("무엇이 더 재밌을까요?")
print("-------------------------------------")
print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)
print("-------------------------------------")

scores = {"수학": 0, "영어": 50, "코딩": 100}
for subject, score in scores.items():  # subject =key
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")

print("-------------------------------------")

# 은행 대기 순번표 001,002,003 처럼 앞에 00이 붙게
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))

print("-------------------------------------")
# answer = input("입력: ")
# print(type(answer))  # 사용자입력은 무조건 문자열
# print("입력하신 값은 "+answer)

print("-------------------------------------")
# 빈 자리는 빈공간으로 두고, 오른쪽 정렬, 총 10공간 확보
print("{0: >10}".format(500))
# 양수 일 때 + 음수 일 때 -
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
# 왼쪽 정렬, 빈칸 _로 채움
print("{0:_<+10}".format(500))

# 3자리마다  콤마 찍어주기
print("{0:,}".format(10000000))
# 3자리마다  콤마 찍어주고,+ - 부호도 붙임
print("{0:+,}".format(10000000))
print("{0:+,}".format(-10000000))
# 3자리마다  콤마 찍어주고,+ - 부호도 붙임, 자릿수 확보
# 돈이 많으면 ^표시로 채움
print("{0:^<+30,}".format(10000000000))

# 소수점 출력
print("{0:f}".format(5/3))
# 소수점 특정 자리 수 까지 표시 (3째 자리에서 반올림)
print("{0:.2f}".format(5/3))

print("-------------------------------------")
# 파일 입출력

# score_file = open("score.txt", "w", encoding="utf8") # w 쓰기
# print("수학 :0", file=score_file)
# print("영어 :50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")  # a = append 덮어쓰기
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 110")
# score_file.close()

score_file = open("score.txt", "r", encoding="utf8")  # r 읽기
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="")  # 줄별로 읽음, 커서 다음줄
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()
print("\n---------------")
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()
print("\n---2---------------")
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()
for line in lines:
    print(line, end="")
score_file.close()
