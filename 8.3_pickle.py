# pickle : 프로그램 상에서 사용하고 있는 데이터를 파일 형태로 저장해주는 것
#           파일 공유 가능

import pickle

# profile_file = open("profile.pickle", "wb")  # w 쓰기 목적,b -> binary
# profile = {"이름": "박영운", "나이": 25, "취미": ["코딩", "영화", "여행"]}
# print(profile)
# pickle.dump(profile, profile_file)  # profile에 있는 정보를 profile_file에 저장
# profile_file.close()

# profile_file = open("profile.pickle", "rb")  # r 읽 목적,b -> binary
# profile = pickle.load(profile_file)  # file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

print("-------------")
# with
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))


# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요.")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())

print("-------------")
