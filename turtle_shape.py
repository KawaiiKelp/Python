import turtle as t
import random as r

# 다각형 그리기
n = int(input("몇각형을 그릴까요? "))

""" for i in range(1, n+1):
    t.begin_fill()
    t.forward(100)
    t.left(360/n)
 """

""" for i in range(n, 2, -1):
    for j in range(i):
        t.begin_fill()
        t.forward(100)
        t.left(360/i)
 """
""" 
bright_nemophila = "#ace5f3"
nemophila = "#9ccee2"
dark_nemophila = "#71a2b6"
bright_sunflower = "#fffcbd"
sunflower = "#ffeb7b"
dark_sunflower = "#b8a645"
bright_anemone = "#be5c5c"
anemone = "#a52a2a"
dark_anemone = "#751d1d"

color_list = ["black", "white", "gray", bright_nemophila, nemophila, dark_nemophila, bright_sunflower, sunflower, dark_sunflower, bright_anemone, anemone, dark_anemone]

for i in range(n, 2, -1):
    t.color(color_list[i])
    
    t.begin_fill()
    for j in range(i):
        t.forward(100)
        t.left(360/i)
    t.end_fill() """

# 이중 반복문 다각형 랜덤 색칠하기

""" nemophila = "#9ccee2"
sunflower = "#ffeb7b"
anemone = "#a52a2a"

color_list = [nemophila, sunflower, anemone]

for i in range(n, 2, -1):
    t.color(r.choice(color_list))
    
    t.begin_fill()
    for j in range(i):
        t.forward(100)
        t.left(360/i)
    t.end_fill() """

# 이중 반복문 다각형 랜덤 색칠하기 중복 없이

nemophila = "#9ccee2"
sunflower = "#ffeb7b"
anemone = "#a52a2a"
brighter_nemophila = "#c7efff"
brighter_sunflower = "#fff4b5"
brighter_anemone = "#d16262"

color_list = [nemophila, sunflower, anemone, brighter_nemophila, brighter_sunflower, brighter_anemone]
prev_color = None

for i in range(n, 2, -1):
    
    available_colors = [c for c in color_list if c != prev_color]
    color = r.choice(available_colors)
    prev_color = color
    
    t.speed(0)
    t.color(color)
    t.begin_fill()
    for j in range(i):
        t.forward(100)
        t.left(360/i)
    t.end_fill()
""" 
for i in range(3, n+1, +1):
    t.speed(0)
    t.color("white")
    t.begin_fill()
    for j in range(i):
        t.forward(100)
        t.left(360/i)
    t.end_fill()

 """
# ↑ 심심해서 맨듬
# 맨든거 다시 지우는거