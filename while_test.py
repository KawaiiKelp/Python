# 제어문 반복문 - for while

# while 문
# 1~10까지의 합을 구하는 프로그램
""" 
i = 1
sum = 0

while i <= 100: #i 1 2 3 4 5 6 7 8 9 10
    sum += i
    i += 1
    print("1부터 10까지의 합:", sum)

 """
 # 3부터 15까지 출력하는 while문 작성
""" 
i = 3

while i <= 15:
    print(i)
    i += 1

# 3부터 15까지 출력하는 for문으로 변경
for i in range(3, 16):
    print(i) """
""" 
while True: # 무한 반복
    score = int(input("점수를 입력하세요: "))
    if score >= 0 and score <= 100:
        break # 박살
print(f"당신의 점수는 {score}점입니다.")
 """
# 키보드로 숫자 하나 입력받고 무한 반복
# 입력된 값이 4면 박살
# 입력된 값 출력 후 무한 반복
""" while True:
    숫자 = int(input("숫자를 입력하세요: "))
    if 숫자 == 4:
        break
    print(f"입력된 숫자는 {숫자}입니다.")
 """
fruit = ['사과', '포도', '배', '참외']

for fruits in fruit:
    print(fruits)

fruits = 0
while fruits < len(fruit):
    print(fruit[fruits])
    fruits += 1

vwp = ['정서', '하루', '카후', '리메', '코코']

select = int(input("1 ~ 5 중에 고르셈\n입력: "))

match select:
    case 1:
        print("당신은 이구미입니다")
    case 2:
        print("당신은 하루구미입니다")
    case 3:
        print("당신은 하나구미입니다")
    case 4:
        print("당신은 메구미입니다")
    case 5:
        print("당신은 사치구미입니다")
    case _:
        print("당신은 그 어느 것에도 속하지 않았습니다")
if select == 1 or select == 2 or select == 3 or select == 4 or select == 5:
    print(f"당신이 좋아하는 {vwp[select-1]}를 열렬히 응원하세요")
else:
    print("VWP 좋아하셔야죠;;;;;;;;;;;;;;;;;;;; 한명만 골라보세요")