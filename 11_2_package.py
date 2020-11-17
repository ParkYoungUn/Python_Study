# import travel.thailand
# # import travel.thailand.ThailandPackage # 패키지 임포트는 클래스나 함수는 직접 할 수 없다.
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()


# print("------------")

# from travel.thailand import ThailandPackage  # 이건 가능함
# trip_to = ThailandPackage()
# trip_to.detail()

# print("------------")

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# print("------------")

from travel import *
# # trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

import random
import inspect
print("------------")

print(inspect.getfile(random))
print(inspect.getfile(thailand))
