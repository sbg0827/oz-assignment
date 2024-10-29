# mymath.py 파일에서 정의된 함수들을 가져옵니다.
from mymath import triangle_area, circle_area, cuboid_area

# 삼각형 넓이 계산
base = 3
height = 10
print(f"삼각형의 넓이: {triangle_area(base, height)}")

# 원의 넓이 계산
radius = 4
print(f"원의 넓이: {circle_area(radius)}")

# 직육면체의 겉넓이 계산
length = 5
width = 10
cuboid_height = 4
print(f"직육면체의 겉넓이: {cuboid_area(length, width, cuboid_height)}")