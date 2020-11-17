class Unit:
    def __init__(self):
        print("Unit 생성자")


class Flyable:
    def __init__(self):
        print("Flyable 생성자")


class FlyableUnit(Unit, Flyable):  # 2개 이상의 다중상속을 받을때 먼저 상속된 class에 대해서만 init함수가 호출됨
    def __init__(self):
        # super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)


dropship = FlyableUnit()
