import math  # math 모듈을 불러옵니다.

# 삼각형의 넓이를 계산하는 함수
def triangle_area(base, height):
    return 0.5 * base * height

# 원의 넓이를 계산하는 함수
def circle_area(radius):
    return math.pi * radius ** 2

# 직육면체의 겉넓이를 계산하는 함수
def cuboid_area(length, width, height):
    return 2 * (length * width + width * height + height * length)

