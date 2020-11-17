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

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):  # __init__ 파이썬의 생성자
        self.name = name  # 멤버 변슈
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{} : {} 방향으로 이동합니다. [속도 : {}]"
              .format(self.name, location, self.speed))
        # self.damage = damage # 메딕은 공격력이 없기 때문에 삭제

        # print("{} 유닛이 생성되었습니다.".format(name))
        # print("체력: {}, 공격력: {}\n".format(hp, damage))


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
class AttackUnit(Unit):  # AttackUnit이 Unit을 상속받음
    def __init__(self, name, hp, speed, damage):  # __init__ 파이썬의 생성자
        Unit.__init__(self, name, hp, speed)
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


# 메딕 : 의무병
# 드랍쉽 : 공중유닛, 수송기

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{} : {} 방향으로 날아갑니다. [속도 : {}]"
              .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스


class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)  # 상속 받은거 초기화 # 지상 스피드 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):  # 메소드 오버라이딩
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


# 벌쳐 : 지상 유닛, 기동성 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저 : 공중유닛, 체력 좋음, 공격력 좋음
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
battlecruiser.move("9시")
# battlecruiser.fly(battlecruiser.name, "9시")

# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사
valkyri = FlyableAttackUnit("발키리", 200, 6, 5)
valkyri.fly(valkyri.name, "3시")

# 파이어뱃 : 공격 유닛, 화염방사기.
firebat1 = AttackUnit("파이어뱃", 50, 5, 16)
firebat1.attack("5시")

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)

# 건물


class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # super()를 통해 초기화 할 때 self는 없이 씀
        super().__init__(name, hp, 0)  # Unit.__init__(self, name,hp,0)
        self.location = location
        # pass  # 넘어간다.

# 서플라이 디폿 : 건물, 1개 / 건물 = 8유닛
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     pass

# game_start()
# game_over()
