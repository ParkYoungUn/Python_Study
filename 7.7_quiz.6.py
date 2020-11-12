
def std_weight(height, gender):  # 키는 m단위(실수), gender(string)
    if gender == "남자":
        return height*height*22
    else:
        return height*height*21


height = 175  # cm
gender = "남자"
weight = round(std_weight(height/100, gender), 2)
print("키 {}cm {}의 표준 체중은 {} 입니다.".format(height, gender, weight))
