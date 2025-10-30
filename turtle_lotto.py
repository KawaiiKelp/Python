import random
import turtle
import time
import math

# 로또 번호 공이 통 안에 있음
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]

numbers = []
for i in range(1, 46): # i 값: number 삽입
    numbers.append(i)
    # print(number)

random.shuffle(numbers)
num1 = numbers[1]
num2 = numbers[2]
num3 = numbers[3]
num4 = numbers[4]
num5 = numbers[5]
num6 = numbers[6]
bonus = numbers[random.randint(7, 44)]
print(num1)
print(num2)
print(num3)
print(num4)
print(num5)
print(num6)
print(bonus)

turtle.speed(0)
turtle.hideturtle()
turtle.colormode(255)
turtle.bgcolor("black")
turtle.color("white")
turtle.write("Random Lotto", align="center", font=("Neo둥근모 Pro", 60, "bold"))

nums = [num1, num2, num3, num4, num5, num6]
start_x = -400
y = -200
spacing = 160

# 6가지 색상 (RGB 튜플)
colors = [
    (255, 99, 71),    # 토마토 (빨강계)
    (255, 165, 0),    # 주황
    (255, 215, 0),    # 금색(노랑)
    (144, 238, 144),  # 연초록
    (135, 206, 250),  # 하늘색
    (186, 85, 211)    # 보라
]

def text_contrast_color(rgb):
    # 간단한 밝기 계산(가시적 대비 기준)
    r, g, b = rgb
    luminance = 0.299 * r + 0.587 * g + 0.114 * b
    return "black" if luminance > 128 else "white"

for i, n in enumerate(nums):
    x = start_x + i * spacing
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    fill = colors[i % len(colors)]
    turtle.color(fill)
    turtle.begin_fill()
    turtle.circle(70, 360)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(x, y + 40)
    turtle.pendown()
    # 숫자 색상은 배경색에 따라 대비가 잘되게 선택
    turtle.color(text_contrast_color(fill))
    turtle.write(f"{n}", align="center", font=("Neo둥근모 Pro", 40, "bold"))
    turtle.color("white")

# 스크린의 전체를 하얗게 채우고 텍스트 출력
# 스크린 크기는 직접 구하기
screen = turtle.Screen()
width = screen.window_width()
height = screen.window_height()
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.fillcolor("white")
turtle.begin_fill()
turtle.goto(width // 2, height // 2)
turtle.goto(-width // 2, height // 2)
turtle.goto(-width // 2, -height // 2)
turtle.goto(width // 2, -height // 2)
turtle.goto(width // 2, height // 2)
turtle.end_fill()
turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
