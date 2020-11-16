# # 마린 : 공격 유닛 , 군인 ,총 쏠수 있음
# name = "마린"  # 유닛의 이름
# hp = 40  # 유닛의 체력
# damage = 5  # 유닛의 공격력

# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력: {}, 공격력: {}\n".format(hp, damage))

# # 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있음, 일반모드/시즈 모드
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("체력: {}, 공격력: {}\n".format(tank_hp, tank_damage))

# tank_name2 = "탱크2"
# tank_hp2 = 150
# tank_damage2 = 35

# print("{} 유닛이 생성되었습니다.".format(tank_name2))
# print("체력: {}, 공격력: {}\n".format(tank_hp2, tank_damage2))


# def attack(name, location, damage):
#     print("{} : {} 방향으로 적군을 공격합니다. [공격력 {}]"
#           .format(name, location, damage))


# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank_name2, "1시", tank_damage2)

class Unit:
    def __init__(self, name, hp, damage):  # __init__ 파이썬의 생성자
        self.name = name  # 멤버 변슈
        self.hp = hp
        self.damage = damage
        print("{} 유닛이 생성되었습니다.".format(name))
        print("체력: {}, 공격력: {}\n".format(hp, damage))


# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# # 레이스 : 공중 유닛 , 비행기 , 클로킹(상대방에게 보이지 않음)
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름: {}, 공격력: {}".format(wraith1.name, wraith1.damage))

# # 마인드 컨트롤 (빼앗음)
# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True

# if wraith2.clocking == True:
#     print("{}는 현재 클로킹 상태입니다.".format(wraith2.name))

# 공격 유닛
class AttackUnit:
    def __init__(self, name, hp, damage):  # __init__ 파이썬의 생성자
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        print("{} : {} 방향으로 적군을 공격합니다. [공격력: {}]"
              .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{} : {} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 체력은 {} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : 파괴되었습니다.".format(self.name))


# 파이어뱃 : 공격 유닛, 화염방사기.
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)
