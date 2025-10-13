"""# 제어문 - 반복문 for 문자열 range 리스트 변수

# 구구단 찍기
for i in range(1, 10):
    print(f"2 * {i} = {2*i}") # 9번

# 8단 찍기
print("구구단 8단")
for i in range(1, 10):
    print(f"8 * {i} = {8*i}") # 9번

# 4단 홀수만 찍기
print("구구단 4단 홀수만")
for i in range(1, 10, 2):
    print(f"4 * {i} = {4*i}") # 5번

# 중복 for문
for i in range(1, 6): #i = 1 2 3 4 5
    # print(i)
    for j in range(1, 6):
        print("잘 지냈니? ")
# 구구단 2~9단

print("구구단 출력하기")
for i in range(2, 10): # i = 2 3 4 5 6 7 8 9
    for j in range(1, 10): # j = 1 2 3 4 5 6 7 8 9
        print(f"{i} * {j} = {i*j:>2}", end='   ')
    print()
    
# 출력 포매팅 정렬하기
name = "케르프"
print(f"{name:<10}") # 왼쪽 정렬
print(f"{name:>10}") # 왼쪽 정렬
print(f"{name:^10}") # 가운데 정렬

# 구구단 변형

print("구구단 출력하기")
for j in range(1, 10): # i = 2 3 4 5 6 7 8 9
    for i in range(2, 10): # j = 1 2 3 4 5 6 7 8 9
        print(f"{i} * {j} = {i*j:>2}", end='   ')
    print()
    
"""

for i in range(1, 6):
    print("*" * i)